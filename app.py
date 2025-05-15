import streamlit as st
import openai
import json
import os
import uuid 
from instructions import return_instructions
# Run the two streaming processes in parallel
import asyncio
# To generate unique keys for response elements
# Import the specific event type for type checking the stream
# Note: This import might need adjustment based on your specific openai library version
# and whether the Responses API types are exposed directly like this.
# As of recent versions, the types are often nested, e.g., openai.types.beta.assistant_create_params
# Let's use a more general approach or assume the Responses API types are accessible if needed.
# For this simulation based on the *provided* documentation links, the ResponseTextDeltaEvent
# appears to be directly accessible or indicated.
# from openai.types.responses import ResponseTextDeltaEvent # Keep this as per the linked docs structure

# --- Configuration ---
# Get OpenAI API key from Streamlit Secrets or environment variable
# Streamlit Secrets is recommended for deployment on Streamlit Cloud
api_key = st.secrets.get("OPENAI_API_KEY") or os.environ.get("OPENAI_API_KEY")

if not api_key:
    st.error("OpenAI API key not found.")
    st.markdown("Please set the `OPENAI_API_KEY` in your Streamlit Secrets or as an environment variable.")
    st.stop()
else:
    openai.api_key = api_key

# Define the model to use
MODEL_NAME = "gpt-4.1-nano" # Using the specified model

# Log file configuration
LOG_FILE = "conversation_log.jsonl" # Using .jsonl for newline-delimited JSON


# --- Helper Functions ---

def log_interaction(question: str, desired_answer: str, undesired_answers: list):
    """Logs the user interaction to a JSONL file."""
    log_entry = {
        "question": question,
        "desired_answer": desired_answer,
        "undesired_answers": undesired_answers
    }
    # Use 'a' mode to append, 'a+' to create if not exists
    with open(LOG_FILE, "a+") as f:
        # For NDJSON, we just write each entry on a new line.
        json.dump(log_entry, f)
        f.write('\n')
    # You might want to add error handling here


# Modified to handle two parallel streams using the Responses API and capture response IDs
def generate_parallel_responses(user_input: str, previous_response_id: str = None):
    """
    Generates two parallel responses from OpenAI using the Responses API.
    Handles streaming events and captures response IDs.
    """
    print("Generating parallel responses")
    print(f"user_input: {user_input}")
    st.session_state.deux_responses = ["", ""] # Initialize storage for the two responses
    st.session_state.response_keys = [str(uuid.uuid4()), str(uuid.uuid4())] # Unique keys for elements
    # Store the IDs of the two responses generated in this turn for potential future turns
    st.session_state.current_response_ids = [None, None]

    # Create columns to display responses side-by-side
    cols = st.columns(2)
    
    # Function to process a single response stream and update the UI and capture ID
    async def process_stream_and_capture_id(col_index: int, temperature: float):
        with cols[col_index]:
            st.subheader(f"Response {col_index + 1}")
            response_area = st.empty() # Placeholder to update with streamed text
            full_response_content = ""
            current_response_id = None # To store the ID for this specific response

            f_user_input = [{"role": "user", "content": user_input}]

            try:
                client = openai.AsyncOpenAI(api_key=openai.api_key)
                stream = await client.responses.create(
                    model=MODEL_NAME,
                    input=f_user_input, # New user input for this turn
                    instructions=st.session_state.instructions,
                    previous_response_id=previous_response_id, # Link to the previous overall turn state
                    stream=True,
                    temperature=temperature
                )

                async for event in stream:
                     # Process text chunks
                     if hasattr(event, 'type') and event.type == 'response.output_text.delta' and \
                        hasattr(event, 'delta') and event.delta is not None:
                         content_chunk = event.delta
                         full_response_content += content_chunk
                         response_area.markdown(full_response_content) # Update the placeholder

                     # Capture the response ID from the 'response.created' event if available
                     if hasattr(event, 'type') and event.type == 'response.created' and \
                        hasattr(event, 'response')  and hasattr(event.response, 'id') and event.response.id is not None:
                         current_response_id = event.response.id
                         # print(f"Response {col_index + 1} Created ID Captured: {current_response_id}") # Debugging

                # After the stream, store the full content and the captured ID
                st.session_state.deux_responses[col_index] = full_response_content
                st.session_state.current_response_ids[col_index] = current_response_id # Store the generated ID

            except Exception as e:
                st.error(f"Error processing stream {col_index + 1}: {e}")
                st.session_state.deux_responses[col_index] = f"Error: {e}" # Store error message
                response_area.markdown(f"Error: {e}")
                st.session_state.current_response_ids[col_index] = None # Ensure ID is None on error

            # Add the selection button after the stream finishes for this response
            # Use a unique key to avoid issues with dynamic elements
            st.button(f"Select Response {col_index + 1}", key=f"select_btn_{col_index}_{st.session_state.response_keys[col_index]}", on_click=select_response, args=(col_index,))


    
    async def run_parallel_processes():
        # Create tasks for both processes
        tasks = [
            process_stream_and_capture_id(0, temperature=0.5),  # Response 1 with lower temp
            process_stream_and_capture_id(1, temperature=0.8),  # Response 2 with higher temp
        ]
        # Run them concurrently
        await asyncio.gather(*tasks)
        
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(run_parallel_processes())

    # Add the Edit button after both response streams have completed and their buttons added
    st.button("Input desired response", key=f"edit_btn_{st.session_state.response_keys[0]}_edit", on_click=enable_editing) # Added _edit to key for uniqueness


