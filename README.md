#  DATA SCRAPING WITH  BEAUTIFULSOUP & SELENIUM
## [Description/Overview](description/overview)
## [Tools and Technology](tools_and_technology)
## [Categories of data scraped](categories_of_data_scraped)
## [Scraping procedure](Scraping_procedure) 
## [How the scraper works](how_the_scraper_works)
## [Note](note)
## Description/Overview
In This project , I was able to scrape grocery products from **jumia Nigeria website** using **beautifulsoup and Selenium**. The project scrapes some important information about each grocery product available at the time of scraping such as product name, current pricings, ratings and discounts (if available) of the products which can be used for further analysis.
## Tools and Technology
For this project, I used
-	BeautifulSoup
-	Selenium
-	Pandas
-	Time
-	ChromeDriver
-	Python
-	Vs code
## Categories of data scraped
The categories of data scraped were
-	Product name
-	Price
-	Discounts ( if available)
-	Ratings of products (if available)
## Scraping procedure
1.	 Install the libraries.

-	Beautifulsoup
-	Selenium
-	Pandas
-	ChromeDriver
-	Lxml

2.	Import the libraries

-	Beautifulsoup
-	Selenium
-	Chromedriver
-	Pandas
-	Time
3.	Run the code
4.	Open the csv dataframe
  ## How the scraper works
1. Selenium opens the Jumia grocery page in a real browser
2. The page is allowed to load fully
3. BeautifulSoup parses through the page 
4. Product information is extracted from each product card
5. Data is stored in a Pandas DataFrame
6. The cleaned data is now saved to a CSV file <img width="771" height="381" alt="image" src="https://github.com/user-attachments/assets/9dad2b89-df95-4958-b49e-1aa82d656286" />



## Note 
Please respect all the jumia guidelines while scraping the data

