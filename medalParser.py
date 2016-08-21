#Parsing Medal Count - make a function to be called later

def parse():

	from lxml import html
	#parsing library
	import requests
	#gets actual page

	page = requests.get('http://www.nbcolympics.com/medals')
	#gets actual webpage
	tree = html.fromstring(page.content)
	#grabs html from page
	rows = tree.xpath('//div[@class="standings-2016"]//table[@class="grid-table"]//tr')
	#the grid-table table occurs twice, need to specify for the one under the standings-2016 class

	rows.pop(0)
	#Gets rid of table header, which we don't care about

	countryData = {}
	#define superdictionary

	for row in rows:
		cells = row.findall('td')
		countryName = cells[1].text_content().strip()
		#grabs the country name from 2nd cell of each row
		countryData[countryName] = {
			'Golds':cells[2].text_content().strip(),
			'Silvers':cells[3].text_content().strip(),
			'Bronzes':cells[4].text_content().strip(),
		}
		#sets the gold, silver, and bronze amounts into a dictionary
		#from the 3rd, 4th, and 5th cell of each row, setting it to the country name
	return countryData