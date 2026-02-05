import cv2
import mediapipe as mp
import pyautogui

# Screen size
screen_width, screen_height = pyautogui.size()

# Mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # Flip frame (mirror effect)
    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    # Convert to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            # Index finger tip (landmark 8)
            index_finger = hand_landmarks.landmark[8]
            x = int(index_finger.x * w)
            y = int(index_finger.y * h)

            # Move mouse
            screen_x = screen_width / w * x
            screen_y = screen_height / h * y
            pyautogui.moveTo(screen_x, screen_y)

            # Thumb tip (landmark 4)
            thumb = hand_landmarks.landmark[4]
            thumb_x, thumb_y = int(thumb.x * w), int(thumb.y * h)

            # Middle finger tip (landmark 12)
            middle_finger = hand_landmarks.landmark[12]
            mid_x, mid_y = int(middle_finger.x * w), int(middle_finger.y * h)

            # Detect pinch (index + thumb close) = Left Click
            if abs(x - thumb_x) < 30 and abs(y - thumb_y) < 30:
                pyautogui.click()
                pyautogui.sleep(0.2)

            # Detect two-finger gesture (index + middle close) = Right Click
            if abs(x - mid_x) < 30 and abs(y - mid_y) < 30:
                pyautogui.click(button='right')
                pyautogui.sleep(0.2)

    cv2.imshow("Hand Screen Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
