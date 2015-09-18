import requests, time, os

username=os.getenv("MATICUSERNAME")
password=os.getenv("MATICPASSWORD")
lapse=float(os.getenv("MATICLAPSE"))


while True:
    r = requests.get('https://updates.dnsomatic.com/nic/update', auth=(username, password))
    status = r.status_code
    print(status)
    if status != 200: 
        print(r.text)
    time.sleep( lapse )