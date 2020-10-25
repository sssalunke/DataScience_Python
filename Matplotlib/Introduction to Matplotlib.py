# Introduction to Matplotlib

%matplotlib inline
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

plt.plot()

plt.plot();  # ; remove that square bracket

plt.plot()
plt.show()

plt.plot([1, 2, 3, 4])

x = [1, 2, 3, 4]
y = [10,20, 30, 40]
#plt.plot(x, y)
plt.plot(x,y);

plt.plot();

# 1st method
fig = plt.figure()  #create a figure
ax = fig.add_subplot()  # adds some axes
plt.show()

# 2nd method
fig = plt.figure() #creates a figure
ax = fig.add_axes([1, 1, 1, 1])
ax.plot(x, y) # add some data
plt.show()

# 3rd method (recommanded)

fig, ax = plt.subplots()
ax.plot(x, y);  # add some data

fig, ax = plt.subplots()
ax.plot(x, [50, 100, 200, 250]);  # add some data

fig, ax = plt.subplots()
ax.plot(x, [50, 100, 200, 250]);  # add some data
type(fig), type(ax)



# Making  figure with Numpy arrays

We want: 
* Line plot
* Scatter plot
* Bar plot
* Histogram
* Subplot

import numpy as np

# Create some data
x = np.linspace(0, 10, 100)
x

x[:10]

# plot the data and create line plot
fig, ax = plt.subplots()
ax.plot(x, x**2);

# use same data to make scatter plot

fig, ax =plt.subplots()
ax.scatter(x, np.exp(x));

# Another scatter plot

fig, ax = plt.subplots()
ax.scatter(x, np.sin(x))   #  sin info shift+tab

# make a plot from dictoinory

nut_butter_prices = {"Almomd butter": 10,
                    "Peanut butter": 8,
                    "Cashew butter": 12}
fig, ax = plt.subplots()
ax.bar(nut_butter_prices.keys(), nut_butter_prices.values())  #no nedd to write x and y
#ax.bar(nut_butter_prices.keys(), height=nut_butter_prices.values())  #no nedd to write x and y 
ax.set(title = "Dan's Nut Butter Store",
      ylabel = "price ($)");


fig, ax = plt.subplots()
ax.barh(list(nut_butter_prices.keys()), list(nut_butter_prices.values()));


# Make some data for histogram and plot it

x = np.random.randn(1000)
fig, ax = plt.subplots()
ax.hist(x);

# Two action for subplots

# subplots option 1

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(nrows = 2,
                                            ncols = 2,
                                            figsize = (10, 5))

# Plot to each different axis
ax1.plot(x, x/2);
ax2.scatter(np.random.random(10), np.random.random(10));
ax3.bar(nut_butter_prices.keys(), nut_butter_prices.values());
ax4.hist(np.random.randn(1000));

# subplots option 2

fig, ax = plt.subplots(nrows=2,
                      ncols=2,
                      figsize=(10,5))

# plot to each different axis
ax[0, 0].plot(x, x/2);
ax[0, 1].scatter(np.random.random(10), np.random.random(10));
ax[1, 0].bar(nut_butter_prices.keys(), nut_butter_prices.values());
ax[1, 1].hist(np.random.randn(1000));


## Plotting from pandas DataFrames

import pandas as pd

# Make a DataFrame

car_sales = pd.read_csv("car-sales.csv")
car_sales

ts = pd.Series(np.random.randn(1000),
              index = pd.date_range("1/1/2020", periods=1000))
#ts
#ts.plot()

ts = ts.cumsum()
ts.plot()

car_sales

# Replace 
car_sales["Price"] = car_sales["Price"].str.replace('[\$\,\.]', '')
car_sales

type(car_sales)

type(car_sales["Price"][0])

# Remove last two zeros

car_sales["Price"] = car_sales["Price"].str[:-2]
car_sales

# adding column
car_sales["Sale Date"] = pd.date_range("1/1/2020", periods=len(car_sales))
car_sales



car_sales["Total Sales"] = car_sales["Price"].cumsum()
car_sales


car_sales["Total Sales"] = car_sales["Price"].astype(int).cumsum()
car_sales

type(car_sales["Price"][0])

