import requests as rq
import csv

BASE_URL = "https://newsapi.org/v2/everything?q=tesla&from=2023-01-07&sortBy=publishedAt&apiKey="
GET_API = open("API.txt", "r")
READ_API = GET_API.read()
URL = BASE_URL + READ_API
GET_CONTENT = rq.get(URL).json()
# total_results = GET_CONTENT["totalResults"]
# source_name = GET_CONTENT["articles"][0]["source"]["name"]
# author_name = GET_CONTENT["articles"][0]["author"]
# content_title = GET_CONTENT["articles"][0]["title"]
# content = GET_CONTENT["articles"][0]["content"]

with open("news.csv", "w", newline="", encoding="utf-8") as csvfile:
    fieldnames = ["title", "content"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()
    for i in GET_CONTENT["articles"]:
        content_title = i["title"]
        content = (i["content"])
        writer.writerow({"title": f"{content_title}", "content": f"{content}"})

