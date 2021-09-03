from googlesearch import search

def search_google(question):
    results=[]
    for j in search(question, tld="co.in", num=10, stop=None, pause=2):
        if "pdf" in j.lower() or "textbook" in j.lower():
            pass
        else:
            results.append(j)
    return results