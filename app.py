import streamlit as st
from app_pages.multi_page import MultiPage

from app_pages.page_project_summary import page_summary_body
from app_pages.page_hypothesis import page_hypothesis_body
from app_pages.leaf_visualizer import page_leaf_visualizer_body

app = MultiPage(app_name = "Powdery Mildew Detector")

app.add_page("Quick Project Summary", page_summary_body)
app.add_page("Hypothesis and Visualization", page_hypothesis_body)
app.add_page("Cherry Leaf Visualizer", page_leaf_visualizer_body)

app.run()