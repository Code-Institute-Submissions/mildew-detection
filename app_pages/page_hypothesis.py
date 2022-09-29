import streamlit as st


def page_hypothesis_body():
    st.write("### Project Hypothesis and Validation")

    st.info(
        f"**Hypothesis**\n\n"
        f"* The cherry leaves that have powdery mildew contains white streaks on them.\n\n"
    )
    st.success(
        f"**Validation**\n\n"
        f"* An Image Montage, shows that typically a leaf containing powdery mildew have white streak on them.\n\n"
        f"* Average Image, Variability Image and Difference between Averages shows a deeper green on"
        f" the leaves compared to the mildew leaves\n\n"
        f"Select the **Cherry Leaf Visualizer** checkbox on the sidebar "
        f"to view the Image Montage, Average and variability of image."
    )