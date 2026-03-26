# Testing Methodology - Image Analyzer

This document describes the testing strategies applied to ensure the reliability of landmkark extraction and classification.

## 1. Automated Testing (Unit Tests)
Unit tests are located in the `tests/` directory and focus on the core logic.
- **Hand Detection**: Tests whether the `extract_landmarks` function correctly identifies hands in sample images.
- **Inference Engine**: Tests the `PredictionEngine` with known safe and unsafe samples to verify the `middle_finger` vs `other` detection.
- **Config Integrity**: Ensures that paths and labels in `src/config.py` are valid.

**Run tests via:**
```bash
python3 -m unittest discover tests
```

## 2. Manual Testing Scenarios (Browser/GUI)
Several manual testing scenarios were performed using the GUI application to simulate real-world usage:

### Scenario A: Clear Middle Finger
- **Input**: Image with a centered, clear middle finger gesture.
- **Expected**: "⚠️ VULGARISM DETECTED" status, red bar, confidence > 90%.
- **Result**: PASSED.

### Scenario B: Neutral Hand Gesture (Peace Sign)
- **Input**: Image with a peace sign gesture.
- **Expected**: "✅ SAFE TO UPLOAD" status, green bar, labeled as `other`.
- **Result**: PASSED.

### Scenario C: No Hand (Landscape Photo)
- **Input**: A photo of a forest or city.
- **Expected**: "✅ No Hands Detected (Safe)" status, Confidence: N/A.
- **Result**: PASSED.

### Scenario D: Edge Case - Poor Lighting
- **Input**: Dimly lit photo of a gesture.
- **Expected**: Detection might fail (No hand detected) or show lower confidence.
- **Action**: Thresholds in `src/config.py` were adjusted (min_confidence 0.3) to handle these cases.

## 3. Integration Testing
Verification of the end-to-end flow from file selection to result display in the GUI.
- **Cursor interaction**: Verified that the GitHub link in the sidebar opens in the default browser.
- **Appearance mode**: Verified that the app correctly toggles between Light/Dark/System themes.
