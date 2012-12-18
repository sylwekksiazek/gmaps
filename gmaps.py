from googlemaps import *
gmaps = GoogleMaps()
address1 = raw_input('Podaj nazwe miejscowosci startowej: ')
address2 = raw_input('Podaj nazwe miejscowosci koncowej: ')
lat1, lng1 = gmaps.address_to_latlng(address1)
lat2, lng2 = gmaps.address_to_latlng(address2)
#print lat1, lng1
#print lat2, lng2
try:
    destination1 = gmaps.latlng_to_address(lat1, lng1)
    destination2 = gmaps.latlng_to_address(lat2, lng2)
    print destination1
    print destination2
    directions = gmaps.directions(address1,address2)
    print float(directions['Directions']['Distance']['meters'])/1000, 'kilometrow'
except ValueError:
    print "Wystapil nieznany blad! Przepraszamy."