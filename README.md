# Hand Gesture Controlled Arduino Car

## Project Overview

This project demonstrates the development of a hand gesture-controlled 2WD car chassis using OpenCV and CVZone libraries for gesture recognition, an Arduino microcontroller for car control, and a Bluetooth module for wireless communication. The system captures hand gestures via a camera, processes them in real-time, and sends corresponding movement commands to the Arduino to control the car.

## Components and Libraries

### Hardware
- **2WD Car Chassis**
- **Arduino**
- **Bluetooth Module**
- **Camera**
- **Laptop/PC**

### Software
- **Python**
- **OpenCV**
- **CVZone**
- **Arduino IDE**

## System Architecture

1. **Hand Gesture Detection:**
   - The camera captures frames in real-time.
   - OpenCV and CVZone libraries are used to detect and track hand gestures.
   - Different gestures are mapped to specific movement commands.

2. **Bluetooth Communication:**
   - The recognized gestures are sent as commands via Bluetooth to the Arduino.
   
3. **Car Control:**
   - The Arduino interprets the commands and controls the motors to move the car accordingly.

## How to Run the Project

### Prerequisites

- Install Python and the required libraries:
  ```sh
  pip install opencv-python cvzone pyserial
  ```
- Connect the Bluetooth module to the Arduino.
- Upload the provided Arduino sketch (`control.ino`) to the Arduino board.
  
### Running the Python Script

1. **Connect your camera to the laptop/PC.**
2. **Modify the COM port in the Python script (`ser = serial.Serial("COM8", 9600, timeout=1)`) to match the port your Bluetooth module is connected to.**
3. **Run the Python script (`gesture.py`)**

4. **The camera feed will start, and hand gestures will be detected and displayed.**

### Gesture Commands

- **One Finger (Right Hand):** Rotate left forward.
- **Two Fingers (Right Hand):** Rotate right forward.
- **Five Fingers (Right Hand):** Move forward.
- **One Finger (Left Hand):** Rotate left backward.
- **Two Fingers (Left Hand):** Rotate right backward.
- **Five Fingers (Left Hand):** Move backward.

### Pausing and Quitting

- **Press `p` to pause/unpause the video capture.**
- **Press `q` to quit the application.**

## Future Enhancements

- **Implement additional gestures for more complex movements.**
- **Optimize gesture recognition for better accuracy and responsiveness.**
- **Extend the system to control other robotic platforms.**

## License
This project is licensed under the [MIT License](LICENSE).
