# Use the python official image
FROM python:3

EXPOSE 5000

RUN apt-get update && apt-get install -y ffmpeg

# Set the working directory
WORKDIR /usr/src/app

COPY requirements.txt /usr/src/app

RUN pip install --no-cache-dir -r requirements.txt

ENV PYTHONPATH="${PYTHONPATH}:/usr/src/app"

COPY ./src ./src

CMD [ "python", "./src/app/main.py" ]
