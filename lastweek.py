import pickle
import warnings
import streamlit as st

warnings.filterwarnings("ignore")
from PIL import Image

picklein = open("model_iris.pkl","rb")
classifier = pickle.load(picklein)

def predictiris_variety(sepal_length,sepal_width,petal_length,petal_width):
    prediction = classifier.predict([[sepal_length,sepal_width,petal_length,petal_width]])
    print(prediction)
    return prediction

def Input_Output():
    st.title("Iris Variety Prediction")
    st.image("https://machinelearninghd.com/wp-content/uploads/2021/03/iris-dataset.png", width=600)

    st.markdown("You are using Streamlit...",unsafe_allow_html=True)
    sepal_length = st.text_input("Enter Sepal Length" ,".")
    sepal_width = st.text_input("Enter Sepal width" ,".")
    petal_length = st.text_input("Enter Petal Length" ,".")
    petal_width = st.text_input("Enter Petal width" ,".")

    result = ""
    if st.button("Click here to Predict"):
        result = predictiris_variety(sepal_length, sepal_width, petal_length, petal_length)
        st.balloons()
    st.success('The output is {}' .format(result))

if __name__ == '__main__':
    Input_Output()