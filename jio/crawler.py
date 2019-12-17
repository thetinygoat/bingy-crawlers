import requests as r
import json
import os


# check if output directory exists
if os.path.exists("output") != True:
    os.mkdir("output")

root_path = os.path.join("output", "jio_{0}.json")
movies_url = (
    "https://prod.media.jio.com/apis/06758e99be484fca56fb/v3.1/home/getget/6/{0}"
)
tv_url = "https://prod.media.jio.com/apis/06758e99be484fca56fb/v3.1/home/getget/9/{0}"


def crawl_movies(url):
    print("crawling movies...")
    # resolve total page range to crawl
    print("crawling " + url.format(0))
    response = r.get(url.format(0))
    parsed_response = json.loads(response.content)
    total_pages = parsed_response["totalPages"]
    # write already fetched result to file
    with open(root_path.format("movies"), "ab") as f:
        f.write(response.content)
    for page_count in range(1, total_pages):
        print("crawling " + url.format(page_count))
        response = r.get(url.format(page_count))
        with open(root_path.format("movies"), "ab") as f:
            f.write(response.content)


def crawl_tvshows(url):
    print("crawling tv shows...")
    # resolve total page range to crawl
    print("crawling " + url.format(0))
    response = r.get(url.format(0))
    parsed_response = json.loads(response.content)
    total_pages = parsed_response["totalPages"]
    # write already fetched result to file
    with open(root_path.format("tvshows"), "ab") as f:
        f.write(response.content)
    for page_count in range(1, total_pages):
        print("crawling " + url.format(page_count))
        response = r.get(url.format(page_count))
        with open(root_path.format("tvshows"), "ab") as f:
            f.write(response.content)


crawl_movies(movies_url)
crawl_tvshows(tv_url)

