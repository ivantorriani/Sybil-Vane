from newsapi import NewsApiClient as nac
from halo import Halo as hlo
import easygui as ez
import datetime 

# Important starters - - - - - - - - - - - - - -


key = 'undisclsed'

client = nac(api_key = key)

i = 0

j = 0


url_holder = []

outlet_holder = []

url_spinner = hlo(text='Gathering URLS...', spinner='bouncingBar')

outlet_spinner = hlo(text = 'Gathering outlets...', spinner = 'bouncingBar')



# Getting URLS and Sources - - - - - - - - - - - - - - I will stop lying. I'm sorry.

def get_dataset():
    current_date = datetime.date.today()
    earlier_date = current_date - datetime.timedelta(days=5)
    #topic = ez.enterbox("Enter keywords here please!")
    data = client.get_everything(
        q = "Harris",
        from_param = (earlier_date),
        to = (current_date)
    )
    
    return data

data = get_dataset()

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


outlets = get_outlets()

print(outlets)

# - - - - - - - - - - - - - -- - - - - - - - - - - - - -




    







