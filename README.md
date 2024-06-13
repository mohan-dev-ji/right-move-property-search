markdown
# Rightmove Property Search and Google Sheets Integration

This project is a Python script that scrapes property listings from Rightmove and writes the data (address, price, and link) to a Google Sheet. It utilizes Selenium for web scraping and the `gspread` library for interacting with the Google Sheets API.

## Prerequisites

Before running the script, make sure you have the following prerequisites installed:

- Python 3.x
- Google Cloud project with the Google Sheets API enabled
- Google Cloud service account credentials (JSON file)

## Installation

1. Clone the repository or download the project files.
2. Create a virtual environment (optional but recommended):

python3 -m venv .venv
source .venv/bin/activate # On Windows, use .venv\Scripts\activate
3. Install the required Python packages:

pip install -r requirements.txt

## Setup

1. Create a new Google Cloud project or use an existing one.
2. Enable the Google Sheets API for your project.
3. Create a service account and download the JSON credentials file.
4. Create a new Google Sheet or use an existing one.
5. Share the Google Sheet with the service account email address (found in the JSON credentials file).

## Usage

1. Open the `main.py` file and update the following variables:
- credentials.json: Path to the JSON credentials file downloaded from Google Cloud.
- NEW_WORKSHEET_NAME: Use existing tab or creates a new one
- SHEET_ID: Is the name of the actual sheet found in the URL after ...d/ and before .../edit
- The AREA and MAX_PRICE can also be changed but must match Rightmove's pre-selections
2. Run the script:

python main.py
3. The script will scrape property listings from Rightmove and write the data (address, price, and link) to the specified Google Sheet.

## Configuration

You can customize the script by modifying the following the GLOBAL variables at the top of `main.py`:

## Dependencies

The project relies on the following Python packages:

- `selenium`: For web scraping and browser automation.
- `gspread`: For interacting with the Google Sheets API.
- `google-auth`: For authenticating with Google APIs.
- `google-auth-oauthlib`: For handling OAuth authentication flows.
- `google-auth-httplib2`: For providing HTTP transport for Google APIs.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).