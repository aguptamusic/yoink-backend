import numpy as np

# Load in all of the restauarants into a list of vectors
centroids = []
with open('restaurants.txt') as restaurants_file:
    for serialized_restaurant in restaurants_file:
        centroids.append([entry.strip() for entry in serialized_restaurant.split('||')])

# Temporarliy define recomendee vector
# recomendee = [3.9, 4, 0.4, 40] # Il Pollaio
recomendee = [3.8448502772041944, 1.5431152590346162, 0.194444, 0.4030218301166912]

# Create objective function to state what we want to minimize (distance between potential candidate and recomendee vector)
def objective(candidate, recomendee): 
    displacement = []
    for i in range(len(recomendee)):
        displacement.append(float(candidate[i + 1]) - recomendee[i])

    #return length of displacement vector == distance
    return np.linalg.norm(displacement)

#Look at each distance find the smallest one (return index because ARGmin)
centroids_distance = [objective(candidate, recomendee) for candidate in centroids]
nearest_neighbor_index = np.argmin(centroids_distance)

# Get the restaurant name
print(centroids[nearest_neighbor_index])
