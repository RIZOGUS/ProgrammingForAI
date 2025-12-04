# Titanic Survival Prediction - Beginner Friendly

A simple classification project to predict passenger survival using a built-in dataset (similar to Spaceship Titanic competition).

## 📋 Overview

This project demonstrates a complete classification workflow for beginners:

- Loading a built-in dataset (no downloads needed!)
- Data exploration and visualization
- Data preprocessing and cleaning
- Training classification models
- Model evaluation and comparison
- Making predictions

## 🚀 Features

- **No Data Download Required**: Uses seaborn's built-in Titanic dataset
- **Beginner-Friendly**: Simple, clean code with clear explanations
- **Two Models**: Logistic Regression and Random Forest
- **Visual Results**: Confusion matrices and feature importance charts
- **Step-by-Step**: 10 easy-to-follow steps

## 📦 Requirements

The main dependencies are:

- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn
- jupyter

Install using:

```bash
pip install -r ../requirements.txt
```

## 🎯 Quick Start

1. **Install dependencies** (if not already installed):

   ```bash
   cd d:\Tasks\PFAI
   pip install -r requirements.txt
   ```

2. **Open Jupyter Notebook**:

   ```bash
   jupyter notebook
   ```

3. **Run the notebook**:
   - Open `titanic_survival_prediction.ipynb`
   - Run all cells (Cell → Run All)

## 📊 Dataset Information

The Titanic dataset contains:

- **891 passengers** in the training data
- **6 main features**: pclass, sex, age, sibsp, parch, fare
- **Target**: survived (0 = No, 1 = Yes)

### Features Explained

- **pclass**: Passenger class (1st, 2nd, 3rd)
- **sex**: Gender (male/female)
- **age**: Age in years
- **sibsp**: Number of siblings/spouses aboard
- **parch**: Number of parents/children aboard
- **fare**: Ticket fare paid

## 🔍 What You'll Learn

1. **Data Loading**: How to load built-in datasets
2. **EDA**: Exploring data with statistics and visualizations
3. **Data Cleaning**: Handling missing values
4. **Feature Engineering**: Converting categorical to numerical data
5. **Model Training**: Training Logistic Regression and Random Forest
6. **Model Evaluation**: Using accuracy, precision, recall, and confusion matrices
7. **Feature Importance**: Understanding which features matter most
8. **Predictions**: Making predictions on new passengers

## 📈 Expected Results

Typical model performance:

- **Logistic Regression**: ~78-80% accuracy
- **Random Forest**: ~80-82% accuracy

Most important features:

1. Sex (gender)
2. Fare (ticket price)
3. Age
4. Passenger class

## 🎓 Understanding the Metrics

- **Accuracy**: Overall percentage of correct predictions
- **Precision**: Of all predicted survivors, how many actually survived
- **Recall**: Of all actual survivors, how many did we predict correctly
- **Confusion Matrix**: Shows true positives, false positives, true negatives, false negatives

## 📝 Project Structure

```
Task-2/
├── titanic_survival_prediction.ipynb  # Main notebook
└── README.md                          # This file
```

## 🤝 Next Steps

After completing this project, you can:

1. Try the actual **Spaceship Titanic** competition on Kaggle
2. Add more features (cabin, embarked, etc.)
3. Try different models (SVM, XGBoost, etc.)
4. Perform hyperparameter tuning
5. Create ensemble models

## 💡 Tips

- Women and children had higher survival rates
- 1st class passengers had better survival chances
- Higher fare usually meant better survival odds
- Age and family size also played important roles

## 📚 Comparison to Spaceship Titanic

This project uses the classic Titanic dataset which is:

- ✅ Built-in (no download needed)
- ✅ Simpler to understand
- ✅ Perfect for learning classification
- ✅ Similar concepts to Spaceship Titanic

The skills you learn here directly apply to the Spaceship Titanic competition!

---

**Happy Learning! 🎉**
