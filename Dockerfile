FROM python:3-alpine

WORKDIR /script

COPY requirements.txt .
COPY script.py .

RUN apk add --no-cache tzdata
ENV TZ=Europe/Oslo
RUN pip install -r requirements.txt

CMD [ "python", "-u", "script.py" ]