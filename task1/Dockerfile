FROM ubuntu:20.04 as build

RUN apt-get update
RUN  apt-get install fortune-mod python3 fcgiwrap nginx  -y
RUN mkdir /usr/lib/cgi-bin -p
COPY ./test.py /usr/lib/cgi-bin/test.py
RUN chmod 755 /usr/lib/cgi-bin/test.py
COPY ./default /etc/nginx/sites-available/default

CMD  /etc/init.d/fcgiwrap start \
    && nginx -g 'daemon off;'