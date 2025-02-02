import cv2
import mediapipe as mp
import csv

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils

# Open webcam
cap = cv2.VideoCapture(0)

# Check if webcam is opened
if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

# Create a CSV file and write the header
csv_filename = "hand_landmarks3.csv"
with open(csv_filename, mode='w', newline='') as file:
    writer = csv.writer(file)
    header = ["Frame", "Hand", "Landmark", "X", "Y", "Z"]
    writer.writerow(header)

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
        
        # Open the CSV file in append mode
        with open(csv_filename, mode='a', newline='') as file:
            writer = csv.writer(file)
            
            # Draw hand landmarks if detected and save to CSV
            if results.multi_hand_landmarks:
                for hand_index, hand_landmarks in enumerate(results.multi_hand_landmarks):
                    for idx, landmark in enumerate(hand_landmarks.landmark):
                        writer.writerow([frame_count, hand_index, idx, landmark.x, landmark.y, landmark.z])
                    
                    # Draw landmarks on the frame
                    mp_drawing.draw_landmarks(frame, hand_landmarks, mp_hands.HAND_CONNECTIONS)
        
        # Display the frame
        cv2.imshow("Live Hand Tracking", frame)
        
        # Exit when 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# Release resources
cap.release()
cv2.destroyAllWindows()

print(f"Hand landmarks saved to {csv_filename}")
