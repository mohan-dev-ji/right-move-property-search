from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time
import gspread
from google.oauth2.service_account import Credentials

NEW_WORKSHEET_NAME = "Ealing property search"
SHEET_ID = "1-1q95HlrFbUaFmMly0TElsSpiaTSeb-hlG_sEckS6mM"
AREA = "Ealing Broadway Station"
MAX_PRICE = "450,000"
URL = "https://www.rightmove.co.uk/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get(URL)

time.sleep(2)

# Click Reject Cookies Button
reject_button = driver.find_element(by=By.ID, value="onetrust-reject-all-handler")
reject_button.click()

time.sleep(2)
location = driver.find_element(by=By.ID, value="ta_searchInput")
location.send_keys(AREA)

# Click for sale button
time.sleep(2)
for_sale_button = driver.find_element(by=By.CSS_SELECTOR, value="[data-testid='forSaleCta']")
for_sale_button.click()

# Find the dropdown element by its id
dropdown = driver.find_element(by=By.ID, value="maxPrice")

# Create a Select object for the dropdown
select = Select(dropdown)

# Select the option by its visible text
select.select_by_visible_text(MAX_PRICE)

submit = driver.find_element(by=By.ID, value="submit")
submit.click()

# Find all <a> tags with the specific CSS selector
link_elements = driver.find_elements(By.CSS_SELECTOR, "a.propertyCard-link.property-card-updates")
# Extract the href values
href_values = [link.get_attribute("href") for link in link_elements]

# Find all <address> tags with the specific CSS selector
address_elements = driver.find_elements(By.CSS_SELECTOR, "address.propertyCard-address.property-card-updates")
# Extract the address values
address_values = [address.get_attribute("title") for address in address_elements]

# Find all prices 
price_elements = driver.find_elements(By.CSS_SELECTOR, "div.propertyCard-priceValue")
# Extract the prices values
price_values = [div.text for div in price_elements]

property_data = [("Address", "Price", "Link")] + list(zip(address_values, price_values, href_values))

scopes = [
    "https://www.googleapis.com/auth/spreadsheets"
]
creds = Credentials.from_service_account_file("credentials.json", scopes=scopes)
client = gspread.authorize(creds)


workbook = client.open_by_key(SHEET_ID)

# list all worksheets in workbook and create a new one id NEW_WORKSHEET_NAME doesn't exist
worksheet_list = map(lambda x: x.title, workbook.worksheets())

if NEW_WORKSHEET_NAME in worksheet_list:
    spreadsheet = workbook.worksheet(NEW_WORKSHEET_NAME)
else:
    spreadsheet = workbook.add_worksheet(NEW_WORKSHEET_NAME, rows=25, cols=3)

spreadsheet.clear()

row = 1
while True:
    for address, price, link in property_data:
        spreadsheet.update_cell(row, 1, address)
        spreadsheet.update_cell(row, 2, price)
        spreadsheet.update_cell(row, 3, link)
        row += 1
        time.sleep(2)
    break

time.sleep(4)
spreadsheet.format("A1:C1", {"textFormat": {"bold": True}})