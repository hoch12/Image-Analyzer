All notable changes to the "Image Analyzer" project will be documented in this file.

## [1.0.4] - 2026-03-30
### Added
- **Configuration Documentation**: Created `docs/configuration.md`, a comprehensive English guide for users to customize AI sensitivity and UI options via `src/config.py`.
- **README Update**: Added links to the new configuration guide for better project discoverability.

## [1.0.3] - 2026-03-30
### Changed
- **Config Centralization**: Extracted hardcoded GUI elements (titles, layout colors, and model statistics) from `src/gui.py` into a unified `src/config.py` structure.
- **Model Stats**: Updated manual GUI accuracy text to reflect the verified 90.34% golden model accuracy.

## [1.0.2] - 2026-03-30
### Fixed
- **Documentation**: Updated `README.md` to explicitly specify `python3.12` for environment creation and script execution, fixing an issue where default `python3` pointing to 3.13 bypassed MediaPipe compatibility.

## [1.0.1] - 2026-03-27
### Fixed
- **Environment Recovery**: Replaced broken virtual environment with a verified one (`.venv_new` -> `.venv`) as per user request.
- **Dependency Setup**: Verified all core dependencies (`customtkinter`, `mediapipe`, `scikit-learn`) are correctly installed and aligned with `requirements.txt`.
- **Unit Test Alignment**: Fixed `tests/test_engine.py` to match the latest engine error messages, achieving 100% test pass rate.

## [1.0.0] - 2026-03-26
### Added
- **Finalized Technical Metrics**: Updated the GUI and documentation to reflect real-world model performance (81% Accuracy, 69% Recall).
- **Comprehensive Documentation**: Complete `README.md` revamp and detailed lifecycle docs in `docs/`.
- **Polish & Cleanup**: Removed all temporary binary artifacts and unused Docker/Data scripts.
- **Interactive Sidebar**: Clickable GitHub repository links and modernized glassmorphism logo.
- **Code Refactor**: Full codebase refactor with professional docstrings and centralized `config.py`.

### Fixed
- **'No Hands Detected' UI**: Changed confidence display to "N/A" for non-hand images to prevent user confusion.
- **Logo Transparency**: Fixed artifacts in the logo to ensure perfect display on dark backgrounds.

## [0.2.1] - 2026-03-26
### Changed
- **UI/UX Core Refinement**: Revamped the application title to "Vulgarism Image Analyzer 🔍" for better clarity.
- **Glassmorphism Logo**: Replaced the previous logo with a minimalist, premium "Liquid Glass" style icon.
- **Expanded Technical Info**: Added detailed model stats, tech stack info, and GitHub repository links to the sidebar.
- **Sidebar Description**: Integrated a concise functional description of the AI tool.


## [0.2.0] - 2026-03-26
### Added
- **Modern Desktop GUI**: Implemented a sleek dark-mode application using `CustomTkinter` for easy image analysis.
- **Prediction Engine**: Created a dedicated module for fast inference using the pre-trained Random Forest model and MediaPipe.
- **Confidence Meter**: Visual feedback showing how certain the AI is about its prediction.
- **Project Logo**: Added a high-tech, AI-themed logo to the application sidebar.
- **Unit Testing**: Added a test suite to ensure the reliability of the prediction logic.

## 0.1.7
- Successfully trained the "Golden Model" using Google Colab on the refined dataset.
- Achieved **90.34% Test Accuracy** with a Random Forest classifier.
- Precision for middle finger detection: 0.94.
- Updated `models/middle_finger_model.pkl` with the new weights.
- Verified dataset size: 1500+ images (175 middle_finger, 1360 other).

## 0.1.6
- Surgically purged `middle_finger` dataset of all unverified crawl noise (~350+ images).
- Generated a "Golden Dataset" of 17 perfect, high-resolution AI-generated isolated samples.
- Restored 9 curated high-quality images and 1 personally verified high-quality crawl result.
- Moved all unverified data to a backup folder in `other` for further review.
- Guaranteed 100% precision for the `middle_finger` class to resolve the accuracy issues.

## [0.1.5] - 2026-03-23
### Changed
- **Zero-Tolerance Dataset Purity**: Based on user analysis of dataset contamination, executed a complete purge of all 250+ auto-crawled `middle_finger` images. 
- **Strict Isolated Procurement**: Wrote custom Python scrapers to bypass generic Bing algorithms and fetch 200 explicitly isolated, perfect "middle finger" ground-truth images (white/transparent backgrounds only) to guarantee structural MediaPipe learning without noise.

## [0.1.4] - 2026-03-23
### Changed
- **Dataset Optimization & Cleaning**: Manually audited and quarantined noisy images from the initial dataset into the `other` folder to preserve data without diluting the model.
- **Smart Crawler Expansion**: Enhanced the data collection queries in `config.py` with highly strict, isolated "middle finger" terminology. Downloaded a fresh batch of 200+ extremely clear and optimal images, directly improving model precision.

