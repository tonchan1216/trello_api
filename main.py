import requests
import json

key = '595475346a2314ee8314c0b991620aa6'
token = 'f1b84cd3a50cd2fe4942bbb641407245b4c7f5914e63315e5ea5c7ba3b97c915'

def get_bord(n):
	payload = {'key': key, 'token': token, 'fields':'name'}
	url = "https://trello.com/1/members/tohnfurutani/boards"
	r = requests.get(url, params=payload)
	result = r.content.decode('utf-8')
	j = json.loads(result)
	return j[n]['id']

def get_card_ids(b_id,fil):
	payload = {'key': key, 'token': token, 'filter':fil}
	url = "https://trello.com/1/boards/"+b_id+"/cards"
	r = requests.get(url, params=payload)
	result = r.content.decode('utf-8')
	cards = json.loads(result)

	for x in cards:
		print(x['dateLastActivity'], end=" ")
		print(x['name'], end=" ")
		try:
			budget = get_custom_field(x['id'])['gABMV2K7-xLnqwE']
		except KeyError:
			budget = 'Unknown'
		print(budget, end="")
		print(x['shortUrl'], end=" ")
		print()
	return 0

def get_custom_field(card_id):
	url = "https://trello.com/1/cards/" + card_id + "/pluginData"
	payload = {'key': key, 'token': token}
	r = requests.get(url, params=payload)
	result = r.content.decode('utf-8')
	j = json.loads(result)
	if len(j) != 0:
		data = json.loads(j[0]['value'])
		return data['fields']
	else:
		return {}

keiri_id = get_bord(11)
t = get_card_ids(keiri_id, 'all')

# for i in t:
# 	print(get_custom_field(i))


