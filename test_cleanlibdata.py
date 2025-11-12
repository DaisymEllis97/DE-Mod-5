import unittest 
import pandas as pd

class TestCleanData(unittest.TestCase):
    
    def setUp(self):
        self.df = pd.DataFrame({
        'Id': [1, 2, 2, 3],
        'Books': ['Book A', 'Book A', 'Book B', 'Book C'],
        'Customer ID' : [101, 102, 102, 103]
    })

#test that dupes are remove based on ID column
def test_remove_duplicates(self):
    df_no_dupliactes = self.df.drop_duplicates(subset='Id')
    expected_Ids = [1, 2, 3]
    self.assertEqual(df_no_dupliactes['Id'].tolist(), expected_Ids,
                     "Dupliactes were not removed correctly")
    
if __name__== '__main__':
    unittest.main()