# This is a python webscraper.
# Simple webscraper using BeautifulSoup4 and Requests
# Tells what the websites language is using html parse + lang tag

import requests
from bs4 import BeautifulSoup


def main():
    try:
        print('Enter Websites name: ', end="")
        valid_website = input()

        page_name = requests.get(valid_website)
        soup = BeautifulSoup(page_name.content, 'html.parser')

        language = valid_website + ' Language is in ' + soup.html['lang']
        print('\n' + language)

    except requests.exceptions.MissingSchema:
        print("Invalid URL\n", end="\n")
        main()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()


