import random
import numpy as np

RATING_POS = 0
PRICE_POS = 1
CUISINE_POS = 2
DISTANCE_POS = 3

person1 = [3.4, 1, 0.194444, 9.572] # Wendy's||3.4||1||0.19444444||9.572
person2 = [3.6, 1, 0.53703704, 23.242] # McDonald's||3.6||1||0.53703704||23.242
person3 = [3.9, 2, 0.62034037, 5.308] # Taqueria Azteca||3.9||2||0.62037037||5.308  Mexican
person4 = [4.2, 2, 0.43518519, 22.223] #Il Fornaio Italian cuisine
person5 = [4.1, 2, 0.02777778, 0.306] #Amber India Argentine
group = [person1, person2, person3, person4, person5]  


def average_preferences(group):
    cuisine_choice = random.randint(0, len(group) - 1)

    avg_rating = np.average([person[RATING_POS] for person in group])
    avg_price = np.average([person[PRICE_POS] for person in group])
    avg_cuisine = group[cuisine_choice][CUISINE_POS]
    avg_distance = np.average([person[CUISINE_POS] for person in group])

    return [avg_rating, avg_price, avg_cuisine, avg_distance]

# fudge factor the rest of the numerical ones ~just to add some spice to your life~
def fudge_preference(preference):
    fudged_rating = preference[RATING_POS] + random.uniform(-0.1, 0.1)
    fudged_price = preference[PRICE_POS] + random.uniform(-0.1, 0.1)
    fudged_cuisine = preference[CUISINE_POS] #no actual cuisines were fudged in this process
    fudged_distance = preference[DISTANCE_POS] + random.uniform(-0.1, 0.1)

    return [fudged_rating, fudged_price, fudged_cuisine, fudged_distance]

# final merge of all preferences:
def merge_preferences(group):
    return fudge_preference(average_preferences(group))

print(merge_preferences(group))