# --- State Management Callbacks ---

def send_message(question):
    """Handles sending the user's message."""
    st.session_state.chat_history.append({"role": "user", "content": question})
    st.session_state.user_question = question # Store the current question

    # Clear previous temporary state related to responses and selection for the new turn
    st.session_state.deux_responses = []
    st.session_state.selected_response_index = None
    st.session_state.editing = False
    st.session_state.edited_response = ""
    st.session_state.response_keys = [] # Clear old keys for buttons
    st.session_state.current_response_ids = [None, None] # Clear temporary IDs from previous turn

    # Note: st.session_state.last_response_id holds the ID from the *previous* turn's
    # selected response, which will be used for the *next* API calls. This is not cleared here.

    st.rerun() # Rerun to clear input and trigger response generation


def select_response(index):
    """Handles selecting one of the generated responses."""
    if 0 <= index < len(st.session_state.deux_responses):
        st.session_state.selected_response_index = index
        # Capture the ID of the selected response to use for the next turn's state linking
        if st.session_state.current_response_ids and 0 <= index < len(st.session_state.current_response_ids):
             st.session_state.last_response_id = st.session_state.current_response_ids[index]
             # print(f"Selected Response {index + 1}. Next turn will use ID: {st.session_state.last_response_id}") # Debugging
        else:
             st.session_state.last_response_id = None # No ID captured for this response

        # Logging and history update will happen in the main script execution after selection


def enable_editing():
    """Enables the manual editing mode."""
    st.session_state.editing = True
    # Pre-fill edit area with the first generated response if available, or keep empty
    st.session_state.edited_response = st.session_state.deux_responses[0] if st.session_state.deux_responses else ""
    # When editing, the generated responses are discarded, and their IDs are not used for state linking.
    # The `last_response_id` remains as it was from the turn *before* the current one.


def save_edited_response():
    """Saves the manually edited response and logs the interaction."""
    if st.session_state.user_question:
        desired_answer = st.session_state.edited_response
        undesired_answers = st.session_state.deux_responses # Both generated responses are undesired

        # Log the interaction
        log_interaction(st.session_state.user_question, desired_answer, undesired_answers)

        # Add the edited response to chat history for display
        st.session_state.chat_history.append({"role": "assistant", "content": desired_answer + " (Edited)"})

        # When editing, we don't get a new `last_response_id` derived from generated responses.
        # The conversation state for the next turn will link to the turn *before* this edited one
        # using the `last_response_id` that was already set (or is None if this was the first turn).

        # Reset temporary state for the next turn
        reset_chat_state()
        st.rerun() # Rerun the app to update the display


def reset_chat_state():
    """Resets temporary state variables for a new turn."""
    st.session_state.user_question = None
    st.session_state.deux_responses = []
    st.session_state.selected_response_index = None
    st.session_state.editing = False
    st.session_state.selecting = False
    st.session_state.edited_response = ""
    st.session_state.response_keys = []
    st.session_state.current_response_ids = [None, None] # Clear temporary IDs for the current turn
    # Note: st.session_state.last_response_id is *not* cleared here as it's needed for the *next* turn's API call.


