FROM python:3-onbuild

COPY dnsomatic.py /
COPY requirements.txt /usr/src/app/

CMD ["python", "dnsomatic.py"]