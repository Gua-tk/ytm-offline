# Use the python official image
FROM python:3

EXPOSE 5000

# Set the working directory
WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/usr/src/app"

COPY ./src ./src

CMD [ "python", "./src/controllers/APIController.py" ]