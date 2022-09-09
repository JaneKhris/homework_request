import requests

url = 'https://akabab.github.io/superhero-api/api/all.json'
resp = requests.get(url)

sh_list = ['Hulk', 'Captain America', 'Thanos']
intel_dict = {}

for element in sh_list:
    for el in resp.json():
        if el['name'] == element:
            intel_dict[element] = el['powerstats'].get('intelligence','')

print(f'Самый умный супергерой из списка: {max(intel_dict, key = intel_dict.get)}')

