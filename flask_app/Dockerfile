FROM python:3.6.7

# setup flask app dir
WORKDIR usr/src/flask_app
COPY . .

# setup SSL certs, if you organization requires it
# COPY <local-path-to-cert> /usr/local/share/ca-certificates/
RUN update-ca-certificates

# install required packages
RUN pip install --no-cache-dir -r requirements.txt --cert /etc/ssl/certs/ca-certificates.crt