import numpy as np
import random
import string
import firebase_admin
from flask import Flask
from flask import request
from firebase_admin import firestore

import constants
import utilities
import preferences
import recommendation
import cuisines
from models import PreferenceModel
from database import db

app = Flask(__name__)

#Okay, here we go:
@app.route('/')
def ping():    
    return 'pong'

#Creates the dinner session with a code
@app.route('/dinners/new')
def create_dinner_session():
    dinner_code = utilities.generate_dinner_code(6)
    db.collection('dinner_sessions').document(dinner_code).set({
        'preferences': []
    })

    return {
        'status': 'OK',
        'result': {
            'dinner_code': dinner_code
        }
    }

#creates dictionary mapping features to corresponding values for every user
@app.route('/dinners/<string:dinner_code>/preferences', methods=['POST'])
def record_user_preference(dinner_code):
    if len(dinner_code) != 6:
        return {
            'status': 'ERROR',
            'message': 'Dinner code not correct length (6)!'
        }

    preference = PreferenceModel(
        request.args.get('name', 'Person'),
        float(request.args.get('price','0')) / 4,
        utilities.convert_pretty_cuisine(request.args.get('cuisine', '')),
        utilities.convert_pretty_distance(request.args.get('distance', '')),
        float(request.args.get('rating', '0')) / 5
    )

    doc_ref = db.collection('dinner_sessions').document(dinner_code)
    doc_ref.update({'preferences': firestore.ArrayUnion([preference.to_dict()])})
    
    return {
        'status': 'OK',
        'result': preference.to_dict()
    }

#gets preferences from every user
@app.route('/dinners/<string:dinner_code>/preferences', methods=['GET'])
def get_user_perferences(dinner_code):
    if len(dinner_code) != 6:
        return {
            'status': 'ERROR',
            'message': 'Dinner code not correct length (6)!'
        }

    dinner_code_preferences =  db.collection('dinner_sessions').document(dinner_code).get().to_dict()['preferences']
    return {
        'status': 'OK',
        'result': dinner_code_preferences
    }

#makes recommendation
@app.route('/dinners/<string:dinner_code>/recommend', methods=['GET'])
def get_recommendation(dinner_code):    
    if len(dinner_code) != 6:
        return {
            'status': 'ERROR',
            'message': 'Dinner code not correct length (6)!'
        }

    # get matching preferences
    dinner_code_preferences =  db.collection('dinner_sessions').document(dinner_code).get().to_dict()['preferences']
    if len(dinner_code_preferences) == 0:
        return {
            'status': 'ERROR',
            'message': 'There are no preferences saved for this dinner code!'
        }

    # vectorize and merge 
    preferences_vectors = list(map(lambda x: [x['rating'], x['price'], x['cuisine'], x['distance']], dinner_code_preferences))
    print(preferences_vectors)
    merged_preference = preferences.merge_preferences(preferences_vectors)
    rec = recommendation.make_recommendation(merged_preference)
    similarity = recommendation.compute_similarity(preferences_vectors, rec[1:])

    # make recommendation
    return {
        'status': 'OK',
        'result': {
            'resturant_name': rec[0],
            'similarity': round(similarity, 4)
        }
    }

#basics
if __name__ == '__main__':
    app.run()