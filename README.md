## Dataset Content
* The dataset is sourced from Kaggle
* The dataset contains +4 thousand images taken from client's crop fields. The images show cherry leaves that are healthy and cherry leaves that contain powdery mildew, which is a fungal disease that affects a wide range of plants. The cherry plantation crop is one of their finest products in the portfolio and the company is concerned about supplying the market with a product of compromised quality.



## Business Requirements
The cherry plantation crop from Farmy & Foods is facing a challenge where their cherry plantations have been presenting powdery mildew. Currently, the process is to manually verify if a given cherry tree contains powdery mildew. An employee spends around 30 minutes in each tree, taking a few samples of tree leaves and verifying visually if the leaf tree is healthy or has powdery mildew. If it has powdery mildew, the employee applies a specific compound to kill the fungus. The time spent applying this compound is 1 minute.  The company has thousands of cherry trees located in multiple farms across the country. As a result, this manual process is not scalable due to time spent in the manual process inspection.

To save time in this process, the IT team suggested an ML system that is capable of detecting instantly, using a leaf tree image, if it is healthy or has powdery mildew. A similar manual process is in place for other crops for detecting pests, and if this initiative is successful, there is a realistic chance to replicate this project to all other crops. The dataset is a collection of cherry leaf images provided by Farmy & Foods, taken from their crops.


* 1 - The client is interested in conducting a study to visually differentiate a cherry leaf that is healthy and that contains powdery mildew.
* 2 - The client is interested to predict if a cherry leaf is healthy or contains powdery mildew.


## Hypothesis and how to validate?
* The tree leaves that have pwdery mildew conatins white streaks on them.
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


## Dashboard Design (Streamlit App User Interface)

### [Dashboard Wireframe](docs/project_wireframe.pdf)
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


## Unfixed Bugs
* You will need to mention unfixed bugs and why they were not fixed. This section should include shortcomings of the frameworks or technologies used. Although time can be a big variable to consider, paucity of time and difficulty understanding implementation is not a valid reason to leave bugs unfixed.

## Deployment
### Heroku

* The App live link is:  https://pp5-mildew-detection.herokuapp.com/
* The project was deployed to Heroku using the steps outlined.

1. create a Heroku app via the Heroku CLI
	- download and install [Heroku CLI](https://devcenter.heroku.com/articles/heroku-cli)
	- Log in to Heroku and create an App using Heroku build-pack 20
		`heroku apps:create pp5-mildew-detection --stack heroku-20`
	This was created using stack-20 because the current default stack heroku-22 doesn't support python version 3.8.13
2. Sign in to check that it was created successfullty
3. At the Deploy tab, select GitHub as the deployment method.
3. Select your repository name and click Search. Once it is found, click Connect.
4. Select the branch you want to deploy, then click Deploy Branch.
5. The deployment process should happen smoothly in case all deployment files are fully functional. Click now the button Open App on the top of the page to access your App.


## Technologies Used

### Main Data Analysis and Machine Learning Libraries
* [TensorFlow](https://www.tensorflow.org/overview) - used during image preprocessing to filter out corrupt images. 
* [Keras](https://keras.io/)
* [joblib](https://pypi.org/project/joblib/) for saving and loading image shape

### OtherFrameworks, Libraries & Programs Used
* [Git](https://git-scm.com/) - used for version control by utilizing the Gitpod terminal to commit to Git and Push to GitHub.
* [GitHub:](https://github.com/) - used to store the projects code after being pushed from Git.
* [Balsamiq:](https://balsamiq.com/) - Balsamiq was used to create the Dashboard [wireframes](https://github.com/) during the design process.

## Credits 

* In this section you need to reference where you got your content, media and extra help from. It is common practice to use code from other repositories and tutorials, however, it is important to be very specific about these sources to avoid plagiarism. 
* You can break the credits section up into Content and Media, depending on what you have included in your project. 

### Content 

- The text for the Home page was taken from Wikipedia Article A
- Instructions on how to implement form validation on the Sign Up page was taken from [Specific YouTube Tutorial](https://www.youtube.com/)
- The icons in the footer were taken from [Font Awesome](https://fontawesome.com/)

### Media

- The photos used on the home and sign up page are from This Open Source site
- The images used for the gallery page were taken from this other open source site



## Acknowledgements (optional)
* In case you would like to thank the people that provided support through this project.
