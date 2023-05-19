FROM python:3.10

WORKDIR /app

ADD . .

RUN pip install -r requirements.txt

RUN chmod +x run.sh

CMD python -m lab6.ws.main