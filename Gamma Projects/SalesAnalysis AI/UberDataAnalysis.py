import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt

# Load the data
cab_data = pd.read_csv("cab_rides.csv")

# Convert time_stamp to datetime and create day and hour columns
cab_data['date_time'] = pd.to_datetime(cab_data['time_stamp'])
cab_data['day'] = cab_data.date_time.dt.day
cab_data['hour'] = cab_data.date_time.dt.hour

# Remove rows with NaN values
cab_data.dropna(inplace=True)

# Encode categorical variables
cab_data = pd.get_dummies(cab_data, columns=['cab_type', 'destination', 'source'], drop_first=True)

# Select features and target variable
x = cab_data[['distance', 'surge_multiplier', 'day', 'hour'] + [col for col in cab_data.columns if col.startswith('cab_type_') or col.startswith('destination_') or col.startswith('source_')]]
y = cab_data['price']

# Split the data into training and testing sets
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.25, random_state=42)

# Train the Linear Regression model
linear = LinearRegression()
linear.fit(x_train, y_train)

# Make predictions
predictions = linear.predict(x_test)

# Create a DataFrame to compare actual and predicted values
df = pd.DataFrame({'Actual': y_test, 'Predicted': predictions})
print(df)

# Plot the first 25 actual vs predicted values
df1 = df.head(25)
df1.plot(kind='bar', figsize=(26, 10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.show()
