import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pprint

import requests
from bs4 import BeautifulSoup as soup
import time as t

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds=ServiceAccountCredentials.from_json_keyfile_name('secret.json',scope)
client=gspread.authorize(creds)

sheet1=client.open('steam_cases').sheet1
#sheet2=client.open('casestest').sheet2

item_list=[
    'Chroma',
    'Shadow',
    'Gamma',
    'Spektrum',
    'Clutch',
    'Horizont',
    'Prisma',
    'Falchion',
    'Handschuhe',
    'Revolver',
    'Jagd',
    'Operation+Bravo',
    'Operation+Hydra',
    'Gefahrenzone',
    'zerfetztes+netz',
    'operation+wildfire',
    'cs20',
    'operation+phoenix',
    'breakout',
    'CS:GO',
    'vanguard',
    'winteroffensive',
    'esports',
]

start_url='https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730&q=case+'


def initiate(item_list, used_doc):
    print('setting up sheet...')
    i=2
    for search in item_list:
        new_url=start_url+search+'#p1_name_asc'
        #print(new_url)
        data = requests.get(new_url)
        page_soup = soup(data.content,'html.parser')
    
        market_listings = page_soup.findAll('a',{'class':'market_listing_row_link'})
    
        for market_listing in market_listings:
            title = market_listing.find('span','market_listing_item_name').text
            if title == None:
                print('too many server requests!')
                break
            #t.sleep(1)
            used_doc.update_cell(1,i, title)
            i+=1
            print(title)
    print('setup successfull!')

initiate(item_list,sheet1)
#initiate(item_list_old,sheet2)





            