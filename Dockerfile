FROM python:3.10

WORKDIR /app
ADD main.py /app/
RUN pip install --no-cache pyzmq click tenacity

ENTRYPOINT [ "python", "main.py" ]
CMD [ "server" ]
