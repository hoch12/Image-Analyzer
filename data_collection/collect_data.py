import cv2
import os
import time

# Configuration
SAVE_DIR_MIDDLE = "data/raw/middle_finger"
SAVE_DIR_OTHER = "data/raw/other"

# Ensure directories exist
os.makedirs(SAVE_DIR_MIDDLE, exist_ok=True)
os.makedirs(SAVE_DIR_OTHER, exist_ok=True)

# Application State
is_recording = False
current_class = "middle_finger"  # default class
frames_saved_middle = len(os.listdir(SAVE_DIR_MIDDLE))
frames_saved_other = len(os.listdir(SAVE_DIR_OTHER))
last_save_time = time.time()
SAVE_INTERVAL = 0.1  # Save a frame every 0.1 seconds (10 fps) when recording

def get_save_dir(cls):
    return SAVE_DIR_MIDDLE if cls == "middle_finger" else SAVE_DIR_OTHER

def main():
    global is_recording, current_class, frames_saved_middle, frames_saved_other, last_save_time
    
    print("=========================================")
    print(" Image Analyzer - Data Collection Script ")
    print("=========================================")
    print("Controls:")
    print("  [1] - Select 'middle_finger' class")
    print("  [2] - Select 'other' class")
    print("  [s] - Toggle recording ON/OFF")
    print("  [q] - Quit script")
    print("=========================================")

    # Initialize Webcam
    cap = cv2.VideoCapture(0)
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Error: Failed to grab frame.")
            break

        # Flip the frame horizontally for a more intuitive mirror view
        frame = cv2.flip(frame, 1)
        
        # Display Information on the frame
        status_color = (0, 255, 0) if is_recording else (0, 0, 255)
        status_text = "RECORDING" if is_recording else "PAUSED"
        
        cv2.putText(frame, f"Status: {status_text}", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, status_color, 2)
        cv2.putText(frame, f"Class: {current_class}", (10, 60), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 255, 0), 2)
        cv2.putText(frame, f"Middle Finger: {frames_saved_middle} imgs", (10, 90), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        cv2.putText(frame, f"Other: {frames_saved_other} imgs", (10, 115), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 255, 255), 1)
        
        cv2.imshow("Data Collection", frame)

        # Handle Save Logic
        if is_recording:
            current_time = time.time()
            if current_time - last_save_time >= SAVE_INTERVAL:
                save_dir = get_save_dir(current_class)
                # Generate unique filename using timestamp
                filename = os.path.join(save_dir, f"img_{int(current_time * 1000)}.jpg")
                cv2.imwrite(filename, frame)
                
                if current_class == "middle_finger":
                    frames_saved_middle += 1
                else:
                    frames_saved_other += 1
                    
                last_save_time = current_time

        # Handle Keyboard Input
        key = cv2.waitKey(1) & 0xFF
        
        if key == ord('q'):
            break
        elif key == ord('1'):
            current_class = "middle_finger"
            print("Class switched to: middle_finger")
        elif key == ord('2'):
            current_class = "other"
            print("Class switched to: other")
        elif key == ord('s'):
            is_recording = not is_recording
            print(f"Recording toggled: {is_recording}")

    # Cleanup
    cap.release()
    cv2.destroyAllWindows()
    print("Data collection finished.")

if __name__ == "__main__":
    main()
