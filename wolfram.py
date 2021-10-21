import requests
def wlfAlpha(text):
    returnedJson = requests.get(f'http://api.wolframalpha.com/v2/query?appid=4PJG6W-L4QUR22XJT&input={text}&output=json').json()
    returnedPods = returnedJson['queryresult']['pods']
    returnVar = {}
    returnVar['images'] = []
    returnVar['text'] = []
    for i in range(len(returnedPods)):
        for j in range(len(returnedPods[i]['subpods'])):
            if returnedPods[i]['subpods'][j]['img']['title'] == "":
                returnVar['images'].append(returnedPods[i]['subpods'][j]['img']['src'])
            returnText = []
            returnText.append(returnedPods[i]['title'] + "\n\t" + returnedPods[i]['subpods'][j]['plaintext'])
            returnVar['text'] = returnText
    return returnVar
print(wlfAlpha('x*2=y^2'))