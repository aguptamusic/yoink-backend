import numpy

all_distances = []
all_centroids = []
with open('./data/restaurants.txt') as f:
    for line in f:
        distance = float(line.split('||')[4].strip())
        if distance < 50:
            all_centroids.append([entry.strip() for entry in line.split('||')])
            all_distances.append(distance)


print(all_distances)
max_distance = numpy.max(all_distances)

print("max_distance = ", max_distance)

with open('./data/restaurants.new.txt', 'w') as f:
    for centroid in all_centroids:
        centroid[1] = float(centroid[1]) / 5
        centroid[2] = float(centroid[2]) / 4
        centroid[4] = float(centroid[4]) / max_distance
        f.write('||'.join((centroid[0], str(centroid[1]), str(centroid[2]), str(centroid[3]), str(centroid[4]), '\n')))

