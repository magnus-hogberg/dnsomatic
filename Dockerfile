FROM resin/raspberry-pi-python:3-slim

COPY dnsomatic.py /
COPY logging.conf /
COPY requirements.txt /usr/src/app/
RUN pip install -r /usr/src/app/requirements.txt

CMD ["python", "dnsomatic.py"]
