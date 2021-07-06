import os
from dotenv import load_dotenv
dotenv_path = os.path.join('../', '.env')
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)

botconfig = {
    'token': os.environ['DTOKEN'],
    'name': 'VisionOne',
    'id': 785383439196487720,
    'prefix': '=',
    'accent1': 0xd7832a,
    'accent2': 0xcb3532,
    'accent3': 0x6eda5f,
    'version': '01R10-210706',
    'owner': '741883312108339231',
    'logs_channel': 861856796041543693,
    'feedback_channel': 861857314670772224,
    'unsplash_ak': os.environ['UNSAKEY'],
    'unsplash_sk': os.environ['UNSSKEY'],
    'unsplash_ur': os.environ['UNSRDC'],
}
