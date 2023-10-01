import praw
from Config import *

def getMemes(subredditTitle):
    reddit_read_only = praw.Reddit(client_id = REDDIT_CLIENT_ID, client_secret = REDDIT_CLIENT_SECRET, user_agent = REDDIT_USER_AGENT)
    subreddit = reddit_read_only.subreddit(str(subredditTitle))
    posts = subreddit.new(limit = 10)
    memePosts=[]
    for post in posts:
        memePost={
            'title':post.title,
            'postText':post.selftext,
            'postImgUrl':post.url,
        }
        memePosts.append(memePost)
    return memePosts