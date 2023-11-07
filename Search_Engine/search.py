'''Hunter Knott, CS 3270, Utah Valley University'''
import pprint
import re
import sys
import urllib.parse, urllib.request

# Holds all text and associated link contents of a specified url and search depth
class HayStack():
    def __init__(self, start_url, search_depth=3):
        self.start_url = start_url
        self.search_depth = search_depth
        self.index = {}
        self.graph = {}
        self.get_pages(start_url, search_depth)
        self.compute_ranks(self.graph)

    # Function that takes a starting url and search depth to crawl a website and return all page references
    def get_pages(self, start_url, depth):
        if depth == 0:
            return
        try:
            # Provided urllib.request from urlopen.py file
            req = urllib.request.Request(start_url, headers={'User-Agent' : 'XY'})
            response = urllib.request.urlopen(req)
            page_content = response.read().decode()
        except:
            print(f"There was an error getting {start_url}: {Exception}")
            return
        
        # RegEx to get runs of alphabetic characters and apostrophes
        words = re.findall(r'\b[a-z\']+|[A-Z]\b', page_content.lower())
        words = set(words)

        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(start_url)
        
        # RegEx to get all links on the same page as each word
        self.graph[start_url] = set()
        links = re.findall(r'href=["\'](http[s]?://.*?)["\']', page_content)
        for link in links:
            if link not in self.graph[start_url]:
                self.graph[start_url].add(link)
                self.get_pages(link, depth - 1)

    # Given function that calculates the rank of each page
    def compute_ranks(self, graph):
        d = 0.85     # probability that surfer will bail
        numloops = 10

        ranks = {}
        npages = len(graph)
        for page in graph:
            ranks[page] = 1.0 / npages

        for _ in range(0, numloops):
            newranks = {}
            for page in graph:
                newrank = (1 - d) / npages
                for url in graph:   
                    if page in graph[url]:  # this url links to page
                        newrank += d*ranks[url]/len(graph[url])
                newranks[page] = newrank
            ranks = newranks
        self.ranks = ranks
    
    # Takes a word as a search key and outputs the webpages that contain that word in rank order
    def lookup(self, search_key):
        search_key = search_key.lower()
        if search_key in self.index:
            results = set(self.index[search_key])
            results = sorted(results, key=lambda url: -self.ranks.get(url, 0))
            return set(results)
        else:
            return set()

# Test driver code to print results of a website crawl
# Provided test has been put inside a file writing statement
def main():
    engine = HayStack('http://roversgame.net/cs3270/page1.html',4)
    with open('results.txt', 'w') as output_file:
        sys.stdout = output_file
        for w in ['pages','links','you','have','I']:
            print(w)
            pprint.pprint(engine.lookup(w))
        print()
        print('index:')
        pprint.pprint(engine.index)
        print()
        print('graph:')
        pprint.pprint(engine.graph)
        print()
        print('ranks:')
        pprint.pprint({page:round(rank,4) for page,rank in engine.ranks.items()})
    sys.stdout = sys.__stdout__

if __name__ == "__main__":
    main()