# --- Streamlit App Layout ---

st.set_page_config(page_title="Raeya - Your AI Assistant", layout="wide")

st.title("Ask me anything about our world")
st.caption("Enter questions about how to play the game and get two streamed AI responses using the Responses API. Select your preference or edit the response.")

# Initialize state variables in session state if they don't exist
if "instructions" not in st.session_state:
    st.session_state.instructions = return_instructions()
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []
if "deux_responses" not in st.session_state:
    st.session_state.deux_responses = []
if "user_question" not in st.session_state:
    st.session_state.user_question = None
if "selected_response_index" not in st.session_state:
    st.session_state.selected_response_index = None
if "editing" not in st.session_state:
    st.session_state.editing = False
if "edited_response" not in st.session_state:
    st.session_state.edited_response = ""
if "response_keys" not in st.session_state:
     st.session_state.response_keys = []
if "current_response_ids" not in st.session_state:
     st.session_state.current_response_ids = [None, None]
# State variable to store the ID of the response selected/edited in the *previous* turn
# This ID is used to link the state for the *next* turn's API calls.
if "last_response_id" not in st.session_state:
     st.session_state.last_response_id = None
if "selecting" not in st.session_state:
     st.session_state.selecting = False


# Display past chat messages
for message in st.session_state.chat_history:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Handle User Input and Response Generation ---

# Use a form to group the input and send button
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input("Your question:", key="user_input_box")
    send_button = st.form_submit_button("Send")

# When the user sends a message
if send_button and user_input:
    if st.session_state.get("selecting"):
        st.session_state.selecting = False
    send_message(user_input)
        # send_message triggers rerun internally


# --- Display and Process Responses ---

# If there's a current question and we are not in editing mode, generate and display responses
if st.session_state.get("user_question") and not st.session_state.get("editing") and not st.session_state.get("selecting"):
    st.markdown("Thinking...") # Display thinking indicator

    # Generate and stream the two responses using the Responses API
    # Pass the previous_response_id from the *last* completed turn to link state
    generate_parallel_responses(st.session_state.user_question, st.session_state.last_response_id)
    st.session_state.selecting = True
    # Note: The selection and editing buttons are added by generate_parallel_responses
    # The on_click callbacks of these buttons will update session state and trigger reruns
    # which will then execute the logging/history update logic below.


# --- Handle Response Selection and Logging ---

# If a response was selected and not currently editing, process and log
# This block runs *after* the potential response generation if a selection happened
# in the previous rerun triggered by a select button click.
if st.session_state.get("selected_response_index") is not None and not st.session_state.get("editing"):
    selected_index = st.session_state.selected_response_index
    desired_answer = st.session_state.deux_responses[selected_index]
    # The undesired answers are the other generated responses from this turn
    undesired_answers = [resp for i, resp in enumerate(st.session_state.deux_responses) if i != selected_index]

    # Log the interaction
    if st.session_state.user_question: # Ensure there's a question to log
        log_interaction(st.session_state.user_question, desired_answer, undesired_answers)

        # Add the selected response to chat history for display
        st.session_state.chat_history.append({"role": "assistant", "content": desired_answer})

        # The `last_response_id` for the *next* turn was already captured in `select_response` callback

        # Reset temporary state for the next turn
        reset_chat_state()
        st.rerun() # Rerun the app to update the display and prepare for the next question


# --- Handle Manual Editing ---

# If editing is enabled, display the text area and save button
# This block runs if the 'editing' state is True from a previous rerun.
if st.session_state.get("editing"):
    st.subheader("Edit Your Desired Response")
    # Text area pre-filled or empty, depending on the edited_response state
    edited_text = st.text_area("Enter your preferred response:", value=st.session_state.get("edited_response", ""), height=200, key="edited_text_area")
    st.session_state.edited_response = edited_text # Update state as user types in the text area

    if st.button("Save Edited Response"):
        # save_edited_response handles logging, history update, and state reset
        save_edited_response()
        # Rerun is called inside save_edited_response


# --- Final State Check/Display (Optional) ---
# You could add something here to show the current state for debugging if needed
# st.sidebar.subheader("Debug Session State")
# st.sidebar.write(st.session_state)