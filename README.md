Agents for ExtensiveAutomation
======================================

Introduction
------------

Agents enable to interact with the system under test  ExtensiveAutomation server.
It's not recommended to use agents in production environnement.

Installation from source
------------------------

The toolbox support both Python 2 and 3. Follow this procedure to execute it
on Windows with Python3.

1. Clone this repository on your machine

        git clone https://github.com/ExtensiveAutomation/extensiveautomation-apptoolbox.git
   
2. Add additional Python packages with the pip command

        py -m pip install pyinstaller pylint pyqt5

3. Execution of agents exists in two modes

    * graphical mode

            cd extensiveautomation-apptoolbox/
            py Systray.py
        
    * command line
    
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

Build portable version for Windows
--------------------------------

Portable version can be build on Windows. Follow this procedure if you want to.

1. Go in the folder `Scripts/qt5/` and execute the script `MakePortable.bat`

2. The output is available in the `dist` folder



How to use the toolbox without reverse proxy in front of the server ?
--------------------------------------------------------------------

By default, the toolbox is configured to be used with a reverse proxy.
It's possible to change that by updating the `settings.ini` as follow:

        [Server]
        rest-api-path = /
        rest-api-ssl = False
        rest-api-port = 8081
        ssl-support = False
        port = 8083