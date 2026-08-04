class dataset:
    def __init__(self,dataset_name,rows,column):
        self.dataset_name=dataset_name
        self.rows=rows
        self.column=column
    def details(self):
        print("Dataset name :",self.dataset_name)
        print("Rows : ",self.rows)
        print("Column : ",self.column)
d1=dataset("sales",10000,12)
d1.details()
        