# Description

This repository contains a fully dockerized streamlit application that acts as interface for data analysis. 

The data consists of 3 tables giving social and economical information, grouped by country. 

* The tabular data comes from 3 sources:
  * https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate
  * https://www.kaggle.com/unsdsn/world-happiness
  * https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016
  
* The 3 tables are merged in a a SQL database with one common primary key : "Country"

* Finally, the streamlit application proposes many Data Visualisation functionalities, useful to understand the data.

  

# Installation

A simple `docker-compose up` command should start all the services. The streamlit interface is then available on default *localhost:8501* endpoint.



# Functionalities Explained

## Scrapping Wikipedia Table

* [Medium: scrapping wikipedia tables](https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722)

To scrape the contents of a wikipedia table the code is contained in  "scrapping/scrap-wikipedia.py"

1. Retrieve url of wikipedia article. 
2. Retrieve the number of the table as there may be many in the specified url.
3. Supply this information on the streamlit application.



## SQL Database

For this project you need a **working version of MySQL Server**. The rest of the dependencies are contained in the requirements.txt file. [Python MySQL Setup](https://www.youtube.com/watch?v=3vsC05rxZ8c&ab_channel=TechWithTim)



## Data Visualisation





## Docker-compose

The containerization is orchestrated via the **docker-compose.yml** file. This file contains the following services :

* Streamlit
* mysql-development