from tkinter import*
from tkinter import messagebox                           
# import os            
# import webbrowser
import tkinter as tk
import csv
import numpy as np
import pandas as pd
from tkinter import ttk
from PIL import Image, ImageTk


def update_progress():
    global progress_value
    if progress_value < 100:
        progress_value += 10
        progress_bar["value"] = progress_value
        progress_label.config(text=f"Progress: {progress_value}%")
        window.after(500, update_progress)

# Create the Tkinter window
window = tk.Tk()
window.title("Health Care System")

# Load the image
image = Image.open("medical.png")
image = image.resize((1000, 550), Image.ANTIALIAS)  # Adjust the size of the image as needed
photo = ImageTk.PhotoImage(image)

# Create a frame to hold the image and progress bar
frame = ttk.Frame(window)
frame.pack(padx=20, pady=20)

# Create the label to display the image
image_label = ttk.Label(frame, image=photo)
image_label.pack()

# Create the progress bar
progress_value = 0
progress_bar = ttk.Progressbar(frame, orient=tk.HORIZONTAL, length=500, mode='determinate')
progress_bar.pack(pady=10)

# Create the label to display the progress percentage
progress_label = ttk.Label(frame, text="Progress: 0%")
progress_label.pack()

# Start the progress update
window.after(500, update_progress)


