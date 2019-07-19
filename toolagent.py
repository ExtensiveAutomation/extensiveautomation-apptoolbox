#!/usr/bin/python

# -------------------------------------------------------------------
# Copyright (c) 2010-2019 Denis Machard
# This file is part of the extensive automation project
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
# MA 02110-1301 USA
# -------------------------------------------------------------------

import Core.InitTool as Tools
from Libs import Settings

from optparse import OptionParser
import sys
import os
import inspect

try:
    xrange
except NameError: # support python3
    xrange = range

# unicode = str with python3
if sys.version_info > (3,):
    unicode = str
    
arg = sys.argv[0]
pathname = os.path.dirname(arg)
path_install = os.path.abspath(pathname)

settingsFile = '%s/settings.ini' % path_install
if not os.path.exists(settingsFile):
    print('config file settings.ini doesn\'t exist.')
    sys.exit(-1)

# adding missing folders
if not os.path.exists( "%s/Logs/" % path_install ):
    os.mkdir( "%s/Logs" % path_install )
if not os.path.exists( "%s/Tmp/" % path_install ):
    os.mkdir( "%s/Tmp" % path_install )
    
Settings.initialize()

plugins = {} 
pkg =  __import__( "Plugins" )
for listing in dir(pkg):
    obj = getattr(pkg, listing)
    if inspect.ismodule(obj):
        for listing2 in dir(obj):
            if listing2.endswith("Agent"):
                obj2 = getattr(obj, listing2)
                if inspect.ismodule(obj2):
                    plugins[obj2.__TYPE__] = obj2
            
# prepare the command line with all options	
parser = OptionParser()
parser.set_usage("./toolagent.py --server_host [address] --agent_name [agent name] --agent_type [agent type]")

parser.add_option('--server_host', dest='server_host', default='127.0.0.1',
                    help="Server host address")
                    
parser.add_option('--server_port', dest='server_port', default=8080,
                    help="Server port (optional default=8080)")
                    
parser.add_option('--agent_name', dest='agent_name', default='', 
                    help="Agent name (example: agent.win.curl01)")
                    
parser.add_option('--agent_type', dest='agent_type', default='', 
                    help="Agent type (%s)" % '|'.join(plugins.keys()) )

parser.add_option('--proxy_host', dest='proxy_host', default='', 
                    help="Proxy address (optional)")
parser.add_option('--proxy_port', dest='proxy_port', default='', 
                    help="Proxy port (optional)")
                    
(options, args) = parser.parse_args()
    
if __name__ == "__main__":

    target_ssl = True
    target_port = 8080
    target_addr = ''

    # check the agent type provided
    if options.agent_type not in plugins.keys():
        parser.print_help()
        sys.exit(2)
    
    Tools.initialize()
    
    if options.server_host and options.agent_name and options.agent_type:
        Tools.start( serverIp=options.server_host, 
                     serverPort=options.server_port, 
                     toolType=options.agent_type, 
                     toolName=options.agent_name,
                     toolDescr="", 
                     sslSupport=True, 
                     isAgent=0, 
                     fromCmd=True )
                     
    elif options.server_host and options.agent_name and options.agent_type and options.proxy_host and options.proxy_port:
        Tools.start( serverIp=options.server_host, 
                     serverPort=options.server_port, 
                     toolType=options.agent_type, 
                     toolName=options.agent_name,
                     toolDescr="", 
                     sslSupport=True, 
                     isAgent=0, 
                     fromCmd=True,
                     supportProxy=True,
                     proxyIp=options.proxy_host, 
                     proxyPort=options.proxy_port
                     )
                     
    else:
        parser.print_help()
        sys.exit(2)
        
    sys.exit(0)    