# First, we need some special tools (called libraries) that help us get information from the internet and work with data
import requests
import json

# Here is a secret code (API key) that lets us use a news website to search for news articles
myapi = "6d997ca299a14282a5588c865ef8533a"
# Ask the user to type in a topic they want to search for (like "sports" or "science")
query = input("Enter topic to search:")
start_date = input("Search start date(YYYY-MM-DD):")
end_date = input("Search end date(YYYY-MM-DD):")
sort = input("Sort by (relevancy, popularity, publishedAt):")


# Create a link
qurl = f"https://newsapi.org/v2/everything?q={query}&from={start_date}&to={end_date}&pageSize=2&sortBy={sort}&apiKey={myapi}"
r = requests.get(qurl)

# Change the news data we got into a form we can easily understand (called JSON) similar to python dictionary krish
news = json.loads(r.text)

# For each news article, we will show the important details
for article in news["articles"]:
    # Show who wrote the article
    print("------------------------------------------")
    print() 
    print(article["author"])
    print(article["title"])
    print(article["description"])
    print(article["url"])
    print(article["publishedAt"])

print("------------------------------------------")
print() 
    # ---E_N_D---