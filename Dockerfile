FROM python

WORKDIR /app

ADD requirements.txt requirements.txt
RUN pip install -r requirements.txt

ADD videotime videotime
ADD configs configs
RUN python videotime/self_critical/get_weights.py

CMD python -m videotime.main
