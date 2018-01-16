FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY buildutils/* /usr/bin/
COPY main/* ./

EXPOSE 8080

ENTRYPOINT [ "startup" ]
