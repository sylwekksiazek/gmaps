from googlemaps import GoogleMaps
import re
gmaps = GoogleMaps()
def remove_html_tags(data):
    p = re.compile(r'<.*?>')
	return p.sub('', data)
print "Wybierz odpowiednia opcje."
print "1. Pokaz trase"
print "2. Pokaz w poblizu..."
wybor = input()
cel = ""
if wybor == 1:
	address1 = raw_input('Podaj nazwe miejscowosci startowej: ')
	address2 = raw_input('Podaj nazwe miejscowosci koncowej: ')
	print ""
	lat1, lng1 = gmaps.address_to_latlng(address1)
	lat2, lng2 = gmaps.address_to_latlng(address2)
	check = ""
	#print lat1, lng1
	#print lat2, lng2
	try:
		destination1 = gmaps.latlng_to_address(lat1, lng1)
		destination2 = gmaps.latlng_to_address(lat2, lng2)
		#print destination1
		#print destination2
		directions = gmaps.directions(address1,address2)
		print "Dystans: ",
		print float(directions['Directions']['Distance']['meters'])/1000, 'kilometrow'
		print ""
		print "Trasa: "
		for steps in directions['Directions']['Routes'][0]['Steps']:
			check = steps['descriptionHtml']
			check = remove_html_tags(check)
			print check
	except ValueError:
	    print "Wystapil nieznany blad! Przepraszamy."
elif wybor == 2:
	cel = raw_input('Czego poszukujesz?: ')
	address3 = raw_input('W jakiej okolicy?: ')
	local = gmaps.local_search(cel + ' ' + address3)
	print local['responseData']['results'][0]['titleNoFormatting']
else:
	print "Zly wybor"
