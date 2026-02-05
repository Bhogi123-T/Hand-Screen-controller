import cv2
import mediapipe as mp
import pyautogui
from math import hypot
import time

# Screen size
screen_width, screen_height = pyautogui.size()

# Mediapipe hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
mp_draw = mp.solutions.drawing_utils

# Webcam
cap = cv2.VideoCapture(0)

# Variables for double click timing and drag control
last_click_time = 0
double_click_interval = 0.4  # seconds
dragging = False

# Variables for swipe detection
prev_x = None
swipe_threshold = 40
swipe_cooldown = 1.0
last_swipe_time = 0

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    h, w, c = frame.shape

    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    result = hands.process(rgb_frame)

    if result.multi_hand_landmarks:
        for hand_landmarks in result.multi_hand_landmarks:
            mp_draw.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

            landmarks = hand_landmarks.landmark

            # Correctly accessing specific landmarks by index
            index_finger = landmarks[8]
            thumb = landmarks
            middle_finger = landmarks

            # Convert normalized coordinates to pixel coordinates
            x = int(index_finger.x * w)
            y = int(index_finger.y * h)

            thumb_x = int(thumb.x * w)
            thumb_y = int(thumb.y * h)

            mid_x = int(middle_finger.x * w)
            mid_y = int(middle_finger.y * h)

            # Move mouse cursor
            screen_x = screen_width / w * x
            screen_y = screen_height / h * y
            pyautogui.moveTo(screen_x, screen_y)

            # Calculate distances for gestures
            pinch_dist = hypot(x - thumb_x, y - thumb_y)
            scroll_dist = hypot(x - mid_x, y - mid_y)

            pinch_threshold = 30

            # Drag and drop with pinch
            if pinch_dist < pinch_threshold:
                if not dragging:
                    pyautogui.mouseDown()
                    dragging = True
            else:
                if dragging:
                    pyautogui.mouseUp()
                    dragging = False

            # Double click on quick pinch
            current_time = time.time()
            if pinch_dist < pinch_threshold:
                if current_time - last_click_time > double_click_interval:
                    pyautogui.click()
                    if current_time - last_click_time < 0.3:
                        pyautogui.doubleClick()
                    last_click_time = current_time

            # Scroll up/down based on index-middle finger distance
            if scroll_dist < 30:
                pyautogui.scroll(-20)  # scroll down
                time.sleep(0.2)
            elif scroll_dist > 100:
                pyautogui.scroll(20)   # scroll up
                time.sleep(0.2)

            # Swipe left/right to send keyboard arrow presses
            if prev_x is not None and (current_time - last_swipe_time) > swipe_cooldown:
                diff = x - prev_x
                if diff > swipe_threshold:
                    pyautogui.press('right')
                    last_swipe_time = current_time
                elif diff < -swipe_threshold:
                    pyautogui.press('left')
                    last_swipe_time = current_time

            prev_x = x

    cv2.imshow("Hand Screen Control", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()

