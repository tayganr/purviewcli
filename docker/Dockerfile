FROM python:3.7

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["tail"]

CMD ["-f","/dev/null"]