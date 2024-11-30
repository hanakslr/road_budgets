"""
Quick script. Given a city name, find its website and infrastructure budget related info.
"""

import argparse
import re
import requests
from bs4 import BeautifulSoup

keywords = ["CIP", "Capital Improvement Plan", "infrastructure", "budget"]
ACCEPTABLE_WEBSITE_DOMAINS = [".us", ".gov"]


def find_website(city, state):
    """
    Given a city name and state, find the city's website.
    """
    query = f"{city} {state} official website"
    response = requests.get(f"https://www.google.com/search?q={query}")

    # Use BeautifulSoup to parse the HTML content and find the first link that
    # contains a .us or .gov domain.
    soup = BeautifulSoup(response.text, "html.parser")

    for a in soup.find_all("a", href=True):
        if any([domain in a["href"] for domain in ACCEPTABLE_WEBSITE_DOMAINS]):
            messy_url = a["href"]
            # Clean up the URL - remove tracking info and other junk
            # Could probably bypass this by using a google search API directly
            clean_url = re.sub(r"^.*?url\?q=", "", messy_url)
            clean_url = re.sub(r"&sa.*$", "", clean_url)

            return clean_url

    raise Exception("Could not find city website")


def main():
    parser = argparse.ArgumentParser(
        description="Find city website and infrastructure budget info."
    )
    parser.add_argument("--city", type=str, help="City or town name")
    parser.add_argument("--state", type=str, help="State name")
    args = parser.parse_args()
    city = args.city
    state = args.state
    print(f"Locating website for {city}, {state}...")

    website = find_website(city, state)
    print(f"Website: {website}")


if __name__ == "__main__":
    main()
