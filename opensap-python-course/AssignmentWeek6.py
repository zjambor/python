"""
In this assignment you are going to build a Python program to access the Apple iTunes Search Service. This service can be used to search information about musicians, albums, songs and so on.

Using the following URL, a search for the term ramones and for the entity type album is performed: https://itunes.apple.com/search?term=ramones&entity=album

Write a program that asks the user for a search term. Perform a search using the iTunes search service for the entity type album. 
The program should then print how many search results where returned. For each result print the artist name, the album name and track count.

Below is an example execution of the program. Note that the output is abbreviated.

Please enter a search term: cash
The search returned 50 results.
Artist: Luke Bryan - Album: Crash My Party - Track Count: 13
Artist: Johnny Cash - Album: The Essential Johnny Cash - Track Count: 36
Artist: Dave Matthews Band - Album: Crash - Track Count: 12
"""

import requests

search_term = input("Please enter a search term: ")

search_link = "https://itunes.apple.com/search?term=" + search_term + "&entity=album"

r = requests.get(search_link)
results = r.json()

print(f"The search returned {results['resultCount']} results.")

for i in results["results"]:
    print(f"Artist: {i['artistName']} - Album: {i['collectionName']} - Track Count: {i['trackCount']}")