# Let's plot the total sales
car_sales.plot(x = 'Sale Date', y = 'Total Sales');

car_sales.plot(x = 'Odometer (KM)', y = "Price", kind = "scatter");

# How about a bar graph?
x = np.random.rand(10, 4)
x

# Turn it intoa datafframe
df = pd.DataFrame(x, columns=['a', 'b', 'c', 'd'])
df

df.plot.bar();

df.plot(kind="bar");

car_sales

car_sales.plot(x= "Make", y="Odometer (KM)", kind = "bar");

# How about histograms?

car_sales["Odometer (KM)"].plot.hist();

car_sales["Odometer (KM)"].plot(kind="hist");

car_sales["Odometer (KM)"].plot.hist(bins =10);

# Lets try another dataset

heart_disease = pd.read_csv("heart-disease.csv")
heart_disease.head()

heart_disease

# Crete an histogram

heart_disease["age"].plot.hist(bins=20);

heart_disease.head()

heart_disease.plot.hist(figsize = (10,30), subplots = True);

# Which one should you use?(pyplot va matplotlib oo method)

* When plotting something quickly, okay to use the pyplot method
* When plotting something more advanced, use the OO method

heart_disease

heart_disease.head()

over_50 = heart_disease[heart_disease["age"] > 50]
over_50

len(over_50)

over_50.head()

#  pyplot method

over_50.plot(kind = 'scatter',
            x = 'age',
            y = 'chol',
            c = 'target');

# OO method mixed with pyplot method

fix, ax = plt.subplots(figsize=(10,6))
over_50.plot(kind = 'scatter',
            x = 'age',
            y = 'chol',
            c = 'target',
            ax = ax);


fix, ax = plt.subplots(figsize=(10,6))
over_50.plot(kind = 'scatter',
            x = 'age',
            y = 'chol',
            c = 'target',
            ax = ax);

ax.set_xlim([45, 100]);

# OO method with scratch

fig, ax = plt.subplots(figsize = (10, 6))

#plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"]);



over_50.target.values

# OO method with scratch

fig, ax = plt.subplots(figsize = (10, 6))

#plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"]);

#customized the plot
ax.set(title = "Heart Disease and Cholesterol Levels",
      xlabel = "Age",
      ylabel = "Cholesterol");

# Add legend
ax.legend(*scatter.legend_elements(), title = "Target");


# OO method with scratch

fig, ax = plt.subplots(figsize = (10, 6))

#plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"]);

#customized the plot
ax.set(title = "Heart Disease and Cholesterol Levels",
      xlabel = "Age",
      ylabel = "Cholesterol");

# Add legend
ax.legend(*scatter.legend_elements(), title = "Target");

#Add Horizontal line
#ax.axhline(over_50["chol"].mean());      #stright line

#Add Horizontal '--' line
ax.axhline(over_50["chol"].mean(),
          linestyle = '--');           # -- line

over_50.head()

# Subplot of chol, age, thalach
fig, (ax0, ax1) = plt.subplots(nrows = 2,
                              ncols = 1,
                              figsize = (10, 10),
                              sharex = True)

# Add data to ax0

scatter = ax0.scatter(x = over_50["age"],
                     y = over_50["chol"],
                     c = over_50["target"])

# Customize ax0
ax0.set(title = "Heart Disease and Cholesterol Levels",
       xlabel = "Age",
       ylabel = "cholesterol");

# Add a legend to ax0
ax0.legend(*scatter.legend_elements(), title = "Target")

#Add a meanline
ax0.axhline(y = over_50["chol"].mean(),
           linestyle = "--")

# Add data to ax1
scatter = ax1.scatter(x = over_50["age"],
                     y = over_50["thalach"],
                     c = over_50["target"])

#customize ax1 
ax1.set(title = "Heart Diseace and Max Heart Rate",
       xlabel = "Age",
       ylabel = "Max Heart Rate");

# add legend to ax1
ax1.legend(*scatter.legend_elements(), title = "Target")

# Add meanline
ax1.axhline(y = over_50["thalach"].mean(),
           linestyle = "--");

# add title to figure
fig.suptitle("Heart Disease  Analysis", fontsize = 18, fontweight = "bold");

