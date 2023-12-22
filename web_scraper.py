import requests
from bs4 import BeautifulSoup
import csv

def scrape_website(url, css_selector):
    # Send a GET request to the web page
    response = requests.get(url)
    
    # Parse the HTML code using BeautifulSoup
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Select elements based on the CSS selector
    elements = soup.select(css_selector)
    
    # Print the results
    for element in elements:
        print(element.text)

    # Save the results to a CSV file
    save_to_csv(elements)

def save_to_csv(data):
    with open('scraped_data.csv', 'w', newline='', encoding='utf-8') as csvfile:
        fieldnames = ['Data']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

        writer.writeheader()
        for item in data:
            writer.writerow({'Data': item.text})

if __name__ == "__main__":
    # Get the URL and CSS selector from the user
    url = input("Enter the URL of the web page: ")
    css_selector = input("Enter the CSS selector for scraping elements: ")

    # Call the function for scraping
    scrape_website(url, css_selector)
