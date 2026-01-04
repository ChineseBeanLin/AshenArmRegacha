# Ashen Arms Automated Reroll Script (My First Automation)

> The script that started it all. A simple Python automation tool built to optimize the "Reroll" process (initial character gacha) in the game *Ashen Arms* (灰烬战线).

![Python](https://img.shields.io/badge/Python-3.x-blue)
![OpenCV](https://img.shields.io/badge/Computer_Vision-OpenCV-green)
![Type](https://img.shields.io/badge/Type-Reroll_Automation-purple)

## 💡 Origin Story
This was my very first attempt at game automation. Faced with the repetitive task of resetting a game account to get a perfect starting team (2+ 3-star characters), I decided to write a script to do it for me. 

Although simple, this project sparked my interest in **Computer Vision** and **Process Automation**, leading to my more advanced works in FSM-based bots.

## ⚙️ How It Works
The script performs a loop of actions to "reroll" the initial gacha results until a specific condition is met.

1.  **Interaction:** Uses **ADB (Android Debug Bridge)** to simulate clicks on the "Redraw" and "Confirm" buttons.
2.  **Recognition:** Captures the screen and uses **OpenCV Template Matching** (`cv2.matchTemplate`) to detect the "3-star rarity" icon on the character cards.
3.  **Decision Logic:** * Scans the 10 character slots.
    * Counts the number of 3-star characters.
    * **Loop:** If count < 2, click "Redraw". If count >= 2, stop and notify.

## 🛠️ Tech Stack
* **Python 3.x**
* **ADB Shell:** For sending raw touch events to the Android emulator.
* **OpenCV:** For detecting visual elements (Star icons).
* **NumPy:** For handling image arrays.

## 📂 Code Highlights
* `count_3star_num()`: Iterates through fixed screen coordinates to check for specific visual patterns.
* `redraw()`: Handles the UI interaction flow for resetting the gacha.

---
*Author: Han Lin*
*See also: [My Advanced FSM Automation Framework](https://github.com/ChineseBeanLin/python_scraping-automation-tools/tree/main/03_gui_automation_rpa/android_fsm_controller)*