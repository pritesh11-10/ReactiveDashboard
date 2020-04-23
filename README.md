# ReactiveDashboard
Developed an interactive dashboard to demonstrate visualization in a way that helps in better understanding and used heroku as a deployment platform.

Dataset used is taken from kaggle.

Reactive Dashboard is developed using streamlit.

EDA and visualization for the dataset is also demonstrated in the notebook folder. EDA is performed using pandas and Visualization is done using plotly.

The dataest taken from kaggle was uploaded on developer's google drive and downloaded the csv file through google drive api

# Reactive Dashbord link :- https://reactivedashboard.herokuapp.com/

Interactive dashboard can be viewed with the help of above link.

Tip:- Dashboard would take some time to load... Please do refresh it take more amount of time

# File Descriptions

Notebook :- Contains .ipynb file where all data wrangling, EDA and data visualization is done.

plots :- Contains all the plotly plots created for visualization purposes.

src :- This folder contains app.py and prepocess.py files

preprocess.py :- This contains the initial setup of getting the csv file

app.py :- Features related to dashboard are developed here.

.gitignore :- The purpose of the . gitignore file is to allow you to ignore files, such as editor backup files, build products or local configuration overrides that you never want to commit into a repository. Without matching. It has folder that contains key for connecting with google drive

Procfile :- This file is created by running the command python ProcGen.py. More ddetails about Procfile, setup.sh can be obtained from the below reference.

requirements.txt :- This file contains all the necessary parameters required for heroku to identify the language of code. 

Note :- If this file is not included than build would fail as heroku won't understand the language.

# Connecting to google Drive using Google Drive API

connect_to_drive :- Used for authentication and connecting to google drive. 

The dataset used was uploaded from Kaggle to google Drive. From the drive the dataset was downloaded. Complete details on using the google drive API can be found in the reference below.

# References
Deploying streamlit dashboard with heroku :- https://gilberttanner.com/blog/deploying-your-streamlit-dashboard-with-heroku

Using Google Drive API
https://medium.com/swlh/google-drive-api-with-python-part-i-set-up-credentials-1f729cb0372b

https://levelup.gitconnected.com/google-drive-api-with-python-part-ii-connect-to-google-drive-and-search-for-file-7138422e0563

https://medium.com/@umdfirecoml/a-step-by-step-guide-on-how-to-download-your-google-drive-data-to-your-jupyter-notebook-using-the-52f4ce63c66c



