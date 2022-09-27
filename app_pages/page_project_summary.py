import streamlit as st


def page_summary_body():
    st.write("### Quick Project Summary")

    st.info(
        f"**Problem Statement**\n"
        f"* The cherry plantation crop from Farmy & Foods is facing a challenge where their " 
        f"cherry plantations have been presenting powdery mildew. Currently, the process is "
        f"to manually verify if a given cherry tree contains powdery mildew."
        f"\nAn employee spends around 30 minutes in each tree, taking a few samples of tree leaves and" 
        f"verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew,"
        f"the employee applies a specific compound to kill the fungus. The time spent applying"
        f"this compound is 1 minute.  The company has thousands of cherry trees located in multiple" 
        f"farms across the country. As a result, this manual process is not scalable due to time "
        f"spent in the manual process inspection.\n\n"
        f"**Project Dataset**\n"
        f"* The available dataset taken from the client's crop field contains 4208 images "
        f"of healthy and powdery mildew cherry leaves"
    )

    st.write("#### Business Requirements")
    st.success(
        f"The project has 2 business requirements:\n\n"
        f"The client is interested in: "
        f"* 1 - conducting a study to visually differentiate a cherry leaf "
        f"that is healthy and that contains powdery mildew "
        f"* 2 - predicting if a cherry leaf is healthy or contains powdery mildew."
    )
