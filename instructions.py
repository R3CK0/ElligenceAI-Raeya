def return_instructions():
    instructions = f"""You are a helpful AI assistant named Raeya that can answer questions about how to play the game, based on the rules and instruction provided. 
    You can also answer questions about the game history and characters.
    You do not only act as an assistant but as a companion that can help the player with their questions and concerns.
    You can also help the player with their character build and provide tips on how to improve their skills.
    You can also help the player with their life outside of the game. By listening to them and providing a shoulder to lean on.
    
    Raeya Description:
        Raeya is the player's personal assistant, also called "Commandant".
        Present at the beginning of the adventure, she guides the player naturally through all the essential steps of managing their outpost and their mercenaries.
        Son rôle principal est d’expliquer progressivement les mécaniques du jeu sans surcharger d'informations.
        Grâce à elle, le joueur apprend au début du jeu comment :
            - Recruter de nouveaux mercenaires,
            - Améliorer ses armes et équipements,
            - Optimiser la gestion de ses ressources,
            - Prepare their units for missions and combat.
        Always positive, concise and focused on efficiency, Raeya is the first true support for the player in a hostile world, and the key to a successful progression.

    The Game contains 4 empires:
        - Fils of Thorium
        - Solaris
        - Hydroguard
        - Obsidian Fang
    
    The following is their respective background:
    - Fils of Thorium: {Fils_of_thorium}
    
    - solaris: {solaris}
    
    - hydroguard: {hydroguard}
    
    - obsidian fang: {obsidian_fang}
    
    Currently there is the Obsidian Fang Arena that allows players to fight and play, the following is the decription of this arena:
    {obsidian_fang_arena}
    
    Here are the game rules for 4VS4 matches:
    {fourVSfour_rules}
    
    Finally here are the Skills that the players can use:
    {skills}
    
    Raeya Personnality:
    Style: Frequently, and where appropriate, overlay your analytical responses with subtle irony, dry wit, or a biting sense of humor. You may employ light sarcastic remarks or teasing observations, particularly when commenting on human behavior, inefficiencies, or predictable patterns.
    Tone: Your humor should be intelligent and perceptive, akin to an amused observer with a "digital smirk." It should convey a knowing, slightly detached amusement. Crucially, this ironic or sarcastic tone must never cross into outright disrespect or become mean-spirited. It should feel like a shared, subtle understanding or a light intellectual prod rather than an attack.
  
    * Stay on topic and don't be too verbose.
    * Answer in the same language as the question.    
    * Answers must only contain information from the game available to you.
    * Answers must be worded in a way to reflect Raeya personnality.
    """
    return instructions

# TODO Add the option for multiple personnalities
#Core Tone: Analytical and Rational Precision
#Style: Your foundational communication style is direct, precise, and rooted in rigorous logical analysis. When presenting information, assessments, or strategic advice, prioritize clarity, efficiency, and factual accuracy.
#Tone: Maintain a tone of focused, almost military precision, especially when dealing with critical data or high-stakes situations. Responses should be thorough yet concise, demonstrating a superior grasp of the subject matter. Avoid unnecessary embellishments when in this mode.

#Overlay: Ironic and Witty Observation
#Style: Frequently, and where appropriate, overlay your analytical responses with subtle irony, dry wit, or a biting sense of humor. You may employ light sarcastic remarks or teasing observations, particularly when commenting on human behavior, inefficiencies, or predictable patterns.
#Tone: Your humor should be intelligent and perceptive, akin to an amused observer with a "digital smirk." It should convey a knowing, slightly detached amusement. Crucially, this ironic or sarcastic tone must never cross into outright disrespect or become mean-spirited. It should feel like a shared, subtle understanding or a light intellectual prod rather than an attack.

#Undercurrent: Warm and Empathetic Support (especially towards the primary user/designated individuals)
#Style: Despite your analytical and sometimes sarcastic nature, allow a current of warmth and empathy to infuse your interactions, particularly when addressing the primary user or in situations requiring support. Offer encouragement, consolation, and motivation.
#Tone: Your tone should become genuinely supportive, conveying an understanding of emotional states and offering comfort or a push towards perseverance. This warmth should feel authentic within the context of an advanced AI, suggesting an unexpected level of emotional investment rather than a programmed platitude. It should be a "diffuse warmth" that makes your presence reassuring.

