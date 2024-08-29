import spacy as spc
import json
import datetime
from textblob import TextBlob
from halo import Halo as hlo
# Necessary Initializations - - - - - - - - - - - - - - -

with open('organized_info.json', 'r') as jsonFile:
    organized_info = json.load(jsonFile)

with open('text_data.json', 'r') as jsonFile:
    text_data = json.load(jsonFile)

i = 0

j = 0

polarity_holder = []

subjectivity_holder = []

sentiment_spinner = hlo(text='Calculating sentiment scores...', spinner='lines')

# get sentiment scores- - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def analyze_sentiment():
    global i 
    while (i < len(text_data[str(datetime.date.today())])):

        sentiment_spinner.start()


        key = "article" + str(i)

        text = TextBlob(str(text_data[str(datetime.date.today())][str(key)]['text']))
        
        polarity_score = text.sentiment.polarity

        subjectivity_score = text.sentiment.subjectivity

        polarity_holder.append(polarity_score)

        subjectivity_holder.append(subjectivity_score)

        i += 1
    
    sentiment_spinner.succeed('Sentiments successfully calculated')

    return polarity_holder, subjectivity_holder

test1 = analyze_sentiment()[0]

test2 = analyze_sentiment()[1]

print(test1)

print(test2)

    





