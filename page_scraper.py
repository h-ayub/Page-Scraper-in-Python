# Page Scraper Application

from lxml import html
import requests
import mimetypes

from urllib.parse import urlparse
import os

def enterWebsite():
    site = input("Please enter the website you are trying to scrape: ")
    text_file = open("links.txt", "w")

    extensions_to_check = [".com", ".edu", ".org", ".net", ".gov", ".tv"]
    main_site = urlparse(site).netloc
    scheme = urlparse(site).scheme

    page = requests.get(site)
    tree = html.fromstring(page.content)

    links = set(tree.xpath('//*/@href'))

    text_file.write("All of the links on this page:")
    print("All of the links on this page:")
    for link in links:
        for extension in extensions_to_check:
            if extension in link and (link[-1] == (extension[-1] or "/") or extension + "/" in link):
                break
        else:
            link = scheme + "://" + main_site + link
        if link[0] == link[1] == "/":
            link = scheme + ":" + link
        text_file.write("\n " + link)
        print(" " + link)

    images = set(tree.xpath('//img/@src'))
    print("\nAll of the images on this page:")
    text_file.write("\n" + "\nAll of the images on this page")
    for image in images:
        for extension in extensions_to_check:
            if extension in image and (image[-1] == (extension[-1] or "/") or extension + "/" in image): # if it is a link don't do anything
                break
        else:
            if image[0] != "/":
                image = "/" + image
            image = scheme + "://" + main_site + image
        if image[0] == image[1] == "/":
            image = scheme + ":" + image
        text_file.write("\n " + image)
        print(" " + image)

if __name__ == "__main__":
    enterWebsite()
    