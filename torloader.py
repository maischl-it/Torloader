#!/usr/bin/env python3.6

import time
import subprocess
import server

speed = 0.0
processTor = None

# Solange die Geschwindigkeit nicht über 2MBit/s liegt, wird Tor neu gestartet
while speed < 2:
    # Den Tor-Prozess beenden, wenn er bereits gestartet wurde
    if processTor != None:
        processTor.kill()

    processTor = subprocess.Popen(["/usr/bin/tor"])

    time.sleep(5)

    # Mit Torify den command über das Tor-Netzwerk ausführen
    processSpeedtest = subprocess.Popen(
        ["torify", "./speedtest-cli", "--simple", "--no-upload"], stdout=subprocess.PIPE)

    # Den Output des vorausgehenden Commands abholen
    output = str(processSpeedtest.communicate()[0])

    indexDownload = output.find("Download")
    indexMB = output.find("Mbit")

    print("OutputSEM: "+output)

    if len(output) >= indexMB:
        speed = float(output[indexDownload+10:indexMB-1])
    else:
        speed = 0.0

    print("speed "+str(speed))

f=open("/var/www/html/assets/speed.json","w")
# f=open("/home/sem/Desktop/test.json","w")
f.write("{\"speed\":"+str(speed)+"}")
f.close()

#HTTP-Server fuer den Neustart vom Tor-Service starten
print("StartServer")
server.startServer(9999)