import cuisines
import string
import random
import constants

#genearte random 6-digit code for a group 
def generate_dinner_code(size=6):
    chars = string.ascii_letters + string.digits
    code = ''.join(random.choice(chars) for _ in range(size))
    return code.upper()

#convert distance string to number
def convert_pretty_distance(distance_string):
    if distance_string.lower() == 'walking':
        return 1.5 / constants.MAX_DISTANCE
    elif distance_string.lower() == 'biking':
        return 6.0 / constants.MAX_DISTANCE
    elif distance_string.lower() == 'driving':
        return 10.0 / constants.MAX_DISTANCE
    elif 'custom' in distance_string.lower():
        distance_parts = distance_string.split('|')
        return float(distance_parts[1]) / constants.MAX_DISTANCE

    return 10.0 / constants.MAX_DISTANCE

#get numerical value of cuisine from string key
def convert_pretty_cuisine(cuisine_string):
    return cuisines.cuisines_dict.get(cuisine_string.strip().lower(), 0.84259259) # default = mcdonald's ¯\_(ツ)_/¯
