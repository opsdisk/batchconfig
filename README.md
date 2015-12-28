batchconfig.py is a Python script to create customized Windows batch files for the purpose of conducting quick Incident Response, surveying a box post-exploitation, or assisting network administrators in managing their networks.  

batchconfig.py is written for Python 2 and only requires a configuration file and an output batch file name.

    python batchconfig.py -i config.cfg -o mybatch.bat

The configuration file is in the form:

    include in batch file? ; friendly name ; windows command ; output file

Examples include:

    y;tasklist modules (dlls);tasklist /m;tasklist_m.txt
    y;windows tasks;dir /a /od c:\windows\tasks;dir_tasks.txt 
   
A configuration file for Windows 6.X kernels is included with one for Windows 5.X kernels soon to follow (added May 12, 2015).  There are slight differences in where Windows placed files, registry keys, and the available commands between the kernel versions.  The batch file should be run from an elevated administrator shell in order to collect the most information.

The configuration files are combination of information collected through network administration, red teaming, cyber defense competitions, incident response, post-exploitation surveys, and various sources such as:

* [SANS Digital Forensics Poster](http://blogs.sans.org/computer-forensics/files/2012/06/SANS-Digital-Forensics-and-Incident-Response-Poster-2012.pdf)
* [Windows Sysinternals autoruns.exe](https://technet.microsoft.com/en-us/sysinternals/bb842062.aspx)

Contributions and suggestions from the community are always welcome.  You can find the files on [https://github.com/opsdisk/batchconfig](https://github.com/opsdisk/batchconfig) and follow [@opsdisk](https://twitter.com/opsdisk) on Twitter for the latest updates. 
