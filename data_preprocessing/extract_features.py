import os
import sys
import cv2
import mediapipe as mp
import pandas as pd
import numpy as np

# Add project root to path for central config
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from src import config

# Ensure output directory exists based on config
os.makedirs(config.DATA_DIR_PROCESSED, exist_ok=True)

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(
    static_image_mode=True,        # Set to True for processing individual images
    max_num_hands=1,               # We only care about the primary hand doing the gesture
    min_detection_confidence=0.5
)

# Classes mapping from central config
CLASSES = config.CLASSES

def extract_features():
    print("===============================================")
    print(" Image Analyzer - MediaPipe Feature Extraction ")
    print("===============================================")
    
    data_rows = []
    total_images_scanned = 0
    images_with_hands = 0
    images_skipped = 0
    
    # Define columns for our CSV
    # We will have 21 landmarks * 3 coordinates (x, y, z) = 63 features + 1 class label
    columns = []
    for i in range(21):
        columns.extend([f"landmark_{i}_x", f"landmark_{i}_y", f"landmark_{i}_z"])
    columns.append("class_label")

    print(f"[*] Scanning directory: {config.DATA_DIR_RAW}")
    
    # Iterate through all classes (folders)
    for class_name, label_id in CLASSES.items():
        class_folder = os.path.join(config.DATA_DIR_RAW, class_name)
        if not os.path.exists(class_folder):
            print(f"[!] Warning: Folder {class_folder} does not exist. Skipping.")
            continue
            
        print(f"\n[*] Processing class: '{class_name}' (Label: {label_id})")
        
        image_files = [f for f in os.listdir(class_folder) if f.lower().endswith(config.ALLOWED_IMAGE_EXTENSIONS)]
        
        for idx, img_file in enumerate(image_files):
            total_images_scanned += 1
            img_path = os.path.join(class_folder, img_file)
            
            # Read image
            image = cv2.imread(img_path)
            if image is None:
                continue
                
            # Convert BGR (OpenCV) to RGB (MediaPipe)
            image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
            
            # Process image and extract landmarks
            results = hands.process(image_rgb)
            
            # If hands are found in the image
            if results.multi_hand_landmarks:
                images_with_hands += 1
                # Take the first detected hand
                hand_landmarks = results.multi_hand_landmarks[0]
                
                # Flatten the 21 landmarks (x, y, z) into a single 1D array
                row = []
                for point in hand_landmarks.landmark:
                    row.extend([point.x, point.y, point.z])
                    
                # Append the class label at the end
                row.append(label_id)
                data_rows.append(row)
            else:
                # No hands detected in the image (e.g., empty room, background)
                images_skipped += 1
                
            # Progress tracker
            if (idx + 1) % 100 == 0:
                print(f"    - Processed {idx + 1}/{len(image_files)} images...")

    # Cleanup MediaPipe
    hands.close()

    print("\n===============================================")
    print(" Extraction Summary:")
    print(f" Total images scanned: {total_images_scanned}")
    print(f" Images WITH hands   : {images_with_hands}")
    print(f" Images SKIPPED      : {images_skipped} (No hands detected)")
    print("===============================================")
    
    if data_rows:
        print(f"\n[*] Creating DataFrame with {images_with_hands} rows and {len(columns)} columns...")
        df = pd.DataFrame(data_rows, columns=columns)
        df.to_csv(config.OUTPUT_CSV_PATH, index=False)
        print(f"[+] Dataset successfully saved to: {config.OUTPUT_CSV_PATH}")
    else:
        print("[-] Error: No hands were detected in any of the images. CSV not created.")

if __name__ == "__main__":
    extract_features()
