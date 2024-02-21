import requests

# Replace 'YOUR_API_KEY_HERE' with your actual Riot Games API key
api_key = 'RGAPI-8eda4b4b-2eb5-4180-8923-af231b3b4e50'

# Replace 'SUMMONER_NAME' with the summoner name you're interested in
summoner_name = 'R0b1L'
X_Riot_Edge_Trace_Id = "c24bc2fa-8c69-4951-ac90-894fa47fff13"
# URL for getting summoner details (replace 'na1' with the appropriate server region code if different)
summoner_url = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/EUW?api_key={api_key}'
# Make a request to get summoner details
summoner_response = requests.get(summoner_url)
# Check if the request was successful
if summoner_response.status_code == 200:
	summoner_data = summoner_response.json()
	summoner_id = summoner_data['puuid']
	
	# URL for getting match history (replace 'na1' with your server region code if different)
	match_history_url = f'https://europe.api.riotgames.com/riot/account/v1/accounts/by-riot-id/{summoner_name}/EUW?api_key={api_key}'
	
	# Make a request to get match history
	match_history_response = requests.get(match_history_url)
	
	if match_history_response.status_code == 200:
		match_history_data = match_history_response.json()
		# Process your match history data here
		print(match_history_data)
	else:
		print("Failed to retrieve match history.")
	
else:
	print("Failed to retrieve summoner details.")

def get_active_items_ranked_by_cost():
	# URL to fetch the latest version of the game
	versions_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
	versions_response = requests.get(versions_url)
	latest_version = versions_response.json()[0]

	# URL to fetch items data
	items_url = f'https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/item.json'
	items_response = requests.get(items_url)
	items_data = items_response.json()['data']

	# Extract items and their costs
	active_items_with_cost = []
	for item_id, item_info in items_data.items():
		# Check for fields that might indicate the item is active; this might need adjustments
		if 'gold' in item_info and item_info['gold']['total'] > 0 and not item_info.get('into') and 'maps' in item_info and item_info['maps']['11']:
			cost = item_info['gold']['total']
			name = item_info['name']
			active_items_with_cost.append((name, cost, item_id))

	# Rank items by cost
	ranked_active_items = sorted(active_items_with_cost, key=lambda x: x[1], reverse=True)

	# Print ranked list of active items
	for name, cost, item_id in ranked_active_items:
		print(f"{name} (ID: {item_id}) - Cost: {cost}")

# Call the function
import requests

def get_item_stats():
	# Fetch the latest version of the game
	versions_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
	versions_response = requests.get(versions_url)
	latest_version = versions_response.json()[0]

	# Fetch items data for the latest version
	items_url = f'https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/item.json'
	items_response = requests.get(items_url)
	items_data = items_response.json()['data']

	# Loop through each item and print its name and stats
	for item_id, item_info in items_data.items():
		if 'from' not in item_info and 'requiredChampion' not in item_info:
			name = item_info.get('name', 'No Name')
			stats = item_info.get('stats', {})
			print(f"Item Name: {name}")
			print("Stats:")
			for stat, value in stats.items():
				print(f"  {stat}: {value}")
			
			print("")

# Execute the function

def display_champion_stats_and_spells(champion_name, cdr=0.0):
    # Fetch the latest game version
    versions_url = 'https://ddragon.leagueoflegends.com/api/versions.json'
    versions_response = requests.get(versions_url)
    latest_version = versions_response.json()[0]

    # Normalize champion name for URL
    champion_name_normalized = champion_name.replace(" ", "").capitalize()

    # Construct the URL to fetch the specific champion's data
    champion_url = f'https://ddragon.leagueoflegends.com/cdn/{latest_version}/data/en_US/champion/{champion_name_normalized}.json'
    
    # Make the request to get the champion's data
    response = requests.get(champion_url)
    if response.status_code == 200:
        champion_data = response.json()['data'][champion_name_normalized]
        
        # Display the champion's base stats
        print(f"Base Stats for {champion_name}:")
        for stat, value in champion_data['stats'].items():
            print(f"  {stat}: {value}")
        print("\nSpells:")

        # Display the stats for each spell, adjusting for CDR
        for spell in champion_data['spells']:
            print(f"\n{spell['name']}")
            # Calculate and display actual cooldown considering CDR
            cooldowns_with_cdr = [round(cd * (1 - (1-1/(1+cdr/100))), 1) for cd in spell['cooldown']]
            print(f"Cooldown (with {int(cdr)} CDR):", "/".join(map(str, cooldowns_with_cdr)))
            # Print Cooldown without CDR
            print("Cooldown (without CDR):", "/".join(map(str, spell['cooldown'])))
            print("Cost:", "/".join(map(str, spell['cost'])))
            if 'vars' in spell:  # Some spells may include scaling information in vars
                for var in spell['vars']:
                    print(f"  {var['key']}: {var['coeff']} (based on {var['link']})")
    else:
        print(f"Failed to retrieve data for {champion_name}. Please check the champion name and try again.")

# Example usage

while True:
    champion_name = input("name: ")
    cdr = float(input("cdr : "))
    display_champion_stats_and_spells(champion_name, cdr)
