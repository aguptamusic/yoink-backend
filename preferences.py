import numpy as np
import random
import constants

#averaging preferences (for cuisine choose randomly from prefs)
def average_preferences(group):
    cuisine_choice = random.randint(0, len(group) - 1)

    avg_rating = np.average([person[constants.RATING_POS] for person in group])
    avg_price = np.average([person[constants.PRICE_POS] for person in group])
    avg_cuisine = group[cuisine_choice][constants.CUISINE_POS]
    avg_distance = np.average([person[constants.CUISINE_POS] for person in group])

    return [avg_rating, avg_price, avg_cuisine, avg_distance]

# fudge factor numerical features ~just to add some spice to your life~
def fudge_preference(preference):
    fudged_rating = preference[constants.RATING_POS] + random.uniform(-0.1, 0.1)
    fudged_price = preference[constants.PRICE_POS] + random.uniform(-0.1, 0.1)
    fudged_cuisine = preference[constants.CUISINE_POS] #no actual cuisines were fudged in this process
    fudged_distance = preference[constants.DISTANCE_POS] + random.uniform(-0.1, 0.1)

    return [fudged_rating, fudged_price, fudged_cuisine, fudged_distance]

# final merge of all preferences:
def merge_preferences(group):
    return fudge_preference(average_preferences(group)) 