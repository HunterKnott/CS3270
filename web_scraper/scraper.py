import requests
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

if __name__ == "__main__":
    api_key = "ejShUxMEpkWI1NDgyz8sZvvjIz7tGgKt"

    year = 2023
    word = "Israel"

    get_word_count(api_key, year, word)