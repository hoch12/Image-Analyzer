import os

# ------------------------------------------------------------------------------
# Image Analyzer - Centralized Configuration
# ------------------------------------------------------------------------------

# --- 1. Data Collection & Preprocessing Paths ---
DATA_DIR_RAW = "data/raw"
SAVE_DIR_MIDDLE = os.path.join(DATA_DIR_RAW, "middle_finger")
SAVE_DIR_OTHER = os.path.join(DATA_DIR_RAW, "other")

DATA_DIR_PROCESSED = "data/processed"
OUTPUT_CSV_PATH = os.path.join(DATA_DIR_PROCESSED, "hand_landmarks.csv")

MODEL_DIR = "models"
MODEL_PATH = os.path.join(MODEL_DIR, "middle_finger_model.pkl")

# --- 2. Class Labels & Machine Learning ---
# 0 = other, 1 = middle_finger
CLASSES = {
    "other": 0,
    "middle_finger": 1
}

# --- 3. Web Crawler Configuration ---
# Maximum images to theoretical download per query
CRAWLER_IMGS_PER_MF_QUERY = 150
CRAWLER_IMGS_PER_OTHER_QUERY = 100

CRAWLER_MIDDLE_FINGER_QUERIES = [
    "person showing middle finger",
    "middle finger gesture",
    "flipping the bird gesture",
    "hand pointing middle finger",
    "middle finger sign",
    "angry person middle finger",
    "showing the finger gesture",
    "middle finger isolated clear",
    "person face with middle finger gesture",
    "celebrity showing middle finger",
    "selfie showing middle finger",
    "crowd person pointing middle finger",
    "woman showing middle finger to camera",
    "man flipping bird portrait",
    "kid showing middle finger"
]

CRAWLER_OTHER_QUERIES = [
    "thumbs up hand gesture",
    "waving hand person",
    "open palm hand",
    "fist bump gesture",
    "peace sign hand fingers",
    "pointing index finger",
    "holding pen hand",
    "ok hand gesture sign",
    "clapping hands",
    "crossed fingers luck",
    "shaking hands gesture",
    "thumbs down gesture",
    "empty room interior",
    "nature landscape background",
    "person walking away",
    "person smiling face portrait",
    "group of people taking selfie",
    "man hands in pockets",
    "woman holding smartphone",
    "crowd of people cheering",
    "person eating food close up",
    "dog playing in park",
    "car driving on street"
]

# --- 4. Validation Rules ---
ALLOWED_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')
