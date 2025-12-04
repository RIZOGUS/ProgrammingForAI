# House Price Prediction - Beginner Friendly

A simple machine learning project to predict house prices using the California Housing dataset (built-in with scikit-learn).

## 📋 Overview

This project demonstrates a complete machine learning workflow for beginners:
- Loading a built-in dataset (no downloads needed!)
- Exploring and visualizing data
- Training multiple ML models
- Comparing model performance
- Making predictions

## 🚀 Features

- **No Data Download Required**: Uses scikit-learn's built-in California Housing dataset
- **Beginner-Friendly**: Simple, clean code with clear explanations
- **Two Models**: Linear Regression and Random Forest
- **Visual Results**: Charts showing model performance
- **Step-by-Step**: 9 easy-to-follow steps

## 📦 Requirements

Install the required packages:

```bash
pip install -r requirements.txt
```

The main dependencies are:
- pandas
- numpy
- matplotlib
- scikit-learn
- jupyter

## 🎯 Quick Start

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Open Jupyter Notebook**:
   ```bash
   jupyter notebook
   ```

3. **Run the notebook**:
   - Open `house_price_prediction_simple.ipynb`
   - Run all cells (Cell → Run All)

## 📊 Dataset Information

The California Housing dataset contains:
- **20,640 samples** (houses in California)
- **8 features**: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
- **Target**: Median house value (in $100,000s)

## 🔍 What You'll Learn

1. **Data Loading**: How to load built-in datasets
2. **Data Exploration**: Understanding your data with statistics and visualizations
3. **Data Preparation**: Splitting data into training and testing sets
4. **Model Training**: Training Linear Regression and Random Forest models
5. **Model Evaluation**: Comparing models using MAE and R² scores
6. **Predictions**: Making predictions on new data

## 📈 Results

The notebook compares two models:
- **Linear Regression**: Simple baseline model
- **Random Forest**: More advanced ensemble model

Typical results:
- Random Forest usually achieves ~81% R² score
- Linear Regression typically achieves ~58% R² score

## 🎓 Understanding the Metrics

- **MAE (Mean Absolute Error)**: Average prediction error (lower is better)
- **R² Score**: How well the model fits the data (closer to 1.0 is better)

**Note**: Prices are in units of $100,000 (e.g., 2.5 = $250,000)

## 📝 Project Structure

```
PFAI/
├── house_price_prediction_simple.ipynb  # Main notebook
├── requirements.txt                      # Python dependencies
└── README.md                            # This file
```

## 🤝 Contributing

This is a beginner-friendly learning project. Feel free to:
- Experiment with different models
- Try feature engineering
- Adjust hyperparameters
- Add more visualizations

## 📚 Next Steps

After completing this project, you can:
1. Try the Kaggle House Prices competition
2. Experiment with other datasets
3. Learn about feature engineering
4. Explore deep learning models

## ⚠️ Notes

- All prices are in $100,000 units
- The dataset is from 1990 California census data
- This is for educational purposes only

## 📧 Support

If you encounter any issues:
1. Make sure all dependencies are installed
2. Check that you're using Python 3.6+
3. Verify Jupyter Notebook is properly installed

---

**Happy Learning! 🎉**
