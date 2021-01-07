# Description

* Aggregate 3 datasets:
  * https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate
  * https://www.kaggle.com/unsdsn/world-happiness
  * https://www.kaggle.com/russellyates88/suicide-rates-overview-1985-to-2016
* Integrate in a SQL database
* Dataviz app creation
* Dockerize (2 dockerfiles one for app one for dataviz scripts or database queries)

# Data Retrieval

### Scrapping Wikipedia Table

* [Medium: scrapping wikipedia tables](https://medium.com/analytics-vidhya/web-scraping-wiki-tables-using-beautifulsoup-and-python-6b9ea26d8722)

To scrape the contents of a wikipedia table. 

1. Inspect the website, the structure of the page and the table. 
2. Modify the **table_scrapping.py** file to adapt to your table 
3. Run the  **table_scrapping.py** file.
4. You should get [complete here]

```python
import requests    
from bs4 import BeautifulSoup as bs

url = "https://en.wikipedia.org/wiki/List_of_countries_by_intentional_homicide_rate"

text = requests.get(url).text

soup = bs(url, "lxml")

print(soup.prettify)

```



# SQL Database

For this project you need a **working version of MySQL Server**. The rest of the dependencies are contained in the requirements.txt file. [Python MySQL Setup](https://www.youtube.com/watch?v=3vsC05rxZ8c&ab_channel=TechWithTim)



# Data Visualisation



# Docker

```docker
docker build -f Dockerfile -t app:latest .
```

```
docker run -p 8501:8501 app:latest
```

