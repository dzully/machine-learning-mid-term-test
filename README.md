# Airline Customer Satisfaction Prediction

This project aims to predict airline customer satisfaction levels (Satisfaction, Neutral, or Dissatisfaction) using machine learning techniques. The goal is to help airline companies understand the key factors influencing customer satisfaction and make data-driven decisions to improve their services.

## Dataset

The dataset used in this project contains the following features:

- Gender: Gender of the passengers (Female, Male)
- Customer Type: The customer type (Loyal customer, disloyal customer)
- Age: The actual age of the passengers
- Type of Travel: Purpose of the flight of the passengers (Personal Travel, Business Travel)
- Class: Travel class in the plane of the passengers (Business, Eco, Eco Plus)
- Flight distance: The flight distance of this journey
- Inflight Wi-Fi service: Satisfaction level of the inflight Wi-Fi service (0: Not Applicable; 1-5)
- Departure/Arrival time convenient: Satisfaction level of Departure/Arrival time convenient
- Ease of Online booking: Satisfaction level of online booking
- Gate location: Satisfaction level of Gate location
- Food and drink: Satisfaction level of Food and drink
- Online boarding: Satisfaction level of online boarding
- Seat comfort: Satisfaction level of Seat comfort
- Inflight entertainment: Satisfaction level of inflight entertainment
- On-board service: Satisfaction level of On-board service
- Leg room service: Satisfaction level of Leg room service
- Baggage handling: Satisfaction level of baggage handling
- Check-in service: Satisfaction level of Check-in service
- Inflight service: Satisfaction level of inflight service
- Cleanliness: Satisfaction level of Cleanliness
- Departure Delay in Minutes: Minutes delayed when departure
- Arrival Delay in Minutes: Minutes delayed when Arrival

The target variable is:

- Satisfaction: Airline satisfaction level (Satisfaction, neutral or dissatisfaction)

## Approach

1. **Exploratory Data Analysis (EDA)**: Perform EDA to understand the data distribution, handle missing values, and visualize the relationships between features and the target variable.

2. **Feature Engineering**: Create new features or transform existing ones if necessary to improve model performance.

3. **Model Selection**: Evaluate different machine learning models, such as Logistic Regression, Random Forest, and Gradient Boosting, to find the best-performing model for the task.

4. **Model Training and Evaluation**: Split the data into training and testing sets, train the selected model(s) on the training data, and evaluate their performance on the testing data using appropriate evaluation metrics.

5. **Model Interpretation**: Interpret the trained model to understand the importance of different features and their impact on customer satisfaction.

6. **Deployment**: Deploy the best-performing model as a web application or API for real-time prediction of customer satisfaction levels.

## Requirements

- Python 3.x
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Seaborn

## Usage

1. Clone the repository: `git clone https://github.com/username/airline-customer-satisfaction.git`
2. Install the required packages: `pip install -r requirements.txt`
3. Run the Jupyter Notebook or Python script to train the models and make predictions.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](LICENSE).