![IronHack Logo](https://s3-eu-west-1.amazonaws.com/ih-materials/uploads/upload_d5c5793015fec3be28a63c4fa3dd4d55.png)

# Project: API & Web Data Scraping and Web Data Pipeline

## Overview

The goal of this project is for you to practice what you have learned in the APIs and Web Scraping chapter of this program. For this project, you will choose both an API to obtain data from and a web page to scrape. For the API portion of the project will need to make calls to your chosen API, successfully obtain a response, request data, convert it into a Pandas data frame, and export it as a CSV file. For the web scraping portion of the project, you will need to scrape the HTML from your chosen page, parse the HTML to extract the necessary information, and either save the results to a text (txt) file if it is text or into a CSV file if it is tabular data.

Aditionally, after you obtain both CSV files you will practice what you have learned in the Intermediate Python and Data Engineering chapter of this program. You will need to import the CSV files and use your newly-acquired skills to build a data pipeline that processes the data and produces a result. You should demonstrate your proficiency with the tools we covered (functions, list comprehensions, string operations, and error handling) in your pipeline.

**You will be working individually for this project**, but we'll be guiding you along the process and helping you as you go. Show us what you've got!

---

## Technical Requirements

The technical requirements for this project are as follows:

* You must obtain data from an API using Python.
* You must scrape and clean HTML from a web page using Python.
* The results should be two files - one containing the tabular results of your API request and the other containing the results of your web page scrape.
* Your code should be saved in a Jupyter Notebook and your results should be saved in a folder named output.

* You must construct a data pipeline with the majority of your code wrapped in functions.
* Each data pipeline stage should be covered: acquisition, wrangling, analysis, and reporting.
* You must demonstrate all the topics we covered in the chapter (functions, list comprehensions, string operations, and error handling) in your processing of the data.
* There should be some data set that gets imported and some result that gets exported.
* Your code should be saved in a Python executable file (.py), your data should be saved in a folder named data, and your results should be saved in a folder named output.

* You should include a README.md file that describes the steps you took and your thought process for obtaining data from the API and web page.


## Necessary Deliverables

The following deliverables should be pushed to your Github repo for this chapter.

* **A Jupyter Notebook (.ipynb) file** that contains the code used to work with your API and scrape your web page.
* **An output folder** containing the outputs of your API and scraping efforts.
* **A Python (.py) code file** that contains the code for your data pipeline.
* **A data folder** containing your data set.
* **An output folder** containing the output of your data pipeline.
* **A ``README.md`` file** containing a detailed explanation of your approach and code for retrieving data from the API and scraping the web page as well as your results, obstacles encountered, and lessons learned.

## Suggested Ways to Get Started

* **Find an API to work with** - a great place to start looking would be [API List](https://apilist.fun/) and [Public APIs](https://github.com/toddmotto/public-apis). If you need authorization for your chosen API, make sure to give yourself enough time for the service to review and accept your application. Have a couple back-up APIs chosen just in case!
* **Find a web page to scrape** and determine the content you would like to scrape from it - blogs and news sites are typically good candidates for scraping text content, and [Wikipedia](https://www.wikipedia.org/) is usually a good source for HTML tables (search for "list of...").
* **Examine the data and come up with a deliverable** before diving in and applying any methods to it.
* **Break the project down into different steps** - note the steps covered in the API and web scraping lessons, try to follow them, and make adjustments as you encounter the obstacles that are inevitable due to all APIs and web pages being different.
* **Use the tools in your tool kit** - your knowledge of intermediate Python as well as some of the things you've learned in previous chapters. This is a great way to start tying everything you've learned together!
* **Work through the lessons in class** & ask questions when you need to! Think about adding relevant code to your project each night, instead of, you know... _procrastinating_.
* **Commit early, commit often**, don’t be afraid of doing something incorrectly because you can always roll back to a previous version.
* **Consult documentation and resources provided** to better understand the tools you are using and how to accomplish what you want.

## Useful Resources API and Web Data Scraping

* [Requests Library Documentation: Quickstart](http://docs.python-requests.org/en/master/user/quickstart/)
* [BeautifulSoup Documentation](https://www.crummy.com/software/BeautifulSoup/bs4/doc/)
* [Stack Overflow Python Requests Questions](https://stackoverflow.com/questions/tagged/python-requests)
* [StackOverflow BeautifulSoup Questions](https://stackoverflow.com/questions/tagged/beautifulsoup)

## Useful Resources Web Data Pipeline

* [Python Functional Programming How To Documentation](https://docs.python.org/3.7/howto/functional.html)
* [Python List Comprehensions Documentation](https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions)
* [Python Errors and Exceptions Documentation](https://docs.python.org/3/tutorial/errors.html)
* [StackOverflow String Operation Questions](https://stackoverflow.com/questions/tagged/string+python)
