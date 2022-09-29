import streamlit as st
import matplotlib.pyplot as plt
from matplotlib.image import imread
from src.machine_learning.evaluate import load_test_evaluation

def page_performance_body():
    version = 'v1'
    output_dir = f"outputs/{version}/"

    st.write("### Train, Validation and Test set: Label Frequencies")

    labels_distribution = plt.imread(f"{output_dir}labels_distribution.png")
    st.image(labels_distribution,
             caption="Label Distribution on Train, Validation and Test sets")
    st.info(f"* The original dataset has a total 2104 images labelled **healthy**"
            f" and 2104 image files labelled powder_mildew\n\n"
            f"* The dataset was split into train, validation and test set in the ratio 0.7, 0.2 and 0.1.")
    st.write('---')

    if st.checkbox("Model History"):
        st.write('### Model History')
        col1, col2 = st.beta_columns(2)
        with col1:
            model_acc = plt.imread(f'{output_dir}model_training_acc.png')
            st.image(model_acc, caption="Model Training Accuracy")
        with col2:
            model_loss = plt.imread(f'{output_dir}model_training_losses.png')
            st.image(model_loss, caption='Model Training Losses')
        st.write('---')

    st.write('### Generalised Performance on Test Set')
    load_test_evaluation(version)
