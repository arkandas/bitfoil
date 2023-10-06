FROM nginx:alpine

RUN apk add --update --no-cache bash apache2-utils sudo

RUN mkdir games

COPY ./nginx.conf /etc/nginx/nginx.conf

ARG NGINX_USER
ENV NGINX_USER $NGINX_USER

ARG NGINX_PASSWORD
ENV NGINX_PASSWORD $NGINX_PASSWORD

RUN htpasswd -c -b /etc/nginx/.htpasswd ${NGINX_USER} ${NGINX_PASSWORD}
