######
#  Q: Am I better-written than api2.Dockerfile? Why or why not?
#########

FROM python:3.7

RUN mkdir app
COPY api_src /app
WORKDIR /app

RUN apt-get update; \
  apt-get clean; \
  apt-get -y install vim; \
  cd /app && pip3 install -r requirements.txt; \ 
  wget https://example.com/largelibthatdoesnotchange -O /app/largelibthatdoesnotchange;

RUN echo "echo 'Simulating long-running make process...'; sleep 300" > /app/fake_make.sh && chmod +x /app/fake_make.sh

ENV PYTHONUNBUFFERED=1

ENTRYPOINT  [ "python3.7", "-u", "api.py" ]