FROM python:3.7

RUN mkdir app
COPY api_src /app
WORKDIR /app

RUN apt-get update; \
  apt-get clean; \
  apt-get -y install vim; \
  cd /app && pip3 install -r requirements.txt; \
  wget https://example.com/largelib -O /app/largelib;

# ensures all prints go straight to stdio instead of buffering
ENV PYTHONUNBUFFERED=1

ENTRYPOINT  [ "python3.7", "-u", "api.py" ]