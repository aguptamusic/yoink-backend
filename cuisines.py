import constants
cuisines_dict = {} #dictionary

with open("./data/cuisines.weighted.txt") as f:
    for line in f:
        cuisine = line.strip().lower().split("||")[0][:-12]
        cuisine_score = float(line.strip().lower().split("||")[1])
        cuisines_dict[cuisine] = cuisine_score


