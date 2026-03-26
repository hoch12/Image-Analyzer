import cv2
import mediapipe as mp

from src.config import DETECTION_CONFIDENCE, TRACKING_CONFIDENCE, MAX_NUM_HANDS

"""
Module for extracting hand landmarks using MediaPipe.
"""

# Initialize MediaPipe Hands once globally to save initialization time during inference
_mp_hands = mp.solutions.hands
_hands_detector = _mp_hands.Hands(
    static_image_mode=True,        # Set to True for processing individual images in GUI
    max_num_hands=MAX_NUM_HANDS,   # Configurable via src/config.py
    min_tracking_confidence=TRACKING_CONFIDENCE,
    min_detection_confidence=DETECTION_CONFIDENCE
)

def extract_landmarks(image_rgb) -> list[float] | None:
    """
    Extracts 63 (21 * 3) hand landmarks from an RGB image using MediaPipe.
    
    Args:
        image_rgb: An RGB image array (e.g. from cv2.cvtColor(img, cv2.COLOR_BGR2RGB))
        
    Returns:
        A flat list of 63 floats [x0, y0, z0, x1, y1, z1...] if a hand is detected.
        Returns None if no hand is detected.
    """
    results = _hands_detector.process(image_rgb)
    
    if not results.multi_hand_landmarks:
        return None
        
    # Take the first detected hand
    hand_landmarks = results.multi_hand_landmarks[0]
    
    # Flatten the 21 landmarks (x, y, z) into a single 1D array (63 features)
    features = []
    for point in hand_landmarks.landmark:
        features.extend([point.x, point.y, point.z])
        
    return features

def cleanup():
    """Closes the MediaPipe detector to free resources."""
    _hands_detector.close()
