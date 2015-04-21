#!/bin/bash
# Reads in a .cfg file and creates a .bat file
# MIT License
# Opsdisk LLC | opsdisk.com 
 
import argparse
import re
import sys

version = '1.0'

def main():
    batchFile.write('''@echo off
setlocal enableextensions enabledelayedexpansion

if [%1] ==[] (
    set target=%COMPUTERNAME%
    echo [-] No target specified, using the local hostname: !target!
    rem exit /b
) else (
    set target=%1
)
set outputDir=!target!

echo [*] Making local output directory
mkdir !outputDir!
if not exist !outputDir! (
    echo    [-] Couldn't create local output directory.
    exit /b
) else (
    echo    [+] Successfully created local output directory
    echo ======================================
)
    ''')

    batchFile.write('echo [*] Starting survey' + '\n')
    batchFile.write('rem Prevents \"Please wait while WMIC is being installed\" being written if wmic is not installed.' + '\n')
    batchFile.write('wmic foo >nul 2>&1' + '\n')
    for line in configFile :
        
        if line in ['\n', '\r\n']: # Blank lines
            pass
        elif re.match('#', line): # Comments
            pass    
        else:
            try:
                execute = line.split(';')[0]
                name = line.split(';')[1]
                command = line.split(';')[2]
                logfile = line.split(';')[3]
                
                if execute in ['y', 'Y'] :
                    batchFile.write('echo [*] Getting ' + name + '\n')
                    batchFile.write(command + ' > !outputDir!\\' + logfile)
                    batchFile.write('echo        [+] Received ' + name + '\n')
                    batchFile.write('echo ' + '='*60 + '\n')
                    batchFile.write('\n')
            except:
                pass
    
    batchFile.write('''
echo [*] Output directory: !outputDir!
echo [*] Script finished

endlocal
    ''')
    
    batchFile.close()
    configFile.close()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='batchconfig version ' + version)
    parser.add_argument('-i', dest="configfile", action='store', help=".cfg file to read in")
    parser.add_argument('-o', dest='batchfile', action='store', default='batchconfig.bat', help='.bat output file (batchconfig.bat if unspecified)')
    args = parser.parse_args()
    
    if not args.configfile:
        print "[-] Specify a config file use"
        sys.exit(0)
    if not args.batchfile:
        print"[-] Specify a .bat output file"
        sys.exit(0)
    
    configFile = open(args.configfile, 'r')
    batchFile = open(args.batchfile, 'w')
    
    main()
    
    print "[*] Done"
    