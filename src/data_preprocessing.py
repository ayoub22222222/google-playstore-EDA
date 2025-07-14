"""
the purpose of this class is loading, cleaning and storing data 
"""

class DataCleaning:
    def __init__(self, file_path):
        self.file_path =file_path
        self.data = None
    def load_data(self):
        """ Load data """
        self.data = pd.read_csv(self.file_path)
        return self.data.head(10)
    def data_overview(self):
        """ check the data type for every columns """
        self.load_data().info()
        print(100 * "-")
    def cln_columns(self):
        """ cleaning columns """
        pass
                 
