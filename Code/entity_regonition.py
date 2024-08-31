import spacy

# Experimentation - - - - - - - - - - - - - - - - - - - - 
nlp = spacy.load('en_core_web_md')

test1 = nlp("Democratic")
test2 = nlp("Republican")

similiar = test1.similarity(test2)

print(similiar)


