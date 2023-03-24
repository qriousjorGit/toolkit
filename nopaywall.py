import requests

def get_free_link(target:str):
    #remove ? from search strings
    if "?" in target:
        position = target.find("?")
        target = target[:position]

    way_back_check = requests.get(f"http://archive.org/wayback/available?url={target}")
    clean_article = way_back_check.json()
    archive_link = (clean_article["archived_snapshots"]["closest"]["url"])
    return archive_link
