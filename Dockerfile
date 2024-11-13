FROM python:3.12.1
COPY . /app
RUN pip install mysql-connector-python && pip install imap-tools && pip install requests
WORKDIR /app
CMD python main.py