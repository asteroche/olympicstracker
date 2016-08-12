#Scoring function

import medalParser

players = [
		{'name': 'Tyler', 'Golds':'Brazil', 'Silvers':'Kazakhstan', 'Bronzes':'Colombia', 'Score':0}, 
		{'name': 'Anna', 'Golds':'Spain', 'Silvers':'Ethiopia', 'Bronzes':'Czech Republic', 'Score':0},
		{'name': 'Nelson', 'Golds':'North Korea', 'Silvers':'Poland', 'Bronzes':'Canada', 'Score':0},
		{'name': 'Daniel', 'Golds':'Netherlands', 'Silvers':'Azerbaijan', 'Bronzes':'Romania', 'Score':0},
		{'name': 'Nick', 'Golds':'Ukraine', 'Silvers':'Belarus', 'Bronzes':'Danmark', 'Score':0}, 
		{'name': 'Matt', 'Golds':'New Zealand', 'Silvers':'Cuba', 'Bronzes':'Mexico', 'Score':0},
		{'name': 'Jess', 'Golds':'Hungary', 'Silvers':'Jamaica', 'Bronzes':'Sweden', 'Score':0},
		{'name': 'James', 'Golds':'Iran', 'Silvers':'Kenya', 'Bronzes':'Ireland', 'Score':0}]
		#defines the teams that players picked

def getPlayers():

	return players

def updateScore():

	countryData = medalParser.parse()

	for player in players:

		defaultValue = {'Golds': 0, 'Silvers': 0, 'Bronzes': 0}

		goldScore = int(countryData.get(player['Golds'], defaultValue)['Golds'])
		silverScore = int(countryData.get(player['Silvers'], defaultValue)['Silvers'])
		bronzeScore = int(countryData.get(player['Bronzes'], defaultValue)['Bronzes'])
##have kyle explain this later
		player['Score'] = goldScore + silverScore + bronzeScore