import json
from flask import *
import pandas as pd
import numpy as np

app = Flask(__name__)

def disease_prediction(Symptom1, Symptom2, Symptom3, Symptom4, Symptom5):
    # Import necessary libraries
    from sklearn.naive_bayes import MultinomialNB
    from sklearn.metrics import accuracy_score
    import pandas as pd
    import numpy as np

    # Load the dataset and other necessary data
    with open('data/symptoms.json', 'r') as json_file:
        dataset = json.load(json_file)
    l1 = dataset.get("name", [])

    # Load the testing data
    tr = pd.read_csv("data/Testing.csv")

    # Load the prognosis data
    with open('data/prognosis.json', 'r') as json_file:
        dataset = json.load(json_file)
    prog = {key: int(value) for key, value in dataset.get("prognosis", {}).items()}
    prognosis = {"prognosis": prog}
    tr.replace(prognosis, inplace=True)

    X_test = tr[l1]

    # Load the training data
    df = pd.read_csv("data/Training.csv")
    df.replace(prognosis, inplace=True)

    X = df[l1]

    y = df[["prognosis"]]
    np.ravel(y)

    # Initialize and fit the Naive Bayes model
    gnb = MultinomialNB()
    gnb = gnb.fit(X, np.ravel(y))

    # Predict the disease based on user input symptoms
    psymptoms = [Symptom1, Symptom2, Symptom3, Symptom4, Symptom5]

    l2 = [0] * len(l1)

    for k in range(0, len(l1)):
        for z in psymptoms:
            if z == l1[k]:
                l2[k] = 1

    inputtest = [l2]
    predicted = gnb.predict(inputtest)[0]

    with open('data/disease_name.json', 'r') as json_file:
        dataset = json.load(json_file)

    diseases = dataset.get("disease",[])

    # Define suggested doctors for each disease
    suggested_doctors = {
        "Fungal infection": "Dr. Nidhi jindal\nProfile link: https://www.practo.com/kolkata/doctor/dr-nidhi-jindal-dermatologist?practice_id=1319383&specialization=Dermatologist&referrer=doctor_listing",
        "Allergy": "Dr. Reeja Mariam George\nProfile link: https://www.practo.com/kolkata/doctor/dr-reeja-mariam-george-general-physician?practice_id=1263361&specialization=Dermatologist&referrer=doctor_listing",
        "GERD": "Dr. Vijay Kumar Rai\n https://www.practo.com/kolkata/doctor/dr-vijay-kumar-rai-gastroenterologist?practice_id=1370187&specialization=Gastroenterologist&referrer=doctor_listing",
        "Chronic cholestasis": "Dr. Debottam Bandyopadhyay\nProfile link: https://www.practo.com/kolkata/doctor/debottam-bandyopadhyay-gastroenterologist?practice_id=1033173&specialization=Gastroenterologist&referrer=doctor_listing",
        "Drug Reaction": "Dr. Saibal Moitra\nProfile link: https://www.practo.com/kolkata/doctor/dr-saibal-moitra-allergist-immunologist?practice_id=741280&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax",
        "Peptic ulcer diseae": "Dr. Gautam Das\nProfile link: https://www.practo.com/kolkata/doctor/dr-gautam-das-gastroenterologist?practice_id=1033173&specialization=Gastroenterologist&referrer=doctor_listing",
        "AIDS": "Dr. Shyama Prasad Roy\nProfile link: https://www.practo.com/kolkata/doctor/dr-shyama-prasad-roy-general-physician1?practice_id=702842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax",
        # Add more diseases and suggested doctors here...
    }

    # Get the predicted disease and suggested doctor
    predicted_disease = diseases[predicted]
    suggested_doctor = suggested_doctors.get(predicted_disease, "Doctor information not available")

    return predicted_disease, suggested_doctor



@app.route('/')
def home():
    return render_template('home.html')

