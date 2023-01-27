FROM python:3.11.1-alpine3.17
RUN mkdir -p /garden
# Change hour
RUN cp /usr/share/zoneinfo/Europe/Madrid /etc/localtime
RUN echo "Europe/Madrid" > /etc/timezone
WORKDIR /PyResources
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
WORKDIR /garden