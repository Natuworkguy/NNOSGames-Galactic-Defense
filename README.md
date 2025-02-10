# Galactic Defense
### NNOS Games presents: Galactic Defense: The new game that is free-to play, but still fun-to-play!

**Galactic Defense** is a simple 2D arcade-style shooter game built with Python and [Pygame](https://www.pygame.org/). In this game, you control a player that moves horizontally along the bottom of the screen. Your objective is to shoot down incoming enemy ships before they reach you. With a nostalgic vibe reminiscent of classic arcade shooters, Galactic Defense offers fast-paced action and a straightforward gameplay experience.

---

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Assets](#assets)
- [Running the Game](#running-the-game)
- [Game Controls](#game-controls)
- [Command-Line Options](#command-line-options)
- [Code Overview](#code-overview)
- [Credits](#credits)
- [License](#license)

---

## Features

- **Player Movement:** Control your spaceship with the left and right arrow keys.
- **Shooting Mechanic:** Press the spacebar to fire bullets at enemy ships.
- **Enemy Behavior:** Multiple enemies move horizontally and descend gradually. When hit by a bullet, they reset to a random position.
- **Scoring System:** Earn points for each enemy hit. Special messages are displayed as you reach certain score thresholds (e.g., "Level 2", "Level 3", etc.).
- **Background Music:** Enjoy continuous background music (with an option to disable it).
- **Debug Mode:** Optional debug mode that prints key events and actions to the console.

---

## Installation

### Prerequisites

- **Python 3**  
- **Pygame**

You can install Pygame via pip:

```bash
pip install pygame
```

### Downloading the Code

Clone or download this repository to your local machine. Ensure that you have the following directory structure:

```
├─ **Version**/
│  ├── assets/
│  │   ├── bgm.mp3
│  │   ├── icon.png
│  │   ├── player.png
│  │   ├── enemy.png
│  │   └── bullet.png
│  └── main.py
└── README.md
```

> **Note:** The `assets` folder must contain all the necessary image and audio files for the game to run correctly.

---

## Assets

The game relies on several asset files located in the `assets` directory:

- **player.png:** Image representing the player's spaceship.
- **enemy.png:** Image used for enemy ships.
- **bullet.png:** Image for the bullets fired by the player.
- **icon.png:** Window icon.
- **bgm.mp3:** Background music file that plays during the game.

Make sure these files are correctly placed in the `assets` directory.

---

## Running the Game

Navigate to the project directory in your terminal and run:

```bash
python3 main.py
```

### Optional Command-Line Arguments

- `--nobgm`  
  Use this flag to disable the background music.
  
  ```bash
  python3 main.py --nobgm
  ```

- `--debug`  
  Enable debug mode, which prints additional debug information (e.g., key presses) to the console.
  
  ```bash
  python3 main.py --debug
  ```

You can combine options as needed:

```bash
python3 main.py --nobgm --debug
```

---

## Game Controls

- **Left Arrow (`←`):** Move the player's spaceship to the left.
- **Right Arrow (`→`):** Move the player's spaceship to the right.
- **Spacebar:** Fire a bullet.

The game ends when an enemy reaches the bottom of the screen, displaying a "GAME OVER" message.

---

## Code Overview

The main script (`main.py`) is structured as follows:

- **Initialization:**  
  The game initializes Pygame, sets up the screen, loads assets, and configures initial game parameters (player/enemy positions, bullet state, etc.).

- **Audio:**  
  The `bgm()` function loads and plays background music (unless the `--nobgm` flag is provided).

- **Asset Loading:**  
  The `load_and_scale_image()` function handles image loading and scaling. Errors in loading assets result in clean exits with informative messages.

- **Game Loop:**  
  The core game loop handles:
  - Event processing (keyboard events for movement and shooting)
  - Player movement and boundary checking
  - Enemy movement and collision detection
  - Bullet firing and collision detection with enemies
  - Score updating and level display based on score thresholds
  - Rendering graphics and updating the display

- **Collision Detection:**  
  The `is_collision()` function checks for overlaps between bullets and enemy images to determine hits.

- **Game Over Handling:**  
  If an enemy moves beyond the screen's bottom, the game displays a "GAME OVER" message and exits.

---

## Credits

- **Game Development:** NNOS Games
- **Programming Language:** Python 3
- **Graphics & Sound:** Provided via the assets in the `assets` directory

Feel free to modify or extend the game as desired!

---

Enjoy the game and happy coding!
