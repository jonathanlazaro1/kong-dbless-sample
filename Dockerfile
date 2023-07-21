FROM kong:3.3

WORKDIR /home/kong
COPY ./kong.json .
