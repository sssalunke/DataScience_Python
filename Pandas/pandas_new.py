import pandas as pd

# 2 main datatypes
series = pd.Series(["BMW", "Toyota", "Honds"])
series

# Dataframe = 1-dimensional

colours = pd.Series(["Red", "Blue", 'White'])
colours

#Dataframe = 2-dimensional
car_data = pd.DataFrame({"car make": series, "colour": colours})
car_data

#import data
car_sales = pd.read_csv("car-sales.csv")
car_sales


# Exporting a Dataframe
car_sales.to_csv("exported-car-sales.csv", index = False)

exported_car_sales = pd.read_csv("exported-car-sales.csv")
exported_car_sales

## Describe Data
# Attribute
car_sales.dtypes

car_sales.columns

car_columns = car_sales.columns
car_columns

car_sales.index

car_sales

car_sales.describe()

car_sales.info()

car_sales.mean()

car_sales.sum()

car_sales["Doors"].sum()

len(car_sales)


## Viewing And Selecting Data

car_sales.head()

car_sales.head(7)

car_sales.tail()


# .loc and .iloc

animals = pd.Series(["cat", "dog", "bird", "panda", "snake"], index = [0, 3, 9, 8, 3])
animals


# .loc refers to index
animals.loc[3]

animals.loc[9]

car_sales

car_sales.loc[3]

animals

# .iloc refers to position
animals.iloc[3]

animals.iloc[:3]  #upto 3

car_sales.loc[:3]

car_sales.head(4)  #same .loc

car_sales

car_sales["Make"]

car_sales.Colour

car_sales["Odometer (KM)"]

car_sales[car_sales["Make"] == "Toyota"]

car_sales[car_sales["Odometer (KM)"] > 100000]

pd.crosstab(car_sales["Make"], car_sales["Doors"])

# Groupby
car_sales.groupby(["Make"]).mean()

%matplotlib inline
import matplotlib.pyplot as plt

car_sales["Odometer (KM)"].plot()

car_sales["Odometer (KM)"].hist()

car_sales

car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '').astype(int)

car_sales # Remove $ sign

car_sales['Price'].plot()

## Manipulating Data

car_sales["Make"].str.lower() # lowercase

car_sales

car_sales["Make"] = car_sales["Make"].str.lower()

car_sales

car_sales_missing = pd.read_csv("car-sales-missing-data.csv")
car_sales_missing

car_sales_missing["Odometer"].mean()

car_sales_missing["Odometer"].fillna(car_sales_missing["Odometer"].mean(), inplace = True)

car_sales_missing

car_sales_missing.dropna(inplace = True)

car_sales_missing

car_sales_missing = pd.read_csv("car-sales-missing-data.csv")
car_sales_missing

car_sales_missing_dropped = car_sales_missing.dropna()
car_sales_missing_dropped

car_sales_missing_dropped.to_csv("car_sales_missing_dropped.csv")



car_sales

# column from series
seats_column = pd.Series([5, 5, 5, 5, 5])


# New column called seats
car_sales["Seats"] = seats_column
car_sales

car_sales["Seats"].fillna(5, inplace = True)

car_sales

#column from python list
fuel_economy = [7.5, 9.2, 5.0, 9.6, 8.7, 4.7, 7.6, 8.7, 3.0, 4.5]
car_sales["Fuel per 100KM"] = fuel_economy
car_sales

car_sales["Total_fuel_used"] = car_sales["Odometer (KM)"]/100 * car_sales["Fuel per 100KM"]

car_sales

car_sales["Total_fuel_used (L)"] = car_sales["Odometer (KM)"]/100 * car_sales["Fuel per 100KM"]

car_sales

# Create a column from single value
car_sales["Number of wheels"] = 4
car_sales

car_sales["Passed road saftey"] = True
car_sales.dtypes

car_sales

car_sales = car_sales.drop("Total_fuel_used", axis = 1) 

car_sales

car_sales_shuffled = car_sales.sample(frac = 1)

car_sales_shuffled

car_sales_shuffled.reset_index()



























