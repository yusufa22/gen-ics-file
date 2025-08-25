FROM alpine

COPY ./* /srv/gencal/
WORKDIR /srv/gencal/
RUN apk add --no-cache python3 py3-pip
RUN pip3 install -r requirements.txt --break-system-packages

CMD [ "python3", "main.py", "prod" ]