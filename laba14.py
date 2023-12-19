import json

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


#zadanie 1
def custom_function(x):
    return -5 * np.cos(10 * x) * np.sin(3 * x) / np.sqrt(x)

x_values = np.linspace(0.1, 10, 1000)

y_values = custom_function(x_values)

plt.figure(figsize=(10, 6))
plt.plot(x_values, y_values, label=r'$Y(x)=-\frac{5 \cos(10x) \sin(3x)}{\sqrt{x}}$',
         color='blue', linewidth=2)

plt.xlabel('x')
plt.ylabel('Y(x)')
plt.title('Graph of the Function')
plt.legend()

plt.grid(True)
plt.show()
# zadanie 2


df = pd.read_csv('lab14.csv')

# 2.1
country1 = input("Enter the first country name: ")
country2 = input("Enter the second country name: ")

df_countries = df[df['Country Name'].isin([country1, country2])]

plt.figure(figsize=(10, 6))

for country in [country1, country2]:
    data = df_countries[df_countries['Country Name'] == country]
    plt.plot(data.columns[3:], data.iloc[0, 3:], label=country)

plt.xlabel('Year')
plt.ylabel('GDP Growth (annual %)')
plt.title('GDP Growth Dynamics for Two Countries (2000-2015)')
plt.legend()
plt.show()


# 2.2
countries = df['Country Name'].unique()

user_country = input(f"Enter a country from the list {countries}: ")

if user_country in countries:
    df_country = df[df['Country Name'] == user_country]
    plt.figure(figsize=(8, 6))
    plt.bar(df_country.columns[3:], df_country.iloc[0, 3:])
    plt.xlabel('Year')
    plt.ylabel('GDP Growth (annual %)')
    plt.title(f'GDP Growth for {user_country} (2000-2015)')
    plt.show()
else:
    print("Invalid country. Please enter a valid country name.")

# zadanie 3

with open('data.json') as f:
    data = json.load(f)

# Extract type and students data
types = [entry['type'] for entry in data]
students = [entry['students'] for entry in data]

# Plotting
plt.figure(figsize=(8, 8))
plt.pie(students, labels=types, autopct='%1.1f%%', startangle=140)
plt.title('Distribution of Students by Type')
plt.show()