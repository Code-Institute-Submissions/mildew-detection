import streamlit as st
import os
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.image import imread
import seaborn as sns
import itertools
import random

def page_leaf_visualizer_body():
    version = 'v1'
    output_dir = f"outputs/{version}"

    st.write('### Cherry Leaf Visualizer')
    st.info(
        f"The client is interested in visually differentiating a cherry leaf "
        f"that is healthy from that which contains powdery mildew."
    )

    if st.checkbox("Difference between average and variability image"):
        avg_healthy = plt.imread(f"{output_dir}/avg_var_healthy.png")
        avg_mildew = plt.imread(f"{output_dir}/avg_var_powdery_mildew.png")

        st.warning(
            f"* We obsereved that a difference in the level of color pigmentation."
            f"The healthy cherry leaf had a slightly darker green compared to the leaf with powdery mildew"
        )

        st.image(avg_healthy, caption="Healthy Cherry Leaf - Average and Variability")
        st.image(avg_mildew, caption="Powdery Mildew Cherry Leaf - Average and Variability")
        st.write('---')

    if st.checkbox('Differences between Healthy and Powdery Mildew cherry leaves'):
        avg_diff = plt.imread(f"{output_dir}/avg_diff.png")

        st.warning(
            f"* Write observation here"
        )

        st.image(avg_diff, caption='Difference between average images')
        st.write('---')

    if st.checkbox("Image Montage"):
        st.write("- To view the montage, select a label and click on **Create Montage** button")
        st.write('- To refresh the image montage, click on **Create Montage** button')
        data_dir = 'inputs/datasets/raw/cherry-leaves/validation'
        labels = os.listdir(data_dir)
        label_to_display = st.selectbox(
            label="Select label",
            options=labels,
            index=0
        )
        if st.button("Create Montage"):
            image_montage(data_dir, label_to_display, nrows=8, ncols=3, figsize=(10,25))
            st.write('---')


def image_montage(dir_path, label_to_display, nrows, ncols, figsize=(15,10)):
  sns.set_style("white")
  labels = os.listdir(dir_path)

  # subset the class you are interested to display
  if label_to_display in labels:

    # checks if your montage space is greater than subset size
    images_list = os.listdir(dir_path+'/'+ label_to_display)
    if nrows * ncols < len(images_list):
      img_idx = random.sample(images_list, nrows * ncols)
    else:
      st.error(
          f"Decrease nrows or ncols to create your montage. \n"
          f"There are {len(images_list)} in your subset. "
          f"You requested a montage with {nrows * ncols} spaces")
      return
    

    # create list of axes indices based on nrows and ncols
    list_rows= range(0,nrows)
    list_cols= range(0,ncols)
    plot_idx = list(itertools.product(list_rows,list_cols))


    # create a Figure and display images
    fig, axes = plt.subplots(nrows=nrows,ncols=ncols, figsize=figsize)
    for x in range(0,nrows*ncols):
      img = imread(dir_path + '/' + label_to_display + '/' + img_idx[x])
      img_shape = img.shape
      axes[plot_idx[x][0], plot_idx[x][1]].imshow(img)
      axes[plot_idx[x][0], plot_idx[x][1]].set_title(f"Width {img_shape[1]}px x Height {img_shape[0]}px")
      axes[plot_idx[x][0], plot_idx[x][1]].set_xticks([])
      axes[plot_idx[x][0], plot_idx[x][1]].set_yticks([])
    plt.tight_layout()
    
    st.pyplot(fig=fig)

  else:
    st.error(
        f"The label you selected doesn't exist."
        f"The existing options are: {labels}"
    )
 