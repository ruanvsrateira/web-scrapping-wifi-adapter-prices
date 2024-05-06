import requests
from bs4 import BeautifulSoup

SITE_URL = "https://br.hubspot.com/blog/marketing/linguagens-de-programacao"
TOP_LANGUAGES = []

def main():
  site_content = requests.get(SITE_URL).text
  soup = BeautifulSoup(site_content, "html.parser")
  top_programming_languages = soup.select(".hsg-featured-snippet ol li")[8:-1]

  for tpl in top_programming_languages:
    TOP_LANGUAGES.append(tpl.text)

  for tl in TOP_LANGUAGES:
    print(f"{TOP_LANGUAGES.index(tl)+1}. {tl}")

if __name__ == "__main__":
  main()