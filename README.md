# DE-Mod-5

#Start process-- examine the files and work out what steps are needed to clean

#Cleanpython script-- this handled data quality errors
#remove duplicates, fix missing values, remove speechmarks, convert dates, create days on loan, drop rows with invalid dates, change 2 weeks to days, convert clean data to csv and out put errors to csv, for customers remove nan values, output clean data to csv, put nan values into csv

#Create unit testing to check python script

#1 unit test created to test the removal of duplicates

#write the code back to SQL into data tables

#refactored code to add in data engineering metrics 
#no of rows updated, no of duplicates removed, no of errors from books csv

#Connect Power BI to SQL to display metrics 
#3 metrics tile displays show how completed ETL automatcially cleans the data and outputs metrics

#next steps
#pass back errors to data qualifiers, create monthly trigger to take csv imports and run python cleaning app, refresh metrics for stakeholders

