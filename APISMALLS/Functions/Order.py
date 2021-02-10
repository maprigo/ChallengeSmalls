import pendulum
from pendulum.constants import DAY_OF_WEEK_TABLE


class Order:
    def __init__ (self):
        self.bDate = self.billingDate()
        
        
    def billingDate(self):
        now = pendulum.now().date() # set now and return just only date 
        date=now.add(days=21).next(pendulum.FRIDAY) # set the period after 3 weeks and set next friday in target 
        return date
            


  

