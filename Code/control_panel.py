# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

from get_data import (
    get_dataset, 
    get_urls,
    get_outlets,
    get_headlines,
    update_ledger
)

from parse_articles import (
    get_text_data,
    update_textledger
)

from sentiment_analysis import (
    analyze_sentiment,
    organize_sentiment
)

# Get Data Boilerplate - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -


#update_ledger() 

update_textledger()

organize_sentiment()