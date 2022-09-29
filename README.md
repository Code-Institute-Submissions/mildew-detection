<h1 align=center>Cherry Leaf Mildew Detector</h1>

![](docs/images/sitepage.png)

This website's machine learning technology offers a platform for users to upload photos of cherry leaves and detect whether or not they are healthy or infected with powdery mildew.

[Live application can be found here](https://pp5-mildew-detection.herokuapp.com/)

# Planning Phase

## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.

### **Project Goal:**

* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Dataset Content
* The dataset is sourced from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves). We created then a fictitious user story where predictive analytics can be applied in a real project in the workplace.
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.

### Sample leaves
---
| 	healthy											         	|											   	 podwery mildew leaf|
| ---													     	| ---															  	|
|<img src="static\images\healthy-1425009578.jpg" height='180px'>| <img src="static\images\mildew-g17a4823aa_640.jpg" height='180px'>|

## Hypothesis and how to validate?
* The tree leaves that have pwdery mildew contains white streaks on them.
    -  conventional data analysis will be used to conduct a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.


## Rationale to map the business requirements to the Data Visualizations and ML tasks
* **Business Requirement 1**: Data Visualization
    In order to  visually differentiate healthy and mildew-infested cherry leaves:
	* As a client I want to  display the "mean" and "standard deviation" images for cherry leaves that are healthy and cherry leaves that contain powdery mildew.
 	* As a client I want to display the differences between an average healthy cherry leaf and a cherry leaf that has powdery mildew.
	* As a client I want to display an image montage for healthy cherry leaf and mildew-infested leaf.

* **Business Requirement 2**:  Classification
	* As a client I want to predict if a given cherry leaf is healthy or contains powdery mildew so that I do not supply the market with a product of compromised quality. 
	* As a client I want to build a binary classifier and generate reports.


## ML Business Case
* As a client I want a ML model to predict if the cherry leaf tree is healthy or has powdery mildew.
* The ideal outcome is provide Farmy & Foods with a faster and reliable mildew detection mechanism that is readily scalable across the multiple farms in the country
* The model success metric are:
    * A study showing how to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
    * The capability to predict if a cherry leaf is healthy or contains powdery mildew.
    * The model accuracy on test data is 97%

---

## Data Understanding

The data is labelled image data split into two folders, each representing the image label. For example, so healthy labelled leaves images are in the healthy directory, while the mildew leaves are in the powder_mildew directory.

The classification dataset included 4208 records (2104 healthy leaves and 2104 infected leaves) was a balanced dataset.


## Data Preparation
Minimal data cleaning was required, the folders were scanned through to delete any non-image file. To adequately perform model training and avoid model overfitting the dataset was split into train, test and validation set. The split ratio of the dataset was 0.7, 0.2, and 0.1 repspectively.
Data augmentation was performed using ImageDataGenerator on the training dataset to increase the image data by artificially and temporarily creating training images through the combination of different processes, such as random rotation, shifts, sheared, zoom and rotated images in the computer's short-term memory (RAM). ImageDataGenertor was also used to rescale the test dataset and validation dataset.

## Modeling
The sequential model is used on the training dataset was used to train the model and validated using the validation dataset. 

The model created was used to make prediction on the unseen test dataset and the Accuracy performance metrics calculated.


## Evaluation
The model accuracy on the test datset is over 97% which is the required percentage accuracy. To test further I uploaded two leaves(healthy and mildew leaves shown under sample data above) which were not part of the dataset were uploaded and the were adequately predicted.

[Mildew Leaf](docs/images/page_3_detector_2.png)

[Healthy Leaf](docs/images/page_3_detector_3.png)

---


## Dashboard Design (Streamlit App User Interface)

### Dashboard Wireframe
Dashboard wireframe was created using balsamiq. The wireframe is in pdf format and can be viewed [here](docs/project_wireframe.pdf)


### Page 1: Quick Project Summary
* A project summary page, showing the project dataset summary and the client's requirements.
* Quick project summary
	* General Information
	* Project Dataset
		* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.

	* Business requirements
		*  The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
		*  The client is interested in predicting if a cherry tree is healthy or contains powdery mildew.

### Page 2: Cherry leaf visualizer
* It will answer business requirement 1
	* Lists the findings related to the study to visually differentiate a cherry leaf that is healthy from one that contains powdery mildew.
	* Checkbox 1 - Difference between average and variability image
	* Checkbox 2 - Differences between Healthy and Powdery Mildew Cherry Leaves
	* Checkbox 3 - Image Montage


### Page 3: Mildew detector
* It will answer business requirement 2
	* Link to download a set of cherry leaf images for live prediction
	* file upload widget to upload one or more images for prediction
	* Display image and prediction statement indicating whether or not a cherry leaf conatins mildew
	* Display table with image name and prediction result
	* Download button to download table

### Page 4: Project Hypothesis and Validation
* Display each project hypothesis and validation

### Page 5: ML performance metrics
* A technical page displaying the model performance


## **Features**
The application is designed using streamlit library. It is has a sidebar menu with five navigation links.

**Navigation** The dashboard developed is a multipage streamlit application with sidebar navigation checkbox links. The navigation links provides quick access to the five pages listed:

- **Page 1: Quick Project Summary**
This page displays a brief overview of the project requirements and the dataset
![](docs/images/page_1_summary.png)

 
- **Page 2: Cherry leaf visualizer**
This page displays a brief overview of the project requirements and the dataset
![](docs/images/page_2_visualizer_difference.png)

