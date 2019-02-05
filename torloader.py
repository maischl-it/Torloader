#!/usr/bin/env python3.6

import time
import subprocess
import server
import os
import signal

# Die PID einer laufenden TOR-Instanz bestimmen


def determinePidOfTor():
    processSpeedtest = subprocess.Popen(
        ["ps", "-C", "tor", "-o", "pid="], stdout=subprocess.PIPE)

    pid = str(processSpeedtest.communicate()[0])

    # Pruefen, ob eine PID zurueckgegeben
    # oder keine gefunden wurde
    if len(pid) == 3:
        return None
    else:
        return int(pid[3:7])


def startTorloader():
    speed = 0.0
    processTor = determinePidOfTor()

    # Solange die Geschwindigkeit nicht über 2MBit/s liegt, wird Tor neu gestartet
    while speed < 2:
        # Den Tor-Prozess beenden, wenn er bereits gestartet wurde
        if processTor != None:
            os.kill(processTor, signal.SIGTERM)
            time.sleep(2)

        processTor = subprocess.Popen(["/usr/bin/tor"]).pid

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

    print(__debug__)
    f = open("/var/www/html/assets/speed.json", "w")
    f.write("{\"speed\":"+str(speed)+"}")
    f.close()


if __name__ == '__main__':
    startTorloader()
