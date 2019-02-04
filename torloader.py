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

print("StartServer")

html = "<html style=\"background-color: red;\"><head><meta http-equiv=\"refresh\" content=\"30\"></head>Speed: " + \
    str(speed)+"</html>"

server.startServer(html, 9999)
