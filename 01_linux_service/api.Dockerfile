FROM python:3.7

RUN apt-get update \
  && apt-get clean \
  && apt-get -y install vim \
  && mkdir /app

COPY api_src/requirements.txt /app/requirements.txt
RUN cd /app && pip3 install -r requirements.txt

COPY api_src /app
WORKDIR /app

# ensures all prints go straight to stdio instead of buffering
ENV PYTHONUNBUFFERED=1

ENTRYPOINT  [ "python3.7", "-u", "api.py" ]