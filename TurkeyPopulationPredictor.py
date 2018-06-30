from matplotlib import pyplot as plt
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
"""
This is a basic program that can predict Turkey's population in the future using a Linear Regression model.
"""

#Getting the input
while True:
    try:
        inp = int(input("Enter a year after 2017: "))
        if inp <= 2017:
            print("Please enter a year in the future. Try again.")
        else:
            break
    except ValueError:
        print("Not a valid input. Try again.")

pop_data = pd.read_excel("TurkeyPopulationChart.xlsx", headers=None)
plt.plot(pop_data["Year"], pop_data["Population"], linewidth=4)
plt.legend()
plt.xlabel("Year")
plt.ylabel("Population")
plt.title("Population in Turkey")

reg = LinearRegression()
x_train, x_test, y_train, y_test = model_selection.train_test_split(pop_data['Year'].to_frame(),
                                                                    pop_data['Population'].to_frame())
reg.fit(x_train, y_train)
print("Prediction: ", reg.predict(inp))
plt.show()
