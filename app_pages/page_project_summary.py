import streamlit as st


def page_summary_body():
    st.write("### Quick Project Summary")

    st.info(
        f"**General Information**\n\n"
        f"Powdery mildew is a fungal disease that affects a wide range of plants. Many different species of fungi "
        f"cause powdery mildew diseases in the order of Erysiphales. It is one of the easier plant diseases to "
        f"identify, as its symptoms are quite distinctive. Infected plants display white powdery spots on the leaves"
        f"and stems. The lower leaves are the most affected, but the mildew can appear on any above-ground part "
        f"of the plant. *[Source](https://en.wikipedia.org/wiki/Powdery_mildew)*" 
        )

    st.info(f"Machine learning functionality on this site can help detect cherry leaves infected "
            f"with mildew instantly and with an accuracy of over 97%. Thus taking away the "
            f"manual and time consuming task of mildew identification on cherry leaves\n\n" 
    )
    if st.checkbox("Problem Statement"):
        st.info(
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

    st.write("#### Business Requirement")
    st.success(
        f"The project has 2 business requirements:\n\n"
        f"The client is interested in:\n\n "
        f"* conducting a study to visually differentiate a cherry leaf "
        f"that is healthy and that contains powdery mildew\n"
        f"* predicting if a cherry leaf is healthy or contains powdery mildew."
    )

    st.write(
        f"* For additional information, please visit and **read** the "
        f"[Project README file](https://github.com/valerieoni/mildew-detection).")