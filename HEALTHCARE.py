from tkinter import*
from tkinter import messagebox, ttk
import tkinter as tk             
from geopy.geocoders import Nominatim
import csv
import numpy as np
import pandas as pd
from PIL import Image, ImageTk
import json, math


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
        with open('symptoms.json', 'r') as json_file:
            dataset = json.load(json_file)

        l1 = dataset.get("name",[])
        
        with open('disease_name.json', 'r') as json_file:
            dataset = json.load(json_file)

        disease = dataset.get("disease",[])

        l2=[]
        for x in range(0,len(l1)):
            l2.append(0)

        # TESTING DATA
        tr=pd.read_csv("Testing.csv")

        with open('prognosis.json', 'r') as json_file:
            dataset= json.load(json_file)
        prog = {key: int(value) for key, value in dataset.get("prognosis", {}).items()}
        prognosis={"prognosis":(prog)}
        tr.replace(prognosis,inplace=True)

        X_test= tr[l1]
        y_test = tr[["prognosis"]]
        np.ravel(y_test)

        # TRAINING DATA
        df=pd.read_csv("Training.csv")

        df.replace(prognosis,inplace=True)

        X= df[l1]

        y = df[["prognosis"]]
        np.ravel(y)

        def message():
            Symptom1= S1En.get()
            Symptom2= S2En.get()
            Symptom3= S3En.get()
            Symptom4= S4En.get()
            Symptom5= S5En.get()
            print(Symptom1,Symptom2,Symptom3,Symptom4,Symptom5)
            if (Symptom1 == "None" and  Symptom2 == "None" and Symptom3 == "None" and Symptom4 == "None" and Symptom5 == "None"):
                messagebox.showinfo("OPPS!!", "ENTER  SYMPTOMS PLEASE")
            else :
                NaiveBayes(Symptom1,Symptom2,Symptom3,Symptom4,Symptom5)

        def NaiveBayes(Symptom1,Symptom2,Symptom3,Symptom4,Symptom5):
            from sklearn.naive_bayes import MultinomialNB
            gnb = MultinomialNB()
            gnb=gnb.fit(X,np.ravel(y))
            from sklearn.metrics import accuracy_score
            y_pred = gnb.predict(X_test)
            print(accuracy_score(y_test, y_pred))
            print(accuracy_score(y_test, y_pred, normalize=False))

            psymptoms = [Symptom1,Symptom2,Symptom3,Symptom4,Symptom5]
            # print(psymptoms)
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
            
            elif(disease[a]=="Diabetes"): #***********
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Sandip Rungta\nProfile link: https://www.practo.com/kolkata/doctor/dr-sandip-rungta-cardiologist?practice_id=1180689&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Gastroenteritis"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Jayanta Paul\nProfile link: https://www.practo.com/kolkata/doctor/dr-jayanta-paul-gastroenterologist-1?practice_id=621621&specialization=Gastroenterologist&referrer=doctor_listing")
            
            elif(disease[a]=="Bronchial Asthma"):
                t4.delete("1.0", END)
                t4.insert(END, "Suggested Doctor: Dr. Shyama Prasad Roy\nProfile link: https://www.practo.com/kolkata/doctor/dr-shyama-prasad-roy-general-physician1?practice_id=702842&specialization=General%20Physician&referrer=doctor_listing&utm_source=opd_google_Pmax")
            
            elif(disease[a]=="Hypertension"):
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
        
        OPTIONS = sorted(l1)

        def checkkey(event):
            value = event.widget.get()
            print(value)
            if value == '':
                data = OPTIONS
            else:
                data = []   
                for item in OPTIONS:
                    if value.lower() in item.lower():
                        data.append(item)                
            update(data)
        
        def update(data):
            lb.delete(0, 'end')
            for item in data:
                lb.insert('end', item)

        def on_listbox_select(event, entry):
            selected_index = lb.curselection()
            if selected_index:
                selected_item = lb.get(selected_index)
                entry.delete(0, tk.END)
                entry.insert(0, selected_item)
                # symptom_var.set(selected_item)


        w2 = Label(root, justify=LEFT, text=" Disease Prediction From Symptoms ")
        w2.config(font=("Elephant", 30), bg="#fab1f0")
        w2.grid(row=1, column=0, columnspan=2)

        S1Lb = Label(root,  text="Symptom 1")
        S1Lb.config(font=("Elephant", 15))
        S1Lb.grid(row=3, column=1, padx=10, pady=10, sticky=W)

        S2Lb = Label(root,  text="Symptom 2")
        S2Lb.config(font=("Elephant", 15))
        S2Lb.grid(row=4, column=1, padx=10, pady=10, sticky=W)

        S3Lb = Label(root,  text="Symptom 3")
        S3Lb.config(font=("Elephant", 15))
        S3Lb.grid(row=5, column=1, padx=10, pady=10, sticky=W)

        S4Lb = Label(root,  text="Symptom 4")
        S4Lb.config(font=("Elephant", 15))
        S4Lb.grid(row=6, column=1, padx=10, pady=10, sticky=W)

        S5Lb = Label(root,  text="Symptom 5")
        S5Lb.config(font=("Elephant", 15))
        S5Lb.grid(row=7, column=1, padx=10, pady=10, sticky=W)

        lr = Button(root, text="Predict",height=2, width=20, command=message)
        lr.config(font=("Elephant", 20))
        lr.grid(row=16, column=1, padx=20, pady=10)


        S1En = Entry(root)
        S1En.grid(row=3, column=2, padx=10, pady=10, sticky=W)
        S1En.bind('<KeyRelease>', checkkey)
        S2En = Entry(root)
        S2En.grid(row=4, column=2, padx=10, pady=10, sticky=W)
        S2En.bind('<KeyRelease>', checkkey)
        S3En = Entry(root)
        S3En.grid(row=5, column=2, padx=10, pady=10, sticky=W)
        S3En.bind('<KeyRelease>', checkkey)
        S4En = Entry(root)
        S4En.grid(row=6, column=2, padx=10, pady=10, sticky=W)
        S4En.bind('<KeyRelease>', checkkey)
        S5En = Entry(root)
        S5En.grid(row=7, column=2, padx=10, pady=10, sticky=W)
        S5En.bind('<KeyRelease>', checkkey)

        lb = Listbox(root)
        lb.grid(row=8, column=2, padx=10, pady=10, sticky=W)
        update(OPTIONS)
        lb.bind("<Return>", lambda event: on_listbox_select(event, S1En))
        lb.bind("<Left>", lambda event: on_listbox_select(event, S2En))
        lb.bind("<Right>", lambda event: on_listbox_select(event, S3En))
        lb.bind("<Up>", lambda event: on_listbox_select(event, S4En))
        lb.bind("<Down>", lambda event: on_listbox_select(event, S5En))

        t3 = Text(root, height=2, width=30)
        t3.config(font=("Elephant", 20))
        t3.grid(row=17, column=1 , padx=10)

        t4 = Text(root, height=2, width=40)
        t4.config(font=("calibri", 20))
        t4.grid(row=18, column=1 , padx=10)

        xyz = Label(root, text="N.B: THIS IS A PREDICTIVE MODEL USED TO MAKE PRIMARY PREDICTION ABOUT DISEASE.\n IT IS RECOMMENDED TO VISIT TO A SPECIALISED DOCTOR IF YOU GO THROUGH SERIOUS PROBLEMS.")
        xyz.config(font=("Calibri", 15), fg="red")
        xyz.grid(row=19, column=1, pady=10,  sticky=W)

        root.mainloop()
        

    def symptoms():
        with open('disease_data.json', 'r') as json_file:
            disease_symptoms = json.load(json_file)

        def search_disease():
            disease = entry.get()

            answer.config(state=tk.NORMAL)
            answer.delete('1.0', tk.END)

            if disease in disease_symptoms:
                symptoms = disease_symptoms[disease]
                for symptom in symptoms:
                    answer.insert(tk.END, f"• {symptom.upper()}\n\n")
            else:
                answer.insert(tk.END, "Disease not found.")

            answer.config(state=tk.DISABLED)

        def checkkey(event):
            value = event.widget.get()
            print(value)
            if value == '':
                data = l
            else:
                data = []
                for item in l:
                    if value.lower() in item.lower():
                        data.append(item)
            update(data)
        
        
        def update(data):
            lb.delete(0, 'end')
            for item in data:
                lb.insert('end', item)
        def on_listbox_select(event):
            selected_index = lb.curselection()
            if selected_index:
                selected_item = lb.get(selected_index)
                entry.delete(0, tk.END)
                entry.insert(0, selected_item) 


        # Driver code
        l = sorted(list(disease_symptoms.keys()))



        window = tk.Tk()
        window.title("Disease Symptoms Search")
        
        #creating text box 
        search_label = tk.Label(window, text="Enter a disease:")
        search_label.pack()
        entry = tk.Entry(window)
        entry.pack()
        entry.bind('<KeyRelease>', checkkey)
        #creating list box
        lb = Listbox(window)
        lb.pack()
        update(l)
        lb.bind("<<ListboxSelect>>", on_listbox_select)
        search_button = tk.Button(window, text="Search", command=search_disease)
        search_button.pack()

        answer_label = tk.Label(window, text="Symptoms:")
        answer_label.pack()
        answer = tk.Text(window, height=30, width=65)
        answer.config(state=tk.DISABLED)
        answer.pack()


        window.mainloop()

    def bloodbank():
        # Global data list to store donor information

        def read_data_from_csv():
            global data
            data = []
            with open('bloodbank.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader)  # Skip the header row
                for row in reader:
                    data.append(row)

        def write_data_to_csv():
            with open('bloodbank.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(['Name', 'Blood Group', 'Phone', 'BloodBank Name','Longitude','Latitude'])
                writer.writerows(data)

        def add_donor(name, blood_group, phone, bloodbank_name, longitude, latitude):
            data.append([name, blood_group, phone, bloodbank_name, longitude, latitude])
            write_data_to_csv()
            messagebox.showinfo('Success', 'Donor added successfully.')

        def search_donor_by_blood_group(blood_group):
            matching_donors = [donor for donor in data if donor[1] == blood_group]
            return matching_donors

        def open_add_donor_window():
            add_window = tk.Toplevel(root)
            add_window.title('Add Donor')
            add_window.geometry("300x300")

            def clear_entries():
                name_entry.delete(0, tk.END)
                blood_group_entry.delete(0, tk.END)
                phone_entry.delete(0, tk.END)
                bloodbank_name_entry.option_clear(0, tk.END)
                longitude_entry.delete(0, tk.END)
                latitude_entry.delete(0, tk.END)

            BBname=sorted(["PEERLESS HOSPITAL","SSKM HOSPITAL BLOOD BANK","FORTIS HOSPITALS LIMITED BLOOD BANK","SOUTH EAST KOLKATA MANAB KALYAN","RUBY GENERAL HOSPITAL","LIONS BLOOD BANK","IBTM&IH","OM BLOOD BANK KOLKATA","LIFE CARE BLOOD BANK","BHORUKA BLOOD BANK","PEOPLE'S BLOODBANK"])
            bloodbank_coords = {
                "PEERLESS HOSPITAL": (88.3939707, 22.4810427),
                "FORTIS HOSPITALS LIMITED BLOOD BANK": (88.3990948, 22.5181021),
                "SOUTH EAST KOLKATA MANAB KALYAN": (88.391084, 22.5256993),
                "RUBY GENERAL HOSPITAL":(88.402884, 22.5131759),
                "LIONS BLOOD BANK":(88.2869754, 22.5010317),
                "IBTM&IH":(88.3751871, 22.5854362),
                "OM BLOOD BANK KOLKATA":(88.3794252, 22.5638132),
                "LIFE CARE BLOOD BANK":(88.370838, 22.5498049),
                "BHORUKA BLOOD BANK":(88.3571161, 22.5550749),
                "PEOPLE'S BLOODBANK":(88.3462425, 22.5257451),
                "SSKM HOSPITAL BLOOD BANK":(88.3437482, 22.5402242)
                }

            name_label = tk.Label(add_window, text='Name:')
            name_entry = tk.Entry(add_window)
            blood_group_label = tk.Label(add_window, text='Blood Group:')
            blood_group_entry = tk.Entry(add_window)
            phone_label = tk.Label(add_window, text='Phone:')
            phone_entry = tk.Entry(add_window)
            bloodbank_name_label = tk.Label(add_window, text='BloodBank Name:')
            bloodbank_name_var = tk.StringVar(add_window)
            bloodbank_name_entry = tk.OptionMenu(add_window, bloodbank_name_var, *BBname)
            longitude_label = tk.Label(add_window, text='Longitude:')
            longitude_var = tk.DoubleVar(add_window)
            bloodbank_name_var.trace("w", lambda *args: longitude_var.set(bloodbank_coords.get(bloodbank_name_var.get(), (0.0, 0.0))[0]))
            longitude_entry = tk.Entry(add_window, textvariable=longitude_var, state="readonly")
            latitude_label = tk.Label(add_window, text='Latitude:')
            latitude_var = tk.DoubleVar(add_window)
            bloodbank_name_var.trace("w", lambda *args: latitude_var.set(bloodbank_coords.get(bloodbank_name_var.get(), (0.0, 0.0))[1]))
            latitude_entry = tk.Entry(add_window, textvariable=latitude_var, state="readonly")
            add_button = tk.Button(add_window, text='Add Donor', command=lambda: add_donor(name_entry.get(), blood_group_entry.get(), phone_entry.get(), bloodbank_name_var.get(), longitude_entry.get(), latitude_entry.get()))
            clear_button = tk.Button(add_window, text='Clear Entries', command=clear_entries)
            
            name_label.pack()
            name_entry.pack()
            blood_group_label.pack()
            blood_group_entry.pack()
            phone_label.pack()
            phone_entry.pack()
            bloodbank_name_label.pack()
            bloodbank_name_entry.pack()
            longitude_label.pack()
            longitude_entry.pack()
            latitude_label.pack()
            latitude_entry.pack()
            add_button.pack()
            clear_button.pack()


        def open_search_donor_window():

            search_window = tk.Toplevel(root)
            search_window.title('Search Donor')

            location_label = tk.Label(search_window, text='Location:')
            location_entry = tk.Entry(search_window)
            blood_group_label = tk.Label(search_window, text='Blood Group:')
            blood_group_entry = tk.Entry(search_window)

            def search_button_click():
        # Get user's location
                user_location = location_entry.get()

                # Geocode the location
                geolocator = Nominatim(user_agent="MyApp")
                location = geolocator.geocode(user_location)
                
                if location:
                    user_lat = location.latitude
                    user_lon = location.longitude
                    display_search_results(blood_group_entry.get(), user_lat, user_lon)
                else:
                    search_results_text.insert(tk.END, "Location not found.")
  
            search_button = tk.Button(search_window, text='Search', command=search_button_click)

            blood_group_label.pack()
            blood_group_entry.pack()
            location_label.pack()
            location_entry.pack()
            search_button.pack()

            search_results_text = tk.Text(search_window, height=20, width=40)
            search_results_text.pack()

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

            def display_search_results(blood_group, user_lat, user_lon):
                search_results_text.delete('1.0', tk.END)
                matching_donors = search_donor_by_blood_group(blood_group)
                
                if matching_donors:
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
                    
                    # Display donors based on sorted bloodbanks
                    for bloodbank_name, bloodbank_info in sorted_bloodbanks:
                        search_results_text.insert(tk.END, f'BloodBank Name: {bloodbank_name}\n')
                        search_results_text.insert(tk.END, f'Distance: {bloodbank_info["distance"]:.2f} km\n\n')
                        i=1
                        for donor in bloodbank_info['donors']:
                            search_results_text.insert(tk.END, f'{i}) Name: {donor[0]}\n')
                            search_results_text.insert(tk.END, f'  Blood Group: {donor[1]}\n')
                            search_results_text.insert(tk.END, f'  Phone: {donor[2]}\n')
                            i+=1
                        search_results_text.insert(tk.END, f'---------------------------------\n')
                else:
                    search_results_text.insert(tk.END, 'No donors found for the given blood group.')




        # Main GUI window
        root = tk.Tk()
        root.title('Blood Bank Management')

        # Load data from CSV file on startup
        read_data_from_csv()

        # Create buttons for different actions
        add_donor_button = tk.Button(root, text='Add Donor', command=open_add_donor_window)
        search_donor_button = tk.Button(root, text='Search Donor', command=open_search_donor_window)

        add_donor_button.grid(row=1, column=1, padx=50, pady=50)
        search_donor_button.grid(row=1, column=2, pady=20)

        root.geometry("300x250")
        root.mainloop()
        


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

    w = Label(root, text="\n--------------------------------------------------------\nPRESENTED BY:\nDEBANJAN DAS\n",fg="black",font=("calibri",18),bg="#bcf6f5")
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
