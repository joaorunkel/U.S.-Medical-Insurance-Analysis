import pandas as pd

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






                                    






        








