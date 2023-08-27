# Use the python official image
FROM python:3

EXPOSE 5000

# Set the working directory
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/usr/src/app"

COPY ./src  /usr/src/app/src

CMD [ "python", "./src/controllers/APIController.py" ]
