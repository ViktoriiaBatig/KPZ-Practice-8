from bs4 import BeautifulSoup
import requests


def parse_ukd_data():
    url = 'https://ukd.edu.ua'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, "html.parser")
    info = soup.find("section", class_="region region-front-specialty professions")
    professions = info.find_all("span", class_="card-title")
    for prof in professions:
        print(prof.text)

def main():
    parse_ukd_data()

if __name__ == '__main__':
    main()