def mainproblem():
    root=Tk()
    root.title("Home")
    root.geometry("1000x750+200+50")
    root.resizable(TRUE,TRUE)
    root.configure(bg="#bcf6f5")
    # hc=Label(text="HEALTHCARE SYSTEM",bg="#d8bcf6",fg="black",padx="1000",pady="30",font=("algerian",50),relief="raised",borderwidth=10)
    # hc.pack()
    e = Label(root, text="HEALTHCARE SYSTEM",fg="black",font=("calibri",50),bg="#f6c4fa",padx='1000',pady='10')
    e.pack()
    f1=Frame(root,bg="#bcf6f5")
    f1.pack(side="top")
    l1=Label(f1,text="PLEASE CHOOSE YOUR OPTION......",fg="black",font=("calibri",20),bg="#bcf6f5",padx='1000',pady='10')
    l1.pack(pady=20)


    def disease():
        l1=['itching','skin_rash','nodal_skin_eruptions','continuous_sneezing','shivering','chills','joint_pain',
        'stomach_pain','acidity','ulcers_on_tongue','muscle_wasting','vomiting','burning_micturition','spotting_ urination','fatigue',
        'weight_gain','anxiety','cold_hands_and_feets','mood_swings','weight_loss','restlessness','lethargy','patches_in_throat',
        'irregular_sugar_level','cough','high_fever','sunken_eyes','breathlessness','sweating','dehydration','indigestion',
        'headache','yellowish_skin','dark_urine','nausea','loss_of_appetite','pain_behind_the_eyes','back_pain','constipation',
        'abdominal_pain','diarrhoea','mild_fever','yellow_urine','yellowing_of_eyes','acute_liver_failure','fluid_overload',
        'swelling_of_stomach','swelled_lymph_nodes','malaise','blurred_and_distorted_vision','phlegm','throat_irritation',
        'redness_of_eyes','sinus_pressure','runny_nose','congestion','chest_pain','weakness_in_limbs','fast_heart_rate',
        'pain_during_bowel_movements','pain_in_anal_region','bloody_stool','irritation_in_anus','neck_pain','dizziness','cramps',
        'bruising','obesity','swollen_legs','swollen_blood_vessels','puffy_face_and_eyes','enlarged_thyroid','brittle_nails',
        'swollen_extremeties','excessive_hunger','extra_marital_contacts','drying_and_tingling_lips','slurred_speech','knee_pain','hip_joint_pain',
        'muscle_weakness','stiff_neck','swelling_joints','movement_stiffness','spinning_movements','loss_of_balance','unsteadiness','weakness_of_one_body_side',
        'loss_of_smell','bladder_discomfort','foul_smell_of urine','continuous_feel_of_urine','passage_of_gases','internal_itching','toxic_look_(typhos)',
        'depression','irritability','muscle_pain','altered_sensorium','red_spots_over_body','belly_pain','abnormal_menstruation','dischromic _patches',
        'watering_from_eyes','increased_appetite','polyuria','family_history','mucoid_sputum','rusty_sputum','lack_of_concentration','visual_disturbances',
        'receiving_blood_transfusion','receiving_unsterile_injections','coma','stomach_bleeding','distention_of_abdomen','history_of_alcohol_consumption',
        'fluid_overload','blood_in_sputum','prominent_veins_on_calf','palpitations','painful_walking','pus_filled_pimples','blackheads','scurring','skin_peeling',
        'silver_like_dusting','small_dents_in_nails','inflammatory_nails','blister','red_sore_around_nose','yellow_crust_ooze']

        disease=['Fungal infection','Allergy','GERD','Chronic cholestasis','Drug Reaction',
            'Peptic ulcer diseae','AIDS','Diabetes','Gastroenteritis','Bronchial Asthma','Hypertension',
            ' Migraine','Cervical spondylosis',
            'Paralysis (brain hemorrhage)','Jaundice','Malaria','Chicken pox','Dengue','Typhoid','hepatitis A',
            'Hepatitis B','Hepatitis C','Hepatitis D','Hepatitis E','Alcoholic hepatitis','Tuberculosis',
            'Common Cold','Pneumonia','Dimorphic hemmorhoids(piles)',
            'Heartattack','Varicoseveins','Hypothyroidism','Hyperthyroidism','Hypoglycemia','Osteoarthristis',
            'Arthritis','(vertigo) Paroymsal  Positional Vertigo','Acne','Urinary tract infection','Psoriasis',
            'Impetigo']

        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)

        # TESTING DATA
        tr=pd.read_csv("Testing.csv")
        tr.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        X_test= tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)

        # TRAINING DATA
        df=pd.read_csv("Training.csv")

        df.replace({'prognosis':{'Fungal infection':0,'Allergy':1,'GERD':2,'Chronic cholestasis':3,'Drug Reaction':4,
        'Peptic ulcer diseae':5,'AIDS':6,'Diabetes ':7,'Gastroenteritis':8,'Bronchial Asthma':9,'Hypertension ':10,
        'Migraine':11,'Cervical spondylosis':12,
        'Paralysis (brain hemorrhage)':13,'Jaundice':14,'Malaria':15,'Chicken pox':16,'Dengue':17,'Typhoid':18,'hepatitis A':19,
        'Hepatitis B':20,'Hepatitis C':21,'Hepatitis D':22,'Hepatitis E':23,'Alcoholic hepatitis':24,'Tuberculosis':25,
        'Common Cold':26,'Pneumonia':27,'Dimorphic hemmorhoids(piles)':28,'Heart attack':29,'Varicose veins':30,'Hypothyroidism':31,
        'Hyperthyroidism':32,'Hypoglycemia':33,'Osteoarthristis':34,'Arthritis':35,
        '(vertigo) Paroymsal  Positional Vertigo':36,'Acne':37,'Urinary tract infection':38,'Psoriasis':39,
        'Impetigo':40}},inplace=True)

        X= df[l1]

        y = df[["prognosis"]]
        np.ravel(y)

        def message():
            if (Symptom1.get() == "None" and  Symptom2.get() == "None" and Symptom3.get() == "None" and Symptom4.get() == "None" and Symptom5.get() == "None"):
                messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
            else :
                NaiveBayes()

        def NaiveBayes():
            from sklearn.naive_bayes import MultinomialNB
            gnb = MultinomialNB()
            gnb=gnb.fit(X,np.ravel(y))
            from sklearn.metrics import accuracy_score
            y_pred = gnb.predict(X_test)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))

            psymptoms = [Symptom1.get(),Symptom2.get(),Symptom3.get(),Symptom4.get(),Symptom5.get()]

            for k in range(0,len(l1)):
                for z in psymptoms:
                    if(z==l1[k]):
                        l2[k]=1

            inputtest = [l2]
            predict = gnb.predict(inputtest)
            predicted=predict[0]

            h='no'
            for a in range(0,len(disease)):
                if(disease[predicted] == disease[a]):
                    h='yes'
                    break

            if (h=='yes'):
                t3.delete("1.0", END)
                t3.insert(END, disease[a])
            else:
                t3.delete("1.0", END)
                t3.insert(END, "No Disease")

            if(disease[a]=="Fungal infection"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Nidhi jindal\nProfile link: https://www.practo.com/kolkata/doctor/dr-nidhi-jindal-dermatologist?practice_id=1319383&specialization=Dermatologist&referrer=doctor_listing")
            elif(disease[a]=="Allergy"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Reeja Mariam George\nProfile link: https://www.practo.com/kolkata/doctor/dr-reeja-mariam-george-general-physician?practice_id=1263361&specialization=Dermatologist&referrer=doctor_listing")
            elif(disease[a]=="GERD"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Vijay Kumar Rai\nProfile link: https://www.practo.com/kolkata/doctor/dr-vijay-kumar-rai-gastroenterologist?practice_id=1370187&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Chronic cholestasis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Debottam Bandyopadhyay\nProfile link: https://www.practo.com/kolkata/doctor/debottam-bandyopadhyay-gastroenterologist?practice_id=1033173&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Drug Reaction"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Saibal Moitra\nProfile link: https://www.practo.com/kolkata/doctor/dr-saibal-moitra-allergist-immunologist?practice_id=741280&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Peptic ulcer diseae"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Gautam Das\nProfile link: https://www.practo.com/kolkata/doctor/dr-gautam-das-gastroenterologist?practice_id=1033173&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="AIDS"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Shyama Prasad Roy\nProfile link: https://www.practo.com/kolkata/doctor/dr-shyama-prasad-roy-general-physician1?practice_id=702842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Diabetes "): #***********
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sandip Rungta\nProfile link: https://www.practo.com/kolkata/doctor/dr-sandip-rungta-cardiologist?practice_id=1180689&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Gastroenteritis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Jayanta Paul\nProfile link: https://www.practo.com/kolkata/doctor/dr-jayanta-paul-gastroenterologist-1?practice_id=621621&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Bronchial Asthma"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Shyama Prasad Roy\nProfile link: https://www.practo.com/kolkata/doctor/dr-shyama-prasad-roy-general-physician1?practice_id=702842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Hypertension "):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Bodhisatwa Choudhuri\nProfile link: https://www.practo.com/kolkata/doctor/bodhisatwa-choudhuri-general-physician?practice_id=735842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Migraine"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Milan Chhetri\nProfile link: https://www.practo.com/kolkata/doctor/dr-milan-chhetri-general-physician?practice_id=741280&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Cervical spondylosis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Arindam Rath\nProfile link: https://www.practo.com/kolkata/doctor/dr-arindam-rath-gynecologist-obstetrician-1?practice_id=1316457&specialization=Gynecologist/Obstetrician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Paralysis (brain hemorrhage)"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sadanand Dey\nProfile link: https://www.practo.com/kolkata/doctor/sadanand-dey-neurologist?practice_id=741280&specialization=Neurologist&referrer=doctor_listing")
            
            elif(disease[a]=="Jaundice"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Shyama Prasad Roy\nProfile link: https://www.practo.com/kolkata/doctor/dr-shyama-prasad-roy-general-physician1?practice_id=702842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Malaria"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sandip Rungta\nProfile link: https://www.practo.com/kolkata/doctor/dr-sandip-rungta-cardiologist?practice_id=1180689&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Chicken pox"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Bodhisatwa Choudhuri\nProfile link: https://www.practo.com/kolkata/doctor/bodhisatwa-choudhuri-general-physician?practice_id=735842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Dengue"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Saibal Moitra\nProfile link: https://www.practo.com/kolkata/doctor/dr-saibal-moitra-allergist-immunologist?practice_id=741280&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Typhoid"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Bodhisatwa Choudhuri\nProfile link: https://www.practo.com/kolkata/doctor/bodhisatwa-choudhuri-general-physician?practice_id=735842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="hepatitis A"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sanjoy Basu\nProfile link: https://www.practo.com/kolkata/doctor/sanjoy-basu?practice_id=1250516&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Hepatitis B"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sanjoy Basu\nProfile link: https://www.practo.com/kolkata/doctor/sanjoy-basu?practice_id=1250516&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Hepatitis C"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sanjoy Basu\nProfile link: https://www.practo.com/kolkata/doctor/sanjoy-basu?practice_id=1250516&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Hepatitis D"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sanjoy Basu\nProfile link: https://www.practo.com/kolkata/doctor/sanjoy-basu?practice_id=1250516&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Hepatitis E"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sanjoy Basu\nProfile link: https://www.practo.com/kolkata/doctor/sanjoy-basu?practice_id=1250516&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Alcoholic hepatitis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sanjoy Basu\nProfile link: https://www.practo.com/kolkata/doctor/sanjoy-basu?practice_id=1250516&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Tuberculosis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sumanta Chatterjee\nProfile link: https://www.practo.com/kolkata/doctor/dr-sumanta-chattarjee-general-physician?practice_id=1033173&specialization=Cardiologist&referrer=doctor_listing")
            
            elif(disease[a]=="Common Cold"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Milan Chhetri\nProfile link: https://www.practo.com/kolkata/doctor/dr-milan-chhetri-general-physician?practice_id=741280&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Pneumonia"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Parijat Debchoudhury\nProfile link: https://www.practo.com/kolkata/doctor/parijat-debchoudhury-cardiologist?practice_id=1247064&specialization=Cardiologist&referrer=doctor_listing")
            
            elif(disease[a]=="Dimorphic hemmorhoids(piles)"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Jayanta Paul\nProfile link: https://www.practo.com/kolkata/doctor/dr-jayanta-paul-gastroenterologist-1?practice_id=621621&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Heartattack"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Aftab Khan\nProfile link: https://www.practo.com/kolkata/doctor/dr-aftab-khan-cardiologist?practice_id=741280&specialization=Cardiologist&referrer=doctor_listing")
            
            elif(disease[a]=="Varicose veins"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Nikhil Prasun\nProfile link: https://www.practo.com/kolkata/doctor/nikhil-prasun-neurologist?practice_id=735842&specialization=Neurologist&referrer=doctor_listing")
            
            elif(disease[a]=="Hypothyroidism"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Shyama Prasad Roy\nProfile link: https://www.practo.com/kolkata/doctor/dr-shyama-prasad-roy-general-physician1?practice_id=702842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Hyperthyroidism"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sandip Rungta\nProfile link: https://www.practo.com/kolkata/doctor/dr-sandip-rungta-cardiologist?practice_id=1180689&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Hypoglycemia"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Saibal Moitra\nProfile link: https://www.practo.com/kolkata/doctor/dr-saibal-moitra-allergist-immunologist?practice_id=741280&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Osteoarthristis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Saumitra Sircar\nProfile link: https://www.practo.com/kolkata/doctor/saumitra-sircar-orthopedist?practice_id=1142246&specialization=Orthopedist&referrer=doctor_listing&utm_source=opd_google_dsa")
            
            elif(disease[a]=="Arthritis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Amitava Narayan Mukherjee\nProfile link: https://www.practo.com/kolkata/doctor/dr-amitava-narayan-mukherjee-orthopedist?practice_id=635703&specialization=Orthopedist&referrer=doctor_listing&utm_source=opd_google_dsa")
            
            elif(disease[a]=="(vertigo) Paroymsal  Positional Vertigo"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Subhankar Dey\nProfile link: https://www.practo.com/kolkata/doctor/subhankar-dey-ear-nose-throat-ent-specialist?practice_id=741280&specialization=Ear-Nose-Throat%20(ENT)%20Specialist&referrer=doctor_listing")
            
            elif(disease[a]=="Acne"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Khushbu Tantia\nProfile link: https://www.practo.com/kolkata/doctor/dr-khushbu-tantia-dermatologist-1?practice_id=1347314&specialization=Dermatologist&referrer=doctor_listing")
            
            elif(disease[a]=="Urinary tract infection"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Md. Mohsin\nProfile link: https://www.practo.com/kolkata/doctor/md-mohsin-1-nephrologist?practice_id=741280&specialization=Nephrologist&referrer=doctor_listing")
            
            elif(disease[a]=="Psoriasis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Debatri Datta\nProfile link: https://www.practo.com/kolkata/doctor/dr-debatri-datta-dermatologist?practice_id=1319383&specialization=Dermatologist&referrer=doctor_listing")
            
            elif(disease[a]=="Impetigo"):
                t4.delete("1.0",END)
                t4.insert(END, "Suggested Doctor: Dr. Barnali Dutta\nProfile link: https://www.practo.com/kolkata/doctor/dr-barnali-dutta-dermatologist?practice_id=1277028&specialization=Dermatologist&referrer=doctor_listing")
            

        root = Tk()
        root.title(" Disease Prediction From Symptoms")
        root.configure()

        Symptom1 = StringVar()
        Symptom1.set(None)
        Symptom2 = StringVar()
        Symptom2.set(None)
        Symptom3 = StringVar()
        Symptom3.set(None)
        Symptom4 = StringVar()
        Symptom4.set(None)
        Symptom5 = StringVar()
        Symptom5.set(None)

        w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
        w2.config(font=("Elephant", 30), bg="#fab1f0")
        w2.grid(row=1, column=0, columnspan=2, padx=100)

        NameLb1 = Label(root, text="")
        NameLb1.config(font=("Elephant", 20))
        NameLb1.grid(row=5, column=1, pady=10,  sticky=W)

        S1Lb = Label(root,  text="Symptom 1")
        S1Lb.config(font=("Elephant", 15))
        S1Lb.grid(row=7, column=1, pady=10 , sticky=W)

        S2Lb = Label(root,  text="Symptom 2")
        S2Lb.config(font=("Elephant", 15))
        S2Lb.grid(row=8, column=1, pady=10, sticky=W)

        S3Lb = Label(root,  text="Symptom 3")
        S3Lb.config(font=("Elephant", 15))
        S3Lb.grid(row=9, column=1, pady=10, sticky=W)

        S4Lb = Label(root,  text="Symptom 4")
        S4Lb.config(font=("Elephant", 15))
        S4Lb.grid(row=10, column=1, pady=10, sticky=W)

        S5Lb = Label(root,  text="Symptom 5")
        S5Lb.config(font=("Elephant", 15))
        S5Lb.grid(row=11, column=1, pady=10, sticky=W)

        lr = Button(root, text="Predict",height=2, width=20, command=message)
        lr.config(font=("Elephant", 15))
        lr.grid(row=15, column=1,pady=20)

        OPTIONS = sorted(l1)

        S1En = OptionMenu(root, Symptom1,*OPTIONS)
        S1En.grid(row=7, column=2)

        S2En = OptionMenu(root, Symptom2,*OPTIONS)
        S2En.grid(row=8, column=2)

        S3En = OptionMenu(root, Symptom3,*OPTIONS)
        S3En.grid(row=9, column=2)

        S4En = OptionMenu(root, Symptom4,*OPTIONS)
        S4En.grid(row=10, column=2)

        S5En = OptionMenu(root, Symptom5,*OPTIONS)
        S5En.grid(row=11, column=2)

        NameLb = Label(root, text="")
        NameLb.config(font=("Elephant", 20))
        NameLb.grid(row=13, column=1, pady=10,  sticky=W)

        NameLb = Label(root, text="")
        NameLb.config(font=("Elephant", 15))
        NameLb.grid(row=18, column=1, pady=10,  sticky=W)

        t3 = Text(root, height=2, width=30)
        t3.config(font=("Elephant", 20))
        t3.grid(row=20, column=1 , padx=10)

        t4 = Text(root, height=2, width=40)
        t4.config(font=("calibri", 20))
        t4.grid(row=21, column=1 , padx=10)

        xyz = Label(root, text="N.B: THIS IS A PREDICTIVE MODEL USED TO MAKE PRIMARY PREDICTION ABOUT DISEASE.\nIT IS RECOMMENDED TO VISIT TO A SPECIALISED DOCTOR IF YOU GO THROUGH SERIOUS PROBLEMS.")
        xyz.config(font=("Calibri", 15), fg="red")
        xyz.grid(row=22, column=1, pady=10,  sticky=W)

        root.mainloop()


    def symptoms():
        disease_symptoms = {
            "Flu":["sudden fever","dry chesty cough","headache","tiredness and weakness","chills","aching muscles,limbs or joint pain","diarrhoea or abdominal pain","nausea or vomiting","sore throat","rinny or blocked nose","loss of appetite","sneezing","difficulty in sleeping"],
            "Common Cold": ["Runny nose", "Sneezing", "Cough", "Mild headache"],
            "Allergies": ["Itchy eyes", "Sneezing", "Runny nose", "Rash"],
            "Influenza": ["Fever", "chills", "muscle aches", "cough", "sore throat", "fatigue"],
            "Migraine": ["Intense headache", "nausea", "vomiting", "sensitivity to light and sound"],
            "Fever": ["Sweating", "Chills","shivering", "Headache","Muscle aches", "Loss of appetite", "Irritability", "Dehydration", "General weakness"],
            "Acute cholecystitis":["high temperature", "nausea","vomiting", "sweating","loss of appetite", "yellowing of the skin"," bulge in the abdomen"],
            "Acute pancreatitis":["nausea"," vomiting", "tenderness", "swelling of the abdomen", "indigestion"],
            "Clostridium Difficile":["watery diarrhoea which can be bloody","painful tummy cramps","feeling sick","dehydration","fever","loss of appetite","weight loss"],
            "Coeliac Disease":["severe diarrhoea","excessive wind and/or constipation","nausea and vomiting","recuurent stomach pain","cramping or bloating","iron,vitamin B12 or folic acid defficiency","anaemia","tiredness","mouth ulcers","skin rash","depression","repeated miscarriages","neurological problems"],
            "Deep vein thrombosis":["pain,swelling and tenderness in one leg","a heavy ache in the affected area","warm skin the area of the clot","red skin particularly at the back of leg below the knee"],
            "Dental Abseces":["an intense throbbing pain in the effected tooth or gumpain that spreads to your ear,jaw and neck on the same side as as the affected tooth or gum","pain that is worst when lying down which may disturb sleep","redness or swelling in face"],
            "Diabetes":["feeling very thirsty","urinating more frequently than usual particularly at night","feeling very tired","weight loss and loss of muscle bulk","itching around the penis or vagina","frequent episodes of thrust,cuts or wounds that heal slowly","blurred vision"],
            "Eye Cancer":["shadows","flashes of light","wiggly lines in vision","blurred vision","dark patch in your eye","partial or total loss of viosion","bulging of one eye","a lump on your eyelid that keeps increasing in size"],
            "Globus":["tightness or pressure in throat","catarrh/mucus unable to clear","area of discomfort in throat","feeling of something stuck or lump in throat"],
            "Glandular Fever":["fever","sore throat","swollen glands in necks and armpits","fatigue","aching muscles","chills","sweat","loss of appetite","pain around or behind eyes","swollen tonsils and adenoids","throat becomes red and ooze fluid","small red or purple spots on the roof of mouth","rash","swelling"],
            "Haemorrhoids":["bleeding after passing a stool","itchy bottom","a lump hanging down outside of the anus which may neede to be pushed back in after passing a stool","a mucus discharge after passing a stool","soreness ,redness and swelling around your anus"],
            "Hodgkin Lymphoma":["night sweats","unintentional weight loss","fever","persistent coughor feeling of breathlessness","persistent itching of the skinall over the body"],
            "Huntington's disease":["lack of emotions and not recognising the needs of others","periods of aggression","excitement","depression","antisocial behaviour and anger","apathy","difficulty concentrating on more than one task and handling complex situations","irritability abd impulsiveness"],
            "Cirrhosis":["tiredness and weakness","loss of appetite","weight loss and muscle wasting", "nausea and vomiting","tenderness or pain around the liver area","very itchy skin", "jaundice", "tendency to bleed and bruise more easily"," hair loss", "fever and shivering","oedema"],
            "Chest infection":["coughing up yellow green phlegm or blood","breathlessness","wheezing", "fever","a rapid heartbeat","chest pain or tightness"],
            "Bronchitis":["sore throat","headache","wheezing","increasing breathlessness when exercising or moving around","a persistent cough that brings up mucus","frequent chest infections"],
            "Breast cancer":["a lump or area of thickened tissue in either breast","a change in the size or shape of one or both breasts","discharge from either of your nipples","a lump or swelling in either of your armpit","dimpling on the skin of your breasts","a rash on or around your nipple","a change in the appearance of your nipple","such as becoming sunken into your breast"],
            "Brain tumours":["severe persistent headaches","seizures","mental or behavioural changes","progressive weakness or paralysis on one side of the body","vision problems","or speech problems"],
            "Bone cancer":["Bone pain","high temperature","unexplained weight loss","sweating","particularly at night"],
            "Bladder cancer":["urinate on a more frequent basis","sudden urges to urinate","a burning sensation when passing urine","pelvic pain","bone pain","unintentional weight loss","swelling of the legs"],
            "Bipolar disorder":["feeling sad","hopeless or irritable","lacking energy","difficulty concentrating and remembering things","loss of interest in everyday activities","feelings of emptiness or worthlessness","guilt and despair","feeling pessimistic","self-doubt","being delusional","having hallucinations and disturbed or illogical thinking","lack of appetite", "difficulty sleeping","waking up early","suicidal thoughts"],
            "Bile duct cancer":["jaundice","unintentional weight loss","abdominal pain","high temperature or above and shivering","loss of appetite"],
            "Benign prostate enlargment":["difficult to start urinating","weaken the flow of urine","need to urinate frequently","wake up frequently during the night to urinate","cause blood in the urine"],
            "Asthma":["wheezing","shortness of breath","a tight chest","coughing"],
            "Arthritis":["joint pain","tenderness and stiffness","inflammation in and around the joints","restricted movement of the joints","warm","red skin over the affected joint","weakness and muscle wasting"],
            "Appendicitis":["feeling sick (nausea)","loss of appetite, diarrhoea"," a high temperature (fever) and a flushed face"],
            "Anxiety":["restlessness","a sense of dread","feeling constantly on edge","difficulty concentrating","irritability"],
            "Angioedema":["a hot or painful sensation in the swollen areas","swelling of the inside of the throat","the windpipe and the tongue","making breathing difficult","swelling of the conjunctiva","abdominal pain caused by swelling in the stomach and bowel", "which can cause nausea","vomiting and diarrhoea","swelling of the bladder or urethra"],
            "Anaphylaxis":["itchy skin or a raised","red skin rash","swollen eyes","lips","hands and feet","feeling lightheaded or faint","swelling of the mouth","throat or tongue","which can cause breathing and swallowing difficulties","wheezing","abdominal pain","nausea and vomiting","collapse and unconsciousness"],
            "Anal cancer":["bleeding from the bottom (rectal bleeding)","loss of bowel control","a discharge of mucus from the anus", "small lumps around the anus", "itching and pain around the anus"],
            "Allergies":["sneezing and an itchy", "runny or blocked nose" , "itchy", "red"," watering eyes", "wheezing", "chest tightness", "a raised"," itchy", "red rash","feeling sick","dry", "red and cracked skin"],
            "Addison's disease":["fatigue","lethargy","muscle weakness","low mood or irritability","loss of appetite and unintentional weight loss","the need to urinate frequently","increased thirst","craving for salty foods"],
            "Venous leg ulcers":["wollen ankles (oedema)","discolouration and darkening of the skin around the ulcer","hardened skin around the ulcer, which may make your leg feel hard or even resemble the shape of an upside-down champagne bottle","a heavy feeling in your legs","aching or swelling in your legs","red, flaky, scaly and itchy skin on your legs (varicose eczema)","swollen and enlarged veins on your legs (varicose veins)","an unpleasant and foul-smelling discharge from the ulcer","worsening pain","a green or unpleasant discharge coming from the ulcer","redness and swelling of the skin around the ulcer","a high temperature (fever)"],
            "Vertigo":["loss of balance","feeling sick or being sick","dizziness"],
            "Folate deficiency anaemia":["extreme tiredness (fatigue)","lack of energy (lethargy)","breathlessness","feeling faint headaches","pale skin","noticeable heartbeats (palpitations)hearing sounds coming from inside the body", "rather than from an outside source (tinnitus)","loss of appetite and weight loss","pale yellow tinge to your skin","a sore and red tongue(glossitis)","mouth ulcers","pins and needles (paraesthesia)","changes in the way that you walk and move around","disturbed visions","irritability","depression","changes in the way you think, feel and behave""a decline in your mental abilities, such as memory, understanding and judgement (dementia)"],
            "Vulval cancer":["ersistent itch in the vulva pain", "soreness or tenderness in the vulva raised and thickened patches of skin that can be red", "white or dark a lump or wart-like growth on the vulva bleeding from the vulva or blood-stained vaginal discharge between periods","an open sore in the vulva","a burning pain when passing urine","a mole on the vulva that changes shape or colour"],
            "Uterus cancer":["periods that are heavier than usual","vaginal bleeding in between normal periods","pain in the back, legs, or pelvis","loss of appetite","tiredness","nausea"],
            "Labyrinthitis":["a feeling of pressure inside your ear(s)","ringing or humming inside your ear(s)","fluid or pus leaking out of your ear(s)","nausea","a high temperature(fever)of 38C or 100.4F or above","changes in vision- such as blured viosion or double vision ","mild headaches","tiredness","cold or illness","being in croded areas or small rooms"],
            "Kidney stones":["a persistent ache in the lower back , which is sometimes also felt in the groin ,men may have pain in testicles","periods of intense pain in the back or side of your abdomen or ocassionally in your groin which may last for minutes or hours","needing to urinate more often than normal","feeling restless and unable to lie still","nausea","pain when you urinate","blood in your urine"],
            "Kideny infections":["pain and discomfort in your side,lowerback or around the genitles","high temperature(it may reach 39.5C or 103.1F","shivering or chills","feeling very weak or tired","loss of appetite","feeling sick or being sick","pain or burning sensation during urination","need to urinate frequently or urgently feeling that you are unable to urinate fully","blood in urine","pain in lower abdomen","cloudy or foul smelling urine"],
            "Kidney cancer":["blood in urine","a persistent pain in the sides brlow the ribs","a lump or swelling in the area of your kidneys","extreme tiredness or anemia","unintentional weight loss","night sweats","a general sense of feeling unwell","swelling of the veins in testicles","a high temperature of 38C or above"],
            "Idiopathic pulmonary fibriosis":["a persistant dry cough","tiredness","loss of appetite and weight loss"],
            "Laryngeal cancer":["change in your voice","difficulty swallowing","lump or swelling in neck","long-lasting cough","persistent sore throat","difficulty breathing"],
            "Laryngitis":["hoarseness","difficulty speaking","sore throat","mild feve","rirritating cough","constant need to clear throat","headache","swollen glands","runny nose","pain when swallowing","feeling tired and achy"],
            "Liver cancer":["unexplained weight loss","loss of appetite","feeling very full after eating", "feeling sick and vomiting","pain or swelling in abdomen","jaundice","ichy skin","feeling very tired and weak"],
            "Lung cancer":["persistent cough","coughing up blood","persistent breathlessness","unexplained tiredness and weight loss","ache or pain when breathing or coughing"],
            "Lyme disease":["tiredness","muscle pain","joint pain","headaches","high temperature","chills","neck stiffness","pain and swelling in the jointsnerve problems","memory problems","difficulty concentrating","heart problems"],
            "Lymphoedema":["aching","heavy feeling","difficulty with movement","repeated skin infections"],
            "Malaria":["high temperature","headaches","sweats","chills","muscle aches","vomiting","diarrhoea"],
            "Malignant brain tumours":["severe, persistent headache","coughing","persistent nausea","vomiting","drowsiness","vision problems","seizures"],
            "Measles":["cold-like symptoms such as  runny nose, sneezing, and a coughsore","red eyes that may be sensitive to light","watery eyes","swollen eyes","high temperature","greyish-white spots in the mouth","aches and pain","loss of appetite","tiredness","irritability","lack of energy"],
            "Mesothelioma":["chest pain","shortness of breath","fatigue","high temperature","sweating particularly at night","persistent cough","loss of appetite","unexplained weight loss","clubbed fingertips","tummy pain or swelling","feeling or being sick","loss of appetite","diarrhoea or constipation"],
            "Mouth cancer":["red or white patches in mouth or throat","lump","ulcers persistent pain in the mouth","pain or difficulty when swallowing","changes in voice or speech problems","swollen lymph nodes in neck","unexplained weight loss","bleeding or numbness in the mouth","teeth becomes loose for no obvious reason","difficulty moving jaw"],
            "Myeloma":["Bone pain","Bone fractures and spinal cord compression","Anaemia","Repeated infections","Raised calcium levels in the blood","Unusual bleeding","Thickened blood","Kidney problems"],
            "Multiple sclerosis":["Muscle spasms","stiffness and weakness","Vision problems","Abnormal sensations","Mobility problems","Bladder problems","Bowel problems","Sexual problems","Speech and swallowing difficulties","Fatigue","Mental health issues","Problems with thinking, learning and planning"],
            "Mumps":["headaches","joint pain","feeling sick","dry mouth","mild stomach pain","feeling tired","loss of appetite","high temperature"],
            "Meniere's disease":["vertigo","tinnitus","hearing loss","sense of pressure or fullness deep inside the ear"],
            "Myasthenia gravis":["slurred speech","difficulty swallowing","difficulty making facial expressions","problems with chewing","change in your voice","choking or accidentally inhaling food which can cause chest infections","shortness of breath","weakness in arms, legs, neck or other parts of body","difficulty holding head up","aching muscles","problems with tasks like climbing stairs","droopy eyelids","double vision"],
            "Nasal and sinus cancer":["persistent blocked nose","nose bleed","mucus draining from nose","decreased sense of smell","pain or numbness in face","swollen glands in the neck","partial loss of vision or double vision","bulging or persistently watering eye","lump or growth on face,nose or roof of mouth"],
            "Nasopharyngeal cancer":[" lump in neck","hearing loss","tinnitus","blocked or stuffy nose","nosebleeds"],
            "Non-Hodgkin lymphoma":["night sweats","unintentional weight loss","high temperature","persistent cough","feeling of breathlessness","persistent itching of the skin all over the body"],
            "Nesophageal cancer":["Difficulty swallowing","persistent indigestion or heartburn","bringing up food soon after eating","loss of appetite","weight loss","persistent vomiting","pain or discomfort in upper tummy, chest or back","persistent cough","hoarseness","tiredness","shortness of breath","pale skin","vomiting blood or coughing up blood"],
            "Ntitis externa":["ear pain","itching and irritation in and around ear canal","redness and swelling of outer ear and ear canal","feeling of pressure and fullness inside ear","scaly skin in and around ear canal","discharge from your ear which can be either thin and watery or thick and pus-liketenderness when move ear or jaw","swollen and sore glands in throat","hearing loss","constant itch in and around ear canal","discomfort and pain in ear that becomes worse when moved"],
            "Pancreatic cancer":["pain in the stomach or back","jaundice","weight loss"],
            "Panic disorder":["palpitation","sweating","trembling","hot flushes","chills","shortness of breath","choking sensation","chest pain","nausea","dizziness","feeling faint","numbness or pins and needles","dry mouth","ringing in ears", "feeling of dread or fear of dying","churning stomach","tingling sensation in  fingers","shivering","shaking"],
            "Parkinson's disease":["tremor - shaking","slowness of movement (bradykinesia)","shuffling walk with very small steps","muscle stiffness (rigidity)"],
            "Penile cancer":["growth or sore on the penis that doesn't heal within 4 weeks","bleeding from penis or from under foreskin","foul-smelling discharge","thickening of skin of penis or foreskin that makes it difficult to draw back the foreskin (phimosis)","change in colour of skin of penis or foreskin","rash on penis"],
            "Peripheral neuropathy":["prickling and tingling sensation in the affected body part","numbness and less of an ability to feel pain","changes in temperature particularly in feet a burning or sharp pain"",loss of balance","twitching and muscle cramps","muscle weakness or paralysis affecting one or more muscles","thinning of muscles","foot drop","constipation or diarrhoea","feeling sick","bloating and belching","low blood pressure ","feel faint or dizzy when standing up","rapid heartbeat","excessive sweating or a lack of sweating","problems with sexual function, such as erectile dysfunction in men","difficulty fully emptying bladder of urine","bowel incontinence","altered sensation or weakness in the fingers","double vision","eye pain","weakness of one side of face","Bell's palsyfoot or shin pain","weakness"],
            "Pneumonia":["cough","difficulty breathing","rapid heartbeat","fever","feeling generally unwell","sweating and shivering","loss of appetite","chest pain"],
            "Polymyalgia rheumatica":["mild to high temperature","depression","fatigue","loss of appetite","weight loss"],
            "Post-polio syndrome":["muscle weakness","shrinking of the muscles","tight joints","pain in muscles or joints","chronic fatigue including physical tiredness","brain fatigue","swallowing and speech problems","respiratory problems like breathlessness and sleep","cramps and muscle twitching","being sensitive to cold temperatures"],
            "Post-traumatic stress disorder":["flashbacks","nightmares","repetitive and distressing images or sensations","physical sensations - such as pain, sweating, nausea or trembling","Avoidance and emotional numbing","irritability","angry outbursts","sleeping problems (insomnia)","difficulty concentrating","other mental health problems - such as depression, anxiety or phobiasself-harming or destructive behaviour – such as drug misuse or alcohol misuse","other physical symptoms - such as headaches, dizziness, chest pains and stomach aches"],
            "Postnatal depression":["persistent feeling of sadness and low mood","loss of interest in the world and no longer enjoying things that used to give you pleasure","lack of energy and feeling tired all the time","trouble sleeping at night and feeling sleepy during the day","feeling that you're unable to look after your baby","problems concentrating and making decisions","loss of appetite or an increased appetite (comfort eating)","feeling agitated, irritable or very apathetic (you can't be bothered)","feelings of guilt, hopelessness and self-blamedifficulty bonding with your baby with a feeling of indifference and no sense of enjoyment in his or her company","frightening thoughts – for example, about hurting your baby; these can be scary, but they're very rarely acted uponthinking about suicide and self-harm"],
            "Pressure ulcers":["shoulders or shoulder blades","elbows","back of your headrims of your earsknees, ankles, heels or toes","spinetail bone"],
            "Prostate cancer":["needing to urinate more frequently, often during the night","needing to rush to the toilet","difficulty in starting to pee (hesitancy)straining or taking a long time while urinating","weak flow","feeling that your bladder has not emptied fully"],
            "Psoriatic arthritis":["The pain","swelling and stiffness of hands, feet, knees, elbows, neck and spine"],
            "Reactive arthritis":["joint pain","tenderness and swelling in knees, feet and ankles","lower back and buttock pain","swelling of fingers and toes","joint stiffness","pain or a burning sensation when urinate","urinating more often than usual","having sudden urge to pee","discharge of fluid from penis or vagina","blood in urine","red eyes","watery eyes","eye pain","swollen eyelids","feeling unusually tired","high temperature","weight loss","mouth ulcers","painless white patches inside mouth","rash","thick and crumbly nails","abdominal pain","diarrhoea"],
            "Restless legs syndrome":["tingling, burning, itching or throbbing","creepy-crawly feeling","feeling like fizzy water is inside the blood vessels in the legs","painful, cramping sensation in legs"],
            "Rhabdomyosarcoma":[" tumour in the head or neck area can sometimes cause a blockage","discharge from nose or throat","eye may appear swollen and protruding","tumour in the abdomen"," pain or discomfort in the abdomen","difficulty going to the toilet (constipation)","tumour in the bladder may cause symptoms such as blood in the urine and difficulty passing urine"],
            "Rheumatoid arthritis":["Pain","Stiffness","Swelling","warmth and redness","tiredness and lack of energy","high temperature","sweating","poor appetite","weight loss"],
            "Rosacea":["flushing","persistent facial redness","visible blood vessels","papules and pus","thickened skin","sensitive and rough skin","raised red patches on skin","facial swelling"],
            "Scarlet fever":["swollen neck glands","loss of appetite","nausea or vomiting","red lines in the folds of body","white coating on tongue","general feeling of being unwell"],
            "Shingles":["headache","burning, tingling, numbness or itchiness of the skin in the affected area","feeling of being unwell","high temperature"],
            "Sickle cell disease":["high temperature","difficulty breathing","drowsiness, confusion, or slurred speech","severe headache","stiff neck, or dizziness","fits","sudden swelling in the tummy","priapism - a painful erection lasting two hours or more","weakness on one or both sides of your body","sudden vision loss or changes in your vision"],
            "Sinusitis":["green or yellow discharge from nose","blocked nose","pain and tenderness around cheeks, eyes or forehead","sinus headache","high temperature","toothache","reduced sense of smell","bad breath"],
            "Sjogren's syndrome":["tooth decay and gum disease","dry cough","difficulty swallowing and chewing","hoarse voice","difficulty speaking","swollen salivary glands","repeated fungal infections in the mouth","burning or stinging eyes","itchy eyes","feeling that there's grit in eyes","irritated and swollen eyelids","sensitivity to light","tired eyes","mucus discharge from your eyes","dry skin","tiredness and fatigue","total exhaustion","muscle pain","joint pain","stiffness and swelling","vasculitis","difficulty concentrating, remembering and reasoning"],
            "Slapped cheek syndrome":["high temperature","runny nose","sore throat","headache","upset stomach","feeling unwell"],
            "Sore throat":["colds or flu","runny nose","cough","high temperature","headache and general aches","laryngitis","dry cough","constant need to clear throat","tonsillitis","red or spotty tonsils","discomfort when swallowing","fever",  "strep throat","swollen glands in neck","discomfort when swallowing","glandular fever"],
            "Stomach cancer":["persistent indigestion","trapped wind and frequent burping","heartburn","feeling full very quickly","feeling sick","pain in stomach or breastbone","difficulty swallowing","vomiting"],
            "Streptococcus":["tonsillitis","sore throat","scarlet fever","cellulitis","pneumonia"],
            "Stroke":["complete paralysis of one side of body","sudden loss or blurring of vision","difficulty understanding what others are saying","problems with balance and co-ordination","sudden and very severe headache","loss of feeling in one side of the body"],
            "Swollen glands":["cold","tonsillitis","glandular fever","throat infection","ear infection","dental abscess","cellulitis"],
            "Testicular cancer":["dull ache or sharp pain in testicles or scrotum","change in the texture or increase in firmness of a testicle","difference between one testicle and other","persistent cough","coughing or spitting up blood","shortness of breath","swelling and enlargement of male breasts","lump or swelling in neck","lower back pain"],
            "Thyroid cancer":["unexplained hoarseness"," sore throat or difficulty swallowing","pain in neck"],
            "Tonsillitis":[" sore throat and pain when swallowing","earache","high temperature","coughing","headache"],
            "Transient ischaemic attack":["complete paralysis of one side of the body","sudden loss or blurring of vision","dizziness","confusion","difficulty understanding what others are saying","problems with balance and co-ordination"],
            "Tuberculosis":["ack of appetite","weight loss","high temperature","night sweats","extreme tiredness or fatigue"],
            "Transverse myelitis":["muscle weakness in legs","mobility problems","unusual sensations and numbness","bladder problems","bowel problems","sexual problems","pain"],
            "Underactive thyroid":["tiredness","being sensitive to cold","weight gain","constipation","depression","slow movements and thoughts","muscle aches and weakness","muscle cramps","dry and scaly skin","brittle hair and nails","loss of libido","pain, numbness and a tingling sensation in the hand and fingers","irregular periods or heavy periods","low-pitched and hoarse voice","puffy-looking face","thinned or partly missing eyebrows","slowheart rate","hearing loss","anaemia"],
            "Urinary tract infection":["need to pee more often than usual","pain or discomfort when peeing","sudden urges to pee","pain low down in tummy","urine that'scloudy","foul-smelling or contains blood feeling generally unwell", "achy and tired","high temperature","pain in your sides or back","shivering and chills","confusion agitation or restlessness"],
            "Hives":["rash may be raised","spread over large areas","range is size from a few millimetres to the size of a hand","change in appearance within 24 hours"],
            "Varicose eczema":["skin becomes itchy","red and swollen","dry and flaky scaly or crustybrown discolouration of the skin","red, tender and tight skin that can eventually become hardened","small, white scars","pain","eczema affecting other parts of the body Left untreated","leg ulcers"],
            "Venous leg ulcers":["swollen ankles","discolouration and darkening of the skin","hardened skin around the ulcer", "aching or swelling in your legs","red, flaky, scaly and itch yskin on legs","swollen and enlarged veins on legs","unpleasant and foul-smelling discharge from the ulcer","worsening pain","redness and swelling of the skin around the ulcer","high temperature"],
            "Vertigo":["loss of balance","feeling sick","dizziness"],
            "Folate deficiency anaemia":["extreme tiredness","lack of energy","breathlessness","feeling faint","headaches","pale skin","noticeable heartbeats","hearing sounds coming from inside the body","tinnitus","loss of appetite","weight loss","pale yellow tinge to your skin","sore and red tongue","mouth ulcers","disturbed vision","irritability","depression","changes in the way you think, feel and behave","decline in mental abilities"],
            "Malaria":["shaking","chills","headache", "muscle aches"," tiredness","Nausea"," vomiting", "diarrhea","fever","anemia","jaundice "],
            "Chicken pox":["rash that turns into itchy", "fluid-filled blisters that eventually turn into scabs"],
            "AIDS":["Fever and muscle pains","Headache","Sore throat","Night sweats","Mouth sores", "including yeast infection","Swollen lymph glands","Diarrhea"],

    }

        def search_disease():
        # Retrieve the entered disease name from the search box
            disease = entry.get()

        # Check if the entered disease exists in the data
            if disease in disease_symptoms:
            # Clear the previous answer (if any)
                answer.config(state=tk.NORMAL)
                answer.delete('1.0', tk.END)

            # Display the symptoms of the disease in the answer box
                symptoms = disease_symptoms[disease]
                for symptom in symptoms:
                    answer.insert(tk.END, f"• {symptom.upper()}\n\n")
                    #answer.config(state=tk.DISABLED)
            else:
            # Clear the previous answer (if any)
                answer.config(state=tk.NORMAL)
                answer.delete('1.0', tk.END)

            # Display a message indicating that the disease was not found
                answer.insert(tk.END, "Disease not found.")
                answer.config(state=tk.DISABLED)
        
    # Create the main window
        window = tk.Tk()
        window.title("Disease Symptoms Search")

    # Create and place the search label and entry
        search_label = tk.Label(window, text="Enter a disease:")
        search_label.pack()

        entry = tk.Entry(window)
        entry.pack()

    # Create and place the search button
        search_button = tk.Button(window, text="Search", command=search_disease)
        search_button.pack()

    # Create and place the answer box
        answer_label = tk.Label(window, text="Symptoms:")
        answer_label.pack()

        answer = tk.Text(window, height=30, width=65)
        answer.config(state=tk.DISABLED)
        answer.pack()

    # Start the GUI event loop
        window.mainloop()

    def bloodbank():
        def read_data_from_csv():
            data = []
            with open('bloodbank.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    data.append(row)
            return data

        def write_data_to_csv(data):
            with open('bloodbank.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Blood Group', 'Phone', 'BloodBank Name'])
                writer.writerows(data)

        def add_donor():
            name = name_entry.get()
            blood_group = blood_group_entry.get()
            phone = phone_entry.get()
            bloodbank_name= bloodbank_name_entry.get()

            if name and blood_group and phone and bloodbank_name:
                data.append([name, blood_group, phone, bloodbank_name])
                write_data_to_csv(data)
                messagebox.showinfo('Success', 'Donor added successfully.')
                clear_entries()
            else:
                messagebox.showerror('Error', 'Please enter all the details.')

        def search_donor():
            blood_group = blood_group_entry.get()

            if blood_group:
                matching_donors = [donor for donor in data if donor[1] == blood_group]
                if matching_donors:
                    display_text.config(state=tk.NORMAL)
                    display_text.delete('1.0', tk.END)
                    for donor in matching_donors:
                        display_text.insert(tk.END, f'BloodBank Name: {donor[3]}\n')
                        display_text.insert(tk.END, f'Name: {donor[0]}\n')
                        display_text.insert(tk.END, f'Blood Group: {donor[1]}\n')
                        display_text.insert(tk.END, f'Phone: {donor[2]}\n---------------------------------\n')
                        
                    display_text.config(state=tk.DISABLED)
                else:
                    messagebox.showinfo('No Match', 'No donors found for the given blood group.')
            else:
                messagebox.showerror('Error', 'Please enter the blood group.')

        def clear_entries():
            name_entry.delete(0, tk.END)
            blood_group_entry.delete(0, tk.END)
            phone_entry.delete(0, tk.END)
            bloodbank_name_entry.delete(0,tk.END)

        data = read_data_from_csv()

        window = tk.Tk()
        window.title('Blood Bank Database Management')

        name_label = tk.Label(window, text='Name:')
        name_label.grid(row=0, column=0, sticky='E')

        name_entry = tk.Entry(window)
        name_entry.grid(row=0, column=1)

        blood_group_label = tk.Label(window, text='Blood Group:')
        blood_group_label.grid(row=1, column=0, sticky='E')

        blood_group_entry = tk.Entry(window)
        blood_group_entry.grid(row=1, column=1)

        phone_label = tk.Label(window, text='Phone:')
        phone_label.grid(row=2, column=0, sticky='E')

        phone_entry = tk.Entry(window)
        phone_entry.grid(row=2, column=1)

        bloodbank_name_label = tk.Label(window, text='BloodBank Name:')
        bloodbank_name_label.grid(row=3, column=0, sticky='E')

        bloodbank_name_entry = tk.Entry(window)
        bloodbank_name_entry.grid(row=3, column=1)

        add_button = tk.Button(window, text='Add Donor', command=add_donor)
        add_button.grid(row=4, column=0, columnspan=2, pady=10)

        search_button = tk.Button(window, text='Search Donor', command=search_donor)
        search_button.grid(row=5, column=0, columnspan=2)

        display_text = tk.Text(window, height=20, width=50)
        display_text.config(state=tk.DISABLED)
        display_text.grid(row=6, column=0, columnspan=2, pady=10)

        clear_button = tk.Button(window, text='Clear Entries', command=clear_entries)
        clear_button.grid(row=7, column=0, columnspan=2)

        window.mainloop()
        


    f3=Frame(root,bg="white",borderwidth=2,relief=RAISED)
    f3.pack(side="top",pady=20)
    b3=Button(f3,text="Check your disease",bg="white",fg="black",padx=40,font=("calibri",20),borderwidth=3,command=disease)
    b3.pack(side="top")
    f2=Frame(root,bg="white",borderwidth=2,relief=RAISED)
    f2.pack(side="top",pady=20)
    b2=Button(f2,text="Check your symptoms",bg="white",font=("calibri",20),fg="black",padx=25,borderwidth=3,command=symptoms)
    b2.pack(side="top")
    f1=Frame(root,bg="white",borderwidth=2,relief=RAISED)
    f1.pack(side="top",pady=20)
    b1=Button(f1,text="Blood Bank Data",bg="white",font=("calibri",20),fg="black",padx=55,borderwidth=3,command=bloodbank)
    b1.pack(side="top")

    w = Label(root, text="\n--------------------------------------------------------\nPRESENTED BY:\nDEBANJAN DAS\nPRIYASHA ROY CHOWDHURY\nSOUMI BHADRA\nTANUSHKA CHANDA",fg="black",font=("calibri",18),bg="#bcf6f5")
    w.pack()

    root.mainloop()

def show_button():
    b10.pack() 
f10=Frame(window,bg="white",borderwidth=2,relief=RAISED)
f10.pack(side="top",pady=20)
b10=Button(f10,text="Start",bg="#ecf0ed",font=("algerian",20),fg="black",padx=55,borderwidth=3,command=mainproblem)
b10.pack(side="top")
b10.pack_forget()
window.after(5000,show_button)

window.mainloop()