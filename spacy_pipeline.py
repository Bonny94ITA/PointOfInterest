from utils.utils import count_occurrences, get_entities, search_with_google, wiki_content
import spacy
import json

nlp = spacy.load("it_core_news_sm")
cities = ["Torino"]

for city in cities:
    # Read wiki pages
    text = wiki_content(city)
    # text = read_text_file('assets/test_sentences.txt')
    doc = nlp(text)

    sentence_list = list(doc.sents) 

    # Opening JSON file
    f = open('./assets/italian_cities.json')
    italian_cities = json.load(f)
    f.close()
    # Count occurrences
    counter = count_occurrences(doc, italian_cities, "name")  
    
    # Max occurrence
    context = max(counter, key=counter.get) 
    #print(context)

    # Get entities without duplicates
    searchable_entities = get_entities(doc, counter)
    #print(searchable_entities)

    # Search addresses with Google
    search_with_google(searchable_entities, context)
