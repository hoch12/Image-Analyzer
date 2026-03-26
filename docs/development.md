# Development Lifecycle - Image Analyzer

This document outlines the engineering phases taken to build the Vulgarism Image Analyzer, from data acquisition to model deployment.

## Phase 1: Research & Problem Definition
The goal was to create a real-time moderation tool for detecting offensive hand gestures (specifically the middle finger) in profile pictures. MediaPipe was selected for hand landmark extraction due to its speed and accuracy on consumer hardware.

## Phase 2: Data Collection (Requirements 8 & 10)
Following the assignment requirements, a custom dataset was harvested using web crawling.
- **Tools**: `icrawler` with Bing/Google search engines.
- **Volume**: 1500+ raw images collected.
- **Classes**: 
    - `middle_finger`: Images of hand showing the middle finger.
    - `other`: Images of open palms, fists, peace signs, and other neutral gestures.
- **Scripts**: `data_collection/collect_data.py`.

## Phase 3: Data Preprocessing & Feature Engineering
Raw images were converted into a structured numerical format.
- **Landmark Extraction**: Each image was processed by MediaPipe to extract 21 hand landmarks (x, y, z coordinates).
- **Flattening**: The 21 landmarks were flattened into a 63-feature vector for classification.
- **Cleaning**: Corrupt images or images where no hand was detected were automatically filtered out.

## Phase 4: Model Training
- **Architecture**: A Random Forest Classifier from `scikit-learn` was chosen for its reliability and low inference latency.
- **Workflow**: Documented in `notebooks/Model_Training.ipynb`.
- **Validation**: 20% test split, achieving ~98.5% accuracy on the current dataset.
- **Export**: The final model is serialized to `models/middle_finger_model.pkl` using `joblib`.

## Phase 5: GUI Application Development
The final stage involved building a desktop interface using `CustomTkinter`.
- **Sidebar**: Technical details and repository links.
- **Real-time Inference**: Drag-and-drop or upload functionality.
- **Confidence Meter**: Visual feedback of the model's certainty.
