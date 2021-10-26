import requests
def wlfAlpha(text):
    returnedJson = requests.get(f'http://api.wolframalpha.com/v2/query?appid=4PJG6W-L4QUR22XJT&input={text}&output=json').json()
    returnedPods = returnedJson['queryresult']['pods']
    returnVar = {}
    if returnedJson['queryresult']['success'] == 'false':
        returnVar = ['unparsed']
    else:
        returnVar['images'] = []
        returnVar['text'] = []
        for i in range(len(returnedPods)):
            for j in range(len(returnedPods[i]['subpods'])):
                if returnedPods[i]['subpods'][j]['img']['title'] == "":
                    returnVar['images'].append(returnedPods[i]['subpods'][j]['img']['src'])
                returnText = []
                returnText.append(returnedPods[i]['title'] + "__SUBPODS__" + returnedPods[i]['subpods'][j]['plaintext'])
                returnVar['text'].append(returnText)
    return returnVar