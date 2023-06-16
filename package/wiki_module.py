import wikipedia
import random

def wiki_search(wiki):
    try:
        search = wikipedia.page(wiki, auto_suggest=False)
    except wikipedia.DisambiguationError as e:
        s = random.choice(e.options)
        search = wikipedia.page(s)

        
    result = []
    details = {
        'input' : search,
        'title' : search.title,
        'link'  : search.url,
        'details' : search.summary,
        }
    result.append(details)
    return result