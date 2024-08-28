from newspaper import Article as art
from get_data import get_urls, get_headlines
import json 
import datetime 
from halo import Halo as hlo
# Documentation - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

#article = art('https://www.nbcnews.com/politics/supreme-court/supreme-court-refuses-revive-bidens-latest-student-loan-debt-relief-pl-rcna167455')
#article.download()
#rticle.parse()

#print(article.text)

i = 0

j = 0


param = len(get_urls())

headline_list = get_headlines()


today_date = datetime.date.today()

article_data = []

l_t_spinner = hlo(text = 'Getting text data...', spinner = 'line')

o_t_spinner = hlo(text = 'Organizing text data', spinner = 'line')

# Gathering text data - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

try:
    with open('organized_info.json', 'r') as jsonFile:
        organized_info = json.load(jsonFile)
except FileNotFoundError:
    organized_info = {}

try:
    with open('text_data.json', 'r') as jsonFile:
        text_data = json.load(jsonFile)
except FileNotFoundError:
    text_data = {}


def get_text_data():
    global i, today_date

    while (i < int(param)):
        l_t_spinner.start()

        article_key = "article" + str(i)
        url = organized_info[str(today_date)][str(article_key)]['url']
        article = art(str(url))

        article.download()
        article.parse()

        article_body = article.text

        article_data.append(article_body)

        i += 1
    
    l_t_spinner.succeed('Text data gathered successfuly')

    return article_data

texts = get_text_data()


def update_textledger():

    global j 
    
    updt_datekey = {

        str(today_date): {}
    }

    text_data.update(updt_datekey)

    with open('text_data.json', 'w') as file:
        json.dump(text_data, file, indent = 4)

    while (j < param):

        o_t_spinner.start()


        
        key = str("article") + str(j)

        data = {
            key : {
                "headline": headline_list[j],
                "text": texts[j]
            }
        }

        text_data[str(today_date)].update(data)

        with open('text_data.json', 'w') as file:
            json.dump(text_data, file, indent = 4)

        j += 1

    o_t_spinner.succeed('Text data successfuly organized')

    
update_textledger()

    







