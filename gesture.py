import serial
import cv2
from collections import Counter
import time
from cvzone.HandTrackingModule import HandDetector
detector = HandDetector(detectionCon=0.8, maxHands=2)

ser = serial.Serial("COM8", 9600, timeout=1)


# Initialize video capture and set the properties
width = 640
height = 480
cam = cv2.VideoCapture(0, cv2.CAP_DSHOW)
cam.set(cv2.CAP_PROP_FRAME_WIDTH, width)
cam.set(cv2.CAP_PROP_FRAME_HEIGHT, height)
cam.set(cv2.CAP_PROP_FPS, 30)
cam.set(cv2.CAP_PROP_FOURCC, cv2.VideoWriter_fourcc(*'MJPG'))

pause = False  # Flag to control pausing/unpausing

while True:
    if not pause:  # Only capture frames if not paused
        ret, frame = cam.read()
        # ret will contain a boolean value indicating if the frame was captured successfully
        # frame will contain the image captured from the camera
        cv2.putText(frame, 'Press q to quit, p to pause/unpause', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
        if ret:
            hands, image = detector.findHands(frame)
            # hands contains elements which have properties of each detected hand, image contains the hand image
            if len(hands) == 0:  # if there are no detected hands
                cv2.putText(frame, 'No hands detected', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                ser.write(b'0')  # no movement
            
            if len(hands) == 1:#if there are detected hands
                cv2.putText(frame, 'One hand detected', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                hand1 = hands[0]#hand1 will be the element which has hand properties
                finger = detector.fingersUp(hands[0])#this counts the fingers up in the detected hand
                #it returns an array of 5 elements, either 1 or 0, from thumb to pinkie i.e [1, 0, 0, 0, 0] means only thumb
                count = Counter(finger)#instance to count number of fingers up
                if hand1['type'] == 'Right':#if hand detected is right hand
                    if count[1] == 1:#if one finger is up, rotate left forward
                        cv2.putText(frame, 'Movement: Rotate left forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                        ser.write(b'0')
                        ser.write(b'1')
                    elif count[1] == 2:#if two fingers are up, rotate right forward
                        cv2.putText(frame, 'Movement: Rotate right forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                        ser.write(b'0')
                        ser.write(b'2')
                    elif count[1] == 5:#if five fingers are up, forward movement
                        cv2.putText(frame, 'Movement: Forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                        ser.write(b'0')
                        ser.write(b'3')
                    else:
                        cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                        ser.write(b'0')
                if hand1['type'] == 'Left':
                    if count[1] == 1:#if one finger is up, rotate left backward
                        cv2.putText(frame, 'Movement: Rotate left backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        ser.write(b'0')
                        ser.write(b'4')
                    elif count[1] == 2:#if two fingers are up, rotate right backward
                        cv2.putText(frame, 'Movement: Rotate right backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        ser.write(b'0')
                        ser.write(b'5')
                    elif count[1] == 5:#if five fingers are up, backward movement
                        cv2.putText(frame, 'Movement: Backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                        ser.write(b'0')
                        ser.write(b'6')
                    else:
                        cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                        ser.write(b'0')
                
            if len(hands) == 2:
                cv2.putText(frame, 'Two hands detected', (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                hand1 = hands[1]; finger1 = detector.fingersUp(hands[1]); count1 = Counter(finger1)
                hand2 = hands[0]; finger2 = detector.fingersUp(hands[0]); count2 = Counter(finger2)
                if hand1['type'] == 'Right':#if first hand detected is right hand
                    if count2[1] == 0:
                        if count1[1] == 1:
                            cv2.putText(frame, 'Movement: Rotate left forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'1')
                        elif count1[1] == 2:
                            cv2.putText(frame, 'Movement: Rotate right forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'2')
                        elif count1[1] == 5:
                            cv2.putText(frame, 'Movement: Forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'3')
                        else:
                            cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                    elif count1[1] == 0:
                        if count2[1] == 1:
                            cv2.putText(frame, 'Movement: Rotate left backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'4')
                        elif count2[1] == 2:
                            cv2.putText(frame, 'Movement: Rotate right backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'5')
                        elif count2[1] == 5:
                            cv2.putText(frame, 'Movement: Backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'6')
                        else:
                            cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                    else:
                        ser.write(b'0')
                if hand1['type'] == 'Left':#if first hand detected is left hand
                    if count2[1] == 0:
                        if count1[1] == 1:
                            cv2.putText(frame, 'Movement: Rotate left backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'4')
                        elif count1[1] == 2:
                            cv2.putText(frame, 'Movement: Rotate right backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'5')
                        elif count1[1] == 5:
                            cv2.putText(frame, 'Movement: Backward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'6')
                        else:
                            cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                    elif count1[1] == 0:
                        if count2[1] == 1:
                            cv2.putText(frame, 'Movement: Rotate left forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'1')
                        elif count2[1] == 2:
                            cv2.putText(frame, 'Movement: Rotate right forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'2')
                        elif count2[1] == 5:
                            cv2.putText(frame, 'Movement: Forward', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                            ser.write(b'3')
                        else:
                            cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                            ser.write(b'0')
                    else:
                        cv2.putText(frame, 'No Movement', (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2, cv2.LINE_AA)
                        ser.write(b'0')

        cv2.imshow('capture image', frame)

    key = cv2.waitKey(1)
    if key == ord('q'):
        ser.write(b'0')
        break
    elif key == ord('p'):  # Toggle pause/unpause
        pause = not pause

# Release resources
cam.release()
cv2.destroyAllWindows()
ser.close()
