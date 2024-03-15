from bs4 import BeautifulSoup
import requests  # Used to get the html of the website

website = 'https://subslikescript.com/series/Breaking_Bad-903747/season-1/episode-1-Pilot'
html = requests.get(website)
content = html.text

soup = BeautifulSoup(content, 'lxml')  # lxml is the parser

# print(soup.prettify()) # pretty print the html

plot = soup.find("p", class_="plot").text

main_article = soup.find("article", class_="main-article")

print(main_article.find("h1").text)  # The .text attribute gets the text of the tag

# using get_text() method
print(main_article.find("h1").get_text())

full_script = soup.find("div", class_="full-script").get_text(separator="\n", strip=True)
"""
 - The difference between .text and .get_text() is that .text is an attribute of the tag, while .get_text() is a method of the tag
 - .text is faster than .get_text() because it is an attribute, while .get_text() is a method
 - We can also pass the separator and strip arguments to .get_text() method. Strip is used to remove the leading and trailing whitespaces while 
 separator is used to separate the text
"""

print(main_article.find("h1").get_text(strip=True))  # Removes the leading and trailing whitespaces
# print(full_script)

# Writing the full script to a file
with open("breaking_bad_script.txt", "w") as file:
    file.write(full_script)
