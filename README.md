# Virtual-Keyboard-Computer-Vision-Mini-Project
## Overview
This project is part of a larger software development initiative for Smart Glasses, specifically focused on creating a Virtual Keyboard using computer vision techniques. The virtual keyboard allows users to interact with a keyboard displayed on the screen by tracking their hand movements and gestures. This implementation utilizes the OpenCV and cvzone libraries to detect and track hand movements, and the pynput library to simulate keyboard inputs.

## Features
- Hand Tracking: Utilizes the cvzone HandTrackingModule to detect and track hand movements.
- Virtual Keyboard: Displays a virtual keyboard on the screen that users can interact with using hand gestures.
- Key Press Simulation: Uses the pynput library to simulate actual key presses on the system based on the user's interactions with the virtual keyboard.

## File Descriptions
### multiHandTracking.py
- This script is responsible for detecting and tracking multiple hands using the cvzone HandTrackingModule. 
- Key functionalities include:
    1. Capturing video feed from the webcam.
    2. Detecting hands and tracking their landmarks.
    3. Calculating distances between key landmarks to determine gestures.
    4. Displaying the processed video feed with hand landmarks and bounding boxes.
### virtualKeyboard.py
- This script implements the virtual keyboard functionality. 
- Key functionalities include:
    1. Displaying a virtual keyboard on the screen.
    2. Detecting hand gestures to determine which key is being "pressed."
    3. Simulating key presses using the pynput library.
    4. Handling special keys like Space, Enter, and Clear.
## Dependencies
1. OpenCV
2. cvzone
3. numpy
4. pynput
