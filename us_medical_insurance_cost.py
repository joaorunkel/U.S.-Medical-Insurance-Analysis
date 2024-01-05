import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import tkinter as tk
from tkinter import ttk
from sklearn.preprocessing import LabelEncoder
import warnings
from tkinter import messagebox

def calculate_average(data, column):
    total = sum(row[column] for row in data)
    return total / len(data)


#Creating dataframe from csv file and converting to a dictionary using records orientation
file_path= 'insurance.csv'
df = pd.read_csv(file_path)
data_dict = df.to_dict(orient='records')

#Insights on costs

#Average charges
avg_charges = calculate_average(data_dict, "charges")

##Average charge per region

avg_charges_per_region = df.groupby('region')['charges'].mean().reset_index() #Average charges per region dataframe
avg_charges_northeast = avg_charges_per_region["charges"][0] #Northeast
avg_charges_northwest = avg_charges_per_region["charges"][1] #Northwest
avg_charges_southeast = avg_charges_per_region["charges"][2] #Southeast
avg_charges_southwest = avg_charges_per_region["charges"][3] #Southwest

##Average charges of smokers

df_smokers = df[df["smoker"]=="yes"] #Create a dataframe for smokers information
df_dict_smokers = df_smokers.to_dict(orient='records') #Convert dataframe to dictionairy
avg_charges_smokers = calculate_average(df_dict_smokers, "charges") #Average charge of smokers

##Average charges of each gender

df_male = df[df["sex"] == "male"] #Create a dataframe for male 
df_female = df[df["sex"] == "female"] #Create a dataframe for male
df_dict_male = df_male.to_dict(orient="records") #Convert male dataframe to dictionairy
df_dict_female = df_female.to_dict(orient="records") #Convert female dataframe to dictionairy

avg_charges_male = calculate_average(df_dict_male, "charges") #Average charges for males
avg_charges_female = calculate_average(df_dict_female, "charges") #Average charges for females

##Average charges of parents

df_parents = df[df["children"] > 0]
df_dict_parents = df_parents.to_dict(orient ="records")
avg_charge_parents = calculate_average(df_dict_parents, "charges")


#Insights on age

##Average age of smokers

avg_age_smokers = calculate_average(df_dict_smokers, "age")

##Average age of parents

avg_age_parents = calculate_average(df_dict_parents, "age")

##Average age per region

avg_age_per_region = df.groupby('region')["age"].mean().reset_index() #Average charges per region dataframe
avg_age_northeast = avg_age_per_region["age"][0] #Northeast
avg_age_northwest = avg_age_per_region["age"][1] #Northwest
avg_age_southeast = avg_age_per_region["age"][2] #Southeast
avg_age_southwest = avg_age_per_region["age"][3] #Southwest


#Insights on gender

##Counting each gender individuals
males = len(df_dict_male)
females = len(df_dict_female)

##Countig smokers for each gender

num_male_smokers = len(df_male['smoker'] == 'yes')
num_female_smokers = len(df_female['smoker'] == 'yes')

#Important Conslusions

def calculate_difference(value, average):
    if value>=average:
        perc = value*100/average -100
        diff = value - average
        return perc, diff
    else:
        perc = 100-value*100/average
        diff = average - value
        return perc, diff

perc_smokers, smokers_diff = calculate_difference(avg_charges_smokers, avg_charges)
print("Smokers pay on average " + f"{round(perc_smokers, 2)}%" + f" or {round(smokers_diff, 2)}$ more than non-smokers.")

perc_gender, gender_diff = calculate_difference(avg_charges_male, avg_charges_female)
print("Males pay "+f"{round(perc_gender)}%" + f" or {round(gender_diff)}$ more than females.")

perc_northeast, diff_northeast = calculate_difference(avg_charges_northeast, avg_charges)
print("Northeast inhabitants pay "+f"{round(perc_northeast, 2)}%" + f" or {round(diff_northeast)}$ above the avarage.")

perc_northwest, diff_northwest = calculate_difference(avg_charges_northwest, avg_charges)
print("Northwest inhabitants pay "+f"{round(perc_northwest, 2)}%" + f" or {round(diff_northwest)}$ under the avarage.")

perc_southeast, diff_southeast = calculate_difference(avg_charges_southeast, avg_charges)
print("Southeast inhabitants pay "+f"{round(perc_southeast, 2)}%" + f" or {round(diff_southeast)}$ above the avarage.")

perc_southwest, diff_southwest = calculate_difference(avg_charges_southwest, avg_charges)
print("Southwest inhabitants pay "+f"{round(perc_southwest, 2)}%" + f" or {round(diff_southwest)}$ under the avarage.")

warnings.simplefilter(action='ignore', category=UserWarning)

#SECTION DEDICATED TO LINEAR REGRESSION MODEL AND CHARGES PREDICTION

inputs =  ['age','sex','bmi','children','smoker']

