FROM python:3

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/src/Converttopdf

COPY req.txt /usr/src/Converttopdf
ADD wsgi-entrypoint.sh /usr/src/Converttopdf/wsgi-enrtypoint.sh
ENV PYTHONPATH=/usr/src/Converttopdf

RUN python -m pip install --upgrade pip
RUN pip install -r req.txt

COPY . /usr/src/Converttopdf
EXPOSE 8000

CMD [ "chmod", "+x", "wsgi-entrypoint.sh" ]
