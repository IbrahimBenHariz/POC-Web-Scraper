# Importation of libraries
import datetime
import random
import string
import time
import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import filedialog
import json
import concurrent.futures

# Creation of a first instance of tkinter librarie + hide the main window
root = tk.Tk()
root.withdraw()

# Setup parameters such as max retries for a web scraping request or delay between failed requests
max_testscrape = 4
delay_testscrape = 10

# Initialize variables
headers_list = []
urls_to_scrap = []
folder_saved_pages_path = ""


# Function to select the file containing headers
def select_headers_file():
    global headers_list
    print("PLEASE SELECT YOUR HEADERS .txt FILE !")
    file_path = filedialog.askopenfilename(
        title="PLEASE SELECT YOUR HEADERS .txt FILE !",
        filetypes=[("Text files", "*.txt")]
    )
    with open(file_path, 'r') as f:
        file_contents = f.read()

    # parse the file .txt to read json objects
    json_data = json.loads(file_contents)
    headers_list = json_data


# Function to select the file containing urls in case multiple different requests are needed
def select_urls_file():
    global urls_to_scrap
    print("PLEASE SELECT YOUR URLS .txt FILE !")
    urls_stamp = []
    file_path = filedialog.askopenfilename(
        title=" PLEASE SELECT YOUR URLS .txt FILE !",
        filetypes=[("Text files", "*.txt")]
    )
    with open(file_path, 'r') as f:
        for line in f:
            # parse the file .txt to read line by line
            urls_stamp.append(line.strip())

    urls_to_scrap = urls_stamp


# Function to select the folder to contain all the scraped pages
def select_folder_pages_scraped():
    global folder_saved_pages_path
    print("SELECT YOUR FOLDER FOR SAVED SCRAPED PAGES !")
    folder_path = filedialog.askdirectory(
        title="SELECT YOUR FOLDER FOR SAVED SCRAPED PAGES !"
    )

    folder_saved_pages_path = folder_path


# The main function : get the result of scraping based on url
def scrape_page(url_stamp):
    url_active = url_stamp
    retry = 0

    # Remind that the user should specify the file for headers and/or select the folder to save scraped pages
    if headers_list == [] or folder_saved_pages_path == "":
        print("BEFORE RUNNING THIS FUNCTION YOU MUST CHECK FOR FUNCTIONS 1 AND 2 !")
        return

    # While loop permitting to retry to send the request when there is an error
    while retry < max_testscrape:
        try:                        # Select a random header provided in the file
            response = requests.get(url_active, headers=random.choice(headers_list))
            html_content = response.content
            # Check the response of the request
            if response.status_code == 200:
                print(f"{url_stamp} : Scraping OK !")
                soup = BeautifulSoup(html_content, "html.parser")
                # Launch the function to save the page in the folder specified by the user
                save_scraped_pages(soup, folder_saved_pages_path)
                return soup.prettify()
            if response.status_code == 404:
                print(f"{url_stamp} : Not found !")
                raise Exception(f'Error: {response.status_code}')
            if response.status_code == 403:
                print(f"{url_stamp} : Forbidden !")
                raise Exception(f'Error: {response.status_code}')
            else:
                raise Exception(f'{url_stamp} : Error: {response.status_code}')
        except(requests.exceptions.RequestException, Exception) as e:
            # retry takes + 1 as long as the page is not scraped (counts specified by the user)
            print(f'Error: {e}')
            retry += 1
            time.sleep(delay_testscrape)


# Function to save the scraped page
def save_scraped_pages(page_stamp, filepath_stamp):
    timestamp = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    # Use a timestamp plus a random suffix to create the name of the file + we use the folder path specified by the user
    suffix = ''.join(random.choices(string.ascii_lowercase, k=4))
    filename = f"{timestamp}_{suffix}.html"
    filepath = filepath_stamp + "/" + filename
    with open(filepath, 'w', encoding="utf-8") as f:
        f.write(page_stamp.prettify())
        # print(f' {urlActive} : Successfully Saved !')


# Function to generate simultaneous request of different URLs (using the URLS file specified by the user)
def run_multiple_scraping_pages():
    select_urls_file()
    # ThreadPoolExecutor allows to run the requests in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls_to_scrap)) as executor:
        # Launch the scraping using the function scrape_page with the URLs from the file
        future_to_url = {executor.submit(scrape_page, url): url for url in urls_to_scrap}
        # Wait till every process are done
        for future in concurrent.futures.as_completed(future_to_url):
            url = future_to_url[future]
            try:
                future.result()
            except Exception as exc:
                print(f'{url} - Exception : {exc}')


# Function to generate simultaneous request of different URLs (using the URLS file specified by the user)
def run_single_page_xtime():
    # Ask user for the url + number of simultaneous requests
    url = input("PLEASE ENTER YOUR URL : ")
    count_stamp = int(input("PLEASE ENTER THE NUMBER OF PROCESS : "))
    # ThreadPoolExecutor allows to run the requests in parallel
    with concurrent.futures.ThreadPoolExecutor(max_workers=count_stamp) as executor:
        # Launch the scraping using the function scrape_page with the URL x times both specified before
        future_to_request = {executor.submit(scrape_page, url): i for i in range(count_stamp)}
        # Wait till every process are done
        for future in concurrent.futures.as_completed(future_to_request):
            try:
                future.result()
            except Exception as exc:
                print(f'{future_to_request[future]} - Exception : {exc}')


# Setup functions depending on the choice of user
menu = {
    "1": select_headers_file,
    "2": select_folder_pages_scraped,
    "3": scrape_page,
    "4": run_single_page_xtime,
    "5": run_multiple_scraping_pages
}


# Simple menu to allow user to use the scraper
while True:
    print("Select an option:")
    print("1. Function 1 : Select Headers File")
    print("2. Function 2 : Select Folder For Saving Page")
    print("3. Function 3 : Scrape A Single URL")
    print("4. Function 4 : Scrape A Single URL Multiple Times")
    print("5. Function 5 : Scrape A List of URLs")
    print("0. Exit")
    choice = input("Enter your choice (1-5, or 0 to exit): ")

    # Exit
    if choice == "0":
        break

    # Execute the function depending on the user choice
    if choice in menu and choice != "3":
        menu[choice]()
    # If choice is 3 a URL must be specified in params
    elif choice == "3":
        params = [input("PLEASE ENTER YOUR URL : ")]
        menu[choice](*params)
    else:
        print("Error of choice ! Please try again.")