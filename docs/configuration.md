# Configuration Guide

This document explains how to customize the **Image Analyzer** by modifying the `src/config.py` file. All core settings—from AI sensitivity to UI appearance—are centralized here.

## 📁 Paths & Directories
*   `BASE_DIR`: Automatically determines the project root folder.
*   `DATA_DIR_RAW`, `DATA_DIR_PROCESSED`: Locations for raw images and the exported `.csv` dataset.
*   `MODEL_PATH`: Points to the pre-trained `.pkl` model file.

## 🤖 AI & Machine Learning
*   `CLASSES`: Maps folder names to numeric IDs. 
    *   `0`: Neutral/Other images.
    *   `1`: Target gesture (Middle Finger).
*   `DETECTION_CONFIDENCE` (Default: `0.3`): How certain the AI must be to start mapping a hand. Increase this (e.g., to `0.5`) to reduce false positives, or decrease it if the AI is missing visible hands.
*   `TRACKING_CONFIDENCE` (Default: `0.3`): Sensitivity during subsequent frame/image tracking.
*   `MAX_NUM_HANDS` (Default: `1`): Limits how many hands the AI processes at once. Increasing this will slow down performance.

## 🕷️ Web Crawler (Data Collection)
*   `CRAWLER_IMGS_PER_MF_QUERY`: Number of images to download for target gestures.
*   `CRAWLER_IMGS_PER_OTHER_QUERY`: Number of images to download for neutral data.
*   `CRAWLER_MIDDLE_FINGER_QUERIES`: A list of search terms used to find vulgar gestures on Bing.
*   `CRAWLER_OTHER_QUERIES`: A list of search terms for "safe" data (palms, faces, nature) to help the model distinguish between hands and noise.

## 🎨 UI & Aesthetics
Customize the look and feel of the desktop application:
*   `GUI_TITLE`: The text displayed in the window header and title bar.
*   `GUI_MODEL_STATS_TEXT`: Technical details shown in the sidebar.
*   `COLOR_VULGAR` (Default: `#E74C3C` - Red): Color used when a gesture is detected.
*   `COLOR_SAFE` (Default: `#2ECC71` - Green): Color used for safe images.

## 📏 Layout & Sizes
*   `GUI_WIDTH` / `GUI_HEIGHT`: Starting dimensions of the application window.
*   `GUI_MIN_WIDTH` / `GUI_MIN_HEIGHT`: Minimum size the user can resize the window to.
*   `GUI_PREVIEW_MAX_WIDTH` / `GUI_PREVIEW_MAX_HEIGHT`: Limits the size of the uploaded image preview to prevent layout breaking.

## ✅ Verification with Test Data
A `test_data/` directory is included in the project root. It contains specialized samples to verify that the configurations (like `DETECTION_CONFIDENCE` or `CLASSES`) are working as expected:
- `mf1.JPG`: Should trigger a **VULGARISM DETECTED** alert.
- `safe1.jpg`, `safe2.jpeg`, `safe3.jpg`: Should result in a **SAFE TO UPLOAD** status.
- `person1f.png`, `person2f.png`: Used to test hand detection on crowded or complex portraits.

---

> [!TIP]
> After modifying `src/config.py`, you must restart the application for the changes to take effect. If you change the `CLASSES` or `CRAWLER_QUERIES`, you may need to re-run the data collection and model training scripts.
