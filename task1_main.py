import pandas as pd
import pycountry_convert as pc
pd.options.mode.chained_assignment = None
pd.set_option("display.max_rows", None, "display.max_columns", None)

def average_age(data_frame):

  print("\nAverage age of developers when they wrote their first line of code is :\n")
  print('%.2f'%(data_frame["Age1stCode"].apply(pd.to_numeric, errors = 'coerce').dropna().mean())) #1st

def python_developers(data_frame):

  print("\nPercentage of developers who know python in each country is :")
  print(round(data_frame[data_frame['LanguageWorkedWith'].str.contains('Python',na = False)].groupby('Country').LanguageWorkedWith.count().div(data_frame.groupby('Country').count()['Respondent']).dropna()*100,2)) #2



def average_salary(data_frame2):

  print("\nAverage salary of developer based on continent in USD is :")
  print(round(data_frame2.groupby('Continent')['ConvertedComp'].mean(),2)) #3
  

def desired_language(data_frame):

  print("\nMost desired programming language for the year 2020 is :\n")
  print(data_frame['LanguageDesireNextYear'].str.split(';', expand = True).stack().value_counts().idxmax()) #--4
  
def hobby_coders(data_frame,data_frame2):

  print("\nDistribution of people who code as a hobby based on gender and continent in % is :")
  

  data_frame2 = data_frame2[data_frame2.Hobbyist != 'No']
  
  data_frame2.loc[(data_frame2['Gender'] != 'Man')& (data_frame2['Gender'] != 'Woman'),'Gender']='Others'


  print(round(data_frame2.groupby(['Continent','Gender'])['Hobbyist'].count().div(data_frame2.groupby(['Continent'])['Gender'].count())*100,2)) #5

def satisfaction(data_frame,data_frame2):
  
  
  data_frame2.loc[(data_frame2['Gender'] != 'Man')& (data_frame2['Gender'] != 'Woman'),'Gender']='Others'
 
  print("\nCareer Satisfaction based on Continent and Gender in % :\n")
  print(round(data_frame2.groupby(['Continent','Gender','CareerSat'])['CareerSat'].count().div(data_frame2.groupby(['Continent'])['CareerSat'].count())*100,2))
  
  print("\nJob Satisfaction based on Continent and Gender in % :\n")
  print(round(data_frame2.groupby(['Continent','Gender','JobSat'])['JobSat'].count().div(data_frame2.groupby(['Continent'])['JobSat'].count())*100,2))

#if __name__ == '__main__':
try:  
    data_frame = pd.read_csv('survey_results_public.csv')
except:
    print("Error reading data")
data_frame2=data_frame[['Country','ConvertedComp']].copy()
data_frame2['Hobbyist'] = data_frame[['Hobbyist']].copy()
data_frame2['Gender'] = data_frame[['Gender']].copy()
data_frame2['CareerSat'] = data_frame[['CareerSat']].copy()
data_frame2['JobSat'] = data_frame[['JobSat']].copy()
data_frame2['Continent']=None
count=0

for row in data_frame2['Country']:
    try:
        country_code = pc.country_name_to_country_alpha2(row, cn_name_format="default")
        continent_name = pc.country_alpha2_to_continent_code(country_code)
        country_continent_name = pc.convert_continent_code_to_continent_name(continent_name)
        data_frame2['Continent'][count]=country_continent_name
        count+=1
    except:
          pass

#Below code can be used for manually checking results of each function
'''while True:
    print("\n\n\nSelect options from below to view report:\n"\
    "\n1. Average age of developers when they wrote their first line of code\n"\
    "2. Percentage of developers who know python in each country\n"\
    "3. Average salary of developer based on continent\n"\
    "4. Most desired programming language for the year 2020\n"\
    "5. Distribution of people who code as a hobby based on gender and continent\n"\
    "6. Report for job and career satisfaction of developer based on their gender and continent\n"\
    "7. Exit\n")
    option = int(input('Option:'))
    if option == 1:
      average_age(data_frame)
      
    elif option == 2:
      python_developers(data_frame)
    elif option == 3:
      average_salary(data_frame2)
    elif option == 4:
      desired_language(data_frame)
    elif option == 5:
      hobby_coders(data_frame,data_frame2)
    elif option == 6:
      satisfaction(data_frame,data_frame2)
    elif option == 7:
      exit()
    else: 
      print("Invalid option selected")'''
    

