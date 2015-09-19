import requests, time, os
import logging

logging.basicConfig()
log = logging.getLogger("dockerdnsomatic")
log.addFilter(logging.Filter(name="dockerdnsomatic"))
log.setLevel(logging.INFO)

username=os.getenv("MATICUSERNAME")
password=os.getenv("MATICPASSWORD")
lapse=float(os.getenv("MATICLAPSE"))


while True:
    r = requests.get('https://updates.dnsomatic.com/nic/update', auth=(username, password))
    status = r.status_code
    log.info(status)
    if status != 200: 
        log.error(r.text)
    time.sleep( lapse )