num_restuarants = 265
with open("./data/cuisines.weighted.txt", 'w') as f2:
    with open("./data/cuisines.txt") as f:
        counter = 1

        for line in f:
            if line.strip() != "Nothing":
                f2.write("||".join((f'{line.strip().lower()} restuarants', str(round(counter / num_restuarants, 8))))  + "\n")

            counter += 1