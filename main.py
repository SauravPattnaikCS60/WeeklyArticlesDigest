import os
from parse_feed import get_articles_feed

def check_directory():
    if not os.path.exists('./data/'):
        os.mkdir('./data/')

def run_orchestrator():
    check_directory()
    get_articles_feed()
    
    

if __name__ == "__main__":
    run_orchestrator()