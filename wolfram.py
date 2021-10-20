import requests, json
def wlfAlpha(text):
    returned_json = requests.get(f'http://api.wolframalpha.com/v2/query?appid=4PJG6W-L4QUR22XJT&input={text}&output=json').json()
    return json.dumps(returned_json)
print(wlfAlpha('x*2=y^2'))