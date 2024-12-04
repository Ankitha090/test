import matplotlib.pyplot as plt
import pandas as pd
data_set=pd.read_csv(r"D:\Datasets\50_Startups.csv")
x=data_set.iloc[:, :-1].values
y=data_set.iloc[:,-1].values
from sklearn.preprocessing import OneHotEncoder
onehotencoder =OneHotEncoder()
x=onehotencoder.fit_transform(x).toarray()
from sklearn.model_selection import train_test_split
x_train, x_test, y_train, y_test=train_test_split(x, y, test_size= 0.2, random_state=0)
from sklearn.linear_model import LinearRegression
regressor=LinearRegression()
a=regressor.fit(x_train, y_train)
b=regressor.predict(x_test)
print('Train Score: ', regressor.score(x_train, y_train))
print('Test Score: ', regressor.score(x_test, y_test))
plt.scatter(y_test,b)
plt.plot([min(y_test),max(y_test)],[min(y_test),max(y_test)],color='blue')
plt.xlabel('Position Levels')
plt.ylabel('Predicted values')
plt.title('Actual vs. Predicted Values')
plt.show()
