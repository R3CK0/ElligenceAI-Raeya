# Streamlit OpenAI Responses API Chat App

This is a Python web application built with Streamlit that interacts with the OpenAI Responses API to answer user questions based on provided documentation context (simulated). It features parallel streamed responses, user selection or editing of answers, and logging of interactions.

It is configured to use the `gpt-4.1-nano` model and leverages the Responses API's built-in state management via `previous_response_id` for conversational turns.

## Features

* Interactive chat interface using Streamlit.
* Generates two parallel responses from the OpenAI API for each question.
* Responses are streamed to the user interface in real-time.
* User can select one of the two generated responses as preferred.
* User can manually edit a response if desired.
* Logs user questions, desired answers, and undesired answers to a JSONL file.
* Manages conversation state across turns using the OpenAI Responses API's `previous_response_id`.
* Uses the `gpt-4.1-nano` model (or a specified alternative).

## Prerequisites

* A GitHub account.
* An OpenAI API key.

## Setting up in GitHub Codespaces

GitHub Codespaces provides a cloud-based development environment that allows you to run this application directly from your browser.

1.  **Create a Repository:** Ensure the code for this Streamlit application (the Python file, let's call it `chat_app.py`, and a `requirements.txt` file) is in a GitHub repository. If you don't have one, create a new repository and add the files.
2.  **Create `requirements.txt`:** In the root of your repository, create a file named `requirements.txt` with the following content:

    ```
    streamlit
    openai
    ```
3.  **Create a Codespace:**
    * Navigate to the repository on GitHub.
    * Click the "Code" button.
    * Go to the "Codespaces" tab.
    * Click "Create codespace on main" (or the branch you are using).
    * GitHub will provision a cloud development environment for you.

## Environment Setup within Codespaces

Once the Codespace is running (it will open in a VS Code-like interface in your browser):

1.  **Open the Terminal:** If the terminal is not already open, you can open it by going to `Terminal > New Terminal`.
2.  **Install Dependencies:** In the terminal, run the following command to install the required Python libraries:

    ```bash
    pip install -r requirements.txt
    ```
3.  **Configure OpenAI API Key:**
    * Streamlit Cloud (and by extension, often Codespaces integrations) prefers using `st.secrets`.
    * In the Codespaces VS Code interface, go to `View > Command Palette...` and search for "Codespaces: Add Codespace Secrets".
    * Click on it. This will open a browser tab or window for your Codespace settings.
    * Under "Repository Secrets", click "New secret".
    * For the "Name", enter `OPENAI_API_KEY`.
    * For the "Value", paste your actual OpenAI API key.
    * Click "Add secret".
    * Alternatively, you can set it as a Codespace environment variable directly in the terminal (though less secure than using secrets):
        ```bash
        export OPENAI_API_KEY='your_openai_api_key_here'
        ```
        *(Note: Setting it this way in the terminal is usually only for the current terminal session or requires adding it to a shell profile file like `.bashrc` or `.zshrc` to persist. Using Codespaces secrets is recommended.)*

## Running the Application

1.  **Open the Terminal:** Ensure you have a terminal open in your Codespace.
2.  **Run the Streamlit App:** Execute the following command:

    ```bash
    streamlit run chat_app.py
    ```
3.  **Access the App:**
    * When Streamlit starts, it typically runs on port 8501.
    * GitHub Codespaces automatically detects running web applications and forwards the port.
    * A pop-up should appear in the bottom right corner of the VS Code interface with a button to "Open in Browser" or "Copy Local Address". Click "Open in Browser".
    * If you don't see the pop-up, you can manually forward the port. Go to the "Ports" tab in the bottom panel (you might need to click `Ctrl + `` to show the panel, then select "Ports"). Find port 8501 and click the "Open in Browser" icon (a globe).

The Streamlit application should now be running and accessible in your browser.

## Logging

The application will create a file named `conversation_log.jsonl` in the same directory as your `chat_app.py` file within the Codespace. Each line in this file will be a JSON object representing a logged interaction. You can view and download this file from the Codespaces file explorer.

## Stopping and Managing the Codespace

To stop your Codespace and avoid incurring compute costs when you are not using it, you can:

* Close the browser tab. (Codespaces will typically shut down after a period of inactivity).
* Go back to the repository on GitHub, click "Code", go to "Codespaces", find your running codespace, click the three dots (...), and select "Stop codespace".

## Customization

* **Model:** You can change the `MODEL_NAME` variable in `chat_app.py` to use a different OpenAI model if `gpt-4.1-nano` is not suitable or available for your use case (e.g., `"gpt-3.5-turbo"` or `"gpt-4o-mini"` if available).
* **Logging:** Modify the `log_interaction` function if you need a different logging format or want to log to a different destination (e.g., cloud storage).

This README provides all the necessary steps for you and others to get the Streamlit application running in a GitHub Codespaces environment.