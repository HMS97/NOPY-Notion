import requests 
import json

token = ''
databaseId = ''

class NOTIONPY():
    def __init__(self,token,databaseId, columns_list = ['iou','data']):
        self.token = token
        self.datasetId = databaseId
        self.URL = f"https://api.notion.com/v1/databases/{self.datasetId}"
        self.HEADERS = {
                    "Notion-Version": "2021-05-13",
                    "Authorization": "Bearer " + self.token,
                    "Content-Type": "application/json"}
        self.columns_list = columns_list
        self.update_column()
        
    def create_dataset(self):
        self.URL = f"https://api.notion.com/v1/databases/{self.datasetId}"

        response = requests.request(
                "PATCH", self.URL, headers=self.HEADERS, data=json.dumps(self.payload)
            )
        return response.json()
    
    def add_col_value(self,in_dic):
        self.URL = "https://api.notion.com/v1/pages"
        assert 'Name' in in_dic.keys(), "There must be a Name." 

        for item in self.columns_list:
            self.add_value(item,'')
        for item in in_dic.keys():
            if item  == 'Name':
                self.add_name(in_dic[item])
                continue
            self.add_value(item,in_dic[item])
            
        response = requests.request(
                "POST", self.URL, headers=self.HEADERS, data=json.dumps(self.payload))
        return 
    
    def add_value(self,column,value):
        self.payload['properties'][column] =  {'rich_text': [{'text': {'content': value}}]}
        return self.payload
    
    def add_name(self,value):
        self.payload['properties']['Name'] =  {'title': [{'text': {'content': value}}]}
        return self.payload    
    
    def update_column(self,columns = None):
        """
        update notion's columns
        columns: list 
        """
        if columns != None:
            self.columns_list.extend(columns)
        self.payload = {
                "parent": { "database_id": self.datasetId },
                "properties": {
                    "Name": {
                        "title":{}
                    }}}
        if self.columns_list != None: 
            for item in self.columns_list:
                self.payload['properties'][item] = {'rich_text':{}} 
        self.create_dataset()
    
