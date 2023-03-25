import pandas as pd
from sklearn.linear_model import LinearRegression

# Load the dataset
data = pd.read_csv('fruit_data.csv')

# Extract the independent variables (Methane gas emission, humidity, temperature, and time)
X = data[['timestamp', 'temperature', 'humidity', 'methane']]

# Extract the dependent variable (lifespan)
y = data['lifespan']

# Create a linear regression model
model = LinearRegression()

# Fit the model to the data
model.fit(X, y)

# Predict the lifespan of a new fruit based on its Methane gas emission, humidity, temperature, and time
new_fruit = [[1.2, 50, 25, 10]]
predicted_lifespan = model.predict(new_fruit)

# Print the predicted lifespan of the new fruit
print('The predicted lifespan of the new fruit is: ', predicted_lifespan)
