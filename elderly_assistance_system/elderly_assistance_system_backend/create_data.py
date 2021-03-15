import schedule
import time
import requests
from datetime import datetime
import datetime as dt
from medicine_history.models import MedicineHistory
from medicine.models import Medicine
from dateutil.relativedelta import relativedelta
import runpy
from OCR_code_video import ocr

def validity(Time):
    time_now=datetime.now().time()
    time_now = datetime.combine(dt.date.today(), time_now)
    timedelta_obj = relativedelta(time_now, Time)
    if timedelta_obj.hours==0 and -45<=timedelta_obj.minutes<=45:
        return 1
    else:
        return 0

def call_ocr_code():
    medicine_objects=Medicine.objects.all() #got todays routine medicine list
    loopCount=0
    for obj in medicine_objects:
        #time_list.append(obj.time)
        if(validity(dt.datetime.combine(dt.date.today(), obj.time))):  #check the medicine is correct for taking or not
            try:
                con_medicine=MedicineHistory.objects.get(medicine_id=int(obj.id),date=dt.datetime.now().date())
                if con_medicine.consumed==True:
                    print("You have already taken your scheduled medicines.",obj.name)
                    return 0
                else:
                    print("Time for ",obj.name," ",obj.time)
                    ocr(obj.name,obj.id,obj.time)


            except:
                #print(obj.id)
                pass
        else:
            loopCount+=1
        #missing_medicine_counter(obj)
    if loopCount==len(medicine_objects):
        #print(loopCount)
        print("Wrong time for medication")
        return 0


def create_data():
    required_medicine=[] #The medicine history data that will be sent to server
    keys_to_remove = ["name","time","started"]

    fetch_url = 'http://127.0.0.1:8000/api/medicine/'
    destination_url = http://127.0.0.1:8000/api/medicine-history/'
    
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
        medicine['medicine_id'] = medicine.pop('id')
        medicine.update(new_keys)
        required_medicine.append(medicine)
        
        
        
    for medicine in required_medicine:
        sent_data = requests.post(destination_url, data = medicine)
        print(sent_data)
        
schedule.every(5).minutes.do(create_data)

#create_data()
while 1:
    schedule.run_pending()
    time.sleep(1)
    call_ocr_code()