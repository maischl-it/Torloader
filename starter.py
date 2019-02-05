#!/usr/bin/env python3.6

import threading
import torloader
import server

#Torloader in einem Thread starten, damit
#der HTTP-Server sofort gestartet werden kann 
threading.Thread(target=torloader.startTorloader).start()

server.startServer(9999)