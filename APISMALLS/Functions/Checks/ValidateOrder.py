import json
from validict import validate


class Validate:
    def __init__(self, json):
        self.json = json
        
    def validateOrder(self):
        #define de template for data on payload
        template = {"order": {"items": [{"name" : str, "quantity" : float}]}}
        try: #this is the way to pass except of error validator
            validate(template, self.json)
        except:
            return False
        return True
        

