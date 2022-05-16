import cv2, mediapipe as mp, time

#Video capture using first camera in the system
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw =  mp.solutions.drawing_utils


while True:
    #Capture hand image
    success,img = cap.read()

    #Process hand image
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    result = hands.process(imgRGB)

    #Check if we have multiple hands, loop through 
    if result.multi_hand_landmarks:
        for handLms in result.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHands.HAND_CONNECTIONS)

    #Show image frame
    cv2.imshow('Image',img)

    #Quit when 'q' is hit
    if cv2.waitKey(1) == ord('q'):
        break

    # cv2.waitKey(0)

# cap.release()
# cv2.destroyAllWindows()








