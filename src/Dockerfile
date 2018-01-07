FROM python:alpine

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY buildutils/runtests /usr/bin/
COPY main/* ./

CMD [ "python", "./your-daemon-or-script.py" ]
