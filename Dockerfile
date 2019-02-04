FROM ubuntu

RUN apt-get update
RUN apt-get install -y tor
RUN apt-get install -y python
RUN apt-get install -y python3.6
RUN apt-get install -y nginx
RUN apt-get install -y curl

#tor-configuration
COPY torrc /etc/tor/torrc

#scripts zur Geschwindigkeitsmessung
COPY speedtest-cli /workdir/
COPY torloader.py /workdir
COPY server.py /workdir

#angular-site zur Darstellung der Geschwindigkeit
COPY web /var/www/html

#nginx-configuration fuer den Redirect auf den Python-Http-Server
COPY torloader.conf /etc/nginx/sites-available/default

WORKDIR /workdir

#Fuer den Aufruf  von speedtest muss die HTTPS-Verifizierung von Python deaktiviert werden
CMD 	/bin/bash && \
	export PYTHONHTTPSVERIFY=0 && \
	nginx && \
	python3.6 torloader.py

EXPOSE 9050 80