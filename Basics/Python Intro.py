myAge = 32
print(myAge)

myAge = 33
print(myAge)

print(myAge/3)

myAge = myAge + 1
print(myAge)

# 1) Create a variable called "restaurantBill" and set its value to 36.17
# 2) Create a variable called "serviceCharge" and set its value to 0.125
# 3) Print out the amount of tip
restaurantBill = 36.17
serviceCharge = 0.125
print(restaurantBill*serviceCharge)

print(type(33))

print(type(33.6))

print(type('Philipp'))

print(type(myAge))

print(type(restaurantBill))

myName = 'Philipp'
print(type(myName))

firstPrime = 1
secondPrime = 2
thirdPrime = 3

primeNumbers = [3, 7, 61, 29, 199]
print(type(primeNumbers))

coolPeople = ['Jay Z', 'Ghandi', 'me']
primeAndPeople = ['King Arthur', 17, 11, 'Jennifer Lopez']
print(type(primeAndPeople))

primeNumbers[2]

bestPrimeEver = primeNumbers[4]
print(bestPrimeEver)

import pandas as pd
data = pd.read_csv('lsd_math_score_data.csv')
print(data)

print(type(data))

onlyMathScores = data['Avg_Math_Test_Score']
print(onlyMathScores)

data['Test_Subject'] = 'Jennifer Lopez'


print(data)

data['High_Score'] = 100


print(data)

# Overwrite values in rows for High_Score to equal average score + 100
data['High_Score'] = data['High_Score'] + data['Avg_Math_Test_Score']
print(data)

# Square the values stored inside High_Score
data['High_Score'] = data['High_Score'] ** 2
print(data)

print(type(onlyMathScores))

# Create a list called columnList. Put 'LSD_ppm' and 'Avg_Math_Test_Score' inside.
# columnList = ['LSD_ppm', 'Avg_Math_Test_Score']
cleanData = data[['LSD_ppm', 'Avg_Math_Test_Score']]
print(cleanData)

print(type(cleanData))

y = data[['Avg_Math_Test_Score']]

print(type(y))

# 1) Create a variable called X
# Set X equal to the values of LSD_ppm
# Make sure X is a dataframe
# 2) print the value of X
# 3) show the type of X
X = data[['LSD_ppm']]
print(X)
print(type(X))

del data['Test_Subject']
print(data)

# Delete High_Score column from data
del data['High_Score']
print(data)

import life as hitchhikersGuide

print(type(hitchhikersGuide))

hitchhikersGuide.theAnswer

# 1) import math module 2) print out value of pi 3) print out value of e
import math
math.pi

math.e

from life import theAnswer

myFavouriteNumber = theAnswer
print(myFavouriteNumber)

theAnswer = theAnswer + 1

print(theAnswer)

hitchhikersGuide.theAnswer

import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

def get_milk():
    print('Open door')
    print('Walk to the store')
    print('Buy milk on the ground floor')
    print('Return with milk galore')

get_milk()

def fill_the_fridge(amount):
    print('Open door')
    print('Walk to the store')
    print('Buy ' + amount + ' cartons on the ground floor')
    print('Return with milk galore')

fill_the_fridge('five')

fill_the_fridge('one thousand')

def milk_mission(amount, destination):
    print('Open door')
    print('Walk to the ' + destination)
    print('Buy ' + amount + ' cartons on the ground floor')
    print('Return with milk galore')

milk_mission('twenty', 'department store')

def times(a, b):
    # result = a*b
    return a*b

test = times(3.14, 5.09)
print(test)

times('Ni',4)

import this

hitchhikersGuide.quote_marvin()

myAge = 'Two Hundred'
print(type(myAge))

myAge = 20.53
print(type(myAge))

result = hitchhikersGuide.square_root(63.14)
print(result)

time = data[['Time_Delay_in_Minutes']]
LSD = data[['LSD_ppm']]
score = data[['Avg_Math_Test_Score']]

%matplotlib inline

plt.title('Tissue concentration of LSD over time', fontsize=17)
plt.xlabel('Time in Minutes', fontsize=14)
plt.ylabel('Tissue LSD ppm', fontsize=14)
plt.text(x=0, y=-0.5, s='Wagner et al. (1968)', fontsize=12)
plt.xticks(fontsize=14)
plt.yticks(fontsize=14)

plt.ylim(1,7)
plt.xlim(0,500)

plt.style.use('classic')

plt.plot(time, LSD, color='#e74c3c', linewidth=3)
plt.show()

regr = LinearRegression()
regr.fit(LSD, score)
print('Theta1 : ', regr.coef_[0][0])
print('Intercept: ', regr.intercept_[0])
print('R-Square: ', regr.score(LSD, score))
predicted_score = regr.predict(LSD)


%matplotlib inline

# Add title 'Arithmetic vs LSD-25'
# Add label on X Axis 'Tissue LSD ppm'
# Add label on Y Axis 'Performance Score'
plt.title('Arithmetic vs LSD-25', fontsize=17)
plt.xlabel('Tissue LSD ppm', fontsize=14)
plt.ylabel('Performance Score', fontsize=14)
plt.ylim(25, 85)
plt.xlim(1, 6.5)
plt.style.use('fivethirtyeight')

plt.scatter(LSD, score, color='blue', s=100, alpha=0.7)
plt.plot(LSD, predicted_score, color='red', linewidth=3)
plt.show()


