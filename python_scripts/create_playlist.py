import ytmusicapi
from ytmusicapi import YTMusic
import pandas as pd


def fetch_id(search):
    results = ytmusic.search(query=search)
    song_results = [result for result in results if result['category']=='Songs' and result['resultType']=='song']
    return song_results[0]['videoId']



# Paste headers from a post request to youtube music in firefox
headers= """
POST /youtubei/v1/music/get_search_suggestions?prettyPrint=false HTTP/3
Host: music.youtube.com
User-Agent: Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:128.0) Gecko/20100101 Firefox/128.0
Accept: */*
Accept-Language: en-US,en;q=0.5
Accept-Encoding: gzip, deflate, br, zstd
Content-Type: application/json
Content-Length: 3033
Referer: https://music.youtube.com/search?q=hit+me+baby+one+more+time
X-Goog-Visitor-Id: CgtDOFVISkdZeTJhRSjxo4S1BjIKCgJaQRIEGgAgZQ%3D%3D
X-Youtube-Bootstrap-Logged-In: true
X-Youtube-Client-Name: 67
X-Youtube-Client-Version: 1.20240722.01.00
X-Goog-AuthUser: 0
X-Origin: https://music.youtube.com
Origin: https://music.youtube.com
Sec-Fetch-Dest: empty
Sec-Fetch-Mode: same-origin
Sec-Fetch-Site: same-origin
Authorization: SAPISIDHASH 1721831940_6ced94150c459846853113481e1dfc915276b4f6 SAPISID1PHASH 1721831940_6ced94150c459846853113481e1dfc915276b4f6 SAPISID3PHASH 1721831940_6ced94150c459846853113481e1dfc915276b4f6
Connection: keep-alive
Alt-Used: music.youtube.com
Cookie: PREF=f6=80&tz=Africa.Johannesburg; YSC=NRBxlR_hfD0; VISITOR_INFO1_LIVE=C8UHJGYy2aE; VISITOR_PRIVACY_METADATA=CgJaQRIEGgAgZQ%3D%3D; _gcl_au=1.1.806022143.1721831616; __Secure-1PSIDTS=sidts-CjIB4E2dka2GtlZ1d-HfKPF6uFP9q0S5T-GcBIFbInK9-LS3jzLRpEskcSZvOv7T5kBpeRAA; __Secure-3PSIDTS=sidts-CjIB4E2dka2GtlZ1d-HfKPF6uFP9q0S5T-GcBIFbInK9-LS3jzLRpEskcSZvOv7T5kBpeRAA; HSID=A2J4C58EZ39_0fLS9; SSID=AfQuoesSyM9Va4Iwb; APISID=vUOoyFrNdLBl8lpw/Aw1ERSPQlCHwwjjjH; SAPISID=CLaHtsX5wmtSdiCS/AbU_3X66k3MXlBxo0; __Secure-1PAPISID=CLaHtsX5wmtSdiCS/AbU_3X66k3MXlBxo0; __Secure-3PAPISID=CLaHtsX5wmtSdiCS/AbU_3X66k3MXlBxo0; SID=g.a000mAjtresnAtn7dUeRDDh6lYSKmKcshN4FYqGIVGUKFu7oc-WHJy1rfbOiQd9zS08FHp1ytgACgYKAfESARISFQHGX2MiQEle3bvzIFu7nEacBWU-vxoVAUF8yKpCqFdmEulgIMy5rzw907J-0076; __Secure-1PSID=g.a000mAjtresnAtn7dUeRDDh6lYSKmKcshN4FYqGIVGUKFu7oc-WH4yAfcOuNFsB8dCWUbysqAwACgYKATQSARISFQHGX2MiQ7s0cRW9BMpiQ35J0W_r4xoVAUF8yKqUNde5YcnY761fHOqAk1hh0076; __Secure-3PSID=g.a000mAjtresnAtn7dUeRDDh6lYSKmKcshN4FYqGIVGUKFu7oc-WHcXMknlryjiizJtyPWWMibwACgYKARUSARISFQHGX2Mi-9Zs5zgvkh9uP32AC85d2BoVAUF8yKoyW2pe8tSOAzxDvEX9OHjo0076; LOGIN_INFO=AFmmF2swRQIhAKcHQ9ixvzTwVnGiQhk3g-owWWhyTI9eGundhyNkIDN-AiBN_c7yCctUN3Rsmx4bItBeKSAS5M9DzLwMhQhaTkqnEw:QUQ3MjNmd1ZOaW82R0x2TDdQVmxtRVpBWmF5NmdEOFlHSFlNQ3lPd1BXRFIzOTY1QlBxV0I0cFJ6bHlXYU50TXZUOExNUy1WWlRJUHdoZjc2Q1lBWmRtVk1pT3N5RFRxbGNQU0l1RElvNXRVRy0taUswTG5yVGc0OHI0bGNlWlRRdmJxZ0pVeE53TU5KZWFHWTZmQXI3WFE1My10MUthU2xR; SIDCC=AKEyXzXQ8etM88NgRmgukMZTww6E4g6Q4KP-0MMYbmtgGaq5HjQdSq3aj-X1MKJ7B6FimXDkqw; __Secure-1PSIDCC=AKEyXzVJy_95yu7p1ABjU-Kswjt_mxFuW4--gAKarqbU93mKsyfY8mtCzBjRl2O4e46wujXs; __Secure-3PSIDCC=AKEyXzVGnvBtDXNpLeNK2lGWcTxdMPuWQbYOig-t_otI-c9poC_6gduLr-6bNZZflAcOypv5Dw
Priority: u=0
TE: trailers"""

ytmusicapi.setup(filepath="browser.json", headers_raw=headers)

ytmusic = YTMusic("browser.json")

df = pd.read_excel('/home/fred/WebstormProjects/wedding-website-live/python_scripts/RSVP for Wedding.xlsx', sheet_name = 'responses')

songs = list(df['song1'].dropna()) + list(df['song2'].dropna()) + list(df['song3'].dropna())

ids = [fetch_id(song) for song in songs]

ytmusic.create_playlist(
    title = "Test Wedding Playlist",
    description = "Test Wedding Playlist.",
    video_ids = ids
)

print('Playlist created')