import streamlit as st
import tensorflow as tf

st.set_option('deprecation.showfileUploaderEncoding', False)
@st.cache(allow_output_mutation=True)
def load_model():
    model=tf.keras.models.load_model('/Users/jonniebrown/Documents/Flatiron/Capstone/half_binary_model.hdf5')
    return model
model=load_model()
st.write("# Diabetic Retinopathy Detector")
st.write("### Upload an image similar to the one shown below to see if it contains DR")

st.image("/Users/jonniebrown/Documents/Flatiron/Capstone/diabetic-retinopathy-detection/Data/train_subset/33_left.jpeg")

file=st.file_uploader("Please upload a retinal image")
import cv2
from PIL import Image, ImageOps
import numpy as np
def import_and_predict(image_data, model):
    
    size = (32,32)
    image=ImageOps.fit(image_data, size, Image.ANTIALIAS)
    img=np.asarray(image)
    img_reshape=img[np.newaxis,...]
    prediction=model.predict(img_reshape)
    
    return prediction
if file is None:
    st.text("Please upload an image file")
else:
    image=Image.open(file)
    st.image(image, use_column_width=True)
    predictions = import_and_predict(image, model)
    class_names = ["does not have DR", "has DR"]
    string = "This image most likely " +class_names[np.argmax(predictions)]
    st.success(string)
