import requests
from bs4 import BeautifulSoup
import csv

zip_code = "92114"  # Replace with your desired zip code
url = f"https://www.zillow.com/homes/for_rent/{zip_code}"

response = requests.get(url)
html_content = response.content

soup = BeautifulSoup(html_content, "html.parser")

#You need to add more CSS selectors, these are examples
titles = soup.select(".list-card-title")
prices = soup.select(".list-card-price")


#Iterates over the data just grabbed
rental_listings = []
for title, price in zip(titles, prices):
    rental_listings.append({
        "Title": title.text.strip(),
        "Price": price.text.strip()
})

#This creates the CSV file
filename = "rental_listings.csv"  # Choose a filename
headers = ["Title", "Price"]

with open(filename, "w", newline="", encoding="utf-8") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    writer.writeheader()
    writer.writerows(rental_listings)