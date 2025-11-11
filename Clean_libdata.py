#import csvs
import pandas as pd #main lib for hadnling and cleaning csv/data STEP ONE
import os #helps python work with file paths
from datetime import datetime 
from sqlalchemy import create_engine

#define data folder 
data_folder = 'data'

#Load the books csv 
books_file = os.path.join(data_folder, '03_library systembook.csv') #joins foler and file name
books_df = pd.read_csv(books_file) #loads csv into a dataframe

#Remove duplicates
books_df = books_df.drop_duplicates() #removes rows that are the same

#Fix missing Values
books_df.dropna(how='all', inplace=True)

#Remove speechmarks
books_df['Book checkout'] = books_df['Book checkout'].str.replace('"','').str.strip()
books_df['Book Returned'] = books_df['Book Returned'].str.replace('"','').str.strip()

#Convert Dates
try:
    books_df['Book checkout'] = pd.to_datetime(books_df['Book checkout'], format='mixed', errors='coerce')
    books_df['Book Returned'] = pd.to_datetime(books_df['Book Returned'], format='mixed', errors='coerce')
except Exception as e:
    print(f"Error: {e}")

#Create Days on Loan
books_df['Days on Loan'] = (books_df['Book Returned'] - books_df['Book checkout']).dt.days

#Drop Rows with InValid Dates
books_df = books_df.dropna(subset=['Book checkout', 'Book Returned'])

#Change 2 weeks to days
books_df['Days allowed to borrow'] = books_df['Days allowed to borrow'].apply(lambda x: int(x.split()[0]) * 7)

# Load customer CSV
customers_file= os.path.join(data_folder, '03_Library SystemCustomers.csv')
customers_df = pd.read_csv(customers_file)

#Remove Dupliactesfrom customers

customers_df = customers_df.drop_duplicates()

#Steo Eight: remove error values to go in sepearte errors CSV

critical_columns= ['Id', 'Books', 'Book checkout', 'Book Returned', 'Days allowed to borrow', 'Customer ID']

#Identify the rows with nan_errors

nan_errors = books_df[books_df[critical_columns].isna().any(axis=1)]

#select rows where days on loan is negative
negative_days = books_df[books_df['Days on Loan'] < 0]

#combine both sets of errors

error_rows = pd.concat([nan_errors, negative_days]).drop_duplicates()

#drop error rows from clean data set

clean_books_df = books_df.drop(error_rows.index)

#Save both versions
clean_books_df.to_csv('03_Library_Systembook_CLEAN.csv', index=False)
error_rows.to_csv('03_Library_Systembook_ERRORS.csv', index= False)

#step nine: remove any errors from system book customers and save csv
customer_critical_columns = ['Customer ID','Customer Name']

#select error rows
customer_nan_errors = customers_df[customers_df[customer_critical_columns].isna().any(axis=1)]

#drop error rows to create the clean customer file
clean_customers_df = customers_df.drop(customer_nan_errors.index)

#save both csvs
clean_customers_df.to_csv('03_Library_SystemCustomers_CLEAN.csv', index=False)
customer_nan_errors.to_csv('03_Library_SystemCustomers_ERRORS.csv', index= False)

#--- Load cleaned data to SQL Server
server = 'localhost' #sql server local
database = 'LibraryDB' #name of cleaned data base

#windows authentication
conn_str = f"mssql+pyodbc://@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server;Trusted_Connection=yes"

engine = create_engine(conn_str)

#write dataframes to SQL server
clean_books_df.to_sql('Books', con=engine, if_exists='replace', index=False)
clean_customers_df.to.sql('Customers', con=engine, if_exists='replace', index=False)

