from googlesearch import search

def search_google(question):
    results=[]
    for j in search(question, tld="co.in", num=10, stop=10, pause=2):
        results.append(j)
    return results