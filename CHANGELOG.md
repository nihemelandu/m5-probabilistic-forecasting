# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).

## [Unreleased]

### Added
- Initial project structure (config/, src/, tests/, notebooks/, results/, logs/)
- Configuration management via `config/config.yaml`
- Dependency management via `requirements.txt`
- Utility functions for logging and config loading (`src/utils.py`)
- Data loader with validation (`src/data_loader.py`)
- Complete series builder implementation (`src/series_builder.py`)
  - All 12 hierarchy levels (42,840 total series)
  - Single-dimension levels: Total, State, Store, Category, Department, Item
  - Two-dimension levels: State×Category, State×Dept, Store×Category, Store×Dept, State×Item, Store×Item
  - Business context documented in function docstrings

### Changed
- None yet

### Fixed
- None yet

---

## [2025-02-17] - Project Initialization

### Added
- README.md with project overview and technical highlights
- CHANGELOG.md for tracking changes
- DEVELOPMENT_LOG.md for business narrative
- .gitignore for Python projects
- Virtual environment setup (m5-env)
- Complete dependency installation (numpy, pandas, statsmodels, scikit-learn, etc.)

### Notes
- Repository created: https://github.com/nihemelandu/m5-probabilistic-forecasting
- Initial commit pushed successfully
