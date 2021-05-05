########################################################################################################################
# INCLUDES
########################################################################################################################
import aiohttp
import praw
import random

########################################################################################################################
# API
########################################################################################################################
async def get_animal(animal, apiKey, mimeType):
    headers = {
        'x-api-key'   : apiKey,
        'Content-Type': 'application/json'
    }
    params = {
        'mime_types': mimeType
    }

    if(animal == 'cat'):
        API = 'https://api.thecatapi.com/v1/images/search'
    elif(animal == 'dog'):
        API = 'https://api.thedogapi.com/v1/images/search'
    else:
        return "Unknown API"

    async with aiohttp.ClientSession() as session:
        async with session.get(API, headers = headers, params = params) as response:
            if response.status != 200 or 'application/json' not in response.headers['content-type']:
                return "Cannot reach API"
            else:
                url = await response.json()
                return url[0]['url']



async def get_keeb(bot):
    r = praw.Reddit(
        client_id=bot.id,
        client_secret=bot.secret,
        password=bot.password,
        user_agent="Safari",
        username=bot.username,
    )

    sr = r.subreddit("mechanicalKeyboards")
    for i in sr.random():
        if i.link_flair_text and i.link_flair_text.strip().lower() == "photos":
            return i.url

