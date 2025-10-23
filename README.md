# Spam SMS Detection

This is a machine learning project that classifies SMS messages as either "spam" or "ham" (not spam).

The project includes a full data processing pipeline, model training, and a simple web application built with Streamlit to perform real-time predictions.

## 🚀 Features

* **Text Preprocessing:** Cleans and prepares text data using NLTK (lowercase, tokenization, removing stopwords, stemming).
* **Feature Extraction:** Converts text into numerical vectors using TF-IDF.
* **Model Training:** Benchmarks over 10 different classifiers (including Naive Bayes, Logistic Regression, and XGBoost) to find the best-performing model.
* **Web App:** A simple UI built with Streamlit to enter a message and get a prediction.

## 💻 Technologies Used

* **Python 3**
* **Streamlit:** For the web app UI
* **Scikit-learn:** For model training and evaluation
* **NLTK (Natural Language Toolkit):** For text preprocessing
* **Pandas:** For data manipulation
* **Matplotlib / Seaborn:** For data visualization (in the notebook)
* **WordCloud:** For visualizing word frequencies

## 🏃 How to Run This Project

You can run this application locally by following these steps:

**1. Clone the repository:**
   ```bash
   git clone [https://github.com/Suman-bera65/Spam-SMS-Detection.git](https://github.com/Suman-bera65/Spam-SMS-Detection.git)
   cd Spam-SMS-Detection
