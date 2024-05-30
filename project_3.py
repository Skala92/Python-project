"""
projekt_3.py: Třetí projekt do Engeto Online Python Akademie
author: Jiri Skalicky
email: Skalicky.jiri92@gmail.com
discord: skala7142
"""

import argparse
import csv
import requests
from bs4 import BeautifulSoup

def main(url, output_file):
    """
    Scrapes election data from the provided URL and writes it into a CSV file.

    Args:
        url (str): URL of the election results page to scrape.
        output_file (str): Name of the output CSV file to save the scraped data.
    """
    try:
        print("Starting data processing...")
        with open(output_file, mode="w", encoding="utf-8-sig", newline='') as f:
            writer = csv.writer(f, delimiter=";")

            header = False
            scrap = requests.get(url)
            soup = BeautifulSoup(scrap.text, "html.parser")
            regions = soup.find_all("td", {"class": "cislo"})

            for line in regions:
                region_data = []
                region_data = get_id_name(line, region_data)
                region_soup = get_soup(URL, line)

                region_results = region_soup.find(id="ps311_t1")
                region_data = get_voters(region_results, region_data)

                parties = region_soup.find(id="inner").find_all("tr")
                region_data = get_party_votes(parties, region_data)

                if not header:
                    column_names = ["Code", "Location", "Registered", "Envelopes", "Valid"]
                    for new_line in parties:
                        if not new_line.find("th"):
                            column_names.append(new_line.find_all("td")[1].string)
                    writer.writerow(column_names)
                    header = True

                writer.writerow(region_data)

        print(f"Data processing finished. File {output_file} is ready.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")

def get_id_name(line, lst):
    """
    Extracts region code and location name from a BeautifulSoup line.

    Args:
        line (BeautifulSoup object): BeautifulSoup line containing region data.
        lst (list): List to append the extracted data.

    Returns:
        list: List containing the extracted region code and location name.
    """
    lst.append(line.find("a").string)
    lst.append(line.parent.find_all()[2].string)
    return lst

def get_soup(base_url, line):
    """
    Retrieves BeautifulSoup object for a specific region's URL.

    Args:
        base_url (str): Base URL for the election results page.
        line (BeautifulSoup object): BeautifulSoup line containing region data.

    Returns:
        BeautifulSoup object: BeautifulSoup object of the region's URL.
    """
    region_url = requests.get(base_url + line.find("a").attrs["href"])
    return BeautifulSoup(region_url.text, "html.parser")

def get_voters(region_results, lst):
    """
    Extracts registered voters, envelopes, and valid votes from region results.

    Args:
        region_results (BeautifulSoup object): BeautifulSoup object containing region results.
        lst (list): List to append the extracted data.

    Returns:
        list: List containing the extracted number of registered voters, envelopes, and valid votes.
    """
    lst.append(region_results.find("td", {"class": "cislo", "headers": "sa2"}).string)
    lst.append(region_results.find("td", {"class": "cislo", "headers": "sa3"}).string)
    lst.append(region_results.find("td", {"class": "cislo", "headers": "sa6"}).string)
    return lst

def get_party_votes(parties, lst):
    """
    Extracts votes for each party from the region's party list.

    Args:
        parties (BeautifulSoup object): BeautifulSoup object containing party data.
        lst (list): List to append the extracted data.

    Returns:
        list: List containing the extracted votes for each party.
    """
    for line in parties:
        if not line.find("th"):
            lst.append(line.find_all("td", {"class": "cislo"})[1].string)
    return lst

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Elections Scraper')
    parser.add_argument('url', type=str, help='URL of the election results page')
    parser.add_argument('output_file', type=str, help='Name of the output CSV file')
    args = parser.parse_args()
    main(args.url, args.output_file)