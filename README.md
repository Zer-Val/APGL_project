# Advanced Python, Git, Linux for Bloomberg

This project is an academic project on the manipulation of Linux commands and the manipulation of a Flask app.

This project aims to implement a webscrapper that uses bash command grep to take the data in the HTML code of the page. We then have to display it on a dashboard hosted on a Virtual Machine on a web server so that we can acces it at any time.

We realised a few Bash scripts to handle the gathering, processing and cleaning of our files.

We have a Flask app to handle the backend, and HTML files to do the frontend. In our case, the .html files contains HTML, CSS an JScript.

We have Cron to apply the Bash scripts, and tmux to keep the dashboard running even when we are not connected to the server.

All of the files are used within a Virtual Environement and you can find the requirements.txt, file if you wish to know which packages we have in the VENV.

This project was a good way for us to learn how to use Linux to automatise tasks and how to setup a server instance and how to use it to create a page that anyone can access.

We thank our teacher and PW teacher for their help.

This project is based on the following project assignement :

## Rules

- This project must be completed by a group of exactly two people.
- This project should be done with the least help of anyone (but internet).
- Add the internet address of the website you want to scrap on the shared Google Sheet.
- Every website should be different to ensure codes will not be similar.
- Ensure your intended website is not yet used by anyone else.
- Similar codes are severely downgraded.
- Indicate on the shared Google Sheet the address of your virtual machine (to access the live dashboard).
- Indicate on the shared Google Sheet the address of your git repository hosting this project (to access your code).
- You should enjoy the process since it might be very useful for your career!

## Objective

Having up-to-date info from continuous scraping of a website, displayed on your online dashboard.

- Find a website that have some dynamic information which changes each minute or so (select one with a stable html structure though, e.g.      [CoinGecko Bitcoin](https://www.coingecko.com/en/coins/bitcoin))
- That specific information should be retrieved (scrapped) using bash
- That specific information should then be displayed on a dashboard, made with Python using the package Dash
- A graph should also display the time series (values scrapped along time)
- The dashboard should be updated every 5 minutes using cron
- A daily report should also be displayed in the dashboard, updated at 8pm each day, and should provide several coherent metrics (e.g. for a financial series, the report could contain daily volatility, open and close price, evolution, etc.)
- Additionnal features are welcome if they add value to the dashboard.

## Specifications

- The code should be versioned using git and hosted on Github
- The code should run h/24 on your online hosted Linux virtual machine (be careful to prevent any cost from your cloud provider)
- The scrapper should be written in bash only without any advanced langage or package (e.g. no Python)
- You should use regex in your scrapper.
- The code and architecture should be clean, easily readable and easy to debug
- The commits of your repository will be evaluated, you should have contributed to a balanced number of commits between the two members of the group.
