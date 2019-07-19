# -*- mode: python -*-

block_cipher = None

datas = [ 
            ( './releasenotes.txt', '.'),
            ( './Resources/small_installer.bmp', '.'),
            ( './settings.ini', '.' ),
            ( './HISTORY', '.'),
            ( './VERSION', '.'),
            ( './LICENSE-LGPLv21', '.'),
            ( './Dlls64/opengl32sw.dll', '.' ),
            ( './Dlls64/imageformats', 'imageformats' ),
            ( './Resources/ExtensiveAutomationToolbox.ico', '.' )
        ]
 
import os 
for f in os.listdir( "./Plugins/"):
    if f == "__pycache__": continue
    if os.path.isdir( "./Plugins/%s" % f ):
        datas.append( ( "./Plugins/%s/" % f, "Plugins/%s/" % f) )
        
hiddenimports = [
    "filecmp",
    "pymysql", 
    "psycopg2", 
    "pymssql",
    "paramiko",
    "selenium",
    "selenium.webdriver",
]   

a = Analysis(['Systray.py'],
             pathex=[ '.', './Dlls64/' ],
             binaries=[],
             datas=datas,
             hiddenimports=hiddenimports,
             hookspath=[],
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)
exe = EXE(pyz,
          a.scripts,
          exclude_binaries=True,
          name='ExtensiveAutomationToolbox',
          debug=False,
          strip=False,
          upx=True,
          console=False,
          icon='./Resources/ExtensiveAutomationToolbox.ico')
coll = COLLECT(exe,
               a.binaries,
               a.zipfiles,
               a.datas,
               strip=False,
               upx=True,
               name='ExtensiveAutomationToolbox')