@app.route('/symptoms', methods=['GET', 'POST'])
def symptoms():
    if request.method == 'POST':
        disease = request.form['disease']
        with open('data/disease_data.json', 'r') as json_file:
            disease_symptoms = json.load(json_file)
        if disease in disease_symptoms:
            symptoms = disease_symptoms[disease]
        else:
            symptoms = ["Disease not found."]
        return render_template('symptoms.html', symptoms=symptoms)

    return render_template('symptoms.html', symptoms=None)

@app.route('/get_suggestions')
def get_suggestions():
    query = request.args.get('query')

    # Replace this with your logic to fetch suggestions based on the query
    # For demonstration purposes, we'll return a list of dummy suggestions
    # suggestions = ['Disease A', 'Disease B', 'Disease C']
    with open('data/disease_data.json', 'r') as json_file:
        disease_symptoms = json.load(json_file)
    suggestions = sorted(list(disease_symptoms.keys()))
    filtered_suggestions = [suggestion for suggestion in suggestions if query.lower() in suggestion.lower()]
    return jsonify(filtered_suggestions)


#---------------------------------------------------------------------->

@app.route('/disease')
def disease():
    return render_template('disease.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        # Retrieve user inputs from the form
        symptom1 = request.form.get('symptom1')
        symptom2 = request.form.get('symptom2')
        symptom3 = request.form.get('symptom3')
        symptom4 = request.form.get('symptom4')
        symptom5 = request.form.get('symptom5')

        # Call your prediction function (disease) with user inputs
        # Replace this with your actual prediction logic
        predicted_disease, suggested_doctor = disease_prediction(symptom1, symptom2, symptom3, symptom4, symptom5)

        # Render the results.html template with prediction results
        return render_template('results.html', disease=predicted_disease, doctor=suggested_doctor)

#---------------------------------------------------------------------->

import tkinter as tk
from tkinter import messagebox
import csv
import math
from geopy.geocoders import Nominatim
from flask import Flask, render_template, request

# Global data list to store donor information
data = []

# Function to read data from CSV
def read_data_from_csv():
    global data
    data = []
    with open('data/bloodbank.csv', 'r') as file:
        reader = csv.reader(file)
        next(reader)  # Skip the header row
        for row in reader:
            data.append(row)

# Function to write data to CSV
def write_data_to_csv():
    with open('data/bloodbank.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Name', 'Blood Group', 'Phone', 'BloodBank Name', 'Longitude', 'Latitude'])
        writer.writerows(data)

# Function to add a donor
def add_donor(name, blood_group, phone, bloodbank_name, longitude, latitude):
    data.append([name, blood_group, phone, bloodbank_name, longitude, latitude])
    write_data_to_csv()
    # data.append([name, blood_group, phone, bloodbank_name, longitude, latitude])
    # write_data_to_csv()
    # messagebox.showinfo('Success', 'Donor added successfully.')

# Function to search donors by blood group
def search_donor_by_blood_group(blood_group):
    matching_donors = [donor for donor in data if donor[1] == blood_group]
    return matching_donors

@app.route('/bloodbank')
def bloodbank():
    return render_template('bloodbank.html')

