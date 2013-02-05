from googlemaps import GoogleMaps
import re
gmaps = GoogleMaps()
def remove_html_tags(data):
	p = re.compile(r'<.*?>')
	return p.sub('', data)
print "Wybierz odpowiednia opcje."
print "1. Pokaz trase"
print "2. Pokaz w poblizu..."
print "3. Pokaz trase do sprecyzowanego celu."
wybor = input()
cel = ""
if wybor == 1:
	try:
		address1 = raw_input('Podaj nazwe miejscowosci startowej: ')
		address2 = raw_input('Podaj nazwe miejscowosci koncowej: ')
		if address1 == "" or address2 == "":
			print ""
			print "Prosze podac poprawne nazwy miejscowosci"
		else:
			print ""
			check = ""
			directions = gmaps.directions(address1,address2)
			print "Dystans: ",
			print float(directions['Directions']['Distance']['meters'])/1000, 'kilometrow'
			print ""
			print "Trasa: "
			for steps in directions['Directions']['Routes'][0]['Steps']:
				check = steps['descriptionHtml']
				check = remove_html_tags(check)
				print check
	except:
	    print "Wystapil nieznany blad! Przepraszamy."
elif wybor == 2:
	try:
		cel1 = raw_input('Czego poszukujesz?: ')
		address3 = raw_input('W jakiej okolicy?: ')
		if address3 == "" or cel1 == "":
			print ""
			print "Prosze podac poprawne nazwy miejscowosci i punkty docelowe."
		else:
			lat3, lng3 = gmaps.address_to_latlng(cel1 + ' ' + address3)
			lat6, lng6 = gmaps.address_to_latlng(address3)
			miejsce = gmaps.latlng_to_address(lat6, lng6)
			destination3 = gmaps.latlng_to_address(lat3, lng3)
			local = gmaps.local_search(cel1 + ' ' + address3)
			print local['responseData']['results'][0]['titleNoFormatting']
			if miejsce != destination3:
				print destination3
			else:
				pass
	except:
		print "Wystapil nieznany blad! Przepraszamy."
elif wybor == 3:
	try:
		address4 = raw_input('Podaj nazwe miejscowosci startowej: ')
		cel2 = raw_input('Czego poszukujesz?: ')
		address5 = raw_input('Podaj miejscowosc, w ktorej szukac: ')
		if address4 == "" or address5 == "" or cel2 == "":
			print ""
			print "Prosze podac poprawne nazwy miejscowosci i punkty docelowe."
		else:
			lat5, lng5 = gmaps.address_to_latlng(cel2 + ' ' + address5)
			destination5 = gmaps.latlng_to_address(lat5, lng5)
			lat7, lng7 = gmaps.address_to_latlng(address5)
			miejsce2 = gmaps.latlng_to_address(lat7, lng7)
			local = gmaps.local_search(cel2 + ' ' + address5)
			if miejsce2 == destination5:
				directions = gmaps.directions(address4,address5)
				print "prowadze do: " + local['responseData']['results'][0]['titleNoFormatting'],
			else:
				directions = gmaps.directions(address4,cel2 + ' ' + address5)
				print "prowadze do: " + local['responseData']['results'][0]['titleNoFormatting'],
				print destination5
			print ""
			print "Trasa: "
			for steps in directions['Directions']['Routes'][0]['Steps']:
				check2 = steps['descriptionHtml']
				check2 = remove_html_tags(check2)
				print check2
			if miejsce2 == destination5:
				print "Niestety, nasz program nie poprowadzi Cie dalej."
			else:
				print "Dotarles na miejsce!"
	except:
	    print "Wystapil nieznany blad! Przepraszamy."

elif wybor != 1 or wybor != 2 or wybor != 3 or wybor == "":
	print "Zly wybor"
