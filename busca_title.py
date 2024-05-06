import requests
from bs4 import BeautifulSoup

def main():
  site_url = input("Digite a url de algum site: ")
  site_response = requests.get(site_url).text
  soup = BeautifulSoup(site_response, "html.parser")
  title = soup.find("title")

  print(title.text)

if __name__ == "__main__":
  main()