FROM python:3.11.6-alpine

RUN mkdir /shop
COPY . /shop
RUN pip install --no-cache-dir -r /shop/requirements.txt

CMD [ "python", "/shop/main.py" ]
