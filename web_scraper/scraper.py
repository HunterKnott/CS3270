import requests
import json
import matplotlib.pyplot as plt

# https://developer.nytimes.com/apis for information

def get_word_count(api_key, year, word):
    article_counts = []
    for month in range(1, 13):
        url = f"https://api.nytimes.com/svc/archive/v1/{year}/{month}.json"
        params = {"api-key": api_key}

        try:
            # Make the API request
            response = requests.get(url, params=params)
            response.raise_for_status()  # Raise an exception for bad responses
            data = response.json()

            count = 0
            for article in data["response"]["docs"]:
                headline = article['headline']['main']
                if word in headline:
                    count += 1
                    # print(f"Headline: {headline}")
                    # print(f"Byline: {article['byline']}")
                    # print(f"Publication Date: {article['pub_date']}")
                    # print(f"URL: {article['web_url']}")
                    # print("-" * 30)
                    # print(f"Snippet: {article['snippet']}")
            article_counts.append(count)
            print(f"Successful retrieval count: {month}")

        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")

    
    x_values = list(range(1, len(article_counts) + 1))
    plt.plot(x_values, article_counts)
    plt.title(f'Instances of the word \"{word}\" in {year} headlines')
    plt.xticks(range(1, len(article_counts) + 1))
    plt.xlabel('Month')
    plt.ylabel('Frequency')
    plt.grid(True)
    plt.show()

def word_search(api_key, query):
    url = f"https://api.nytimes.com/svc/search/v2/articlesearch.json"
    params = {
        "q": query,
        "api-key": api_key
    }

    try:
        # Make the API request
        response = requests.get(url, params=params)
        response.raise_for_status()  # Raise an exception for bad responses
        data = response.json()

        # Process and print the results
        if "response" in data and "docs" in data["response"]:
            articles = data["response"]["docs"]
            print(f"Number of articles found: {len(articles)}")

            for article in articles:
                headline = article["headline"]["main"]
                date_published = article["pub_date"]
                print("-" * 30)
                print(f"Headline: {headline}")
                print(f"Date Published: {date_published}")

        else:
            print("No articles found.")

    except requests.exceptions.RequestException as e:
        print(f"Error making request: {e}")

if __name__ == "__main__":
    api_key = "ejShUxMEpkWI1NDgyz8sZvvjIz7tGgKt"

    while True:
        print("\nMenu:")
        print("1. Get word count")
        print("2. Word Search")
        print("Q. Quit")

        choice = input("Enter a choice of action: ")

        if choice == "1":
            year = int(input("Enter the year to look at: "))
            word = input("Enter the word to measure: ")
            get_word_count(api_key, year, word)
        elif choice == "2":
            query = input("Enter the word to search for: ")
            word_search(api_key, query)
        elif choice == "q" or "Q":
            print("Quitting the program.")
            break
        else:
            print("Invalid choice. Please enter a number on the menu.")