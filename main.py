
import streamlit as st
import pandas as pd
from tensorflow.keras.models import load_model

# Create a DataFrame for the first 10 instances with the correct features
df_instances = pd.DataFrame({
    'URLLength': [21, 21, 23, 21, 30, 35, 30, 44, 22, 20, 27, 32],
    'DomainLength': [14, 15, 16, 14, 23, 28, 23, 24, 15, 13, 20, 26],
    'IsDomainIP': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'TLD': [0, 0, 0, 39, 16, 0, 0, 0, 10, 0, 0, 61],
    'URLSimilarityIndex': [100, 73.8292011, 100, 100, 100, 100, 100, 42.14631298, 100, 100, 100, 57.51391466],
    'CharContinuationRate': [1, 1, 1, 1, 0.5625, 1, 0.733333333, 0.6, 0.75, 1, 1, 1],
    'TLDLegitimateProb': [0.5229071, 0.5229071, 0.5229071, 0.0384199, 0.0100856, 0.5229071, 0.5229071, 0.5229071, 0.0230451, 0.5229071, 0.5229071, 0.0075051],
    'URLCharProb': [0.052581297, 0.059010196, 0.062429253, 0.059441525, 0.053810581, 0.057332855, 0.060975837, 0.055578119, 0.057455005, 0.058993718, 0.057183875, 0.056363497],
    'TLDLength': [3, 3, 3, 3, 2, 3, 3, 3, 2, 3, 3, 4],
    'NoOfSubDomain': [1, 1, 1, 1, 3, 1, 1, 1, 2, 1, 1, 1],
    'HasObfuscation': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'NoOfObfuscatedChar': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'LetterRatioInURL': [0.381, 0.429, 0.435, 0.381, 0.5, 0.629, 0.533, 0.727, 0.364, 0.35, 0.519, 0.625],
    'NoOfQMarkInURL': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'IsHTTPS': [1, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    'LineOfCode': [1327, 2, 414, 319, 575, 1442, 467, 2, 561, 649, 1017, 2],
    'LargestLineLength': [15133, 2826, 924, 406, 2426, 2686, 187, 132, 1820, 16721, 563, 41],
    'HasTitle': [1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0],
    'DomainTitleMatchScore': [100, 100, 100, 100, 0, 100, 0, 0, 0, 100, 100, 0],
    'HasFavicon': [0, 0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 0],
    'Robots': [1, 0, 1, 0, 0, 0, 0, 0, 1, 1, 0, 0],
    'IsResponsive': [1, 1, 1, 0, 1, 1, 0, 0, 1, 1, 0, 0],
    'NoOfURLRedirect': [0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    'NoOfSelfRedirect': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'HasDescription': [0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 0],
    'NoOfPopup': [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'NoOfiFrame': [0, 0, 0, 0, 1, 19, 0, 0, 1, 0, 0, 0],
    'HasExternalFormSubmit': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    'HasSocialNet': [1, 0, 0, 1, 1, 1, 0, 0, 1, 1, 1, 1],
    'HasSubmitButton': [1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0],
    'HasHiddenFields': [1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0],
    'HasPasswordField': [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    'Bank': [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    'Pay': [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    'Crypto': [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    'HasCopyrightInfo': [1, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0],
    'NoOfImage': [40, 0, 8, 8, 8, 22, 14, 0, 16, 13, 47, 0],
    'NoOfCSS': [28, 0, 0, 1, 5, 3, 5, 0, 8, 8, 0, 0],
    'NoOfJS': [44, 1, 0, 0, 15, 25, 5, 0, 16, 12, 1, 0],
    'NoOfSelfRef': [1, 1, 71, 0, 117, 59, 7, 0, 122, 41, 1, 0],
    'NoOfEmptyRef': [11, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0]
})

# Load the trained Keras model
model = load_model('phishing_model.h5')

# Streamlit app title
st.title("Phishing URL Classification")

# Display the first 10 instances as a table
st.subheader("Select an Instance from the Table Below")
st.dataframe(df_instances)

# Allow user to select a row by index
selected_row = st.selectbox('Select an instance for prediction:', df_instances.index)

# Extract the selected instance
instance = df_instances.iloc[selected_row:selected_row+1].values

# Ensure the instance shape matches the model's input shape
instance = instance[:, :41]  # Adjust this if the model expects 41 features

# Make prediction on the selected instance
prediction_prob = model.predict(instance)
predicted_label = (prediction_prob > 0.5).astype(int)

# Display the prediction
st.subheader('Prediction')
if predicted_label[0][0] == 1:
    st.write('This URL is classified as **Phishing**.')
else:
    st.write('This URL is classified as **Legitimate**.')

# Display the selected instance
st.subheader('Selected Instance Features')
st.write(df_instances.iloc[selected_row:selected_row+1])
