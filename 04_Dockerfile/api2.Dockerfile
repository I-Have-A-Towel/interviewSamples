######
#  Q: Am I better-written than api1.Dockerfile? Why or why not?
#########

FROM python:3.7

RUN mkdir /app && wget https://example.com/largelibthatdoesnotchange -O /app/largelibthatdoesnotchange;

RUN apt-get update \
  && apt-get clean \
  && apt-get -y install vim

COPY api_src/requirements.txt /app/requirements.txt
RUN cd /app && pip3 install -r requirements.txt

COPY api_src /app
WORKDIR /app

ENV PYTHONUNBUFFERED=1

ENTRYPOINT  [ "python3.7", "-u", "api.py" ]