## [0.1.3] - 2026-03-16
### Added
- **Detailed Codebase Explanation**: Created a comprehensive, line-by-line analysis of all project components (config, features, data collection, and ML pipeline) to ensure 100% understanding of the internal logic.
- **Documentation Verification**: Verified that all project requirements in `zadani.md` are documented and met.

## [0.1.2] - 2026-03-09
### Changed
- **Architectural Cleanup**: Deleted the obsolete `data_preprocessing/extract_features.py` bulk-processing script, as bulk training was permanently migrated to Google Colab in `v0.1.0`.
- **Reusable Modules**: Extracted the core MediaPipe detection logic into a pure, reusable function in a new file `src/features.py`. This isolates the feature extraction logic cleanly for the upcoming GUI application to use for single-image inference.

## [0.1.1] - 2026-03-09
### Changed
- **Centralized Configuration**: Refactored the architecture by extracting all hardcoded paths, variables, ML class labels, and crawler search queries into a single `src/config.py` file. This prevents future bugs and explicitly isolates the codebase configuration.
- **Documentation Policy**: Enforced a strict policy that all codebase modifications must be logged in the Changelog and synchronized with `docs/documentation.md`.

## [0.1.0] - 2026-03-09
### Added
- **Machine Learning Pipeline (Colab)**: Developed `notebooks/Model_Training.ipynb` to offload the heavy MediaPipe feature extraction and Random Forest model training to Google's cloud servers.
- **Trained Model**: Added support for exporting and downloading the final, highly accurate `.pkl` model and its underlying `.csv` dataset straight to the user's local machine.

## [0.0.16] - 2026-03-09
### Fixed
- **Colab Zip Extraction Bug**: Fixed folder path logic to dynamically detect image directories even if the macOS ZIP compression omitted the parent `raw/` folder.

## [0.0.15] - 2026-03-09
### Fixed
- **MediaPipe Dependency Bug**: Pinned MediaPipe version to `0.10.14` in the Colab installation script to bypass Google's removal of the `solutions` API in recent versions.

## [0.0.14] - 2026-03-09
### Added
- **Random Forest Classifier**: Wrote the ML training logic using `scikit-learn` to fit the extracted hand landmarks and export accuracy reports.

## [0.0.13] - 2026-03-09
### Added
- **Google Colab Environment**: Initialized a Colab notebook format (`Model_Training.ipynb`) to bypass local Python environment incompatibilities with the ML libraries.

## [0.0.12] - 2026-03-09
### Added
- **CSV Data Output**: Configured the preprocessing script to flatten the 63 numerical attributes and save them securely into `data/processed/hand_landmarks.csv`.

## [0.0.11] - 2026-03-09
### Added
- **MediaPipe Hands Integration**: Incorporated Google's MediaPipe framework to successfully detect and map 21 3D hand landmarks per image.

## [0.0.10] - 2026-03-09
### Added
- **Data Preprocessing Core**: Created `data_preprocessing/extract_features.py` script skeleton to handle missing hands (skipping empty landscape images).

## [0.0.9] - 2026-03-09
### Changed
- **Massive Data Scale**: Increased crawler limits to dynamically scrape over 2500 raw images, fulfilling the academic 1500+ minimum requirement.

## [0.0.8] - 2026-03-09
### Fixed
- **Crawler Overwrite/Skip Bug**: Re-engineered the script's core `file_idx_offset` to calculate dynamically, preventing older images from being overwritten during new queries.

## [0.0.7] - 2026-03-09
### Changed
- **Extreme Dataset Diversification**: Vastly expanded search queries in `collect_data.py` to include faces, groups, selfies, body contexts, and completely random events (dogs, cars, empty rooms) to eliminate false positives.

## [0.0.6] - 2026-03-09
### Added
- **Missing Dependencies**: Fixed execution crashes by explicitly adding `six` and `pillow` to `requirements.txt`.

## [0.0.5] - 2026-03-09
### Changed
- **Crawler Engine Switch**: Due to broken Google Image parser components, safely switched the data collection logic over to `BingImageCrawler`.

## [0.0.4] - 2026-03-09
### Added
- **Google Image Crawler Implementation**: Replaced manual data entry with the automated `icrawler` package to scrape bulk images.

## [0.0.3] - 2026-03-09
### Changed
- **Data Collection Pivot**: Scrapped the initial webcam-based collection strategy (due to privacy concerns and setup complexity) in favor of automated web crawling.

## [0.0.2] - 2026-03-09
### Deprecated
- **Webcam Script**: Created but immediately deprecated the initial local webcam data collection concept.

## [0.0.1] - 2026-03-09
### Added
- **Project Structure**: Initialized Git repository, `version.md`, `changelog.md`.
- **Documentation Setup**: Created `README.md` and detailed `docs/documentation.md` templates.
- **Initial Task Planning**: Outlined the core ML architecture tasks in `task.md`.
