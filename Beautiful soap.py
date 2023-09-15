# Beautiful Soup object repesents HTML as a set of Tree with method used to parse HTML
from bs4 import BeautifulSoup
import requests
import json
import pandas as pd

# html = "<!DOCTYPE html><html><head><title>Page Title</title></head><body><h3><b id='boldest'>Lebron James</b></h3><p> Salary: $ 92,000,000 </p><h3> Stephen Curry</h3><p> Salary: $85,000, 000 </p><h3> Kevin Durant </h3><p> Salary: $73,200, 000</p></body></html>"
# #Parse a document into BeautifulSoup constructor

# soup = BeautifulSoup(html, 'html5lib') # represent the document as nested data structure
 # soup = BeautifulSoup(html, 'lxml') # using xml parser


# # print( soup.prettify()) # display the HTML in the nested structure



# print("h3 tag :" ,soup.h3) # print all h3 tags
# # Create tag object 
# tagObject = soup.title
# print("tag object title:",tagObject)

# # If there is more than one <code>Tag</code> with the same name, the first element with that <code>Tag</code> name is called
# tagObject = soup.p
# print("tag object p:",tagObject)

# tagObject = soup.b
# print("tag object p:",tagObject)

# # use <b> tag as child 
# tag_child =tagObject.b
# print(tag_child)

# #access the parent with the < parent>
# parent_tag=tag_child.parent
# print(parent_tag)

# Python script for web scraping to extract data from a websit
# def scrape_data(url):
#     response = requests.get(url)
#     print(response)
#     soup = BeautifulSoup(response.text, 'XML')
#     print(soup.prettify())

# Your code here to extract relevant data from the website

# scrape_data("https://www.google.com/")


# url = "https://web.archive.org/web/20200318083015/https://en.wikipedia.org/wiki/List_of_largest_banks"

# r = requests.get(url)

# html_data = r

# print(html_data)
# print(" ***** ")
# print(r)

# print("any")



# Initialize an empty list to store API data

# Make a GET request to the API endpoint
api_url = 'http://api.exchangeratesapi.io/v1/latest?base=EUR&access_key=ba808e8a0c46021853c5f6cbae028284'  # Replace with the actual API URL
response = requests.get(api_url)


# Check if the request was successful (status code 200)
if response.status_code == 200:
    # Append the text from the API response to the list
    data = json.loads(response.text)
    df = pd.DataFrame(data)
else:
    print("Failed to fetch data from the API")

# Now, api_data_list contains the text data from the API response
print(df)

df.to_json("exchange_rates_1.json" )








