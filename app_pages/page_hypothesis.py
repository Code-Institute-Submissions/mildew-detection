import streamlit as st


def page_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"* We suspect powdery mildew leaves conatin white streaks on them, "
        f"typically in along the leaf veins, that can differentiate, from a healthy leaves. \n\n"
        f"* An Image Montage, shows that typically a parasitized cell has white streaks. "
        f"Average Image, Variability Image and Difference between Averages shows a deeper green on"
        f" the leaves compared to the mildew leaves"
    )