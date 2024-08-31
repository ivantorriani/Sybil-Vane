import spacy
import json 
from openai import OpenAI as oa

# Boilerplate - - - - - - - - - - - - - - - - - - - - 

oa_key = 'xxx'

oa_client = oa(api_key = oa_key)

with open('keywords.json', 'r') as jsonFile:
    keywords = json.load(jsonFile)

i = 0

j = 0

v  = 0

# - - - - - - - - - - - - - - - - - - - - 

def ai_parsing(direc, aidesc):
    directory = direc
    
    completion = oa.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": aidesc},
            {"role": "user", "content": directory,}
        ]
    )


    data = completion.choices[0].message.content
    return data



