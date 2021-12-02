FROM python:3.7

WORKDIR /opt/app

COPY . .

RUN pip install --no-cache-dir purviewcli

ENTRYPOINT ["tail"]

CMD ["-f","/dev/null"]