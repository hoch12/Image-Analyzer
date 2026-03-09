# Changelog

All notable changes to the "Image Analyzer" project will be documented in this file.

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
