# Project 3: Election Results Scraper 2017

## Description
This Python script scrapes parliamentary election results from the [volby.cz](https://volby.cz) website and saves them to a CSV file. It collects data on:
- Registered voters
- Issued envelopes
- Valid votes
- Results for various political parties in different regions

## Installation
To install the required packages, it's recommended to create a new virtual environment and use pip. Follow these steps:

1. **Create a virtual environment:**
    ```sh
    python -m venv venv
    ```

2. **Activate the virtual environment:**
    - On Windows:
      ```sh
      venv\Scripts\activate
      ```
    - On macOS/Linux:
      ```sh
      source venv/bin/activate
      ```

3. **Install required packages:**
    ```sh
    pip install -r requirements.txt
    ```
Or use this site: https://code.visualstudio.com/docs/python/environments

## Running the Script
The script `project_3.py` requires two arguments to run:

1. **link-to-location:** URL of the chosen territorial unit from [volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ)
2. **output-file:** Name of the output CSV file (e.g., `results.csv`)

### Command Syntax:
```sh
python project_3.py <link-to-location> <output-file>
