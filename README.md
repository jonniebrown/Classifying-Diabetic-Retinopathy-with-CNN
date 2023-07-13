# Classifying Diabetic Retinopathy with CNN

In this project I use AI to detect the presence of Diabetic Retinopathy in thousands of retinal images provided by eyePACS using a Convolutional Neural Network (CNN). In the end my model had a 73% accuracy score. 

![Image Description](Images/diabetic-retinopathy-vector.jpg)

## Introduction
Diabetic Retinopathy (DR) is a condition that causes vision loss and blindness for people who have diabetes. The longer you have diabetes the more likely you will develop DR. This condition is significant because it’s the leading cause of blindness in adults affecting over 103 million people worldwide. And right now over one third of people with diabetes have this condition. These numbers are predicted to grow. In fact, the number of people with diabetes has doubled every 20 years since 1945. So with more and more people getting diagnosed with diabetes, the more and more people are going to develop DR, and thus, the need to prevent and diagnose will only grow.

## Data
To do this I fed my computer over 35,000 images provided by a company called eyePACS. And the data was split into 5 categories. On a scale from 0-4, 0 being no DR, 1-mild, 2 moderate, 3 severe, 4 proliferative DR. I engineered this to be binary - whether DR is present or not. 
