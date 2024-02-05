# Selenium Scraper Readme

## Overview

Selenium Scraper is a Python application designed for web scraping using the Selenium framework. It provides a simple and flexible way to automate the extraction of data from websites. This readme file will guide you through the steps to set up and run the Selenium Scraper.

## Prerequisites

Before running the Selenium Scraper, ensure that you have the following prerequisites installed on your system:

- Python 3.x: [Download Python](https://www.python.org/downloads/)
- Chrome or Firefox browser
- ChromeDriver or GeckoDriver (based on the browser you choose): [Download ChromeDriver](https://sites.google.com/chromium.org/driver/) or [Download GeckoDriver](https://github.com/mozilla/geckodriver/releases)

## Installation

1. Extract the zip file

2. Navigate to the project directory:

   ```bash
   cd selenium-scraper
   ```

3. Install the required dependencies:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration
The default Configuration resides in the file scrape_config.py

## Running the Scraper

Execute the following command to run the Selenium Scraper:

```bash
python scraper_vista.py
```

The scraper will launch the specified browser, navigate to the provided URL, and start scraping data according to the configured parameters.

## Customization

Feel free to customize the `scraper_vista.py` file to adapt the scraper to your specific scraping needs. You can modify the script to interact with different elements on the webpage, extract specific data, and handle various scenarios.

## Important Notes

- Respect the website's terms of service and legal requirements while using the scraper.
- Be cautious with the frequency and volume of requests to avoid overloading the server and getting blocked.
- Regularly check and update the scraper code if the website structure changes.

Happy scraping! If you encounter any issues or have suggestions for improvement, feel free to open an issue on the GitHub repository.