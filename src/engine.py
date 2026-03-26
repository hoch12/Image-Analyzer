import cv2
import joblib
import numpy as np
import os
from PIL import Image
from src.features import extract_landmarks
from src.config import MODEL_PATH, CLASSES

class PredictionEngine:
    """
    Core engine for loading the ML model and performing inference on images.
    Connects MediaPipe landmark extraction with a Scikit-Learn classifier.
    """
    def __init__(self):
        """Initializes the engine and attempts to load the pre-trained model."""
        self.model = None
        self._load_model()
        
    def _load_model(self):
        """
        Loads the pre-trained scikit-learn model from the disk.
        Uses joblib for efficient deserialization of the Random Forest model.
        """
        if os.path.exists(MODEL_PATH):
            try:
                self.model = joblib.load(MODEL_PATH)
            except Exception as e:
                print(f"Error loading model from {MODEL_PATH}: {e}")
        else:
            print(f"Model file not found at {MODEL_PATH}")

    def predict(self, image_path: str = None, pil_image: Image.Image = None):
        """
        Predicts whether the given image contains a specific hand gesture (e.g., middle finger).
        
        This method performs the following steps:
        1. Loads the image from path or PIL object.
        2. Extracts 21 hand landmarks (63 coordinates) using MediaPipe.
        3. Feeds the landmarks into the Random Forest classifier.
        4. Returns the predicted label and confidence score.

        Args:
            image_path (str, optional): Path to the image file.
            pil_image (Image.Image, optional): Already loaded PIL Image object.
            
        Returns:
            dict: A dictionary containing:
                - "success" (bool): Whether the process completed without errors.
                - "label" (str): Predicted class ('middle_finger', 'other', or 'no_hand').
                - "confidence" (float): Probabilistic certainty of the prediction.
                - "message" (str): Human-readable status message.
        """
        if not self.model:
            return {"success": False, "message": "Model not loaded. Ensure the .pkl file exists."}

        try:
            # 1. Image acquisition
            if pil_image:
                img = np.array(pil_image.convert("RGB"))
            elif image_path:
                img = cv2.imread(image_path)
                if img is None:
                    return {"success": False, "message": "Could not read image file."}
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            else:
                return {"success": False, "message": "No image input provided."}

            # 2. Feature Extraction
            landmarks = extract_landmarks(img)
            
            if landmarks is None:
                return {
                    "success": True, 
                    "label": "no_hand", 
                    "confidence": 0.0, 
                    "message": "No hand detected in the image."
                }

            # 3. Model Inference
            features = np.array(landmarks).reshape(1, -1)
            prediction = self.model.predict(features)[0]
            
            # Map numeric class back to name for readability
            inv_classes = {v: k for k, v in CLASSES.items()}
            label = inv_classes.get(prediction, "unknown")
            
            # 4. Confidence Score Calculation
            confidence = 1.0
            if hasattr(self.model, "predict_proba"):
                probs = self.model.predict_proba(features)[0]
                confidence = float(np.max(probs))

            return {
                "success": True,
                "label": label,
                "confidence": confidence,
                "message": f"Detection complete: {label.replace('_', ' ').capitalize()}"
            }

        except Exception as e:
            return {"success": False, "message": f"Inference Error: {str(e)}"}
