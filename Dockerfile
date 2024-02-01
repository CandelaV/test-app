

FROM python:3.9-slim

WORKDIR /src
COPY ./requirements.txt /src/requirements.txt
COPY ./src /src/

# Copy uvicorn log config
COPY log_conf.yml /src/

RUN pip install --upgrade pip
RUN pip install --no-cache-dir --upgrade -r /src/requirements.txt

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--log-config", "log_conf.yml", "--no-access-log"]