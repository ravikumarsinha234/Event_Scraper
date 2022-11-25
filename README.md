# Event_Scraper

This repository contains a project which is used for scrapping the events happening in and around atlanta in the upcoming days.

## Scrape a webpage
Create a python program called scrape.py that takes a date in ISO format as an argument:  
> python3 scrape.py 2022-10-02 result.xlsx  


The program will then create and excel spreadsheet that lists the names of events that will happen  
on that date and their urls. It should look like this when you open it in Excel:  

Behind the scenes, your program will  
• fetch the web page at https://discoveratlanta.com/events/all/  
• parse the result using BeautifulSoup and html.parser  
• step through each article inspecting the dates of the events  
• skip articles that do not contain the desired date  
• for articles that have the desired date, note the title and the URL  
• make a dataframe with all the titles and URLs  
• write the dataframe to an ExcelWriter  
• resize the columns to be a reasonable width  
• write it to the file named on the command line  
You are putting data into only 2 columns – Don’t include the dataframe’s index in the excel file.  
