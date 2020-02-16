import requests
import urllib.parse
import time

#constants
API_KEY = "<api-key>"
LAT = '37.427802' # location of huang
LONG = '-122.174318'

search_queries = []
num_restuarants = 147

#compute distance based on place_id
def compute_distance(place_id):
    opts = {
        'key': API_KEY,
        'origins': f'{LAT},{LONG}',
        'destinations': f'place_id:{place_id}'
    }

    opts_string = urllib.parse.urlencode(opts)
    req = requests.get(f'https://maps.googleapis.com/maps/api/distancematrix/json?{opts_string}')
    res = req.json()

    first_element = res['rows'][0]['elements'][0]
    if first_element['status'] == 'ZERO_RESULTS' or 'distance' not in first_element:
        return -1

    return first_element['distance']['value'] / 1000

#Get all of the resturant cuisines to search for
with open("./data/cuisines.weighted.txt") as f:
    for line in f:
        search_queries.append((line.split("||")[0], float(line.split("||")[1])))

with open('./data/restaurants.new.txt', 'w') as data_file:
    #Get restaurants for each cuisine
    for search in search_queries:
        print(f'new cuisine: {search[0]}')
        radius = '5000'


        #dictionary with argument list for function
        search_req_opts = {
            'key': API_KEY,
            'query': search[0], #search for cuisine
            'location': f'{LAT},{LONG}',
            'radius': radius
        }

        #make it into URL format for API
        search_req_opts_string = urllib.parse.urlencode(search_req_opts)

        #put it at the end as argument
        search_req = requests.get(f'https://maps.googleapis.com/maps/api/place/textsearch/json?{search_req_opts_string}')

        #gets the response data (reads in as dictionary)
        search_req_response = search_req.json()
        len_results = len(search_req_response['results'])
        print(f'\tNumber of results here: {len_results}')

        #print results
        for result in search_req_response['results']:
            if 'permanently_closed' not in result:
                place_id = result['place_id']


                name = result['name']
                rating = result['rating'] / 5
                price = result.get('price_level', 2) / 4
                cuisine = search[1]

                distance = compute_distance(place_id)

                if distance != -1 and distance < 50:
                    restaurant_save_data = '||'.join((name, str(rating), str(price), str(cuisine), str(distance / 50)))
                    data_file.write(f'{restaurant_save_data}\n')