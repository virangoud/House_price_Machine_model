This project focuses on predicting house prices in metro cities using machine learning. I worked on this notebook originally on Kaggle and then exported it to GitHub. The main objective was to clean the data, perform EDA, engineer useful features, and build different ML models to predict house prices accurately.

The final Stacked Model achieved: Train Accuracy: 89% Test Accuracy: 82%

📌 About the Project

The project includes the full end-to-end workflow of a typical machine learning prediction system:

1.Cleaning raw housing data

2.Removing outliers

3.Converting categorical data into numeric form

4.Engineering additional features

5.Building and comparing different ML models

6.Combining models into a stacked ensemble for better performance

7.Evaluating accuracy and analyzing errors

8.Everything is done inside the Jupyter Notebook.

🛠️ Data Preprocessing

The data preprocessing section includes:
Checking null values and data types
Handling missing values
Cleaning inconsistent entries
Converting categorical values
Feature engineering (e.g., parking, extra space, BHK count, area size)
Removing extreme outliers
Preparing the final dataset for modeling
The cleaned dataset formed the foundation for good model performance.

📊 Exploratory Data Analysis (EDA)

The notebook includes several visualizations and insights, such as:
Price distribution
Square-foot vs Price relationship
Impact of number of bedrooms on price
Location-based comparison
Correlation heatmap
These insights helped guide model selection and feature creation.

🤖 Machine Learning Models
Multiple models were tested, including:
Linear Regression
Xgbooost and LightGBM
Stacked Ensemble Model (Final Model)
The Stacked Model combined predictions from multiple models, which helped improve accuracy and reduce error.

📈 Model Performance
Final Stacked Model Accuracy:
Training Score: 89%
Testing Score: 82%

The stacked model performed better by 1.2 percantage than individual models and showed a good balance of bias and variance.
