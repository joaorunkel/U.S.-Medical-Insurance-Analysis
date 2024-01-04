import pandas as pd


#Creating dataframe from csv file and converting to a dictionary using records orientation
file_path= 'insurance.csv'
df = pd.read_csv(file_path)
data_dict = df.to_dict(orient='records')

num_of_patients = len(data_dict)

#Insights on costs
total_cost= 0

##Calculate total cost
for data in data_dict:
    # Ensure 'charges' key exists and convert it to float
    if 'charges' in data:
        charges_value = float(data['charges'])
        total_cost += charges_value

##Average insurance charges
avg_charges = total_cost / num_of_patients


##Average charge per region

###Northeast
total_northeast = 0
num_northeast_patients = 0
for data in data_dict:
    if data['region'] == 'northeast':
        total_northeast = data['charges'] + total_northeast
        num_northeast_patients += 1

avg_charges_northeast = total_northeast / num_northeast_patients

###Northwest
total_northwest = 0
num_northwest_patients = 0
for data in data_dict:
    if data['region'] == 'northwest':
        total_northwest = data['charges'] + total_northwest
        num_northwest_patients += 1

avg_charges_northwest = total_northwest / num_northwest_patients

###Southeast
total_southeast = 0
num_southeast_patients = 0
for data in data_dict:
    if data['region'] == 'southeast':
        total_southeast = data['charges'] + total_southeast
        num_southeast_patients += 1

avg_charges_southeast = total_southeast / num_southeast_patients

###Southwest
total_southeast = 0
num_southwest_patients = 0
for data in data_dict:
    if data['region'] == 'southeast':
        total_southeast = data['charges'] + total_southeast
        num_southwest_patients += 1

avg_charges_southwest = total_southeast / num_southwest_patients

##Average charges of smokers

total_smokers = 0
num_smoker_patients = 0
for data in data_dict:
    if data['smoker']=='yes':
        total_smokers = data['charges'] + total_smokers
        num_smoker_patients += 1

avg_charges_smokers = total_smokers/num_smoker_patients

##Average charges of each sex

total_men = 0
num_men_patients = 0
total_woman = 0
num_woman_patients = 0
for data in data_dict:
    if data['sex'] == 'male':
        total_men = data['charges'] + total_men
        num_men_patients += 1
    elif data['sex'] == 'female':
        total_woman = data['charges'] + total_woman
        num_woman_patients += 1

avg_charges_men = total_men / num_men_patients
avg_charges_woman = total_woman / num_woman_patients

#Insights on age

##Average age of smokers

total_age_smokers = 0
for data in data_dict:
    if data['smoker']=='yes':
        total_age_smokers = total_age_smokers + data['age']
        
avg_age_smokers = total_age_smokers / num_smoker_patients

##Average age of parents

total_age_parents = 0
num_parents_patients = 0
for data in data_dict:
    if data['children']> 0:
        total_age_parents = total_age_parents + data['age']
        num_parents_patients += 1

avg_parents_age = total_age_parents/num_parents_patients

##Average age per region

###Northeast
total_age_northeast = 0
for data in data_dict:
    if data['region'] == 'northeast':
        total_age_northeast = total_age_northeast + data['age']

avg_age_northeast = total_age_northeast / num_northeast_patients

###Northwest
total_age_northwest = 0
for data in data_dict:
    if data['region'] == 'northwest':
        total_age_northwest = total_age_northwest + data['age']

avg_age_northwest = total_age_northwest / num_northwest_patients

###Southeast
total_age_southeast = 0
for data in data_dict:
    if data['region'] == 'southeast':
        total_age_southeast = total_age_southeast + data['age']

avg_age_southeast = total_age_southeast / num_southeast_patients

###Southwest
total_age_southwest = 0
for data in data_dict:
    if data['region'] == 'southwest':
        total_age_southwest = total_age_southwest + data['age']

avg_age_southwest = total_age_southwest / num_southwest_patients


#Insights on gender

##Counting each gender individuals
females = 0
males = 0
for data in data_dict:
    if data['sex'] == 'female':
        females +=1
    elif data['sex'] == 'male':
        males += 1

##Countig smokers for each gender
num_female_smokers = 0
num_male_smokers = 0
for data in data_dict:
    if data['sex'] == 'female' and data['smoker'] == 'yes':
        num_female_smokers += 1
    elif data['sex'] == 'male' and data['smoker'] == 'yes':
        num_male_smokers += 1

perc_male_smokers = num_male_smokers *100 / num_smoker_patients
perc_female_smokers = num_female_smokers*100/num_smoker_patients


                                    






        








