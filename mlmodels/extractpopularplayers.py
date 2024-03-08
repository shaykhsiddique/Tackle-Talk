import pandas as pd
import re
import spacy
from Levenshtein import distance
from collections import Counter

nlp = spacy.load("en_core_web_sm")

def pridectplayers():
    
    df = pd.read_csv('mlmodels/data.csv') 
    df = df.dropna(subset=['comments'])

    string_array = df['Name'].astype(str).to_numpy()
    players = clean_names(string_array)

    df = df.drop(df.columns[:4], axis=1)
    flat_array = df.stack().dropna().values.tolist()

    # Sample comments (replace with your actual comments)
    comments = flat_array

    # Known player names (first name, last name pairs)
    all_player_names = players

    # Count the occurrences of each player name
    all_extracted_player_names = []
    for comment in comments:
        extracted_player_names = extract_normalized_player_names(comment, all_player_names)
        all_extracted_player_names.extend(extracted_player_names)

    # Use Counter to count occurrences
    player_name_counter = Counter(all_extracted_player_names)

    # Find the top 3 mentioned players
    top_players = player_name_counter.most_common(3)
    top_players_fullnames = []
    for (first_name, last_name), count in top_players:
        top_players_fullnames.append(first_name.capitalize()+" "+ last_name.capitalize())
    
    return top_players_fullnames






def clean_names(name_array):
    # Use regular expression to keep only English letters and convert to lowercase
    cleaned_array = [re.sub(r'[^a-zA-Z ]', '', name).lower() for name in name_array]
    
    # Split names into first name and last name using space as a separator
    cleaned_array = [(first, last.split()[0]) for first, last in (name.split(maxsplit=1) for name in cleaned_array)]
    
    return cleaned_array

def clean_text(text_list):
    cleaned_text_list = [re.sub(r'[^a-zA-Z ]', '', text).lower() for text in text_list]
    return cleaned_text_list

# Extract and normalize player names from comments
def extract_normalized_player_names(comment, known_player_names):
    extracted_names = []

    for first_name, last_name in known_player_names:
        # Check for exact match with either first name or last name
        if (
            first_name.lower() in comment.lower()
            or last_name.lower() in comment.lower()
        ):
            extracted_names.append((first_name, last_name))

    # If no direct match, use NLP with Levenshtein distance for fuzzy matching
    if not extracted_names:
        doc = nlp(comment)
        for ent in doc.ents:
            if ent.label_ == "PERSON":
                # Check Levenshtein distance for fuzzy matching
                best_match = min(
                    known_player_names,
                    key=lambda known_name: distance(ent.text.lower(), known_name[1].lower())
                )
                extracted_names.append(best_match)

    return extracted_names

