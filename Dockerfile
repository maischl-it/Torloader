FROM ubuntu

RUN apt-get update
RUN apt-get install -y tor
RUN apt-get install -y python
RUN apt-get install -y python3.6

COPY torrc /etc/tor/torrc
COPY speedtest-cli /workdir/
COPY torloader.py /workdir
COPY server.py /workdir

WORKDIR /workdir

#Fuer den Aufruf  von speedtest muss die HTTPS-Verifizierung von Python deaktiviert werden
CMD 	/bin/bash && \
	export PYTHONHTTPSVERIFY=0 && \
	python3.6 torloader.py

EXPOSE 9050 9999