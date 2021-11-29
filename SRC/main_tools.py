from Configuration.configuration import engine
import pandas as pd
import random 
from textblob import TextBlob

def authors():
    query = list(engine.execute("SELECT distinct(Name_Author) FROM Friends_API.Authors;"))
    author_list = [{'name': element[0]} for element in query]
    return author_list

def lines(): 
    query = list(engine.execute("SELECT distinct(Text) FROM Friends_API.Quotes;"))
    lines_list = [{'line': element[0]} for element in query]
    return lines_list

def episode_title():
    query = list(engine.execute("SELECT distinct(Title_Episode) FROM Friends_API.Episodes;"))
    episodes = [{'episode': element[0]} for element in query]
    return episodes

def quotes(author):
    query = f"""
    SELECT Quotes.Text, Authors.Name_Author
    FROM Friends_API.Quotes
    INNER JOIN Friends_API.Authors
    ON Authors.id_Author=Quotes.Authors_id_Author
    WHERE Name_Author= '{author}';
    """
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient='records')

def quotes_episode(author,episode):
    query = f"""
    SELECT Quotes.Text, Authors.Name_Author, Episodes.Title_Episode
    FROM Friends_API.Quotes
    INNER JOIN Friends_API.Authors
    ON Authors.id_Author=Quotes.Authors_id_Author
    INNER JOIN Friends_API.Episodes
    ON Episodes.id_Episode=Quotes.Episodes_id_Episode
    WHERE Name_Author= '{author}' AND Title_Episode= '{episode}';
    """
    data = pd.read_sql_query(query,engine)
    return data.to_json(orient='records')

def new_quote(episode,author,quote):
    engine.execute(f"""
    INSERT INTO Quotes (Episodes_id_Episode,Authors_id_Author,Text)
    VALUES ({episode}, {author}, '{quote}');
    """)
    return f"Your quote has been successfully included: {episode} {author} {quote}"



