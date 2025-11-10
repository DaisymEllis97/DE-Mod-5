import pandas as pd #main lib for hadnling and cleaning csv/data STEP ONE
import os #helps python work with file paths

#define data folder STEP TWO
data_folder = 'data'

#Load the books csv STEP THREE

books_file = os.path.join(data_folder, '03_library systembook.csv') #joins foler and file name
books_df = pd.read_csv(books_file) #loads csv into a dataframe

#Remove duplicates STEP FOUR

books_df = books_df.drop_duplicates() #removes rows that are the same

#Fix missing Values- STEP FIVE

books_df['customer id'] = books_df['customer id'].fillna ('unknown')
books_df['books'] = books_df['books'].fillna('unknown')

# Convert Dates- STEP SIX

books_df['book check out'] = pd.to_datetime(books_df['book check out'], errrors='coerce')
books_df['book returned'] = pd.to_datetime(books_df['book returned'], errors='coerce')

#Drop Rows with InValid Dates- STEP SEVEN (change this to if valid ok, if day is invalid take it out into an errors csv)

books_df = books_df.dropna(subset=['book check out', 'book returned'])

# Load customer CSV- STEP EIGHT

customers_file= ps.path.join(data_folder, '03_Library SystemCustomers.csv')
customers_df = pd.read_csv(customers_file)

# Remove Dupliactes and fix missing values (customers csv)- STEP NINE

customers_df = customers_df.drop_duplicates()
customers_df['customer id'] = customer_df['customer id'].fillna ('unknown')
customers_df['customer name'] = customers_df['customer name'].fillna ('unknown')




   


   
   
   
   
   
   
   
   
   
   
   
   
    #handle missing or invalid values
    median_days= books_df.drop(columns=['days allowed to borrow'])
    books_df = books.df.rena,e(columns={'days_allowed_numeric': 'days allowed to borrow'})


    #Save cleaned csvs- STEP 10

    books_df.to_csv(os.path.join(data_folder, 'books_clean.csv'), index=False)
    customers_df.to_csv(os.path.join(data_folder,'customers_clean.csv', index=False))

    #Print confirmation that cleaned csvs have been succesfully created
    print("Cleaning Complete! Two new csvs created: books_clean.csv and custoemrs_clean.csv")


      








