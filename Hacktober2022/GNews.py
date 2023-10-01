import gnewsclient
from gnewsclient import gnewsclient
def getNews():
    client = gnewsclient.NewsClient(language='tamil',
    location='india',
    topic='Business',
    use_opengraph = True,
    max_results=10)

    return (client.get_news())