![](docs/images/page_2_visualizer_diff.png)

   
- **Page 3: Mildew Detector**
This provides the interface for the user to upload test samples and predict wether or not the samples provided are healthy or infested with powdery leaf mildew. It features a *Browse file* button which user can use to upload one or more image files. Prediction is not made until the user clicks on the *Make Prediction* button. The image uploaded as well as the prediction and report is displayed to the user when the prediction is complete

![](docs/images/page_3_detector.png)


 ![](docs/images/page_3_detector_2.png)

 
- **Page 4: Hypothesis and Visualization**
This page shows the project hypothesis and how it is validated across the project.
![](docs/images/page_4_hypothesis.png)
  
 
- **Page 5: ML Performance Metric**
Technical information about the model and data are displayed on this page. It shows the:
  * label frequencies of the train, validation and test datasets
  * training model accuracy and loss charts
  * generalised performance on the test sets
  
![](docs/images/page_5_metrics.png)

---


## Bugs and Fixes

* After deploying my project to Heroku, the Image Montage was not displaying since the directory holding the images had been excluded from the GitHub push due to privacy issues, indicating that the data can only be shared with professionals who are formally participating in the project.


## Deployment
Steps I took to setup environment and deploy to Heroku

### Workspace Setup
The repository for this project was created off the [template](https://github.com/Code-Institute-Solutions/milestone-project-mildew-detection-in-cherry-leaves) provided by Code Institute and GitPod workspace was used to develop this project.

- Click the `Use This Template` button.
- Add a repository name and brief description.
- Click the `Create Repository from Template` to create your repository.
- Click `Gitpod` to create a Gitpod workspace.
- To return to the current workspace, login to your gitpod acoount and open the workspace created earlier, since clicking on GitPod button on the GitHub page creates a new workpspace each time.


*Cloning the GitHub Repository*

Cloning your repository will enable you to work on a local version of the repository.

1. Locate the [project repository](https://github.com/valerieoni/mildew-detection)
2. Press the arrow on the Code button
3. To clone the repository using HTTPS, copy the [link](https://github.com/valerieoni/mildew-detection.git) that is shown in the drop-down
4. Open Git Bash
5. Change the current working directory to the location where you want the cloned created
6. In the terminal type `git clone` and then paste the link you copied in step 3
	`git clone https://github.com/valerieoni/mildew-detection.git`
7. Press enter and your local clone will be created.


### Creating Heroku App
The Python version in the project is set to 3.8.13, which is not supported by Heroku's current default stack, heroku-22.
As a result of the above, the app was created from Heroku CLI and set to use buildstack heroku-20.

Steps take to create the app is as follows:
1. download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli) if not already installed
2. Copy API key from heroku
	- sign in and click on the avatar icon and select **Account Settings**
	- Scroll down to the API Key section and click **Reveal** button, and copy key displayed.
3. login to Heroku via the console and enter your details when prompted
	`heroku login -i`
	- enter key copied from step 2 when prompted for password
4. create the app
	`heroku apps:create pp5-mildew-detection --stack heroku-20`


### Deploying to Heroku
1. Sign in to Heroku
2. Select app
3. At the Deploy tab, select GitHub as the deployment method.
4. Select your repository name and click Search. Once it is found, click Connect.
5. Select the branch you want to deploy, then click Deploy Branch.
6. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Technologies Used

### Main Data Analysis and Machine Learning Libraries
* [TensorFlow](https://www.tensorflow.org/overview) - used during image preprocessing to filter out corrupt images. 
* [Keras](https://keras.io/) - used for the CNN model
* [joblib](https://pypi.org/project/joblib/) for saving and loading image shape
* [numpy](https://numpy.org/) - used for array manipulation.
* [pandas](https://pandas.pydata.org/) - used to structure the data
* [matplotlib](https://matplotlib.org/) For creating the charts and plots for data visaulization
* [seaborn](https://seaborn.pydata.org/) Used in conjuction with matplotplib for data visualization
* [plotly](https://plotly.com/) - used for ploting charts for data visualization
* [streamlit](https://streamlit.io/) For the dashboard development
* [scikit-learn](https://scikit-learn.org/stable/) - used for data processing


### OtherFrameworks, Libraries & Programs Used
* [Git](https://git-scm.com/) - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/) - used to store the projects code after being pushed from Git.
* [Balsamiq:](https://balsamiq.com/) - Balsamiq was used to create the Dashboard [wireframes](docs/project_wireframe.pdf) during the design process.
* [Heroku](https://www.heroku.com/) - Deployment platform for the project
* [GitPod](https://www.gitpod.io/) - Workspace used for the project
* [AmIResponsive](http://ami.responsivedesign.is/) - Used to generate responsive image used in README file.



## Credits 
I used several internet sources to resolve issues and solve difficulties when constructing this website, as well as modules to add functionality.

### Content 

- The codes used to implement the functionalities in the project are from the Code Institute training by GyanShashwat1611 at [Github site](https://github.com/GyanShashwat1611/WalkthroughProject01/)
- Dataset is from [Kaggle](https://www.kaggle.com/codeinstitute/cherry-leaves)


### Media

- The images used in the readme and as sample download files on the dashboard are sourced from [pixabay](https://pixabay.com/) and [iStock](https://www.istockphoto.com/)


## Acknowledgements
* I would like to thank my mentor, Marcel Mulders for his support, guidance and feedbacks throughout the course of the project.
