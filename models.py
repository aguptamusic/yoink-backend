class PreferenceModel:
    def __init__(self, name, price, cuisine, distance, rating):
        self.name = name
        self.price = price
        self.cuisine = cuisine
        self.distance = distance
        self.rating = rating

    @staticmethod
    def from_dict(source):
        return PreferenceModel(source['name'], source['price'], source['cuisine'], source['distance'], source['rating'])

    def to_dict(self):
        return {
            'name': self.name,
            'price': self.price,
            'cuisine': self.cuisine,
            'distance': self.distance,
            'rating': self.rating
        }
    
    def __repr__(self):
        return('PreferenceModel(name={}, price={}, cuisine={}, distance={}, rating={}').format(self.name, self.price, self.cuisine, self.distance, self.rating)