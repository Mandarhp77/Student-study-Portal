from youtubesearchpython import VideosSearch

def youtube_search(search):
    video = VideosSearch(search, limit=10)
    result = []
    for i in video.result()['result']:
        resultdict = {
        'input':search,
        'title' : i['title'],
        'duration' : i['duration'],
        'thumbnails' : i['thumbnails'][0]['url'],
        'channel' : i['channel']['name'],
        'link' : i['link'],
        'viewcount' : i['viewCount']['short'],
        'published' : i['publishedTime'],
        }
        result.append(resultdict)
    return result
        