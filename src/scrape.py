import gspread
from oauth2client.service_account import ServiceAccountCredentials


import requests
from bs4 import BeautifulSoup as soup
import time as t

scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('/home/mecampen/steamscrape/steamscrape/src/secret.json',scope)
client = gspread.authorize(creds)

sheet1=client.open('steam_cases').sheet1

start_url='https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730&q=case+'

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

def check_for_new_item():
    test_url = 'https://steamcommunity.com/market/search?category_730_ItemSet%5B%5D=any&category_730_ProPlayer%5B%5D=any&category_730_StickerCapsule%5B%5D=any&category_730_TournamentTeam%5B%5D=any&category_730_Weapon%5B%5D=any&category_730_Type%5B%5D=tag_CSGO_Type_WeaponCase&appid=730&q=case'
    data = requests.get(new_url)
    page_soup = soup(data.content,'html.parser')
    new_titles = []
    market_listings = page_soup.findAll('a',{'class':'market_listing_row_link'})

    for market_listing in market_listings:
        i = 0
        title = market_listing.find('span','market_listing_item_name').text
        new_titles.append(title)
        i += 1


def recent_time():
    localtime = t.localtime(t.time())
    return str(localtime.tm_mday)+'.'+str(localtime.tm_mon)+'.'+str(localtime.tm_year)

#scraper
def update(days):#check_for_new_item()
    j = days + 1
    dateandtime = recent_time()

    case_row = sheet1.row_values(1)[1::]
    price_dict = {}
    updated_values = [dateandtime]

    for search in item_list:
        i = 2
        new_url = start_url+search+'#p1_name_asc'
        data = requests.get(new_url)
        page_soup = soup(data.content,'html.parser')

        market_listings = page_soup.findAll('a',{'class':'market_listing_row_link'})

        for market_listing in market_listings:
            price = market_listing.find('span', 'normal_price').span.text
            price = price[1:6]
            if price[3]==' ':
                price = price[0:4]
            name = market_listing.find('span','market_listing_item_name').text
            price_dict[name] = price

    #print("case_row ", case_row)
    #print("price_dict ", price_dict.keys())

    for case_name in case_row:
        updated_values.append(price_dict[case_name])

    sheet1.insert_row(updated_values, j)
    print("inserted values successfully!")

def main():
    dates=sheet1.col_values(1)
    days=len(dates)
    print('days:{}'.format(days))
    if len(dates) == 0:
        update(1)
    elif dates[days-1][0:2]!=recent_time()[0:2]:
        print('last entry: {}'.format(dates[days-1]))
        print('today:{}'.format(recent_time()))
        print('updating sheet...')
        update(days)
        print('finished!')
    else:
        print('last entry: {}'.format(dates[days-1]))
        print('today:{}'.format(recent_time()))
        print('sheet is up to date!')

if __name__ == "__main__":
    main()


