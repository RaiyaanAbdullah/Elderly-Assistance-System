import schedule
import time
import requests
from datetime import datetime



def create_data():
    required_medicine=[] #The medicine history data that will be sent to server
    keys_to_remove = ["id","started"]

    fetch_url = 'http://127.0.0.1:8000/api/medicine/'
    destination_url = 'http://127.0.0.1:8000/api/medicine-history/'
    
    '''
    Example of data to be sent
    {
        "name": "Ranitid",
        "date":"2020-04-15",
        "time": "15:23:00",
        "consumed": True,
        "time_of_consumption": "15:23:00"
        
    }
    '''

    received = requests.get(fetch_url).json() #The medicine list data received sent from server
    today = datetime.today().strftime('%Y-%m-%d')
    new_keys = {"date" : today, "consumed" : "False", "time_of_consumption" : "00:00:00"}

    for medicine in received:
        for key in keys_to_remove:
            medicine.pop(key)
        medicine.update(new_keys)
        required_medicine.append(medicine)
        
        
        
    for medicine in required_medicine:
        sent_data = requests.post(destination_url, data = medicine)
        print(sent_data)
        
schedule.every(10).seconds.do(create_data)

while 1:
    schedule.run_pending()
    time.sleep(1)