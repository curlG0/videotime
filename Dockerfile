FROM python

WORKDIR /app

ADD videotime videotime
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

CMD python videotime/main.py
