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


class ApiPull():

    def __init__(self):
        pass

    def get_global_stats(self):
        response = requests.get(url)
        data = response.json()
        global_stats = data['Global']
        return global_stats

    def get_deaths(self):
        deaths = self.get_global_stats()
        death_stats = deaths['TotalDeaths']
        return death_stats

    def get_cases(self):
        cases = self.get_global_stats()
        case_stats = cases['TotalConfirmed']
        return case_stats

    # def get_mortality_rate(self):
    #     deaths = self.get_deaths
    #     cases = self.get_cases
    #     print(deaths)
    #     print(cases)
    #     mortality_rate = deaths / cases
    #     return mortality_rate


if __name__ == "__main__":
    instance = ApiPull()
    print(instance.get_global_stats())
    death = (instance.get_deaths())
    cases = (instance.get_cases())
    print (cases)
    print(death)
    print(death/cases)

