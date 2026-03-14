# start with the slim python image — keeps the container small
FROM python:3.9-slim

WORKDIR /app

# copy requirements first so Docker can cache the dependency install layer
# (if requirements don't change, this layer won't re-run on rebuilds)
COPY requirements.txt .

# make sure pip and setuptools are up to date before installing anything
RUN pip install --upgrade pip setuptools

# install our app's dependencies (no-cache keeps the image lean)
RUN pip install --no-cache-dir -r requirements.txt

# now copy the actual source code
COPY app ./app

EXPOSE 5000

# fire up the flask server
CMD ["python", "app/main.py"]
