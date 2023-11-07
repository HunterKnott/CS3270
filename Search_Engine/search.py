'''Hunter Knott, CS 3270, Utah Valley University'''
import pprint
import re
import urllib.parse, urllib.request

class HayStack():
    def __init__(self, start_url, search_depth=3):
        # crawls starting from the given web page, finding and following all embedded webpage links until it reaches 
        self.start_url = start_url
        self.search_depth = search_depth
        self.index = {}
        self.graph = {}
        self.get_pages(start_url, search_depth)
        self.compute_ranks(self.graph)

    def get_pages(self, start_url, depth):
        if depth == 0:
            return
        try:
            req = urllib.request.Request(start_url, headers={'User-Agent' : 'XY'})
            response = urllib.request.urlopen(req)
            page_content = response.read().decode()
        except:
            print(f"There was an error getting {start_url}: {Exception}")
            return
        
        words = re.findall(r'\b[a-z\']+|[A-Z]\b', page_content.lower()) # Runs of alphabetic characters and apostrophes
        words = set(words)

        for word in words:
            if word not in self.index:
                self.index[word] = set()
            self.index[word].add(start_url)
        
        self.graph[start_url] = set()
        links = re.findall(r'href=["\'](http[s]?://.*?)["\']', page_content)
        for link in links:
            if link not in self.graph[start_url]:
                self.graph[start_url].add(link)
                self.get_pages(link, depth - 1)

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
    
    def lookup(self, search_key):
        search_key = search_key.lower()
        if search_key in self.index:
            results = set(self.index[search_key])
            results = sorted(results, key=lambda url: -self.ranks.get(url, 0))
            return set(results)
        else:
            return set()

def main():
    engine = HayStack('http://roversgame.net/cs3270/page1.html',4)
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

if __name__ == "__main__":
    main()