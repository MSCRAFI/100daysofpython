import requests
from bs4 import BeautifulSoup
url="http://alheraedu.com"
# Get HTML
GetContent=requests.get(url)
htmlContent=GetContent.content
# print(htmlContent)
# Parse the HTML
soup=BeautifulSoup(htmlContent, "html.parser")
# print(soup.prettify)
# HTML Tree Traversal
title=soup.title
# print(title)
# Scrap Anchor Tags
Anchor=soup.find_all("a")
# Get links from "href" in Anchor Tags
for links in Anchor:
 if links.get("href")!="#":
  GetLinks=links.get("href")
  print(GetLinks)