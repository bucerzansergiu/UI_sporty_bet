# Twitch Mobile Automation Framework

A simple Selenium + Python + pytest automation framework for testing Twitch mobile using Page Object Model design pattern.

## Project Structure

```
.
├── conftest.py                 # Pytest fixtures (driver setup)
├── requirements.txt            # Python dependencies
├── helpers/
│   └── driver_helper.py       # Chrome mobile driver configuration
├── pages/
│   ├── base_page.py           # Base page with common methods
│   ├── twitch_home_page.py    # Home page object
│   ├── twitch_search_results_page.py  # Search results page object
│   └── twitch_streamer_page.py        # Streamer page object
├── tests/
│   └── test_twitch_mobile.py  # Test file
└── screenshots/                # Screenshots folder (auto-created)
```

## Setup

1. Install Python dependencies:
```bash
pip install -r requirements.txt
```

2. Make sure you have Chrome browser installed on your system.

## Running Tests

Run the test with pytest:
```bash
pytest tests/test_twitch_mobile.py -v -s
```

Run all tests:
```bash
pytest -v -s
```

Generate HTML report:
```bash
pytest tests/test_twitch_mobile.py -v -s --html=report.html --self-contained-html
```

## Test Description

The test performs the following steps:
1. Opens m.twitch.tv in mobile emulation mode
2. Navigates to /directory page
3. Searches for "Starcraft II"
4. Scrolls down 2 times
5. Selects a random streamer from the results
6. Waits for the streamer page to load
7. Takes a screenshot (saved in `screenshots/` folder)

## Features

- **Page Object Model**: Clean separation of page logic and test logic
- **Mobile Emulation**: Uses Chrome mobile emulator (iPhone configuration)
- **Pytest Integration**: Uses pytest fixtures for driver management
- **Screenshots**: Automatic screenshot capture
- **Flexible Locators**: Multiple fallback locators for stability
- **Simple and Clean**: Easy to understand and extend

