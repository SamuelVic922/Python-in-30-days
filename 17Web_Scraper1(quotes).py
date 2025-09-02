# Today (27/08/2025) we are building a project that scrapes data from a website and saves it to a CSV file.
import requests
from bs4 import BeautifulSoup
import pandas as pd


url = "https://quotes.toscrape.com/"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error connecting to the website:", e)
    exit(1)

print(f"Status Code : {response.status_code}")

soup = BeautifulSoup(response.text, "html.parser")

quotes_list = []
authors_list = []

for quote_block in soup.find_all("div", class_="quote"):
    quote = quote_block.find("span", class_="text").get_text()
    author = quote_block.find("small", class_="author").get_text()
    print(f"{quote} - {author}")
    quotes_list.append(quote)
    authors_list.append(author)

data = {"Quote": quotes_list,
        "Author": authors_list}
quotes_data = pd.DataFrame(data)
quotes_data.to_csv("quotes.csv", index=False)
print("Quotes have been saved to quotes.csv")
