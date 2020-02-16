all_centroids = []
with open('./data/restaurants.txt') as restaurants_file:
        for serialized_restaurant in restaurants_file:
            all_centroids.append([entry.strip() for entry in serialized_restaurant.split('||')])
