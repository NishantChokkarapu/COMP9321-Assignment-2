import os
import warnings
import pickle
import numpy as np
from sklearn.preprocessing import LabelEncoder
warnings.filterwarnings("ignore", category=DeprecationWarning) 

class Predictor:
    def __init__(self, zip_code, property_type, room_type, guest_count,
                 bed_count):
        self.zip_code = zip_code
        self.property_type = property_type
        self.room_type = room_type
        self.guest_count = guest_count
        self.bed_count = bed_count

    def predict(self):
        #X axis would have columns "property_type","accommodates","beds","room_type","zipcode"
        # need to refer to the values of label encoders for X_test values
        le_property_type = LabelEncoder()
        le_room_type = LabelEncoder()
        le_zipcode = LabelEncoder()
        # The encoding for property_type
        le_property_type.fit(['Aparthotel', 'Apartment', 'Barn', 'Bed and breakfast', 'Boat', 
        'Boutique hotel', 'Bungalow', 'Cabin', 'Camper/RV', 'Campsite', 'Casa particular (Cuba)', 
        'Castle', 'Cave', 'Chalet', 'Condominium', 'Cottage', 'Dome house', 'Earth house', 'Farm stay', 
        'Guest suite', 'Guesthouse', 'Heritage hotel (India)', 'Hostel', 'Hotel', 'House', 
        'Island', 'Loft', 'Minsu (Taiwan)', 'Other', 'Resort', 'Serviced apartment', 
        'Tent', 'Tiny house', 'Tipi', 'Townhouse', 'Train', 'Treehouse', 'Villa', 'Yurt'])
        #encoding for room_type
        le_room_type.fit(['Entire home/apt', 'Hotel room', 'Private room', 'Shared room'])

        #stored model for zip code
        zip_code_file = open('zipcode_encoder.pkl', 'rb')
        le_zipcode = pickle.load(zip_code_file)
        zip_code_file.close()

        filename = 'price_prediction_model.sav'
        with open(filename, 'rb') as file:  
            loaded_model = pickle.load(file)
        #X axis would have columns "property_type","accommodates","beds","room_type","zipcode"
        self.property_type = le_property_type.transform(self.property_type)
        self.room_type = le_room_type.transform(self.room_type)
        self.zip_code = le_zipcode.transform(self.zip_code)
        X_test = [[self.property_type,self.guest_count,self.bed_count,self.room_type,self.zip_code]]
        predicted_result = loaded_model.predict(X_test)
        print(predicted_result)     