df['sex'] = df['sex'].map({'male': 0, 'female': 1})
df['smoker'] = df['smoker'].map({'no': 0, 'yes': 1})

X = df[inputs]
y = df['charges']

# Provide feature names to X
X.columns = inputs

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)






#UI SECTION

def open_bmi_calculator():
    bmi_calculator = tk.Toplevel(window)
    bmi_calculator.title("BMI Calculator")

    # BMI Calculator UI components (you can customize this based on your needs)
    tk.Label(bmi_calculator, text="Enter Weight (kg):").grid(row=0, column=0, padx=10, pady=5)
    weight_entry = tk.Entry(bmi_calculator)
    weight_entry.grid(row=0, column=1, padx=10, pady=5)

    tk.Label(bmi_calculator, text="Enter Height (m):").grid(row=1, column=0, padx=10, pady=5)
    height_entry = tk.Entry(bmi_calculator)
    height_entry.grid(row=1, column=1, padx=10, pady=5)

    # BMI Entry field in the main window
    bmi_entry_main_window = bmi_entry

    # Function to calculate BMI
    def calculate_bmi():
        try:
            weight = float(weight_entry.get())
            height = float(height_entry.get())
            bmi = weight / (height ** 2)
            bmi_entry_main_window.delete(0, tk.END)  # Clear the existing value in BMI entry
            bmi_entry_main_window.insert(0, f"{bmi:.2f}")  # Set the calculated BMI to BMI entry
            messagebox.showinfo("BMI Result", f"Your BMI is: {bmi:.2f}")
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for weight and height.")

    # Button to calculate BMI
    calculate_button = tk.Button(bmi_calculator, text="Calculate BMI", command=calculate_bmi)
    calculate_button.grid(row=2, column=0, columnspan=2, pady=10)

# Display warnings using Tkinter messagebox
def show_warning(message):
    messagebox.showwarning("Warning", message)

warnings.showwarning = show_warning

def predict_cost():
    # Get user inputs
    age = float(age_entry.get())
    bmi = float(bmi_entry.get())
    children = float(children_entry.get())
    sex = gender_var.get()
    smoker = smoker_var.get()

    # Convert categorical variables to numerical values
    sex = 0 if sex == 'male' else 1
    smoker = 1 if smoker == 'yes' else 0

    if sex == 0 and smoker == 1:
        result_label.config(text="Warning: Males who smoke may have higher insurance costs.", fg="red")
    else:
        result_label.config(text="")

    # Create a feature array for prediction
    features = [[age, sex, bmi, children, smoker]]

    # Make prediction
    prediction = model.predict(features)[0]

    # Ensure the predicted value is non-negative
    prediction = max(prediction, 0)

    # Update the result label
    result_label.config(text=f"Predicted Insurance Cost: ${prediction:.2f}")


# Tkinter window setup
window = tk.Tk()
window.title("Insurance Cost Prediction")

# Labels and Entry Widgets
tk.Label(window, text="Age:").grid(row=0, column=0, padx=10, pady=5)
age_entry = tk.Entry(window)
age_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="BMI:").grid(row=1, column=0, padx=10, pady=5)
bmi_entry = tk.Entry(window)
bmi_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Children:").grid(row=2, column=0, padx=10, pady=5)
children_entry = tk.Entry(window)
children_entry.grid(row=2, column=1, padx=10, pady=5)

tk.Label(window, text="Gender:").grid(row=3, column=0, padx=10, pady=5)
gender_var = tk.StringVar()
gender_var.set("male")
gender_dropdown = ttk.Combobox(window, textvariable=gender_var, values=["male", "female"])
gender_dropdown.grid(row=3, column=1, padx=10, pady=5)

tk.Label(window, text="Smoker:").grid(row=4, column=0, padx=10, pady=5)
smoker_var = tk.StringVar()
smoker_var.set("no")
smoker_dropdown = ttk.Combobox(window, textvariable=smoker_var, values=["no", "yes"])
smoker_dropdown.grid(row=4, column=1, padx=10, pady=5)

tk.Label(window, text="Age:").grid(row=0, column=0, padx=10, pady=5)
age_entry = tk.Entry(window)
age_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="BMI:").grid(row=1, column=0, padx=10, pady=5)
bmi_entry = tk.Entry(window)
bmi_entry.grid(row=1, column=1, padx=10, pady=5)

tk.Label(window, text="Age:").grid(row=0, column=0, padx=10, pady=5)
age_entry = tk.Entry(window)
age_entry.grid(row=0, column=1, padx=10, pady=5)

tk.Label(window, text="BMI:").grid(row=1, column=0, padx=10, pady=5)
bmi_entry = tk.Entry(window)
bmi_entry.grid(row=1, column=1, padx=10, pady=5)

# Button to open BMI calculator
bmi_calculator_button = tk.Button(window, text="Don't know your BMI?", command=open_bmi_calculator)
bmi_calculator_button.grid(row=1, column=2, padx=10, pady=5)

# Run Tkinter event loop
window.mainloop()



                                    






        








