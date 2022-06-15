# Python forum scraper
> A scraper which scrapes through python-forum.io discussion forum (5 pages deep) and displays the most popular threads
> with the largest number of views.
> The result can be seen [_here_](https://dmytrozelenkov.pythonanywhere.com/).

## Table of Contents
* [General Info](#general-information)
* [Technologies Used](#technologies-used)
* [Features](#features)
* [Screenshots](#screenshots)
* [Setup](#setup)
* [Usage](#usage)
* [Project Status](#project-status)
* [Room for Improvement](#room-for-improvement)
* [Acknowledgements](#acknowledgements)
* [Contact](#contact)
<!-- * [License](#license) -->

## General Information
- The project is built using Django.

## Technologies Used
- Python - version 3.9
- Django - version 4.05
- Sqlite3 - version 3.38.5
- Bootstrap - version 4.0.0


## Features
- Demonstrates usage of BeautifulSoup library for scraping 
- Data model is built and migrated to Sqlite3 (models.py file)
- Scraper goes five pages deep and finds data based on class atribute and text from <td> element
- Regular expressions are used for string conversion
- Data is stored in Sqlite3 table


## Screenshots
![Example screenshot](https://live.staticflickr.com/65535/52148382338_81e6237df5_b.jpg)


## Setup
<!-- What are the project requirements/dependencies? Where are they listed? A requirements.txt or a Pipfile.lock file perhaps? Where is it located? -->


## Usage
<!-- Provide various use cases and code examples here. -->


## Project Status
This project is for testing purposes.


## Room for Improvement
When hosted on pythonanywhere.com the scraper won't get data due to pythonanywhere.com using proxies and the website
not whitelisted. Subscription plan should be changed to allow scraping external resources.

Room for improvement:
- Handling exceptions due to proxy error


To do:
- Add exception handler


## Contact
Created by Dmytro Zelenkov - feel free to contact me!

