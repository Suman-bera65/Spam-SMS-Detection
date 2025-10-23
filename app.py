import streamlit as st
import pickle
import nltk
import string
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer

# Ensure NLTK dependencies are downloaded
nltk.download('punkt')
nltk.download('stopwords')

# Initialize stemmer
ps = PorterStemmer()

# Text preprocessing function
def transform_text(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)

# -------------------------------
# Load trained model and vectorizer
# -------------------------------
try:
    with open("vectorizer.pkl", "rb") as f:
        tfidf = pickle.load(f)
    with open("model.pkl", "rb") as f:
        model = pickle.load(f)
except Exception as e:
    st.error(f"Error loading model/vectorizer: {e}")
    st.stop()

# -------------------------------
# Streamlit UI
# -------------------------------
st.title("📩 Email / SMS Spam Classifier")

input_sms = st.text_input("Enter the message")

if st.button("Predict"):
    if input_sms.strip() == "":
        st.warning("Please enter a message before predicting.")
    else:
        # 1. Preprocess
        transform_sms = transform_text(input_sms)

        # 2. Vectorize
        vector_input = tfidf.transform([transform_sms])

        # 3. Predict
        result = model.predict(vector_input)[0]

        # 4. Display
        if result == 1:
            st.error("🚨 Spam Message Detected!")
        else:
            st.success("✅ This message is not spam.")