@app.route('/add_donor', methods=['GET', 'POST'])
def add_donor_route():
    bloodbank_names= sorted(["PEERLESS HOSPITAL","SSKM HOSPITAL BLOOD BANK","FORTIS HOSPITALS LIMITED BLOOD BANK","SOUTH EAST KOLKATA MANAB KALYAN","RUBY GENERAL HOSPITAL","LIONS BLOOD BANK","IBTM&IH","OM BLOOD BANK KOLKATA","LIFE CARE BLOOD BANK","BHORUKA BLOOD BANK","PEOPLE'S BLOODBANK"])
    bloodbanks=[
        {"name": "PEERLESS HOSPITAL", "longitude": "88.3939707", "latitude": "22.4810427"},
        {"name": "FORTIS HOSPITALS LIMITED BLOOD BANK", "longitude": "88.3990948", "latitude": "22.5181021"},
        {"name": "SOUTH EAST KOLKATA MANAB KALYAN", "longitude": "88.391084", "latitude": "22.5256993"},
        {"name": "RUBY GENERAL HOSPITAL", "longitude": "88.402884", "latitude": "22.5131759"},
        {"name": "LIONS BLOOD BANK", "longitude": "88.2869754", "latitude": "22.5010317"},
        {"name": "IBTM&IH", "longitude": "88.3751871", "latitude": "22.5854362"},
        {"name": "OM BLOOD BANK KOLKATA", "longitude": "88.3794252", "latitude": "22.5638132"},
        {"name": "LIFE CARE BLOOD BANK", "longitude": "88.370838", "latitude": "22.5498049"},
        {"name": "BHORUKA BLOOD BANK", "longitude": "88.3571161", "latitude": "22.5550749"},
        {"name": "PEOPLE'S BLOODBANK", "longitude": "88.3462425", "latitude": "22.5257451"},
        {"name": "SSKM HOSPITAL BLOOD BANK", "longitude": "88.3437482", "latitude": "22.5402242"}
    ]
    # Get form data
    if request.method == 'GET':
        # Render the add_donor.html template for GET requests
        return render_template('add_donor.html', bloodbank_names=bloodbank_names, bloodbanks=bloodbanks)
    
    name = request.form.get('name')
    blood_group = request.form.get('blood_group')
    phone = request.form.get('phone')
    bloodbank_name = request.form.get('bloodbank_name')
    longitude = request.form.get('longitude')
    latitude = request.form.get('latitude')

    # Check if all required fields are filled out (you can add more validation)
    if not name or not blood_group or not phone or not bloodbank_name or not longitude or not latitude:
        # Handle the error appropriately, e.g., by rendering an error page
        return render_template('error.html', message='All fields are required.')

    # Assuming you have a function 'add_donor' to add donor data to your system
    add_donor(name, blood_group, phone, bloodbank_name, longitude, latitude)

    # Redirect to a success page after adding the donor
    return redirect(url_for('success'))

@app.route('/success')
def success():
    return render_template('success.html')


@app.route('/search_donor', methods=['GET', 'POST'])
def search_donor_route():
    if request.method == 'POST':
        blood_group = request.form['blood_group']
        
        # Get user's location
        user_location = request.form['location']

        # Geocode the location
        geolocator = Nominatim(user_agent="MyApp")
        location = geolocator.geocode(user_location)

        if location:
            user_lat = location.latitude
            user_lon = location.longitude
            matching_donors = search_donor_by_blood_group(blood_group)
            bloodbanks = {}

            # Group donors by bloodbank
            for donor in matching_donors:
                bloodbank_name = donor[3]
                if bloodbank_name not in bloodbanks:
                    bloodbanks[bloodbank_name] = {'distance': None, 'donors': []}
                bloodbanks[bloodbank_name]['donors'].append(donor)

            # Calculate distances and store bloodbank info
            for bloodbank_name, bloodbank_info in bloodbanks.items():
                bloodbank_lat = float(bloodbank_info['donors'][0][5])
                bloodbank_lon = float(bloodbank_info['donors'][0][4])
                distance = haversine(user_lat, user_lon, bloodbank_lat, bloodbank_lon)
                bloodbank_info['distance'] = distance

            # Sort bloodbanks by distance
            sorted_bloodbanks = sorted(bloodbanks.items(), key=lambda x: x[1]['distance'])
            
            return render_template('bb_results.html', bloodbanks=sorted_bloodbanks)
        else:
            return render_template('location_not_found.html')
    else:
        return render_template('search.html')

# Function to calculate haversine distance
def haversine(lat1, lon1, lat2, lon2):
    R = 6371.0  # Earth's radius in kilometers

    lat1 = math.radians(lat1)
    lon1 = math.radians(lon1)
    lat2 = math.radians(lat2)
    lon2 = math.radians(lon2)

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    distance = R * c
    return distance

if __name__ == '__main__':
    read_data_from_csv()
    app.run(debug=True)
