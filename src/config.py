import os

"""
Central configuration for the Image Analyzer project.
Contains data paths, model parameters, and search queries for the crawler.
"""

# --- Project Root & Paths ---
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Data directories
DATA_DIR = os.path.join(BASE_DIR, "data")
DATA_DIR_RAW = os.path.join(DATA_DIR, "raw")
DATA_DIR_PROCESSED = os.path.join(DATA_DIR, "processed")

# Specific data subdirectories
SAVE_DIR_MIDDLE = os.path.join(DATA_DIR_RAW, "middle_finger")
SAVE_DIR_OTHER = os.path.join(DATA_DIR_RAW, "other")
OUTPUT_CSV_PATH = os.path.join(DATA_DIR_PROCESSED, "hand_landmarks.csv")

# Model storage
MODEL_DIR = os.path.join(BASE_DIR, "models")
MODEL_PATH = os.path.join(MODEL_DIR, "middle_finger_model.pkl")

# --- Model & ML Configuration ---
# 0 = other, 1 = middle_finger
CLASSES = {
    "other": 0,
    "middle_finger": 1
}

# --- MediaPipe Configuration ---
# Thresholds for hand detection and tracking in individual images
DETECTION_CONFIDENCE = 0.3
TRACKING_CONFIDENCE = 0.3
MAX_NUM_HANDS = 1

# --- Web Crawler Configuration ---
# Maximum images to attempt downloading per individual query
CRAWLER_IMGS_PER_MF_QUERY = 80
CRAWLER_IMGS_PER_OTHER_QUERY = 100

# Search terms used by icrawler to build the training dataset
CRAWLER_MIDDLE_FINGER_QUERIES = [
    "middle finger extended hand sign illustration",
    "offensive middle finger hand gesture stock photo",
    "middle finger hand gesture sign isolated on white",
    "giving the middle finger clear close up",
    "middle finger gesture hand drawing vector",
    "hand showing middle finger graphic symbol"
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
    "nature landscape background",
    "person walking away",
    "person smiling face portrait",
    "group of people taking selfie",
    "man hands in pockets",
    "woman holding smartphone"
]

# --- Validation Rules ---
ALLOWED_IMAGE_EXTENSIONS = ('.png', '.jpg', '.jpeg')

# --- GUI Configuration ---
GUI_TITLE = "Vulgarism Image Analyzer 🔍"
GUI_MODEL_STATS_TEXT = "Accuracy: 90.34%\nRecall: 69%\nDataset: 2500+ samples\nModel: Random Forest\nLanguage: Python\n\nGitHub: hoch12/Image-Analyzer"
GUI_GITHUB_URL = "https://github.com/hoch12/Image-Analyzer"
COLOR_VULGAR = "#E74C3C"
COLOR_SAFE = "#2ECC71"

# --- UI Layout & Sizes ---
GUI_WIDTH = 950
GUI_HEIGHT = 750
GUI_MIN_WIDTH = 850
GUI_MIN_HEIGHT = 650
GUI_SIDEBAR_DESC = "AI tool for automatic\nmoderation of vulgar\nhand gestures in images."
GUI_PREVIEW_MAX_WIDTH = 500
GUI_PREVIEW_MAX_HEIGHT = 400
