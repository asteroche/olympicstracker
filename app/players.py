#Scoring function

import medalParser

players = [
		{'name': 'Tyler', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'Brazil', 'Silvers':'Kazakhstan', 'Bronzes':'Colombia', 'Score':0}, 
		{'name': 'Anna', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'Spain', 'Silvers':'Ethiopia', 'Bronzes':'Czech Republic', 'Score':0},
		{'name': 'Nelson', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'North Korea', 'Silvers':'Poland', 'Bronzes':'Canada', 'Score':0},
		{'name': 'Daniel', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'Netherlands', 'Silvers':'Azerbaijan', 'Bronzes':'Romania', 'Score':0},
		{'name': 'Nick', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'Ukraine', 'Silvers':'Belarus', 'Bronzes':'Danmark', 'Score':0}, 
		{'name': 'Matt', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'New Zealand', 'Silvers':'Cuba', 'Bronzes':'Mexico', 'Score':0},
		{'name': 'Jess', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'Hungary', 'Silvers':'Jamaica', 'Bronzes':'Sweden', 'Score':0},
		{'name': 'James', 'Goldscore':0, 'Silverscore':0, 'Bronzescore':0, 'Golds':'Iran', 'Silvers':'Kenya', 'Bronzes':'Ireland', 'Score':0}]
		#defines the teams that players picked

def getPlayers():

	return players

def updateScore():

	countryData = medalParser.parse()

	for player in players:

		defaultValue = {'Golds': 0, 'Silvers': 0, 'Bronzes': 0}

		goldScore = int(countryData.get(player['Golds'], defaultValue)['Golds'])
		player['Goldscore']=goldScore
		silverScore = int(countryData.get(player['Silvers'], defaultValue)['Silvers'])
		player['Silverscore']=silverScore
		bronzeScore = int(countryData.get(player['Bronzes'], defaultValue)['Bronzes'])
		player['Bronzescore']=bronzeScore
##have kyle explain this later
		player['Score'] = goldScore + silverScore + bronzeScore