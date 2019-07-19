Agents pour ExtensiveAutomation
======================================

Introduction
------------

Les agents permettent de déporter l'exécution d'un test.
Les agents peuvent être exécutés sur Windows, Linux et MacOS via:
 - la ligne de commande
 - un mode graphique
Il est n'est pas recommandé d'utiliser les agents dans un environnement de production.

Installation depuis les sources
------------------------

Les agents supportent Python2 et 3. Cette procédure explique comment exécuter le client.

1. Cloner le dépôt sur votre machine

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-apptoolbox.git
   
2. Installer les paquets suivants avec la commande pip

        py -m pip install pyinstaller pylint pyqt5

3. Exécuter les agents 

    * en mode graphique

            cd extensiveautomation-apptoolbox/
            py Systray.py
        
    * en mode ligne de commande
    
            cd extensiveautomation-apptoolbox/
            py toolagent.py
            
            Usage: ./toolagent.py --server_host [address] --agent_name [agent name] --agent_type [agent type]

            Options:
              -h, --help            show this help message and exit
              --server_host=SERVER_HOST
                                    Server host address
              --server_port=SERVER_PORT
                                    Server port (optional default=8080)
              --agent_name=AGENT_NAME
                                    Agent name (example: agent.win.curl01)
              --agent_type=AGENT_TYPE
                                    Agent type (adb|command|curl|database|dummy|file|ftp|s
                                    elenium2-server|selenium3-server|sikulix-
                                    server|gateway-sms|soapui|socket|ssh)
              --proxy_host=PROXY_HOST
                                    Proxy address (optional)
              --proxy_port=PROXY_PORT
                                    Proxy port (optional)
                                
Version portable pour Windows
--------------------------------

Une version portable sur Windows peut être disponible. 
La procédure ci-dessous explique comment.

1. Allez dans le répertoire `Scripts/qt5/` et exécuter le script `MakePortable.bat`

2. L'exécutable est disponible dans le répertoire `dist`