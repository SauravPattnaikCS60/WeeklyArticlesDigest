from utils import *
from urls import get_urls
import feedparser
import os
import random
import json

def get_articles_feed():
    try:
        if not os.path.exists('data/archive.json'):
            existing_file_json = None
        else:
            existing_file_json = json.load(open('data/archive.json','r'))
        
        urls = get_urls()
        all_articles = {}
        for key,url in urls.items():
            articles = []
            feed = feedparser.parse(url)
            feed_entries = feed.entries
            
            is_randomized = random.choice([0,1])
            if is_randomized:
                random.shuffle(feed_entries)

            if existing_file_json:
                existing_file_names = [res['title'] for res in existing_file_json[key]]
            else:
                existing_file_names = []
                    
            top_n = 3
            
            for entry in feed_entries:
                if entry.title not in existing_file_names and 'quiz' not in entry.title.lower() and 'podcast' not in entry.title.lower():
                    article_json = {}
                    article_json['title'] = entry.title
                    article_json['link'] = entry.link
                    article_json['summary'] = entry.summary
                    article_json['date'] = parse_date(entry.updated_parsed)
                    articles.append(article_json)
                
                if len(articles) == top_n:
                    break
                
            all_articles[key] = articles
            if existing_file_json:
                existing_file_json[key] += articles

        json.dump(all_articles, open('data/articles.json','w'))
        
        if existing_file_json:
            json.dump(existing_file_json, open('data/archive.json','w'))
        else:
            json.dump(all_articles, open('data/archive.json','w'))
    except:
        return