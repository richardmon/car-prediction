# Car Price Prediction
## Set Up
This project is meant to by run with python 3.
To get all the necessary libraries run
```
pip install -r requirements.txt
```

## Data collection
In order to start the data scrapping you will need to run the command
```
cd get_data
scrapy crawl cars -o crawl_data.csv
```
This will create *craw_data.csv*, a csv file with all the information and an image folder,
with the respective images

## Data Analysis
This is done by running the command
```
cd ..
jupyter-notebook
```
This will prompt you to select the proper file.
Open **Features, Exploratio and Prediction.ipynb**,
read through it and create an issue if you think something must be addressed.
