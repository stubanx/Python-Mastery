import requests, json
query = input("What type of news you want?:=- ")
# date = input("Date today (YYYY-MM-DD):=- ")
url = f"https://newsapi.org/v2/everything?q=+{query}+&sortBy=relevancy&apiKey=6d997ca299a14282a5588c865ef8533a"
# url = f"https://newsapi.org/v2/everything?q=+south+indian+bank+share+&from=2024-07-01&to=2024-07-31&sortBy=popularity&apiKey=6d997ca299a14282a5588c865ef8533a"
r = requests.get(url)
news = json.loads(r.text)
# print(news,type(news))
i=0
bestOfToday = []
for article in news["articles"]:
    print()
    print()
    print(article["title"])
    print(article["description"])
    print(article["content"])
    print(article["url"])
    i+=1
    if i==10:
        break
print("so these where all about today news")