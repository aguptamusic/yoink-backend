import numpy as np
import centroids
import constants

#get distance from any restaurant's candidate vector to recomended vector based on preferences
def objective(candidate, preference):
    displacement = []
    for i in range(len(preference)):
        displacement.append((float(candidate[i + 1]) - preference[i]) * constants.MODIFIERS[i]) #appends displacement vectors for each candidate

    #return lengts of displacement vectors == distances
    return np.linalg.norm(displacement)

#find index of vector with smallest distance
def make_recommendation(recomendee):
    centroids_distance = [objective(candidate, recomendee) for candidate in centroids.all_centroids]

    nearest_neighbor_index = np.argmin(centroids_distance)
    nearest_neighbor = centroids.all_centroids[nearest_neighbor_index]
    floated_nearest_neighbor = [float(entry) for entry in nearest_neighbor[1:]]
    return [nearest_neighbor[0]] + floated_nearest_neighbor #list with recc. restaurant and info

#average of all the correlation coefficients 
def compute_similarity(preferences, recommendation):
    return np.average([(abs(np.dot(preference, recommendation)) / (np.linalg.norm(preference) * np.linalg.norm(recommendation)) ) for preference in preferences])

