# Changelog

All notable changes to the "Image Analyzer" project will be documented in this file.

## [0.0.2] - 2026-03-09
### Changed
- **Data Collection Strategy**: Switched from webcam to web scraping (BingImageCrawler) to protect user privacy and automate the collection.
- **Dataset Expansion**: Added diverse search queries (over 20 total) to gather up to 2400 images, including backgrounds and other non-hand gestures to ensure robustness.
### Added
- **Dependencies**: Added `icrawler`, `six`, `pillow`, `lxml`, `bs4`, `requests` to `requirements.txt`.

## [0.0.1] - 2026-03-09
### Added
- **Project Structure**: Initialized project structure and tracking files (`version.md`, `changelog.md`).
- **Documentation**: Initialized `README.md` and detailed `docs/documentation.md`.
- **Planning**: Outlined the task list and data collection strategy via webcam.
