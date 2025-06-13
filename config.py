import re
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("28933540"))
API_HASH = getenv("e862babec20722cd3060288021d6397b")

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7576323434:AAFQE5FnCjAAGQx3X3gyHyxSj_4RJzFaeLE")

BOT_USERNAME = getenv("BOT_USERNAME", "@Falling_for_u_bot")

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://likimusic:likhith@8123@cluster0.tn8iknx.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 240))

API_URL = getenv("API_URL", 'https://api.thequickearn.xyz') #youtube song url
API_KEY = getenv("API_KEY", None) # youtube song api key, get it from https://t.me/RahulTC

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002889415304", ))

# Get this value from @FallenxBot on Telegram by /id
OWNER_ID = int(getenv(" 5867783630", ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("fallen for you")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HRKU-AAVj82WgXWW50cpSvpzZoKGxrZgEJQQ32nqFA4sx1Vow_wI3k4MANOUJ")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/JIYOXC/Wleowleo",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/dpzchannel143")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/kannada_chatting0")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))


# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "48037b43459c4bacbce6c61be2575ade")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "103c89540301422aa880a462ca556416")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", 300))


# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @StringFatherBot on Telegram
STRING1 = getenv("STRING_SESSION", "AQG5faQAY_qBDCisdW6v5ZrFT9xfa5kRWzXVWZFK51ETa7SNE9htxj381537pwrmGxumpTgrCJJMwQBjHEiJnwyXbxWw2M6xWeJI_lR90qCCm78SI38wLzciIXjZ8I1oUvhPp5HBihfFqpo-V-oxpkR2nWfLh3jHf89Z3jh4e_mmiiMw7nhyLbtew80EW48_97Jq-k-Bsb7BIL3OaehrcZewQkKeEj7jKNP78oh1knkZog7Lew9WWUJWBjVfsW89Hm01FeC7Gj0Mg-F6W8lkd0VnqhUHNXNnmf5_EUNk0JuzewzhQA4Jpt4QF2ucOYNMSHt3oPcj7kvT54vnOia4vrIVsNqg7gAAAAG0m17KAA")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://telegra.ph/file/8d7b534e34e13316a7dd2.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://telegra.ph/file/ca95213f8c1dd9a19c239.jpg"
)
PLAYLIST_IMG_URL ="https://telegra.ph/file/8d7b534e34e13316a7dd2.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/e906c2def5afe8a9b9120.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/bd995b032b6bd263e2cc9.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/bb0ff85f2dd44070ea519.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/6298d377ad3eb46711644.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/37d163a2f75e0d3b403d6.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/b35fd1dfca73b950b1b05.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/95b3ca7993bbfaf993dcb.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", "https://t.me/dpzchannel143"):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", "https://t.me/kannada_chatting0"):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
)
