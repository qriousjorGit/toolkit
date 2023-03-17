import requests
import pprint as p
from internetarchive import get_item

archive_access_key = "Y1XTeSkxjH1o7EDN"
archive_secret_key = "NGtXQVNJhWG1p1XW"

# target = input("Page?")
# way_back_check = requests.get(f"http://archive.org/wayback/available?url={target}")
# clean_article = way_back_check.json()
#
# print(type(clean_article))
# p.pprint(clean_article)
# print(clean_article["archived_snapshots"]["closest"]["url"])

# archive_link = (clean_article["archived_snapshots"]["closest"]["url"])

#
# def return_clean_link():
#     return archive_link

def get_free_link(target:str):
    way_back_check = requests.get(f"http://archive.org/wayback/available?url={target}")
    clean_article = way_back_check.json()
    archive_link = (clean_article["archived_snapshots"]["closest"]["url"])
    return archive_link

# print(get_free_link("https://www.nytimes.com/live/2023/03/16/world/france-pension-vote"))

