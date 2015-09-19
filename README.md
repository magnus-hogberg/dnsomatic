# Docker DNS-O-MATIC

Runs a python script in a while loop that calls dnsomatic nic api. https://www.dnsomatic.com/wiki/api

Use requests library. http://docs.python-requests.org/en/latest/


Example to run:

    docker run -d -e MATICUSERNAME={OMATICUSERNAME} -e MATICPASSWORD={OMATICPASS} -e MATICLAPSE=300 sector7b/dnsomatic