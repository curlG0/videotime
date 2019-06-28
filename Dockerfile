FROM python

WORKDIR /app

ADD videotime videotime
ADD requirements.txt requirements.txt

RUN pip install -r requirements.txt

RUN python videotime/self_critical/get_weights.py

CMD python -m videotime.main
