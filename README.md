# WordMatch
#### Video Demo:  https://streamable.com/r0pdsk
#### Description: WordMatch is an innovative and educational web application specifically designed to enhance the process of learning new words in an engaging and effective way. The primary objective of the app is to help users expand their vocabulary in both English and Dutch through an interactive game format. The game’s core concept involves players being presented with a list of words in English and their corresponding Dutch translations. The challenge for the player is to match each word pair within a limited time frame, adding a sense of urgency and excitement to the learning experience. This timed approach not only encourages users to focus and engage but also introduces a fun, competitive element, making vocabulary acquisition feel more like a game than a traditional study session.

#### The format of the game is straightforward yet effective: players are given a set of word pairs and must match them as quickly as possible. Once the player successfully matches a pair, the game moves to the next challenge. The timer adds an extra layer of complexity, motivating players to think quickly while reinforcing the words in their memory. This combination of timing and matching ensures that users are not just passively learning, but actively engaging with the material, which is known to significantly improve retention.

#### To ensure smooth functionality and efficient management of the word pairs, I utilized SQLite3, a lightweight and user-friendly database. SQLite3 is an excellent choice for this project due to its simplicity and ability to manage data in a streamlined manner. The database stores the English and Dutch word pairs and their corresponding translations. By using SQLite3, the application can scale easily and accommodate a variety of word sets, ensuring that users have access to a broad vocabulary range for their learning. Furthermore, the database structure is simple enough to allow quick retrieval of word pairs during gameplay, thus maintaining a seamless user experience.

#### On the backend of the web application, Python was used along with Flask, a lightweight web framework. Flask acts as the backend framework, connecting the user interface to the database. It allows the application to dynamically load word pairs based on user interaction, facilitating a smooth flow of data between the server and the client. The Flask framework also handles game session management, ensuring that the experience is personalized for each player. Flask’s minimalistic and flexible structure makes it an ideal choice for such an interactive application, as it provides the necessary functionality without unnecessary overhead.

#### On the client side, the game’s interactive elements are powered by JavaScript. Multiple JavaScript scripts are used to manage various game mechanics, including tracking the player’s progress, handling user input, and ensuring that the game’s timing and transitions work smoothly. These scripts also manage the display of the word pairs, arranging them in a visually appealing and intuitive format that enhances the overall user experience. The client-side JavaScript also manages the dynamic aspects of the game, such as showing real-time updates, providing feedback to the player, and ensuring that the game’s logic is executed flawlessly.

#### The integration of Flask, SQLite3, and JavaScript creates a seamless and interactive user experience, where users can learn new vocabulary while having fun. The app’s design ensures that the learning process is both efficient and enjoyable, combining education with entertainment. By leveraging the strengths of each of these technologies, WordMatch offers an innovative approach to language learning that is engaging, effective, and scalable for future expansion.

## Table of Contents

- [Setup](#setup)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Setup
1. Navigate to the project directory:
    ```bash
    cd WordMatch
    ```
3. Install the dependencies:
    ```bash
    pip install Flask
    pip install cs50
    ```

## Usage

To start the script, run:
```bash
python project.py
```
