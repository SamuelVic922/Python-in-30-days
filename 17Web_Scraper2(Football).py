# Today(30/08/2025), We are going to be building a web scraper to extract football data from a website and save it into a CSV file.
import requests
from bs4 import BeautifulSoup
import pandas as pd

date = input("Enter the date (YYYY-MM-DD): ")
url = f"https://www.bbc.com/sport/football/scores-fixtures/{date}"
try:
    response = requests.get(url)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print("Error connecting to the website:", e)
    exit(1)


soup = BeautifulSoup(response.text, "html.parser")


teams = [t.get_text() for t in soup.find_all(
    "span", class_="ssrcss-c8w0oz-MobileValue emlpoi31")]
home_scores = [h.get_text()
               for h in soup.find_all("div", class_="ssrcss-qsbptj-HomeScore e56kr2l2")]
away_scores = [a.get_text()
               for a in soup.find_all("div", class_="ssrcss-fri5a2-AwayScore e56kr2l1")]

matches = []
for i in range(0, len(teams), 2):  # step by 2 (home & away teams)
    match = {
        "home": teams[i],
        "home_score": home_scores[i] if i < len(home_scores) else None,
        "away": teams[i+1],
        "away_score": away_scores[i+1] if i+1 < len(away_scores) else None,
    }
    matches.append(match)

for m in matches[:5]:
    print(m)

df = pd.DataFrame(matches)
df.to_csv("football_scores.csv", index=False)

print("Saved to football_scores.csv ✅")
