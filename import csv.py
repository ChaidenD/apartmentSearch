import csv
import requests
from bs4 import BeautifulSoup

def scrape_zillow_rentals(zip_code):
    url = f"https://www.zillow.com/homes/for_rent/{zip_code}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, "html.parser")

    rentals = soup.find_all("article", class_="list-card")

    data = []
    for rental in rentals:
        title = rental.find("a", class_="list-card-link")["aria-label"]
        price = rental.find("div", class_="list-card-price").text
        address = rental.find("address", class_="list-card-addr").text
        data.append([title, price, address])

    return data

def save_to_csv(data):
    with open("rental_listings.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Price", "Address"])  # Write header
        writer.writerows(data)  # Write data rows

def main():
    zip_code = input("Enter the zip code: ")
    rental_data = scrape_zillow_rentals(zip_code)
    save_to_csv(rental_data)
    print("Data saved to rental_listings.csv")

if __name__ == "__main__":
    main()
