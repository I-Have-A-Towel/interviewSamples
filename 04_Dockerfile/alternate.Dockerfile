###
# What might be the benefit of:
#   a) splitting the installation/setup activities into separate RUN statements
#       ie: apt-get installations, pip installations, largelib download
#   b) running them in a specific order (other than necessity)
#   c) setting `ENV PYTHONUNBUFFERED=1`
##
FROM python:3.7

RUN mkdir app
COPY api_src /app
WORKDIR /app

RUN apt-get update; \
  apt-get clean; \
  apt-get -y install vim; \
  cd /app && pip3 install -r requirements.txt; \ 
  wget https://example.com/largelib -O /app/largelib;

ENV PYTHONUNBUFFERED=1

ENTRYPOINT  [ "python3.7", "-u", "api.py" ]