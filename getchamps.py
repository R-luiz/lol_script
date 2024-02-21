
from riotwatcher import LolWatcher, ApiError
import pandas as pd

api_key = 'RGAPI-cc2c44f9-7c0b-43a0-b106-52c196bc6d77'
watcher = LolWatcher(api_key)
my_region = 'euw1'

me = watcher.summoner.by_name(my_region, 'Dazh')
summoner_id = me['id']
my_ranked_stats = watcher.league.by_summoner(my_region, summoner_id)
# print(my_ranked_stats)
my_matches = watcher.match.matchlist_by_puuid('euw1', me['puuid'])
match_detail = watcher.match.by_id('euw1', my_matches[0])
# for row, i in enumerate(match_detail['metadata']['participants'], 0):
# 	print(row, i)
# print(match_detail)
participants = []
for i, key in enumerate(match_detail['info']['participants'], 0):
    # for k, v in key.items():
    #     print(k, end='; ')
    # print()
	print(key['role'], key['lane'], ':', key['summonerName'], '--->', key['championName'])
	if i == 4:
		print('-------------------')
 

# for i, row in enumerate(match_detail, 0):
# 	participants_row = {}
# 	participants.append(participants_row)
# for row in participants:
# 	print(row['champion'])