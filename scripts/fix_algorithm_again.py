with open('./data/restaurants.new.txt', 'w') as f2:
    with open('./data/restaurants.txt') as f:
        for line in f:
            f2.write(f'{line.strip()[:-2]}\n')
