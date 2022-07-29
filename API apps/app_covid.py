#from typing_extensions import Self
import requests
#import config
"""
Documentation at 
https://documenter.getpostman.com/view/10808728/SzS8rjbc
"""
# 1.get the API data from the web server
# This API server does not require an API key
# 2. Convert the data into a useful python objects: usually a list or dictionaries



url = "https://api.covid19api.com/summary"


#data = self.response.json
#deaths = global_stats['TotalDeaths']
#cases = global_stats['TotalConfirmed']
#mortality_rate = deaths / cases

class Stats():

    def __init__(self, deaths, cases, mortality_rate, global_stats):
        self.deaths = deaths
        self.cases = cases
        self.mortality_rate = mortality_rate
        self.global_stats = global_stats

class ApiPull():

    def __init__(self):
        pass

        

    def get_global_stats(self):
        response = requests.get(url)
        data = response.json()
        global_stats = data['Global']
        return global_stats
    
if __name__ == "__main__":
    instance = ApiPull()
    print(instance.get_global_stats())