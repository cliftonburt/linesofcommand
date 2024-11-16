# Lines of Command

## Overview

**Lines of Command** is an interactive fiction game set during the Napoleonic Wars in 1805. Players step into the role of a British naval captain, navigating the high seas, managing a ship, solving intricate puzzles, and dealing with the ongoing conflicts of the time. The game is played via a command-line-inspired interface, and it emphasizes historical accuracy, immersive naval operations, and dynamic storytelling.

## Gameplay Features

- **Command-Line Inspired Interface**: Issue orders using natural language or specific commands, with the game's first officer rephrasing them in authentic naval terminology. The current implementation uses an HTML5 faux-terminal interface, providing an immersive terminal-inspired experience accessible via web browsers.
- **Dynamic Officer Team**: Your officers provide real-time feedback, suggestions, and interpretations, making it feel like you’re truly commanding a ship from the early 19th century.
- **Exploration and Navigation**: Sail an open-world ocean map, exploring ports, enemy waters, and hidden locations, all while encountering dynamic events.
- **Missions and Engagement**: Begin your naval journey with three core missions—"The Blockade," "Smuggler's Run," and "Rescue and Retribution"—with future missions and content expansions planned.
- **Puzzles and Backstory**: Encounter and solve new challenges, such as cryptographic puzzles, ship repairs, navigation challenges, and more.

## Core Gameplay Elements

- **Navigation and Exploration**: Players navigate using a coordinate-based map, issuing commands like `sail [direction]`, `set course [destination]`, and `drop anchor`.
- **Combat and Tactical Decisions**: Engage in ship-to-ship combat, where positioning, resource management, and officer advice influence outcomes. Commands include `fire [cannons]`, `brace`, and `engage [target]`.
- **Puzzles**: Weekly puzzles range from decoding semaphore signals and Caesar ciphers to handling mechanical failures or managing spy interrogations. Each puzzle adds depth to the backstory and gradually escalates in complexity.
- **Officer System**: Your team of officers—such as Lt. Hardy (Navigation), Lt. Campbell (Gunnery), and Dr. Milton (Surgeon)—provide advice on courses of action, with specific command recommendations to help the captain execute plans effectively.

## Sample Commands
- **Navigation**: `sail [direction]`, `set course [destination]`, `weigh anchor`, `drop anchor`.
- **Combat**: `fire [cannons]`, `brace`, `engage [target]`, `board the enemy`, `strike colors`.
- **Crew and Ship Management**: `inspect ship`, `repair [part]`, `rations [amount]`, `splice the mainbrace`.
- **Officers' Advice**: Use the `advise` command to prompt officers to provide situational recommendations with actionable commands.

## Planned Features for Future Expansions
- **Weekly Puzzles and Storyline Updates**: New puzzles will be released every week, introducing fresh challenges and advancing the story, culminating in a larger narrative arc over the year.
- **Seasonal and Environmental Changes**: Reflect the challenges of different seasons—from treacherous winter storms to political shifts that alter alliances or trade routes.
- **Modular Content Expansion**: Additional missions, characters, ship upgrades, and locations will be introduced over time, keeping gameplay engaging and evolving.
- **Platform Expansion**: Once the MVP (Minimum Viable Product) is established using the HTML5 faux-terminal interface, future versions may expand to Discord, Slack, and other chat platforms based on demand.

## Getting Started
### Development Roadmap
**1. Initial Release: Core Mechanics**
- Implement basic command-line-inspired navigation and core ship functions in an HTML5 faux-terminal interface.
- Introduce the first officer to interpret player commands.
- Develop three core missions and a coordinate-based ocean map for exploration.
- Ship with three initial puzzles to introduce the mechanics.

**2. Core System Build**
- **Command System**: Develop an NLP parser for understanding natural language and predefined commands.
- **Feedback System**: Implement the first officer system to confirm player commands with authentic naval terminology, making gameplay feel realistic.

**3. Ongoing Development**
- Release new puzzles.
- Add more officers with unique skills and specialized advice.
- Expand the map, missions, and available upgrades based on player progress.

### How to Play
To play **Lines of Command**, simply enter commands via the HTML5 faux-terminal interface. Examples of commands include:
- `sail NW` - Sail northwest to explore new parts of the ocean map.
- `engage enemy frigate` - Enter into combat with an enemy vessel.
- `splice the mainbrace` - Reward your crew with a ration of rum to boost morale.
- `advise` - Request guidance from your officers on the optimal course of action.

The game begins with a short tutorial to help you get accustomed to the controls and understand your role as a captain of a British Man-o-War during the Napoleonic era.

## Contributing
We welcome contributions to the **Lines of Command** project! Whether you have ideas for new puzzles, want to improve the existing storyline, or help build core mechanics, your input is valuable.
- **Bugs & Feature Requests**: Please submit these via GitHub Issues.
- **Collaborators**: If you're interested in collaborating, please reach out—we'd love to expand the world of **Lines of Command** together.

## Community and Updates
- **Weekly Puzzle Releases**: Stay tuned for weekly releases of new puzzles and backstory elements.
- **Community Engagement**: Share your theories, solve puzzles together, and connect with other captains. Updates and hints will be provided regularly on the GitHub project page.

## License
**Lines of Command** is an open-source project. Contributions are welcome, and we hope you enjoy helping to build and expand this unique command-line naval experience.

## Contact
For questions, suggestions, or collaboration, please contact the project owner through GitHub or join our discussion forum linked on the project page.