## Customizing matplot plotsand getting stylish

# see the different styles availables
plt.style.available

car_sales

car_sales["Price"].values

car_sales["Total Sales"].plot();

plt.style.use('seaborn-whitegrid')

car_sales["Total Sales"].plot();

plt.style.use('seaborn')

car_sales["Total Sales"].plot();

car_sales.plot(x = "Odometer (KM)", y = "Price", kind = "scatter");

car_sales.plot(x = "Odometer (KM)", y = "Total Sales", kind = "scatter");

plt.style.use('ggplot')

car_sales["Total Sales"].plot();

# Create some data
x = np.random.randn(10, 4)
x

df = pd.DataFrame(x, columns = ['a', 'b', 'c', 'd'] )
df

ax = df.plot();

ax = df.plot(kind = 'bar')
type(ax)

# Customize our plot with the set() method
ax = df.plot(kind = 'bar')

# Add some labels and title
ax.set(title = "Random Number Bar Graph from DataFrame",
      xlabel = "Row Number",
      ylabel = "Random Number")

# Make the legend visible
ax.legend().set_visible(True)


#set the style
plt.style.use("seaborn-whitegrid")

# OO method with scratch

fig, ax = plt.subplots(figsize = (10, 6))

#plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"],
                    cmap='winter');  # this change the color scheme

#customized the plot
ax.set(title = "Heart Disease and Cholesterol Levels",
      xlabel = "Age",
      ylabel = "Cholesterol");

# Add legend
ax.legend(*scatter.legend_elements(), title = "Target");

#Add Horizontal line
#ax.axhline(over_50["chol"].mean());      #stright line

#Add Horizontal '--' line
ax.axhline(over_50["chol"].mean(),
          linestyle = '--');           # -- line

#set the style
plt.style.use("seaborn-whitegrid")

# OO method with scratch

fig, ax = plt.subplots(figsize = (10, 6))

#plot the data
scatter = ax.scatter(x = over_50["age"],
                    y = over_50["chol"],
                    c = over_50["target"]);

#customized the plot
ax.set(title = "Heart Disease and Cholesterol Levels",
      xlabel = "Age",
      ylabel = "Cholesterol");

# Add legend
ax.legend(*scatter.legend_elements(), title = "Target");

#Add Horizontal line
#ax.axhline(over_50["chol"].mean());      #stright line

#Add Horizontal '--' line
ax.axhline(over_50["chol"].mean(),
          linestyle = '--');           # -- line

This plot shows some information about the heart disease dataset....

# Customize the y and x axis limitations

# Subplot of chol, age, thalach
fig, (ax0, ax1) = plt.subplots(nrows = 2,
                              ncols = 1,
                              figsize = (10, 10),
                              sharex = True)

# Add data to ax0

scatter = ax0.scatter(x = over_50["age"],
                     y = over_50["chol"],
                     c = over_50["target"],
                     cmap = "winter")

# Customize ax0
ax0.set(title = "Heart Disease and Cholesterol Levels",
       xlabel = "Age",
       ylabel = "Cholesterol");

#change the x axis limits
ax0.set_xlim([50,80])

# Add a legend to ax0
ax0.legend(*scatter.legend_elements(), title = "Target")

#Add a meanline
ax0.axhline(y = over_50["chol"].mean(),
           linestyle = "--")

# Add data to ax1
scatter = ax1.scatter(x = over_50["age"],
                     y = over_50["thalach"],
                     c = over_50["target"],
                     cmap = 'winter')

#customize ax1 
ax1.set(title = "Heart Diseace and Max Heart Rate",
       xlabel = "Age",
       ylabel = "Max Heart Rate");

# change ax1 x axis limits
ax1.set_xlim([50, 80])
ax1.set_ylim([60, 200])

# add legend to ax1
ax1.legend(*scatter.legend_elements(), title = "Target")

# Add meanline
ax1.axhline(y = over_50["thalach"].mean(),
           linestyle = "--");

# add title to figure
fig.suptitle("Heart Disease  Analysis", fontsize = 18, fontweight = "bold");

fig

fig.savefig("heart-disease-analysis-plot-saved-with-code.png")

