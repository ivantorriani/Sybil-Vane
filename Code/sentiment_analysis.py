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

organizer_spinner = hlo(text='Organizing Sentiment Scores...', spinner='lines')


with open('organized_info.json', 'r') as jsonFile:
    organized_info = json.load(jsonFile)

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

polarity_data = analyze_sentiment()[0]
subjectivity_data = analyze_sentiment()[1]



def organize_sentiment():
    global j
    while (j < len(text_data[str(datetime.date.today())])):

        organizer_spinner.start()

        key = "article" + str(j)

        polarity_score = polarity_data[j]

        subjectivity_score = subjectivity_data[j]

        data = {

            "polarity": float(polarity_score),
            "subjectivity": float(subjectivity_score)
        }

        #organized_info[str(datetime.date.today())].update(data)

        organized_info[str(datetime.date.today())][str(key)].update(data)

        with open('organized_info.json', 'w') as file:
            json.dump(organized_info, file, indent = 4)

        j += 1

    organizer_spinner.succeed('Scores successfuly organized')

        
organize_sentiment()









