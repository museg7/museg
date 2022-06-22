## What's up Kangers

import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "1BJWap1wBuzLXPETsQZW1mrucyWypZlCzRcgDPBp6Aj0kFIeWfMt5Tw-JljAClHXNVrVllXts-EOWsDRdWGCJz_KBILyvwLFg7EubYHxaJx2tH1x_U9Cb9eFBuDz3TH9r5DNralS8J8ty3ib2gpOo0qWW-SLgXox3TKb7oCI7SKj-QwHx5JQfqgboL4WEuQ4Zkh_DrQSUSoNt_Mli68yigbPxoUnCJVxavYkpnZPoUk2fdPOyzuR3CKrmH2cI8cQms_xxQ7i0D7IJRufq21WbPB-pk-l8J-8MC_dCCgWcsCxVebjUSrttS8zjuYY4pYsVPtU6q9zJ1la9Ql2sVzzLolNaMaE6Bpg=")
BOT_TOKEN = getenv("BOT_TOKEN", "5289123976:AAFKmfUrlTeqFRapMPB6Y9SxRrQPiHLElLI")
BOT_NAME = getenv("BOT_NAME", "sro")
API_ID = int(getenv("API_ID", "5700184"))
API_HASH = getenv("API_HASH", "bd4f565c58aaf91cccec435a03e3968c")
OWNER_NAME = getenv("OWNER_NAME", "carlos")
OWNER_USERNAME = getenv("OWNER_USERNAME", "tii9t")
ALIVE_NAME = getenv("ALIVE_NAME", "carlos")
BOT_USERNAME = getenv("BOT_USERNAME", "s3_rbot")
OWNER_ID = getenv("OWNER_ID", "1854384004")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "tii9t")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "oc_c3")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "oc_c3")
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
HEROKU_API_KEY = getenv("UPDATES_CHANNEL", "HEROKU_API_KEY")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "5183684102").split()))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
ALIVE_IMG = getenv("ALIVE_IMG", "https://te.legra.ph/file/407ce4c57a645c11f65c0.jpg")
START_PIC = getenv("START_PIC", "https://te.legra.ph/file/7713b9828bced85d9b46e.jpg")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "10"))
UPSTREAM_REPO = getenv("UPSTREAM_REPO", "https://github.com/muntazer995/ing")
IMG_1 = getenv("IMG_1", "https://te.legra.ph/file/402c519808f75bd9b1803.jpg")
IMG_2 = getenv("IMG_2", "https://te.legra.ph/file/c74686f70a1b918060b8e.jpg")
IMG_3 = getenv("IMG_3", "https://te.legra.ph/file/90e3b3aeb77e3e598d66d.jpg")
IMG_4 = getenv("IMG_4", "https://te.legra.ph/file/478f9fa85efb2740f2544.jpg")
IMG_5 = getenv("IMG_5", "https://te.legra.ph/file/2a726c634dbc3b9e8f451.jpg")
IMG_6 = getenv("IMG_6", "https://te.legra.ph/file/430dcf25456f2bb38109f.jpg")
