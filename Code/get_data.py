from newsapi import NewsApiClient as nac
from halo import Halo as hlo
import easygui as ez
import datetime 

import json


# Important starters - - - - - - - - - - - - - -


key = 'r'

client = nac(api_key = key)

i = 0
j = 0
v = 0
r = 0

url_holder = []

outlet_holder = []

headline_holder = []

url_spinner = hlo(text='Gathering URLS...', spinner='bouncingBar')

outlet_spinner = hlo(text = 'Gathering outlets...', spinner = 'bouncingBar')

headline_spinner = hlo(text = "Gathering headlines...", spinner = 'line')



# Getting URLS and Sources - - - - - - - - - - - - - - 

def get_dataset(que):
    current_date = datetime.date.today()
    earlier_date = datetime.date.today() - datetime.timedelta(1)
    query = que
    #topic = ez.enterbox("Enter keywords here please!")
    data = client.get_everything(
        q = que,
        from_param = (earlier_date),
        to = (current_date),
        page_size = 50,
        sort_by="relevancy"
        
    )
    
    return data

data = get_dataset("Harris")




def get_urls():
    global i 
    while (i < len(data['articles'])):
        url_spinner.start()
        article_url = data['articles'][i]['url']
        url_holder.append(article_url)
        i += 1
    
    url_spinner.succeed('URLS gathered successfuly')

    return url_holder

def get_outlets():  
    global j 
    while (j < len(data['articles'])):
        outlet_spinner.start()
        article_outlet = data['articles'][j]['source']['name']
        outlet_holder.append(article_outlet)
        j += 1

    outlet_spinner.succeed('Outlets gathered successfully')
    return outlet_holder

def get_headlines():
    global r
    while(r < len(data['articles'])):
        headline_spinner.start() 
        article_headline = data['articles'][r]['title']
        headline_holder.append(str(article_headline))
        r += 1
    headline_spinner.succeed("Headlines gathered successsfully")
    return headline_holder




url_list = get_urls()

outlet_list = get_outlets()

headline_list = get_headlines()


# Organizing Data - - - - - - - - - - - - - -- - - - - - - - - - - - - -

try:
    with open('organized_info.json', 'r') as jsonFile:
        organized_info = json.load(jsonFile)
except FileNotFoundError:
    organized_info = {}


def update_ledger():
    global v
    updt_datekey = {

        str(datetime.date.today()): {}
    }

    organized_info.update(updt_datekey) #Set up the date key for the day

    with open('organized_info.json', 'w') as file: #Dump the date key so that its on the json file
        json.dump(organized_info, file, indent = 2)


    while (v < len(get_urls())):
        key = str("article") + str(v)

        data = {
            key : {
                "source": outlet_list[v],
                "url": url_list[v],
                "headline": headline_list[v]
            }

        }

        organized_info[str(datetime.date.today())].update(data)

        with open('organized_info.json', 'w') as file:
            json.dump(organized_info, file, indent = 4)
        
        v += 1


update_ledger()































    







