FROM python:3.7-alpine as base
#ENV BIBLE_HOME=production

#RUN apt-get update -y && \
#    apt-get install -y python-pip python-dev

# We copy just the requirements.txt first to leverage Docker cache
RUN mkdir /app/
WORKDIR /app/

COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
ENV FLASK_APP=main.py

################## START IMAGE: DEBUGGER ############################
FROM base as debug
RUN pip install ptvsd

WORKDIR /app/
CMD python3 -m ptvsd --host 0.0.0.0 --port 5678 --wait --multiprocess -m flask run -h 0.0.0 -p 5000

################### START IMAGE: PRODUCTION #########################
FROM base as prod

ENTRYPOINT [ "python3" ]
CMD [ "main.py" ]