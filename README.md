# Virtual-Keyboard-Computer-Vision-Mini-Project
## Overview
This project is part of a larger software development initiative for Smart Glasses, specifically focused on creating a Virtual Keyboard using computer vision techniques. The virtual keyboard allows users to interact with a keyboard displayed on the screen by tracking their hand movements and gestures. This implementation utilizes the OpenCV and cvzone libraries to detect and track hand movements, and the pynput library to simulate keyboard inputs.

## Features
Hand Tracking: Utilizes the cvzone HandTrackingModule to detect and track hand movements.
Virtual Keyboard: Displays a virtual keyboard on the screen that users can interact with using hand gestures.
Key Press Simulation: Uses the pynput library to simulate actual key presses on the system based on the user's interactions with the virtual keyboard.

## File Descriptions
### multiHandTracking.py
This script is responsible for detecting and tracking multiple hands using the cvzone HandTrackingModule. Key functionalities include:
    Capturing video feed from the webcam.
    Detecting hands and tracking their landmarks.
    Calculating distances between key landmarks to determine gestures.
    Displaying the processed video feed with hand landmarks and bounding boxes.
### virtualKeyboard.py
This script implements the virtual keyboard functionality. Key functionalities include:
    Displaying a virtual keyboard on the screen.
    Detecting hand gestures to determine which key is being "pressed."
    Simulating key presses using the pynput library.
    Handling special keys like Space, Enter, and Clear.
## Dependencies
    OpenCV
    cvzone
    numpy
    pynput
