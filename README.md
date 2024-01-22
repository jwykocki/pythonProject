## Job Offers Scrapper - Python Project

### Description  
The main feature of this project is scrapping job offers from justjoin.it and nofluffjobs.com. This tasks is scheduled and interval can be specified in config file. Offers are saved in MySQL database on Docker. 
Project also create an HTTP server, where user can send GET request on /offers endpoint, and wil receive offers from database. Before every new offers fetch, the old ones from database are removed. 
Server, scheduler, database and scrapper parameters can be set in config.ini file.  
### Technologies  
Web scrapping - Selenium  
Scheduler - BackgroundScheduler from APscheduler  
Connecting to DB - SQLAlchemy  
### How to run  
1) Download source code to your directory
2) docker-compose -f compose.yml up
3) Run project
4) After first scheduler interval, GET /offers request can be send on http://localhost:8090/offers
