import unittest
import os
import numpy as np
from src.engine import PredictionEngine
from PIL import Image

class TestPredictionEngine(unittest.TestCase):
    def setUp(self):
        self.engine = PredictionEngine()

    def test_engine_initialization(self):
        # If the model exists, it should be loaded, otherwise it should be None
        # This just checks that it doesn't crash on init
        self.assertTrue(hasattr(self.engine, 'model'))

    def test_predict_no_image(self):
        result = self.engine.predict(image_path=None, pil_image=None)
        self.assertFalse(result["success"])
        self.assertIn("No image input provided.", result["message"])

    def test_predict_invalid_path(self):
        result = self.engine.predict(image_path="non_existent.jpg")
        self.assertFalse(result["success"])
        self.assertIn("Could not read image", result["message"])

    def test_prediction_flow(self):
        # Create a dummy blank image
        dummy_img = np.zeros((100, 100, 3), dtype=np.uint8)
        pil_img = Image.fromarray(dummy_img)
        
        result = self.engine.predict(pil_image=pil_img)
        self.assertTrue(result["success"])
        # Since it's a blank image, no hand should be detected
        self.assertEqual(result["label"], "no_hand")

if __name__ == "__main__":
    unittest.main()
