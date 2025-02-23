import cv2
import mediapipe as mp

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Check if webcam is opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Function to count the number of extended fingers
def count_fingers(landmarks):
    # Define finger tip landmarks
    finger_tips = [8, 12, 16, 20]  # Index, middle, ring, pinky tips
    finger_bases = [7, 11, 15, 19]  # Finger bases (just before the tips)

    extended_fingers = 0
    
    for i, tip in enumerate(finger_tips):
        # Check if the tip is above the base (indicating it is extended)
        if landmarks[tip].y < landmarks[finger_bases[i]].y:
            extended_fingers += 1
            
    # Check for the thumb separately
    # Thumb is a little different since its base is on the opposite side
    thumb_tip = 4
    thumb_base = 2
    if landmarks[thumb_tip].x > landmarks[thumb_base].x:
        extended_fingers += 1

    return extended_fingers

frame_count = 0

with mp_hands.Hands(static_image_mode=False, max_num_hands=2, min_detection_confidence=0.5, min_tracking_confidence=0.5) as hands:
    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to capture frame")
            break
        
        frame_count += 1
        
        # Flip the frame horizontally for a natural view
        frame = cv2.flip(frame, 1)
        
        # Convert the frame to RGB
        rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        
        # Process the frame to detect hands
        results = hands.process(rgb_frame)
        
        # Draw hand landmarks and count fingers if detected
        if results.multi_hand_landmarks:
            for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                # Count the number of extended fingers
                extended_fingers = count_fingers(hand_landmarks.landmark)

                # Draw landmarks on the frame
                mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)

                # Display the number of fingers detected
                cv2.putText(frame, f"Fingers: {extended_fingers}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        # Display the frame
        cv2.imshow("Live Hand Tracking", frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()

print("Hand tracking with finger count displayed in video.")