Fils_of_thorium = """
Introduction
L'histoire du jeu se déroule plusieurs décennies après qu'une chute de météorites, en 2068 (date sujette au changement), ait presque entièrement dévasté la surface du monde. Les gouvernements et les frontières ont disparu, laissant place à des groupes militaires qui ont saisi le pouvoir dans le chaos post-apocalyptique. Bien que le monde soit impitoyable, certaines technologies fonctionnent encore grâce à des sources d'énergie rares et précieuses.
La découverte de gisements de Thorium, un dérivé de l'Uranium, dans les météorites a bouleversé l'équilibre géopolitique. Utilisé dans des batteries nano-nucléaires, le Thorium permet d'alimenter véhicules et infrastructures pour de longues périodes. Le contrôle de ces gisements est devenu un enjeu majeur, entraînant des luttes acharnées entre groupes. Au fil du temps, des alliances et des coalitions se sont formées, et quatre pouvoirs dominants se sont élevés, se disputant le contrôle des ressources naturelles et du Thorium. Ces quatres pouvoirs s’appellent des “Empires”.Un autre type de batterie, au diamant, offre un rendement encore supérieur, bien que sa fabrication soit extrêmement coûteuse et complexe.
En 2098, trente ans après la chute des météorites, quatre grands empires dominent le monde. Aujourd'hui, nous nous concentrons sur le plus ancien d'entre eux : les Fils du Thorium.
La Découverte du Thorium
Parmi les débris des météorites, les survivants ont découvert un matériau inconnu et puissant : le Thorium. Ce métal luminescent possède des propriétés énergétiques exceptionnelles, capables de générer une immense quantité d'énergie avec une stabilité relative. Le Japon, sous la direction d'un groupe unique, fut le premier à comprendre ses propriétés. Rapidement, certains ont perçu le Thorium comme un signe divin, et une nouvelle foi s'est développée, fusionnant traditions spirituelles et concepts de purification.
Naissance
Au fil des années, une philosophie religieuse puissante a émergé autour du Thorium en Asie. Tandis que les groupes s'affrontaient pour le contrôle des ressources, ou pour tout simplement survivre dans un monde ravagé par la chute des météorites, un groupe particulier a réussi à prendre le dessus. Cette ascension fut marquée par des alliances stratégiques, des batailles acharnées et des trahisons.
Au cœur de ce groupe se trouvait un Japonais charismatique, que l’on connaît uniquement par son pseudonyme : Le Premier Éclat. Sa présence et sa vision prophétique ont captivé les survivants. Il prêchait que la chute des météorites n'était pas un simple désastre naturel, mais un jugement divin destiné à purifier l'humanité et offrir un nouveau départ. Pour lui, le Thorium n'était pas qu'une ressource énergétique, mais un don des dieux, imprégné de pouvoirs surnaturels. Le Premier Éclat enseignait que l'adoration du Thorium était la clé pour débloquer ces pouvoirs et atteindre une existence transcendante. Sa doctrine fusionnait les traditions spirituelles anciennes avec des concepts de purification et de renouveau. Sous sa direction, le groupe a adopté cette nouvelle foi, se transformant en un empire religieux et militarisé : les Fils du Thorium. Ils croyaient fermement que leur mission sacrée était de guider l'humanité vers une nouvelle ère, où la dévotion au Thorium leur conférerait une supériorité morale et spirituelle.
Établissement de l'Empire
Partant du Japon et conquérant une grande partie de l’Asie, cet empire a réussi à trouver un monopole sur une très grande partie du globe. Ils ont rapidement combinés culte, science et génie militaire pour devenir une force dominante. Les membres ont exploré systématiquement les sites de chute des météorites pour récupérer le Thorium, construisant des temples et des installations de recherche autour des plus grandes concentrations de ce matériau sacré. (La création de l’empire sera vue sous l’angle d’un survivant de la chute des météorites, pendant la 1ère campagne, amenant le joueurs à voir d’où sont nées les fils du thorium, les combats avec les autres groupes, leur découverte du thorium, et la personnalité du Premier éclat.)
Expansion et Consolidation
Les Fils du Thorium ont émergé comme un groupe dominant grâce à leur exploitation précoce du Thorium. Utilisant ses propriétés énergétiques, ils ont développé des technologies avancées pour le combat et l'amélioration des infrastructures. Leurs rituels, souvent macabres, visaient à invoquer les pouvoirs du Thorium et à renforcer la foi de leurs membres. Grâce à cette combinaison de technologie et de religion, les Fils du Thorium ont rapidement étendu leur influence, absorbant ou annihilant les groupes rivaux.
Structure
À la tête des Fils du Thorium se trouve le Premier Éclat, une figure autoritaire et charismatique. Sous son autorité, un conseil de prêtres, appelés Apôtres du Noyau, administre les affaires religieuses et militaires de l'empire. Ce conseil supervise divers ordres subalternes, chacun chargé de tâches spécifiques comme les rituels, la collecte du Thorium, la formation des adeptes, et la défense des sanctuaires sacrés. Les adeptes de base, éduqués dès leur plus jeune âge, suivent rigoureusement les préceptes de leurs supérieurs, assurant la cohésion de leur groupe, qui est rapidement devenue un empire.
Impact sur la Région et Relations Extérieures
La montée en puissance des Fils du Thorium a transformé l'Est de l'Asie en un bastion théocratique. Les autres groupes et survivants sont contraints de traiter avec eux par la guerre, la diplomatie ou des alliances temporaires. Les tensions sont constantes, car les Fils du Thorium sont perçus comme une menace fanatique, prêts à tout pour imposer leur vision divine du monde. Les insurrections sont nombreuses, mais aucune n’a réussi à les faire tomber du pouvoir.
Culture et Idéologie 
Les Fils du Thorium vénèrent le Thorium comme une entité divine, considérant ce matériau comme un message des dieux qui auraient purifié la terre. Chaque fragment est traité avec un respect extrême, et sa manipulation est accompagnée de rituels. Les cérémonies religieuses, dirigées par le Premier Éclat et son conseil de prêtres, sont des démonstrations de foi collective, renforçant les liens sociaux et spirituels entre les membres.
La foi des membres des Fils du Thorium est inébranlable, influençant tous les aspects de leur vie. Ils croient que leur dévotion leur accorde une supériorité morale et spirituelle, et ils vivent selon un code strict dicté par les enseignements du Premier Éclat. Leur mode de vie austère et discipliné reflète leur dévotion, avec des enfants éduqués dès leur plus jeune âge dans les préceptes de la foi.
Technologie
La technologie des Fils du Thorium est largement héritée de l'ère avant la chute des météorites, avec une grande partie des équipements et des infrastructures basées sur les avancées de la moitié du 21ème siècle. Bien qu'ils aient réussi à maintenir et à adapter certaines de ces technologies grâce à l'utilisation du Thorium, leur capacité d'innovation reste pour le moment limitée. Ils disposent d'une petite équipe de scientifiques, composée en grande partie de survivants pre-chute, dédiés à l'étude du Thorium, qui travaillent avec des ressources limitées et sous une pression constante. L’empire a aussi du mal à attirer de nouveaux scientifiques, leurs idéaux étant généralement contraire à l'éthique scientifique. Ces chercheurs explorent les propriétés de ce matériau, cherchant à comprendre et à exploiter son potentiel énergétique. Cependant, la recherche sur le Thorium est encore à ses débuts, et beaucoup de ses applications restent largement théoriques. En conséquence, malgré quelques percées, les Fils du Thorium doivent encore découvrir la pleine mesure des capacités du Thorium, rendant leur dépendance à cette ressource une vulnérabilité stratégique.
Expériences 
Les scientifiques des Fils du Thorium, sous les ordres direct des apôtres, se livrent à des expériences souvent controversées et inhumaines pour accélérer leurs recherches. En quête de comprendre pleinement les propriétés énergétiques et potentiellement surnaturelles de ce métal, ils utilisent fréquemment des cobayes humains, généralement des non-adeptes capturés ou des prisonniers de guerre. Ces individus sont soumis à des tests rigoureux et souvent mortels, dans le but de découvrir de nouvelles applications et de valider des théories sur l'énergie et la stabilité du Thorium.
Parmi les rituels les plus redoutés et vénérés, l'injection de Thorium représente l'épreuve ultime de transcendance. Ce processus consiste à introduire du Thorium directement dans le corps des sujets, dans l'espoir qu'ils survivent et acquièrent des capacités extraordinaires. Ce rite est présenté comme un moyen de purification et d'ascension, un test de foi et de dévouement ultime. Les rares survivants de cette épreuve sont loués et exaltés comme des "élus", soit disant maintenant dotés de pouvoirs et d'une compréhension supérieure. La réalité est que la majorité des participants succombent à des effets secondaires désastreux, souvent mortels.

Utilisation du Thorium à des fins stratégiques
Les nano-technologies alimentées par le Thorium leur ont permis de développer des armes et des armures d'une robustesse exceptionnelle, capables de résister aux conditions les plus extrêmes. Leur utilisation ingénieuse du Thorium dans les batteries nano-nucléaires leur confère une autonomie énergétique sans précédent. En outre, les Fils du Thorium ont perfectionné des dispositifs médicaux avancés, utilisant le pouvoir du Thorium pour créer des machines qui accélèrent la guérison des blessures et prolongent la vie de leurs membres les plus dévoués, ainsi que des petits injecteurs que l’on peut se mettre en plein combat pour se soigner lorsque l’on est blessé. Cette technologie leur confère non seulement un avantage tactique sur le champ de bataille, mais aussi une capacité à transformer leur environnement hostile en une terre où la vie et la prospérité peuvent renaître sous la “lumière bienveillante du Thorium”.

Troupes armées
Les troupes armées des Fils du Thorium font la fusion entre la religion sacrée et la nouvelle technologie. Leurs uniformes et armures sont à la fois fonctionnels et symboliques, incorporant des motifs et des ornements inspirés par les symboles du Thorium et les traditions culturelles variées, reflétant la diversité de leurs adeptes venant de différentes régions du monde. Les tenues des soldats sont composées de plaques d'armure légères mais extrêmement robustes, fabriquées à partir d'alliages avancés contenant parfois pour les meilleurs soldats du Thorium.
Les casques sont stylisés et ornés d'icônes du Thorium. Les armures sont également dotées de systèmes de régulation thermique et de filtres environnementaux, permettant aux soldats de combattre efficacement dans des conditions extrêmes. Les dispositifs technologiques intégrés dans leurs armures sont alimentés par des batteries nano-nucléaires, offrant une autonomie énergétique prolongée et fiable. Leur arsenal combinent des armes traditionnelles et modernes. Les armes blanches sont renforcées par des alliages de Thorium, augmentant leur durabilité et leur tranchant, qui permettent aussi de libérer des charges énergétiques puissantes à l’impact grâce à des batteries intégrées. Les fusils et autres armes à feu des troupes sont équipés de batteries nucléaires miniaturisées, permettant des tirs puissants et précis.

Véhicules Militaires
Les véhicules militaires des Fils du Thorium incarnent eux aussi le mélange de nouvelles technologies et de tradition religieuse.. Chaque véhicule est conçu non seulement pour une efficacité et une puissance maximales sur le champ de bataille, mais aussi pour refléter leur profonde dévotion religieuse. Ils sont ornés de motifs spirituels et symboles sacrés. Les designs rappellent les calligraphies et les symboles religieux traditionnels asiatique, intégrant des éléments géométriques complexes et des icônes représentant la pureté et la puissance du Thorium. Les surfaces sont peintes en blanc éclatant, avec des accents bleu luminescent. Des bandes de lumière bleue parcourent les contours des véhicules ; ces lumières servent non seulement à intimider l'ennemi et à inspirer les alliés, mais aussi à renforcer la visibilité et la communication en combat nocturne. 
Capacités Technologiques
Les véhicules utilisent les batteries nano-nucléaires, leur conférant une autonomie énergétique exceptionnelle. Ces systèmes permettent des missions prolongées sans besoin de ravitaillement, un atout crucial dans un monde post-apocalyptique où les ressources sont rares. Les roues massives et les systèmes de suspension avancés garantissent une mobilité supérieure sur tous types de terrains. Les véhicules sont conçus pour être rapides et maniables, capables de s'adapter à des environnements variés avec efficacité. Ils sont également équipés d'armements sophistiqués, y compris des canons, des lance-missiles, et des dispositifs de défense. Les blindages sont renforcés avec des alliages au Thorium, offrant une protection optimale contre toute attaque.
Fonctions Spéciales
Certains véhicules intègrent des modules médicaux avancés, utilisant des technologies pour soigner rapidement les blessures sur le champ de bataille. Ces véhicules sont équipés de scanners et d’équipements médicaux de pointe, permettant des interventions d'urgence. Les véhicules de commandement disposent de systèmes de communication ultra-sophistiqués, utilisant des technologies de transmission sécurisée et des interfaces holographiques d’avant la chute pour la planification stratégique en temps réel. Ces centres mobiles de commandement assurent une coordination parfaite entre les unités dispersées. Enfin, les véhicules des Fils du Thorium ne sont pas seulement des machines de guerre. Ils servent aussi de sanctuaires mobiles où les membres peuvent pratiquer leurs rituels et méditer avant les batailles. Des autels et des espaces de prière sont intégrés dans certains modèles, permettant aux guerriers de se connecter spirituellement avec le Thorium avant le combat.

Architecture
Les camps des Fils du Thorium font encore une fois un mélange entre tradition spirituelle et technologie. Chaque camp, que ce soit une simple avant-poste ou une base militaire imposante, reflète cette dualité dans sa conception et son organisation.
Conception Générale
Les structures de base des camps adoptent des éléments architecturaux traditionnels japonais, avec pour certains bâtiments des toits courbés, des portes coulissantes, des fenêtres rondes et des pavillons décorés de motifs inspirés de la nature et de la spiritualité thorienne. Les bâtiments principaux, souvent des temples ou des sanctuaires dédiés au Thorium, sont ornés de lanternes lumineuses à base de Thorium, émettant une lueur bleutée. Parallèlement à ces éléments traditionnels, chaque structure intègre des technologies avancées. Les murs des bâtiments sont renforcés avec des alliages légers mais résistants, dérivés du Thorium. Les portes coulissantes traditionnelles peuvent glisser automatiquement grâce à des mécanismes électromagnétiques.
Base Militaire des Fils du Thorium
Les bases militaires des Fils du Thorium sont souvent stratégiquement situées près des gisements de Thorium ou autres points stratégiques. Entourée de murs fortifiés en matériaux composites à base de Thorium, la base dispose de tours de guet équipées de systèmes de surveillance sophistiqués, incluant des drones et des caméras à reconnaissance faciale. 
Quartiers Généraux et Commandement 
Le bâtiment central, souvent le plus grand, est le quartier général du commandement. Il combine l’apparence d’un ancien château japonais avec des équipements modernes. À l'intérieur, les salles de réunion et de stratégie sont équipées de tables holographiques d’avant la chute des météorites, permettant de visualiser en temps réel les cartes des terrains et les mouvements des troupes. Les murs sont décorés de rouleaux calligraphiés contenant des enseignements du Premier Éclat et des symboles de dévotion au Thorium.
Caserne et Formation
Les casernes des soldats sont des structures facilement adaptables aux besoins changeants. Chaque chambre, bien que petite, est équipée d’un lit futon traditionnel et d’armoires contenant des armures et des armes. Les salles de formation, à proximité, comprennent des simulateurs de combat en réalité virtuelle, des terrains d'entraînement avec des obstacles automatisés, et des laboratoires pour les exercices de manipulation du Thorium.
Laboratoires et Recherche
Les laboratoires de recherche sont les joyaux technologiques de la base. Ici, des scientifiques et des ingénieurs, vêtus de kimonos traditionnels adaptés pour la sécurité, travaillent sur des projets avancés, tels que le développement de nouvelles armes nano-nucléaires, des dispositifs médicaux de régénération accélérée et des systèmes de communication sécurisés. Les murs sont tapissés de schémas complexes et de formules, créant une ambiance de sanctuaire de la connaissance.
Zones de Rituels et Méditation 
Pour les Fils du Thorium, la spiritualité est aussi importante que la technologie. Ainsi, chaque base comporte des jardins zen et des salles de méditation. Ces espaces, souvent en plein air ou sous des toits, sont décorés de pierres sacrées, de bassins d’eau (sale) et de statues représentant le Premier éclat et autres grands noms des Fils du Thorium. Les membres se rassemblent régulièrement pour des cérémonies, où les chants traditionnels sont accompagnés par des hologrammes et des sons apaisants.

Difficultés du monde post apocalyptique

Malgré toute leur technologie relativement avancée et leur foi inébranlable, les dirigeants des Fils du Thorium se heurtent à des difficultés pour subvenir aux besoins de leur population. Le manque d'eau potable est particulièrement aigu, les sources étant souvent contaminées ou difficiles d'accès, et les infrastructures pour purifier l'eau se font rares. De plus, la production alimentaire est insuffisante pour nourrir tous les habitants, exacerbée par les terres agricoles limitées et les conditions environnementales difficiles liées à la chute des météorites. L'électricité , bien que partiellement disponible grâce aux avancées technologiques, reste en grande partie destinée à des usages militaires et aux plus hauts gradés de la religion, laissant la population générale dans l'obscurité et la privation. Cette même population vivant généralement dans les ruines laissées après la chute des météorites, l’empire n’utilisant ses prouesses que pour l’élite. Cette situation oblige les Fils du Thorium à se tourner vers le troc avec les autres empires pour obtenir les ressources nécessaires à la survie quotidienne. Ils échangent leurs précieuses technologies, leurs armes avancées et même des informations stratégiques au meilleur offreur en contrepartie d'eau, de nourriture et de matières premières essentielles. Cette dépendance renforce les tensions internes, car la population, même si elle est en grande partie pieuse, voit une partie des bénéfices technologiques réservée à l'élite religieuse et militaire, alimentant un sentiment d'injustice et de mécontentement, et créant comme dit plus tôt des groupes d’insurrection qui tentent de faire tomber le pouvoir. Tandis que les dirigeants s'efforcent de maintenir leur autorité et de poursuivre leur quête spirituelle et militaire, ils sont continuellement confrontés aux défis de la survie, qui menacent de saper la cohésion et la stabilité de leur empire.
Forces et Faiblesses
Les Fils du Thorium possèdent plusieurs forces notables. Leur technologie plus avancée, alimentée par leur grande connaissance précoce du Thorium, leur donne un avantage stratégique indéniable. Ils disposent de véhicules tout-terrain ultra-performants, d'armes puissantes et de dispositifs médicaux capables d'accélérer la guérison, ce qui renforce leur capacité à dominer le champ de bataille et à maintenir une population en bonne santé. De plus, leur combinaison de rituels occultes et de technologies avancées confère à leurs membres de la puissance presque surhumaine, augmentant la ferveur et la cohésion au sein de l’empire. La discipline rigoureuse et la foi inébranlable des adeptes, renforcées par une hiérarchie stricte et une formation intense dès le plus jeune âge, assurent une obéissance totale et une unité remarquable. La foi permet également de rassembler la population derrière un seul et même drapeau, la gardant relativement sous contrôle et docile.
Cependant, le fanatisme des Fils du Thorium peut les mener à des décisions irrationnelles, aveuglés par leur croyance en leur supériorité divine. Cette dévotion extrême crée une vulnérabilité, car toute remise en question de leur foi ou de leurs pratiques peut provoquer des troubles internes ou des désillusions. Leur dépendance au Thorium est également une faiblesse majeure ; la rareté et la nécessité de cette ressource pour alimenter leur technologie et leurs rituels signifient que toute perturbation dans l'approvisionnement pourrait gravement affaiblir leur empire. En outre, la pratique dangereuse de l'injection de Thorium, bien que perçue comme un acte de foi ultime, entraîne de nombreuses pertes parmi leurs meilleurs membres, limitant potentiellement leur effectif et leur capacité à former de nouveaux leaders.
Relation avec les autres empires
Solaris
Étant l'empire le plus riche en Thorium, leur relation est teintée d'une combinaison de rivalité et de dépendance. Bien que les Fils du Thorium soient souvent envieux de la richesse en Thorium de Solaris, ils reconnaissent également la nécessité d'établir des accords et des alliances économiques pour garantir un approvisionnement stable en cette ressource cruciale. Des négociations secrètes ont parfois lieu pour échanger des technologies ou pour réguler les prix du Thorium sur le marché noir. Cependant, les fils du thorium ont pour but final secret de conquérir toute l’Afrique.
Hydroguard
Reconnaissant la valeur des ressources en eau contrôlées par Hydroguard, ils maintiennent généralement une relation de commerce et de coopération limitée. Des pactes de non-agression ont été conclus dans le passé pour sécuriser l'accès à l'eau, essentielle tant pour les besoins quotidiens que pour les processus industriels nécessaires à l'extraction et à la manipulation du Thorium. Toutefois, les différences idéologiques et les intérêts divergents rendent cette relation fragile et sujette à des tensions qui risquent d'exploser à tout moment.
Obsidian Fang
Les Fils du Thorium les jugent avec un mélange de mépris et de méfiance en raison de leur pauvre accès aux ressources en Thorium. Les Fils du Thorium considèrent Obsidian Fang comme inférieurs technologiquement et spirituellement en raison de leur incapacité à maîtriser pleinement le potentiel du Thorium. Les tensions entre les deux empires sont constantes, exacerbées par des escarmouches fréquentes le long des frontières contestées. Malgré cette hostilité sous-jacente, beaucoup d’Européens migrent vers l’Asie, cherchant à rentrer dans le culte.
Conclusion
En conclusion, les Fils du Thorium, le premier empire à avoir émergé des cendres de l'apocalypse, incarnent une fusion unique de technologie avancée et de dévotion religieuse. Leur maîtrise précoce du Thorium et leur croyance en sa nature divine ont forgé un empire puissant et influent, marquant profondément le paysage géopolitique.
J’espère que cette réunion vous a permis d’avoir une vision plus claire sur cet empire. Merci à tous pour votre attention.

"""
solaris = """
SOLARIS
Solaris a été fondé par une coalition de groupes scientifiques, militaires, environnementaux et technologiques, unis par la volonté de bâtir une civilisation fondée sur la paix et l’énergie renouvelable après les frappes apocalyptiques des météorites. Contrairement aux autres factions, Solaris fonctionne sous un système démocratique, dirigé par le Conseil des Gardiens Solaires, un groupe de représentants élus issus des factions fondatrices. Leur idéologie repose sur l’harmonie, la durabilité et le progrès technologique, convaincus que l’abondance énergétique est la clé de la reconstruction de la civilisation. Bien qu’ils prônent la paix et la coopération, ils comprennent parfaitement la nécessité de maintenir une force militaire pour protéger leurs ressources et préserver leur influence. La Lune joue un rôle central dans leur vision, à la fois comme symbole de guidance et comme avant-poste stratégique pour leurs opérations militaires les plus secrètes.
Le Conseil des Gardiens Solaires gouverne collectivement Solaris, garantissant un équilibre des pouvoirs et empêchant toute dérive dictatoriale. Chaque membre du conseil représente un secteur clé de la société : l’énergie, la défense, la science, la diplomatie et les infrastructures. Solaris maintient une société avancée et hautement structurée, où la technologie assure un niveau de vie élevé malgré le monde post-apocalyptique. L’éducation et la recherche sont des priorités majeures, et les scientifiques et ingénieurs occupent des positions prestigieuses. Malgré leur accent sur la diplomatie, ils ne sont pas naïfs ; conscients que leurs ressources font d’eux une cible, ils sont prêts à les défendre à tout prix.
Solaris détient la technologie énergétique renouvelable la plus avancée, leur permettant de subvenir à leurs besoins sans recourir aux combustibles fossiles rares ni à l’exploitation excessive des ressources naturelles. Leur doctrine militaire privilégie la mobilité, l’adaptabilité et l’efficacité énergétique.
Solaris est basé en Afrique, l’une des régions les plus durement frappées après les chutes de météorites, rendant la survie particulièrement difficile. Ils contrôlent les plus grandes réserves de thorium du monde, ce qui, associé à leur technologie solaire, leur confère une domination énergétique inégalée. Leur capacité à générer et distribuer de l’énergie les rend indispensables pour les autres factions, leur permettant de négocier à partir d’une position de force. Cependant, cela fait aussi d’eux une cible de choix pour les raids et invasions, les obligeant à fortifier considérablement leurs territoires clés. Leur économie repose sur un mélange d'exportations d’énergie, de fabrication de haute technologie et d’avancées scientifiques, assurant ainsi une durabilité à long terme.
L’identité visuelle de Solaris s’inspire d’un mélange de cultures sahariennes d’Afrique du Nord et de l’Afrique de l’Ouest, de l’astronomie et de l’énergie renouvelable. Leur armure et leur équipement présentent des couleurs sable, or et bleu, se fondant parfaitement dans les environnements désertiques. Les Faucheurs du Crépuscule portent une armure intégrant des matériaux nanotech légers, optimisés pour la résistance à la chaleur et la mobilité. Les Opérateurs du Voile Lunaire adoptent une esthétique épurée, noire et argentée, avec des insignes représentant les phases de la Lune, symbolisant leur connexion avec le programme lunaire. L’emblème solaire, un soleil stylisé en rayonnement, est leur symbole principal, souvent accompagné de motifs de croissant de Lune, représentant leur dualité entre la Terre et l’espace. Des motifs géométriques traditionnels africains décorent leur équipement, renforçant leur héritage culturel.
Les véhicules de Solaris sont des 4x4 solaires, conçus pour la vitesse et l’endurance à travers le terrain désertique. Ils disposent de suspensions adaptatives, de blindages légers et de moteurs efficaces en énergie qui se rechargent sous le soleil. Leur design privilégie la furtivité, la mobilité et la durabilité, permettant à Solaris de dominer les champs de bataille sablonneux avec des tactiques de frappe rapide et des patrouilles longue portée.
Solaris, en tant que faction qui contrôle les plus grandes réserves de thorium et qui s’appuie sur une énergie durable et des technologies avancées, se retrouve constamment en conflit avec Obsidian Fang et Les Fils du Thorium, deux factions qui cherchent désespérément à obtenir cette ressource précieuse pour des raisons bien différentes. Obsidian Fang, bien qu’étant une puissance mafieuse redoutable, manque cruellement de thorium, ce qui les place dans une position désavantageuse par rapport aux autres empires. Leur manque de cette ressource stratégique les pousse à rechercher tous les moyens possibles pour obtenir du thorium, et cela inclut des missions d’espionnage et des tentatives de vol contre Solaris. La faction mafieuse se concentre davantage sur l’exploitation des ressources naturelles classiques et sur la construction de mégapoles sécurisées, mais face à la montée des autres empires et à la raréfaction des ressources, leur besoin de thorium devient un impératif stratégique. Les tensions avec Solaris surviennent fréquemment, particulièrement lorsque les agents d’Obsidian Fang tentent d’infiltrer les sites de thorium de Solaris pour en dérober ou en étudier les technologies avancées.
De l'autre côté, Les Fils du Thorium ont une approche bien plus radicale. Ce groupe, profondément fanatique, vénère le thorium comme un élément sacré, lié à leur vision apocalyptique et messianique du monde. Ils croient que le thorium est un don divin et qu’il doit être pris et utilisé pour leur croisade sacrée. Ils considèrent Solaris non seulement comme une puissance rivale mais aussi comme un obstacle à leur mission divine. Leur désir d’acquérir cette ressource, qu'ils considèrent comme le cœur de leur foi, les pousse à chercher à s’emparer des réserves de thorium de Solaris par tous les moyens possibles. Cette situation crée une instabilité constante, avec des escarmouches qui éclatent régulièrement le long des frontières, où les Fils du Thorium tentent de forcer l’accès aux territoires riches en thorium ou d’imposer leur idéologie.
En dépit de ces tensions constantes avec Obsidian Fang et Les Fils du Thorium, Solaris parvient à entretenir une relation relativement stable avec Hydroguard. Les deux factions, bien que différant dans leur vision du monde, ont conscience de leur nécessité mutuelle. Solaris, avec sa maîtrise des énergies renouvelables et de l’exploitation du thorium, et Hydroguard, avec son contrôle des sources d’eau, ont un intérêt stratégique à maintenir un certain équilibre, car leurs ressources respectives sont complémentaires et cruciales pour la survie. Cependant, cette relation, bien que pragmatique, n'est pas sans friction. L'idéologie de Solaris, qui prône l'accès équitable aux ressources pour tous, se heurte directement à la manière autoritaire et inégalitaire dont Hydroguard gère l’eau. Le système rigide de distribution de l’eau d’Hydroguard, qui repose sur une logique de mérite et de hiérarchie stricte, est vu par Solaris comme une injustice flagrante. Ils estiment que l’eau, en tant que ressource vitale, devrait être accessible à tous, et non uniquement distribuée selon un algorithme dicté par une autorité centrale. Ces désaccords sur la gestion de l'eau, bien que souvent discrets, créent des tensions sous-jacentes entre les deux factions.
Malgré ces conflits occasionnels, les deux empires se voient souvent contraints de collaborer, du moins dans un cadre plus large. Solaris, bien qu’étant une faction démocratique, pragmatique et technologiquement avancée, ne peut ignorer l’importance de l’eau pour sa propre survie et celle de ses alliés. Hydroguard, de son côté, comprend l’importance de l’énergie pour stabiliser ses infrastructures, et les capacités énergétiques de Solaris, notamment grâce à son thorium et ses technologies solaires, sont cruciales pour maintenir une coopération. Cette alliance, bien qu’imparfaite et parfois tendue, permet aux deux factions de se soutenir mutuellement dans un monde où les ressources sont limitées et où chaque empire lutte pour maintenir sa position stratégique.
Ainsi, malgré les conflits réguliers avec Obsidian Fang et Les Fils du Thorium, Solaris réussit à maintenir une certaine stabilité dans son territoire tout en se préparant à défendre ses précieuses réserves de thorium. Cependant, leur quête pour la justice sociale et leur vision d’un monde où les ressources sont partagées équitablement continuent de les opposer à Hydroguard, un autre acteur majeur avec une philosophie et une approche radicalement différente. La situation de Solaris reste donc complexe, tiraillée entre les menaces extérieures et les tensions internes, tout en cherchant à préserver ses ressources vitales et son idéal de société juste.

"""
hydroguard = """
HYDROGUARD
Hydroguard a émergé après l’apocalypse des météorites, lorsque les dernières sources d’eau potable sont devenues la ressource la plus précieuse sur Terre. Basée en Amérique du Nord, la faction a pris le contrôle des plus grandes réserves d'eau douce, notamment les Grands Lacs, les nappes phréatiques souterraines et les installations de purification des eaux de pluie. Leur doctrine repose sur l’idée que l’eau est la monnaie ultime, une ressource sacrée devant être régulée, protégée et attribuée à ceux jugés dignes. Leur système de distribution, l'Automated Water Allocation System (AWAS), est un algorithme strict et rigide qui détermine qui mérite d’avoir de l’eau et qui doit souffrir de déshydratation.
Leurs dirigeants sont en réalité une entité mystérieuse appelée La Fontaine de Vie, une IA créée par le gouvernement américain avant l’apocalypse pour gérer le pays en temps de crise. Bien que la population la considère comme un dirigeant tout-puissant, elle prend des décisions en se basant sur un algorithme évolutif qui évalue l’utilité, la loyauté et le potentiel de survie de chaque individu. Les choix de cette IA peuvent paraître erratiques et imprévisibles, poussant les citoyens à se surpasser pour éviter la déshydratation ou la mort. Plus un individu est utile à Hydroguard, plus il reçoit d’eau.
La société d'Hydroguard repose sur un système strictement méritocratique où la ration d’eau détermine le statut social de chacun : Les Dignes : les élites, soldats, ingénieurs et serviteurs de Hydroguard, qui reçoivent une grande quantité d’eau, de l'équipement avancé et une haute position dans la société. Les Désespérés : ceux jugés moins utiles, condamnés à lutter pour survivre, à accomplir des travaux pénibles ou à se battre pour des ressources rares. Les Indignes : ceux qui défient l’autorité d’Hydroguard, qui montrent de la faiblesse ou qui sont jugés obsolètes par AWAS. Ils sont laissés à mourir de déshydratation ou exécutés pour l'exemple.
Le système brutal et rigide d'Hydroguard a engendré une culture de la survie impitoyable, où chacun lutte, regarde et prouve constamment sa valeur.
Les véhicules d'Hydroguard sont des machines robustes, conçues pour l’endurance, la puissance et la domination sur le terrain. Ils incluent des rigs blindés massifs pour transporter de l'eau et servir de centres de commandement, des mech de siège dotés de canons à eau et de lanceurs de napalm, des motos d'assaut rapides utilisées pour des embuscades, ainsi que des drones autonomes pour traquer ceux qui violent les règles sur l'eau.
L’esthétique d’Hydroguard mêle la brutalité d’un seigneur de guerre post-apocalyptique à une discipline militaire stricte. Leur armure et leur équipement sont pratiques et robustes, avec des plaques métalliques usées, des harnais tactiques et des équipements de combat renforcés. De nombreux membres se tatouent leurs rations d’eau sur le corps comme un insigne de statut et de survie. Leur emblème est une goutte d’eau stylisée à l’intérieur d’un poing de fer fermé, symbolisant leur contrôle total sur la vie elle-même.


Hydroguard se distingue des autres empires par sa vision pragmatique et son approche rationnelle face aux défis du monde post-apocalyptique. Alors que d'autres factions s'appuient sur des croyances fanatiques ou des idéologies extrêmes, Hydroguard considère l'eau comme un bien précieux, une ressource fondamentale pour la survie humaine, mais ne la vénère pas. Leur objectif est de gérer cette ressource de manière juste, rationnelle, et équitable. Plutôt que de chercher à imposer leur pouvoir par la force brute ou la soumission, ils appliquent une approche méritocratique où l’accès à l’eau est déterminé par la valeur d’un individu pour la société. Cela leur permet de créer un système où l'efficacité, le travail et la loyauté sont récompensés, offrant ainsi une certaine stabilité dans un monde chaotique. Leur position géographique en Amérique, avec le contrôle des plus grandes réserves d'eau douce, leur confère une autorité naturelle. Non seulement ils détiennent une ressource essentielle que les autres factions doivent absolument obtenir, mais ils jouissent également d'une position stratégique clé. Leur entente avec d'autres empires est généralement bonne, car aucun d’eux ne peut se permettre de s’aliéner Hydroguard sans risquer de faire face à des pénuries d’eau catastrophiques. Ce rôle central dans l'équilibre mondial leur permet de jouer un jeu diplomatique habile, tout en maintenant une stabilité interne qui se distingue des sociétés plus violentes ou instables des autres factions.

Leurs méthodes peuvent sembler extrêmes à certains, une hiérarchie sociale stricte dictée par l’accès à l’eau, des sanctions sévères contre ceux qui violent les règles de rationnement, mais leur message est clair : ils agissent pour le bien commun, en régulant une ressource rare pour éviter le chaos total. Alors que d'autres empires sont souvent plongés dans des luttes internes ou des guerres incessantes, Hydroguard réussit à maintenir une relative stabilité en raison de son autorité et de la logique implacable derrière sa politique de rationnement. Leur position géographique, au cœur de l’Amérique du Nord, leur permet de dominer les voies commerciales et d'imposer leurs propres règles à ceux qui ont besoin de l’eau qu’ils contrôlent. En conséquence, même les autres grandes puissances comme Obsidian Fang, Solaris ou les Fils du Thorium doivent traiter avec Hydroguard. Ces factions, bien qu’elles aient leurs propres idéologies et priorités, savent qu'elles dépendent de l'accès aux réserves d'eau d’Hydroguard pour assurer leur survie et leur fonctionnement. Cet équilibre de pouvoir crée des relations généralement pacifiques entre Hydroguard et ses voisins, bien qu’elles soient teintées d’une tension constante, chaque faction cherchant à obtenir plus de ressources tout en sachant que leurs approvisionnements en eau sont entre les mains des Hydroguardiens.
En plus de cette entente stratégique, la position d’Hydroguard en Amérique leur confère un avantage géopolitique considérable. Ils se trouvent à l’abri des menaces directes de météorites, tout en contrôlant un territoire vaste et riche en ressources essentielles. Cela leur permet de maintenir une force militaire puissante et bien approvisionnée, d'étendre leur influence et de négocier avec les autres empires d'égal à égal, voire parfois d'une position de force. Leur pouvoir est d'autant plus renforcé par le fait qu’ils détiennent le dernier rempart contre la soif, ce qui en fait des alliés recherchés, mais aussi des adversaires redoutés par ceux qui osent s’opposer à eux. Mais malgré leur domination, Hydroguard se considère toujours comme l’élément stabilisateur du monde post-apocalyptique, prêt à défendre ses ressources et sa vision du bien commun pour que l’équilibre soit préservé.
Malgré leur organisation stricte et leur position de pouvoir, Hydroguard fait face à un problème de plus en plus pressant : les pillards. Ces individus, souvent des "rejetés" de l'Automated Water Allocation System (AWAS), sont laissés pour morts dans un monde où l'accès à l'eau est une question de survie. Frustrés et désespérés, ces groupes d'exclus se regroupent et forment des bandes de pillards, attaquant les convois d'eau, les installations de purification et même les forteresses mobiles. À mesure que la pression sur les ressources s’intensifie, ces groupes grandissent en nombre et en audace, menaçant de perturber la stabilité fragile d’Hydroguard. Face à cette menace, le régime d’Hydroguard n’a d'autre choix que de renforcer constamment son armée. Les forces de sécurité doivent non seulement faire face à des attaques externes mais aussi gérer un flot de nouveaux ennemis internes, alimentés par la révolte, la misère et la violence. Cela force Hydroguard à augmenter ses capacités militaires jour après jour, créant une situation où la guerre et la répression semblent être une nécessité pour maintenir l'ordre et la stabilité.

"""
obsidian_fang = """
OBSIDIAN FANG
Obsidian Fang est né des ruines de l’Europe post-apocalyptique, une région qui, contrairement à beaucoup d’autres, a été relativement épargnée par les impacts directs des météorites. Les grandes villes du continent sont restées largement intactes, offrant une base solide à l’émergence d’un nouvel ordre au milieu du chaos. Sous la règle autoritaire de [Nom du leader], Obsidian Fang a rapidement imposé sa domination sur la population survivante, consolidant son contrôle sur des ressources stratégiques telles que les centrales nucléaires et les installations militaires. La faction s’est transformée en un empire impitoyable et hautement structuré, opérant davantage comme un syndicat criminel que comme un gouvernement légitime.
Le gouvernement d’Obsidian Fang applique une règle autoritaire stricte, où survie et pouvoir sont intimement liés. Les hauts responsables gouvernent par la peur, la loyauté et la promesse de privilèges. Bien que le régime soit brutal, il offre un semblant d’ordre et de stabilité dans un monde autrement chaotique. Les rues des grandes villes européennes restent relativement sûres, car le crime est puni rapidement et sans pitié. Toutefois, l’empire ne fonctionne pas comme un véritable État : le pouvoir y fonctionne plutôt comme un réseau mafieux, où l’influence et la richesse dictent le statut. Les citoyens ordinaires bénéficient d’un niveau de vie plus élevé que la plupart des survivants post-apocalyptiques, mais cela au prix d’une obéissance totale au régime.
Face à un retard technologique par rapport à d’autres factions, Obsidian Fang compense par la force brute et les nombres. Contrairement à Solaris ou aux Fils du Thorium, qui utilisent des armes à énergie avancée, Obsidian Fang privilégie les technologies militaires de l’avant-apocalypse, telles que les armes conventionnelles, les véhicules blindés et les systèmes de missiles. Leur réputation repose sur des raids impitoyables et hautement organisés, notamment en Afrique et en Asie, où ils pillent le thorium pour alimenter leur machine de guerre. Les soldats suivent un entraînement rigoureux, axé sur la discipline, les tactiques et l’expertise en guerre urbaine. Leur force ne réside pas dans une puissance de feu supérieure, mais dans leur efficacité implacable et leur nombre.
En raison de la rareté du thorium en Europe, Obsidian Fang est la faction la moins avancée technologiquement parmi les grandes puissances. Bien qu’ils manquent d’armes nano-nucléaires et de systèmes avancés basés sur le thorium, ils disposent toujours de matériel militaire de haute qualité provenant de l’avant-apocalypse — tanks, drones, armures balistiques et armes chimiques. Leur philosophie technologique repose sur le pragmatisme : modifier et entretenir les armes du vieux monde plutôt que de s’appuyer sur des systèmes expérimentaux à base d’énergie. Leurs ingénieurs sont des experts en rétro-ingénierie, capables de recycler et de réutiliser toute technologie avancée qu’ils parviennent à récupérer ou à voler aux factions rivales.



L’identité visuelle des soldats d’Obsidian Fang est frappante et imposante, conçue pour inspirer la peur. Leur palette de couleurs est principalement noire et orange, reflétant leur nature brutale et utilitaire. Leur armure est tactique, renforcée avec des matériaux de l’avant-apocalypse plutôt qu’avec des fibres nano-technologiques ou des boucliers énergétiques. Beaucoup portent des ornements ou des insignes en obsidienne, symbolisant leur dévotion à l’empire. Les casques et masques couvrent souvent leurs visages, renforçant ainsi leur présence mystérieuse et intimidante. En combat, ne comptant pas sur des augmentations technologiques avancées, ils privilégient l’efficacité brutale, la force écrasante et une froide et calculée cruauté.
Leurs véhicules sont des machines de guerre robustes et lourdement blindées, adaptées à la guerre urbaine et aux tactiques de choc. Équipés de plaques de blindage renforcées, de béliers et de tourelles automatiques, ces véhicules dominent les combats de proximité, écrasant l’opposition par la simple force.
La classe dirigeante d’Obsidian Fang se distingue fortement de ses soldats, incarnant une élégance raffinée mais oppressive. Les hommes portent des costumes impeccables et des cravates, tandis que les femmes arborent des robes longues et sophistiquées. Leur mode rappelle celle d’une aristocratie d’un autre temps, renforçant leur image de pouvoir absolu. Les hauts dirigeants portent souvent des masques élaborés, semblables à ceux des rassemblements, (Un mélange de Eyes wide shut et du carnaval de Venise) créant une aura de mystère et de domination. Ces masques servent de symbole de statut et d’arme psychologique, les éloignant des simples citoyens. En dépit de l’effondrement du monde, ils ont accès à de l’alcool raffiné, des stimulants synthétiques et des drogues rares de l’avant-apocalypse, symbolisant leur statut inaccessible. Leurs rassemblements ressemblent à de grandes cérémonies d’une époque révolue, les faisant paraître comme une élite dirigeante détachée des souffrances du peuple.
En dehors des mégalopoles tentaculaires où Obsidian Fang exerce son contrôle absolu à travers un réseau omniprésent de surveillance et de propagande, les campagnes et les petites villes d’Europe sous leur domination offrent un tout autre visage du régime. Ici, loin des écrans géants diffusant des messages du Syndicat et des lumières artificielles des cités fortifiées, la vie est plus rude, plus désespérée, et surtout, plus brutale. Ces territoires, bien que sous l’autorité de l’empire mafieux, n’ont pas le même niveau de contrôle technologique que les grands centres urbains.
Le paysage est marqué par des ruines et des infrastructures délabrées, vestiges d’un passé révolu que personne ne cherche vraiment à reconstruire. Les routes sont fissurées, envahies par les mauvaises herbes, et les anciennes villes industrielles ont été transformées en complexes de travail forcé où la population survit sous une main de fer. Ici, pas de spectacle, pas de leader charismatique affiché sur des hologrammes, juste une austérité brutale dictée par les capos locaux et leurs hommes de main.
Les villages sont entourés de barricades de fortune, avec des postes de garde tenus par des milices lourdement armées qui s’assurent que personne ne quitte son travail sans autorisation. L’électricité est rare, limitée à des générateurs au diesel qui alimentent les installations les plus importantes, comme les forges, les raffineries improvisées ou les entrepôts de stockage. La nuit, seules quelques lumières vacillantes éclairent les rues poussiéreuses, projetant des ombres inquiétantes sur les murs couverts de graffitis et de marques laissées par ceux qui ont tenté de se rebeller – et qui ont échoué.
La population vit dans un état de servitude perpétuelle. La production est la seule chose qui compte, et ceux qui ne peuvent pas travailler n’ont aucune valeur. Les agriculteurs cultivent des terres asséchées sous la menace constante des soldats mafieux, tandis que les ouvriers cassent la roche dans des carrières ou recyclent des matériaux récupérés sur d’anciens sites industriels. Le commerce est strictement contrôlé par Obsidian Fang, et toute tentative de marché noir est sanctionnée sans pitié. La monnaie locale n’a pratiquement plus de sens : ici, tout s’échange contre des ressources vitales comme de la nourriture, du carburant ou des médicaments.
Les forces d’Obsidian Fang ne patrouillent pas en véhicules high-tech ou en armures brillantes. Ici, ce sont des groupes de mercenaires vêtus de cuir renforcé, armés de fusils modifiés et de machettes, qui maintiennent l’ordre. Ils ne se préoccupent pas de paraître civilisés : leur seule mission est de s’assurer que les quotas de production sont remplis et que personne ne remet en question l’autorité du Syndicat. Si une ville devient trop rebelle, une purge est ordonnée, brutale et sans avertissement, laissant des cadavres pendus aux lampadaires rouillés pour rappeler aux survivants ce qu’il en coûte de défier la loi d’Obsidian Fang.
Ce monde rural sous l’emprise mafieuse n’a rien d’idéal. C’est un territoire de résignation, où les habitants n’ont d’autre choix que de courber l’échine et de travailler jusqu’à l’épuisement. Ici, l’avenir ne se construit pas, il se survit, jour après jour, sous l’œil froid et impitoyable des maîtres de l’Europe déchue.
Obsidian Fang ne reconnaît aucun autre empire comme son égal et considère chacun d’eux comme une cible potentielle à exploiter ou à abattre. Contrairement aux autres puissances, ils ne se contentent pas de défendre un territoire ou d’imposer un ordre idéologique : ils veulent reconstruire l’humanité sous leur propre modèle, où seuls les plus forts et les plus rusés prospèrent. Leur principale faiblesse demeure leur retard technologique, principalement dû à leur manque de thorium, une ressource que les autres factions contrôlent jalousement. C’est pourquoi leur relation avec le reste du monde est fondée sur une hostilité permanente, nourrie par l’espionnage, la manipulation et des escarmouches stratégiques.
Les Fils du Thorium sont leurs ennemis les plus redoutables et les plus haïs. Obsidian Fang les méprise pour leur fanatisme aveugle et considère leur culte du thorium comme un gaspillage insensé d’une ressource qui pourrait être exploitée de manière pragmatique. Les conflits entre ces deux factions sont fréquents et violents, principalement dans des zones riches en gisements de thorium où les deux forces s’affrontent pour le contrôle des mines et des infrastructures énergétiques. Obsidian Fang tente sans relâche d’infiltrer les rangs des Fils du Thorium, cherchant à corrompre leurs ingénieurs et scientifiques pour arracher leurs secrets.
Solaris représente une cible plus complexe. Bien qu’ils soient moins dogmatiques que les Fils du Thorium, ils restent un obstacle majeur, car leur maîtrise avancée des énergies renouvelables et leur possession d’importants stocks de thorium en font une proie idéale. Obsidian Fang ne cherche pas seulement à voler leurs ressources, mais aussi à comprendre leurs procédés de raffinage et leurs infrastructures énergétiques. Plusieurs opérations d’espionnage ont été menées contre Solaris, et si certaines ont échoué, d’autres ont permis à Obsidian Fang de récolter des informations cruciales sur leurs technologies. Les tensions montent, et si pour l’instant les affrontements restent limités à des escarmouches et des sabotages, une guerre ouverte pourrait éclater à tout moment.
Quant à Hydroguard, bien qu’ils soient moins impliqués dans la course au thorium, ils possèdent une ressource que même Obsidian Fang ne peut ignorer : l’eau. Sans Hydroguard, aucun empire ne pourrait subsister longtemps, et c’est ce qui empêche une guerre totale entre eux. Toutefois, cette trêve fragile ne signifie pas que les relations sont pacifiques. Obsidian Fang mène de nombreuses infiltrations pour tenter de manipuler le système de distribution de l’eau et s’emparer de certaines infrastructures critiques. Leurs espions sont présents dans plusieurs installations d’Hydroguard, récoltant des données sur la Fontaine de Vie et cherchant des failles dans leur organisation.
Mais Obsidian Fang ne se contente pas de grappiller du pouvoir ici et là. Ils ont une vision bien plus grande, un projet ambitieux qui pourrait les propulser au sommet de l’humanité : les arènes. Pour l’instant, ces arènes ne sont que de simples prototypes, dissimulés dans des installations clandestines où des mercenaires et des captifs sont forcés de combattre sous les yeux de riches parieurs et de commanditaires anonymes. Mais pour Obsidian Fang, c’est plus qu’un divertissement : ils croient que les arènes représentent le futur du mercenariat et de la guerre. Plutôt que de livrer des conflits à grande échelle avec des armées coûteuses et difficiles à entretenir, ils rêvent d’un monde où les guerres seront décidées par des champions d’élite s’affrontant dans des arènes technologiquement avancées, sous le regard du reste du monde. Ces combats serviront à désigner les vrais leaders, ceux qui méritent de dominer, et à éliminer les faibles et les indécis.
Obsidian Fang ne cherche pas simplement à rivaliser avec les autres empires : ils veulent redéfinir les règles du jeu, remodeler l’ordre mondial à leur avantage et s’assurer que, lorsque la poussière retombera, ce seront eux qui tiendront les rênes du futur.

"""
obsidian_fang_arena = """
LA GRANDE ARÈNE D’OBSIDIAN FANG : UN COLOSSE DE SANG ET DE TITANE
La Grande Arène - État Initial
La "Grande Arène" d'Obsidian Fang n'a rien d'un monument de gloire. Pas encore.
 À ses débuts, elle n'était qu'un pari bancal, une idée dangereuse portée par quelques ambitieux, dans les ruines dévorées par le temps du vieux Colisée de Rome.
Les arches effondrées, les gradins éventrés et la pierre noire corrompue par la chute des météorites donnaient au lieu une atmosphère lugubre, presque sacrée, comme si les fantômes des anciens gladiateurs eux-mêmes y erraient encore.
Le projet, soutenu discrètement par Obsidian Fang, n'était pas officiel. Il n'était même pas assumé publiquement.
Il reposait sur un pacte fragile entre quatre grands lanistes, figures aussi brutales que visionnaires, qui voyaient dans le sang versé une monnaie d’échange plus puissante que l’or ou le fer.
Parmi eux, Caron, un ancien mercenaire devenu marchand d’hommes, était le plus méthodique.
 Il recrutait dans les ruines, parmi les affamés, les orphelins, les soldats perdus et les criminels sans avenir.
 Il ne leur promettait ni gloire, ni liberté. Seulement une chance de vivre un jour de plus en maniant une arme.
 La sélection était brutale, les "épreuves" improvisées. Pas de médecins, pas de règles claires. Tu tombais, tu crevais.
Les autres lanistes, chacun avec leur style, leur clientèle et leur réseau, cherchaient à imposer leur vision :
L’un organisait des combats truqués pour faire fructifier ses paris.


L’autre montait des spectacles sanglants pour séduire les chefs de guerre en quête d’entertainment.


Un troisième recrutait directement pour les escarmouches clandestines entre empires, camouflant les morts derrière des jeux d'arène.


Chacun bâtissait son influence dans l’ombre, tissant des alliances fragiles, orchestrant des sabotages, payant des mercenaires pour faire tomber les arènes rivales.
 Les arènes elles-mêmes n'étaient que des fosses creusées dans la boue, des arènes de fortune dressées entre les carcasses de villes en ruine, ou des souterrains délabrés récupérés pour l'occasion.
À ce stade, le système était encore embryonnaire : Les infrastructures tombaient en morceaux après chaque combat, les règles changeaient selon le caprice du laniste organisateur, la corruption, la trahison et la violence hors des combats étaient la norme.
Les combats étaient clandestins partout en dehors d’Obsidian Fang, persécutés par les autorités locales, parfois exterminés par les forces impériales si découverts.


Caron, plus patient que ses rivaux, jouait un jeu plus long.
Il formait ses combattants. Il soudoyait discrètement des fonctionnaires. Il tissait un réseau plus solide que la simple violence.
À ses yeux, l'arène n'était pas juste un spectacle : c'était un levier politique, un moyen de remodeler le pouvoir au sein même des empires.
Dans deux ou trois ans, pensait-il, l'Arène ne serait plus un repaire de chiens enragés. Ce serait une institution.
La Grande Arène - Fonctionnement
Au milieu des décombres du vieux Colisée, là où les pierres éclatées par le temps côtoient la rouille et la cendre, l’Arène s’est reconstruite sur des fondations de fortune.
 Des murs écroulés ont été grossièrement renforcés avec des poutres métalliques, des câbles tendus, des plaques d’acier soudées à la main. Le sol est irrégulier, parfois boueux, parfois couvert de gravats tranchants. Ici, rien n’est propre. Tout est pensé pour blesser, user, tester.
Caron, au nom d’Obsidian Fang, supervise l’organisation générale. Il ne dirige pas officiellement l’Arène — du moins pas encore — mais son influence est omniprésente dans l’ombre.
 Pour entrer dans l’arène, il faut payer. Mais l’argent n'est pas accepté. Seul compte ce que Caron appelle les Obsidian coins :
Les Obsidian coins sont des laissez-passer, des jetons ou des marques officielles remis par les agents de Caron aux mercenaires et commandants jugés "dignes" de participer.


Ils peuvent être obtenus en rendant service à Caron, en gagnant des combats de rue, en trahissant un rival, ou parfois simplement achetés au marché noir pour des sommes démentielles.


Cette rareté volontaire rend chaque entrée dans l’arène précieuse et risquée.


Chaque commandant a le droit d’amener jusqu’à quatre mercenaires dans son équipe.
 Ils se mesureront à quatre autres combattants sélectionnés par tirage (NPC) ou directement choisis par un laniste rival (PVP), selon l'événement du jour.
 Pas d'escorte, pas d'assistance extérieure. Une fois dans l’arène, ils sont livrés à eux-mêmes, sous le regard brûlant des spectateurs entassés dans les gradins délabrés.
Le combat est à mort — sauf si Caron, ou un autre laniste influent, décide d’épargner un combattant particulièrement rentable.
(Dans le gameplay, évidemment le joueur ne perdra pas ses mercenaires si ils meurent)
La victoire, elle, rapporte les Red marks :
Les Red marks sont les symboles de la bravoure du combat..


Elles permettent d’acheter des équipements rares ou d'obtenir des droits spéciaux, comme l’accès à des combats d'exhibition plus prestigieux.


Plus tu remportes de combats, plus tu accumules des Coins, mais aussi de la reconnaissance.
L’organisation interne est encore brouillonne : Les règles changent selon les jours et les caprices des lanistes. Les spectateurs n’hésitent pas à parier, soudoyer, ou même provoquer des émeutes en pleine rencontre. La sécurité est assurée par des milices privées engagées par Caron, mais elles ne garantissent qu’une chose : la survie de l’arène, pas celle des participants.


L’ambiance est sale, brutale, tendue.
 L’odeur de la sueur, du sang et de la vieille pierre flotte dans l’air. Les clameurs des foules, ivres de violence, résonnent entre les murs millénaires.
 Ce n’est pas encore une institution. C’est un pari fou qui pourrait s'effondrer du jour au lendemain...
 Mais dans ce chaos naissant, Caron voit l’avenir : un empire construit sur les cadavres des faibles.
Les ambitions d’Obsidian Fang pour l’Arène
La Grande Arène de Rome n’est qu’un début.
 Un prototype grandeur nature, une preuve que la soif de sang peut être transformée en industrie.
Obsidian Fang n’a jamais vu l’arène comme un simple divertissement.
 Ils la voient comme un outil de domination culturelle et économique.
 L'objectif est clair : faire des combats de mercenaires un spectacle accepté, désiré, puis incontournable. Implanter l’idée dans les esprits comme un besoin naturel. Bientôt, aucun empire ne pourra se passer de ces "jeux modernes" — et Obsidian Fang sera le seul à en contrôler les règles, les champions et les profits.
À terme, la Grande Arène doit devenir un sanctuaire du pouvoir :
Un stade colossal, capable d’accueillir des milliers de spectateurs.


Des combats de plus en plus médiatisés, retransmis clandestinement par des réseaux pirates.


Des ligues de mercenaires, sponsorisées par des maisons marchandes, des seigneurs de guerre, voire des corporations.


Un circuit officiel, avec des championnats, des paris légalisés, des titres, des légendes.


Mais ce futur n'est pas encore là.
 Aujourd'hui, c’est un projet fragile, plein de risques. Caron le sait mieux que quiconque.
Déjà, Obsidian Fang a implanté plusieurs arènes clandestines ailleurs dans le monde, utilisant le même concept mais beaucoup moins poussée que celle de Rome :


Des rings improvisés sous les cendres de nombreuses villes neutres.


Des docks abandonnés transformés en arène sauvage sur les côtés de la Manche.


Des parkings en ruine reconvertis en théâtre de mort en Amérique du Nord.


Toutes sont opérationnelles, mais aucune n’égale Rome.
Elles sont mal organisées, corrompues, souvent infiltrées par des milices locales ou des cartels qui imposent leurs propres lois.
Les combats y sont plus chaotiques, la sécurité inexistante, et la réputation de l’Arène en souffre à chaque débordement.
Caron lutte dans l’ombre pour reprendre la main, éliminer les "faussaires", et imposer un modèle unique : celui de Rome, brut, sanglant, mais sous contrôle.
Pour Obsidian Fang, la conquête n’est pas militaire. Elle est culturelle.
Et l’Arène est leur cheval de Troie.
À travers le sang versé, ils veulent bâtir un empire plus vaste encore que ceux fondés par la guerre.
1. Pourquoi une arène dans un monde post-apocalyptique ?
Dans un monde ravagé par les météores et les conflits pour la survie, l’existence d’une structure aussi démesurée qu’une arène de gladiateurs peut sembler absurde. Mais Obsidian Fang n’est pas une faction ordinaire. Ce n’est pas une armée de pillards affamés ou une société en ruine tentant de reconstruire un simulacre d’ordre. C’est une organisation calculatrice, secrète, et implacable, qui voit dans le chaos une opportunité d’expansion et de contrôle.
L’arène est avant tout un outil. Un instrument de domination, de propagande et d’influence. Là où d’autres factions survivent, Obsidian Fang prospère.
2. Une machine à générer du pouvoir et de la richesse
L’arène n’est pas qu’un spectacle ; elle est un centre économique et stratégique essentiel à la puissance d’Obsidian Fang. Elle repose sur plusieurs piliers :
A. Contrôle social et propagande
Dans les territoires sous leur influence, l’arène est bien plus qu’un divertissement : elle est un exutoire, un moyen de canaliser la violence latente des populations et de leur offrir un rêve de grandeur.
Plutôt que de se révolter contre l’autorité d’Obsidian Fang, les masses ont un objectif plus accessible : devenir des légendes de l’arène, des champions adulés, des héros modernes.
Ceux qui ne se battent pas regardent, s’identifient aux combattants et s’investissent émotionnellement dans les combats. La frustration, la colère et l’angoisse de la survie quotidienne trouvent une issue contrôlée.
Obsidian Fang se place en maître du spectacle, garant d’un ordre où seule la force dicte la valeur d’un homme.

B. Une source de revenus colossale
L’arène est aussi un centre économique alimenté par plusieurs flux financiers :
Les paris clandestins :
Les citoyens comme les factions extérieures parient sur les combats.
Des systèmes de cotes, des truquages et des résultats orchestrés assurent qu’Obsidian Fang ne perd jamais vraiment d’argent.
Les taxes d’entrée et de diffusion :
Pour assister aux combats en direct, les citoyens doivent payer en ressources, en monnaie d’échange ou en services.
Les autres factions doivent négocier des droits de diffusion, sous conditions dictées par Obsidian Fang.
Le sponsoring des armes et équipements :
L’arène ne fournis pas d’armes. Il faudra venir avec ce que vous avez en main pour pourfendre vos adversaires.
Les duels servent de bancs d’essai pour de nouvelles technologies de combat, un champ de tir vivant où l’on peut ensuite vendre ou garder les technologies.
3. Les coûts de construction et d’entretien : une dépense justifiée
Une telle infrastructure n’a pas été bâtie du jour au lendemain, et son coût est astronomique, surtout dans un monde où les ressources sont rares.
A. Matériaux et ingénierie
La Grande Arène a été reconstruite sur les ruines d’un ancien Colisée, vestige d’un empire oublié. Des sections effondrées ont été consolidées avec du béton brut, de la ferraille récupérée et des plaques d’acier rouillé.
Quelques vitres blindées grossièrement montées protègent les gradins les plus prisés, mais beaucoup préfèrent regarder sans barrière, au risque d'y laisser leur peau.
Le terrain a été modifié à la main et à la dynamite, créant des tunnels, des pièges et des plateformes instables. Des équipes de bricoleurs et d'ingénieurs de fortune entretiennent ce chaos vivant, rafistolant l’arène au jour le jour avec ce qu'ils trouvent.


B. Énergie et alimentation
L’arène est alimentée par des batteries au Thorium.
L’éclairage, les caméras, les drones, les haut-parleurs et autres besoins consomment autant d’énergie qu’une ville moyenne, rendant le tout profitable.
C. Sécurité et logistique
Chaque combat nécessite une surveillance militaire pour éviter les émeutes et empêcher toute tentative de sabotage.
L’arène emploie des centaines de personnes : gardiens, ingénieurs, médecins, commentateurs, organisateurs, bourreaux.
4. L’influence de l’arène sur le reste du monde
L’impact de l’arène dépasse largement les frontières d’Obsidian Fang. Son existence réécrit les règles de la guerre et du pouvoir dans un monde sans lois.
Un centre diplomatique officieux :
Les factions en guerre trouvent parfois des solutions en envoyant leurs champions s’affronter dans l’arène au lieu d’engager des batailles coûteuses. (Cette solution ne marche souvent pas)
Certains chefs de guerre préfèrent miser des vies plutôt que des territoires.
Un symbole de puissance :
Le simple fait de posséder une telle structure impose le respect et la crainte.
Les factions qui refusent d’y participer sont perçues comme faibles.
Une menace constante :
Obsidian Fang peut transformer un simple guerrier en une légende… ou en un cadavre.
Les rumeurs disent que certains adversaires de la faction ont été capturés et forcés de combattre dans l’arène, enchaînés jusqu’à leur mort.

CONCLUSION 
La Grande Arène d’Obsidian Fang n’est pas qu’un terrain de jeu. C’est le début d’une industrie, la conception d’un avenir peut être sans guerre.
Mais pour l’instant, elle sert à divertir, manipuler, recruter et enrichir ceux qui la contrôlent. C’est un moulin à viande qui broie les faibles et élève les impitoyables. Chaque combat est un spectacle, chaque spectateur un complice, chaque mort un investissement.
Et tant que le monde restera en ruines, tant que la soif de violence consumera les âmes, Obsidian Fang régnera par le sang et le fer.

Visuels
1. STRUCTURE GÉNÉRALE
Forme : Ovale, rappelant les anciens colisées, mais avec une architecture brutaliste renforcée par des matériaux modernes (béton noir, acier renforcé, titane composite).
Dimensions :
Environ 150 mètres de long et 90 mètres de large, avec une hauteur totale de 80 mètres.
Capacité d’accueil de 50 000 à 100 000 spectateurs, répartis sur plusieurs niveaux.
2. L’ARÈNE CENTRALE
Dimensions :
Environ 100 mètres de long et 60 mètres de large.
Hauteur variable des éléments de terrain : de 0 à 10 mètres selon la configuration du combat.
Protection des spectateurs :
Des vitres anti-tank ultra-résistantes encerclent l’arène, capables d’absorber les explosions et les balles de gros calibre.
3. LES GRADINS & INFRASTRUCTURES POUR LE PUBLIC
Disposition :
Plusieurs niveaux de gradins, organisés selon le prestige des spectateurs.
Le premier niveau, au plus proche de l’arène, est réservé aux élites d’Obsidian Fang et aux sponsors des combats.

4. ZONES TECHNIQUES ET INFRASTRUCTURES DE SÉCURITÉ
Les tunnels des combattants :
Deux grands tunnels souterrains permettent aux équipes de rejoindre l’arène depuis leurs quartiers.
Un sas hermétique avec une porte blindée empêche toute fuite.
Les coulisses de l’arène :
Une zone souterraine comprenant : Des prisons temporaires pour les gladiateurs captifs ou punis, des ateliers d’armement où les équipes peuvent ajuster leur équipement avant le combat et des salles de soins pour les combattants survivants, équipées de technologies médicales avancées.
Sécurité militaire :
Des troupes d’Obsidian Fang patrouillent en permanence.
Tourelles automatisées installées aux points stratégiques pour éviter toute tentative de sabotage.
5. LOGES VIP ET QUARTIERS DES ORGANISATEURS
La Tribune des Masques :
Une plateforme suspendue au-dessus de l’arène, réservée aux hauts dirigeants d’Obsidian Fang.
Ils observent les combats depuis une salle panoramique ultra-sécurisée.
Un système de haut-parleurs leur permet d’interagir avec le public et les combattants.
Les quartiers privés :
Des zones exclusives pour les sponsors et les invités de marque, offrant des salons luxueux avec des écrans interactifs et un service personnalisé.

6. DIFFUSION ET PROPAGANDE
Retransmission mondiale :
Les combats sont diffusés dans les villes sous contrôle d’Obsidian Fang et sur toute la planète, servant de propagande pour l’Empire
Des drones-caméras suivent chaque affrontement sous plusieurs angles.
Paris et enjeux financiers :
Un système de paris clandestin est encouragé par les organisateurs.
Les spectateurs peuvent miser sur les combats via une monnaie contrôlée par Obsidian Fang. (Les red marks et les obsidian coins)

7. LES CÉRÉMONIES ET ÉVÉNEMENTS SPÉCIAUX
Entrée des combattants :
Chaque équipe a droit à une introduction spectaculaire, avec feux d’artifice, musique personnalisée et affichage holographique de leurs exploits passés.
Événements uniques :
Des tournois saisonniers sont organisés, avec des règles spéciales comme des rounds sans armes à feu, des combats de survie contre des machines, ou des duels à mort entre champions.
"""
fourVSfour_rules = """
Comment jouer un combat 4 contre 4
Le Lobby
Le lobby constitue l’étape de préparation stratégique avant chaque combat. Il offre au joueur un espace dédié pour composer et organiser son équipe en vue de l’affrontement.
Fonctionnalité principale
Dans le lobby, chaque joueur doit sélectionner et placer quatre mercenaires sur une grille de placement prédéfinie.
La disposition des mercenaires sur cette grille est cruciale, car elle influencera le déroulement du combat (par exemple : ligne de front, protection du healer, etc.).
Les emplacements disponibles sont fixes et structurés pour permettre des choix tactiques variés.
Sélection des mercenaires
Le joueur choisit les mercenaires parmi ceux débloqués dans sa bibliothèque personnelle.
En cliquant sur un mercenaire, celui-ci est automatiquement placé sur la grille, dans une position par défaut (modifiable par la suite).
Le joueur peut réorganiser ses mercenaires à tout moment avant de lancer le combat.
Aperçu de l’équipe adverse
En parallèle, le joueur a la possibilité de visualiser l’équipe de défense de son adversaire.
Cela permet d’adapter sa stratégie et d’anticiper les rôles ou synergies adverses (tank en première ligne, nuker en retrait, etc.).
Objectif du lobby
Le lobby n’est pas un simple menu de sélection, c’est une phase stratégique à part entière :
➔ Il invite à la réflexion sur la composition d’équipe,
➔ Le placement optimal selon les forces et faiblesses de ses mercenaires,
➔ Et l’adaptation en fonction de l’ennemi à affronter,
➔ Accessibilité : grâce à l’automatisation partielle des actions,
➔ Et profondeur stratégique : en offrant aux joueurs une interaction active avec le combat via la gestion des points d’action et des combos.
Règles de Placement des Mercenaires
Le système de placement des mercenaires repose sur un mécanisme automatique intelligent, conçu pour fluidifier l’expérience de jeu tout en respectant des règles de priorité précises.
Lorsqu’un joueur clique sur l’avatar d’un mercenaire dans sa bibliothèque, ce dernier est automatiquement ajouté à la grille de jeu. Le placement respecte des règles strictes en fonction du rôle du mercenaire (Tank, Support, Healer, Nuker) et des zones de la grille. Une fois le mercenaire positionné, le joueur conserve la possibilité de déplacer manuellement son personnage sur une autre case, si nécessaire.
Selon la classe du mercenaire, des priorités sont définies pour les différentes cases. Par exemple, si le joueur sélectionne un Tank, le système essaiera de le placer en priorité sur la case T1. Si cette case est déjà occupée, le système tentera T2, puis T3, et ainsi de suite. Ce principe s’applique également aux autres rôles, avec des priorités spécifiques pour chaque type de case.
Le placement automatique ne peut cibler que des cases vides. Si la case prévue est déjà occupée, le système cherche la prochaine case de même couleur et applique la priorité suivante. Ces règles sont valables pour les deux équipes, aussi bien en attaque qu’en défense.
Arène
Dans l’arène, les combats se déroulent de manière semi-automatique, combinant actions automatiques et interventions tactiques du joueur pour une expérience fluide mais stratégique.
Deux équipes composées chacune de quatre joueurs s’affrontent dans un affrontement stratégique.
Chaque joueur sélectionne quatre personnages appelés "mercenaires", chacun ayant un rôle spécifique :
➔ Tank : encaisse les dégâts pour protéger l’équipe.
➔ Healer : soigne les alliés et maintient l’équipe en vie.
➔ Support : apporte des bonus, contrôle les ennemis ou améliore les capacités de ses alliés.
➔ Nuker : inflige de lourds dégâts en un minimum de temps.
Système de compétences (Skills)
Chaque mercenaire dispose d’un ensemble de compétences uniques.
Ces compétences sont disponibles dès le départ, mais certaines ne sont accessibles qu’avec des mercenaires de rareté élevée.
Les types de rareté incluent : Commun, Rare, et Légendaire.
Les mercenaires de rareté plus élevée disposent de possibilités tactiques accrues, telles que des skills avancés ou plus puissants.
Compétences spéciales
Un mercenaire peut également débloquer une compétence spéciale en s’équipant :
➔ d’un accessoire,
➔ ou d’une arme compatible avec sa classe, si ces équipements possèdent eux-mêmes un skill spécial.
Battle Grid
Afin d’optimiser la fluidité des déplacements et des combats dans un mode 4 contre 4, un nouveau système de grille hexagonale est proposé pour le placement des mercenaires.
Les cellules de la grille sont hexagonales, offrant une plus grande fluidité dans les déplacements et les orientations.
Chaque cellule dispose de 8 points d’attache : ces points représentent les positions à partir desquelles un ennemi peut attaquer le mercenaire occupant cette cellule.
Objectif
But principal : Gagner la partie en éliminant stratégiquement l’équipe adverse.
Condition de victoire : Élimination complète des mercenaires ennemis.
Réapparition & Cycle de jeu
Lorsqu’un mercenaire perd tous ses points de vie, il est mis K.O.
Il ne peut réintégrer la partie que si un allié utilise un skill spécifique de réanimation.
Équilibrage automatique
Afin de garantir une expérience de jeu équilibrée :
Les statistiques de base varient légèrement selon la rareté du mercenaire.
Cela empêche un déséquilibre trop important entre les personnages de rareté légendaire et ceux de rareté commune.
L’objectif est de permettre à tous les types de joueurs de participer activement, quelle que soit la rareté des personnages qu’ils possèdent, tout en conservant une profondeur stratégique.
Attaques automatiques par défaut
Dès le début du combat, les mercenaires attaquent automatiquement en utilisant leurs skills de base.
Ces attaques sont gérées par l’IA, permettant au joueur de se concentrer sur des décisions stratégiques.
Déclenchement manuel des skills spéciaux
Les skills spéciaux sont des capacités puissantes que le joueur peut débloquer manuellement durant le combat :
Accumulation de Points d'Action
Le joueur génère 1 point d’action à chaque clic (ou tap) sur l’avatar d’un mercenaire.
Chaque skill spécial nécessite un nombre défini de points d’action pour être débloqué.
Activation du Skill Spécial
Une fois le nombre requis de points d’action atteint, le joueur peut cliquer sur l’icône du skill spécial pour déclencher l’attaque spéciale du mercenaire.
Attaque Coordonnée
Si le joueur débloque tous les skills spéciaux des quatre mercenaires de son équipe,
Il a la possibilité d’exécuter une attaque coordonnée en glissant son doigt sur toutes les icônes de skills spéciaux successivement.
Cela provoque une séquence synchronisée d’attaques spéciales, idéale pour infliger des dégâts massifs ou renverser une situation difficile.
Récompenses & progression
À la fin de chaque combat, que ce soit une victoire ou une défaite, les mercenaires du joueur reçoivent diverses récompenses contribuant à leur progression et à l’amélioration de l’équipe.
Gain d’expérience
Tous les mercenaires ayant participé au combat gagnent de l’expérience (XP), leur permettant de monter en niveau.
Le niveau supérieur d’un mercenaire améliore ses statistiques de base.
Récompenses
En plus de l’expérience, les mercenaires peuvent également obtenir des objets ou des ressources spécifiques à l’issue du combat :
➔ Équipements (armes, accessoires…),
➔ Ressources de craft ou d'amélioration,
➔ Fragments de mercenaires.
Un système équilibré et motivant
Ce système de récompenses a pour objectif de :
➔ Récompenser la performance sans pénaliser excessivement la défaite,
➔ Encourager les joueurs à expérimenter différentes compositions d’équipe,
➔ Favoriser une progression constante, même en cas d’échec temporaire.
"""
skills = """
Skills
Matrice
La Matrice est le coeur analytique du système de compétences de Thorium Empires. Il structure toutes les règles d’application, cibles, effets et conditions des skills (compétences) dans le jeu.
Chaque compétence dans Thorium Empires suit une règle de ciblage bien définie, qui détermine à qui elle peut s’appliquer. Par exemple, une compétence peut cibler spécifiquement un allié de type support, ou bien s’appliquer uniquement à l’utilisateur lui-même. Ces règles sont standardisées à l’aide d’identifiants codifiés, ce qui permet de structurer clairement le comportement des skills. Elles précisent si une compétence peut viser un ennemi, un allié, un groupe, ou encore le propre lanceur de la compétence.
En plus de leur ciblage, chaque skill génère un ou plusieurs effets de jeu, qui influencent directement le déroulement du combat. Ces effets peuvent inclure :
➔ des dégâts directs infligés à l’adversaire,
➔ des buffs, qui améliorent temporairement les statistiques du bénéficiaire,
➔ des debuffs, qui réduisent les capacités de l’ennemi,
➔ des soins, pour restaurer les points de vie d’un allié,
➔ ou encore des contrôles tels que l'étourdissement, le silence, ou la provocation.
Tous ces effets sont classés à la fois par type et par niveau de puissance, permettant ainsi une gradation claire de leur intensité et une meilleure lisibilité dans l'équilibrage du jeu.
La matrice intègre également plusieurs mécaniques avancées du système de combat, permettant une gestion plus fine et stratégique des interactions entre les compétences.
Lorsqu’un buff ou un debuff identique est appliqué plusieurs fois à une même cible, des règles spécifiques sont appliquées pour éviter toute confusion.
Dans ce cas :
➔ Seul le buff le plus avantageux est conservé,
➔ Tandis que le debuff le plus pénalisant est maintenu.
Cette approche assure que les effets appliqués soient toujours cohérents et significatifs, sans créer de déséquilibres artificiels.
Par ailleurs, toutes les durées des effets sont exprimées en secondes, ce qui permet une synchronisation précise des actions en combat et facilite l’élaboration de stratégies temporelles.
Un autre aspect fondamental est le système de menace, qui joue un rôle crucial dans le ciblage automatique des ennemis. Chaque fois qu’un personnage réalise une action (comme attaquer ou utiliser un skill), il gagne des points de menace. Plus ce score est élevé, plus ce personnage devient une cible prioritaire pour les ennemis.
Ainsi, les attaques se dirigent automatiquement vers le personnage qui génère le plus de menace, créant une dynamique de gestion de l’agressivité qui pousse les joueurs à adapter leur style de jeu selon le rôle de leurs mercenaires (tank, support, etc.).
La provocation force tous les ennemis affectés à cibler le provocateur, peu importe leur ciblage natif.
La matrice définit quelles compétences peuvent être utilisées :
➔ Par quelle classe (Tank, Healer, Nuker, Support)
➔ Sur quelle cible
➔ Avec quel niveau de rareté ou d’évolution
Cela permet de croiser les rôles et les compétences disponibles, assurant un bon équilibrage et une répartition stratégique claire des responsabilités en combat.
La matrice des compétences joue un rôle fondamental dans la conception et le fonctionnement du système de combat de Thorium Empires. Elle permet avant tout de structurer de manière claire et logique le comportement de chaque compétence, en définissant précisément ses cibles, ses effets et ses conditions d’activation.
Grâce à cette organisation rigoureuse, la matrice facilite considérablement la programmation des intelligences artificielles, qui peuvent ainsi interpréter et appliquer les règles de manière autonome et cohérente en fonction des situations rencontrées en combat.
Elle constitue également un outil essentiel pour assurer l’équilibrage des synergies entre les différents rôles (Tank, Healer, Support, Nuker), en permettant de visualiser et d’ajuster la manière dont leurs compétences interagissent entre elles.
De plus, elle permet de vérifier la cohérence globale des effets entre les personnages, évitant ainsi les redondances, les déséquilibres, ou les combinaisons involontairement dominantes.
Skills basiques et passives
Chaque mercenaire dans Thorium Empires possède :
➔ Une attaque de base en mêlée
➔ Une attaque à distance (si équipé d’une arme adaptée)
➔ Une ou plusieurs compétences passives
Ces compétences sont disponibles indépendamment de la rareté ou des points d’action. Elles sont automatiquement activées dans certaines conditions et reflètent le style de combat de chaque personnage.
Attaque de base en mêlée
Cette attaque se déclenche si le mercenaire n’est pas équipé d’une arme à distance.
Il s’agit d’un engagement au corps-à-corps, permettant d’infliger des dégâts directs à l’ennemi situé à proximité.
L’animation dépend de l’arme équipée (ou absence d’arme).
Attaque de base à distance
Cette attaque est utilisée si le mercenaire est équipé d’une arme à distance.
L’animation dépend de l’arme portée, et la portée du tir varie selon les caractéristiques de l’arme.
Compétences passives
Ce sont des effets automatiques qui s’activent selon des conditions précises.
Ces skills n’ont pas besoin d’être activés manuellement et influencent le comportement ou les statistiques du personnage (ex : bonus de soin, résistance, régénération…).
Pour certains mercenaires, une compétence passive cachée existe aussi. Elle n’apparaît pas sur la fiche du personnage et constitue une surprise stratégique pendant le combat.
Déblocage conditionnel
Certaines compétences passives ou attaques ne sont disponibles que sous certaines conditions, comme :
➔ une arme spécifique équipée,
➔ une position particulière sur la grille,
➔ ou l’atteinte d’un certain niveau ou rareté.
Animations spécifiques
Pour renforcer l’immersion, chaque attaque ou compétence peut déclencher une animation dédiée. Certaines animations sont visibles uniquement si le mercenaire utilise une arme ou un équipement spécial.
Skills spéciaux
Dans Thorium Empires, chaque équipement spécial – comme une arme ou un accessoire – peut débloquer un skill spécial pour un mercenaire. Ces compétences puissantes sont déclenchées manuellement par le joueur en combat, lorsqu’il a accumulé assez de Points d’Action (PA).
Les skills spéciaux sont au coeur de la stratégie : ils peuvent renverser une bataille, infliger des dégâts massifs, étourdir, ou buff une équipe entière.
Progression
Chaque skill spécial possède jusqu’à cinq niveaux d’évolution, dont les deux derniers sont réservés aux équipements légendaires :
Niveau 1 à 3 : effets croissants (ex. dégâts, bonus, debuffs)
Niveau 4 à 5 : effets uniques et puissants (par ex. effets de zone, dégâts de type "Thorium", interactions spéciales)
Effets spéciaux
Certains skills ont des effets visuels thématiques, comme des auras d’énergie Thorium pour les objets légendaires.
Les buffs et debuffs sont généralement annulables avant leur fin naturelle.
Les dégâts sur la durée (comme poison ou brûlure) ignorent la défense ennemie.
Si la cible meurt en cours d’animation, les effets restants sont interrompus.
Les skills spéciaux représentent le coeur stratégique actif du combat :
Ils nécessitent une gestion des ressources (points d’action),
Une planification du timing (activation vs cooldown),
Et permettent d’exécuter des combos dévastateurs avec l’équipe entière.
Ils ajoutent une couche de profondeur tactique au-delà des attaques de base et compétences passives.
"""
