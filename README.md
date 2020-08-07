# DNAC-AURA

The Cisco DNA Center AURA (Audit & Upgrade Readiness) command line tool performs a variety of health, scale & upgrade readiness checks for the DNA Center and the rest of the Fabric network. The tool is extremely simple to run and is executed on the DNA Center. The tool uses API calls, DB reads & show commands (read only operations) and hence, doesn't affect performance or cause impact to the DNA Center or the networking devices.

## To Download

This script needs to be downloaded onto Cisco DNA Center.  First ssh to DNAC.

```
ssh -p2222 maglev@<dnacIP>
```

The next step is to get the script onto Cisco DNA Center.  There are three ways of doing this, depending on access from DNAC to the internet 
### Option 1.  git clone direct
If you have access to the internet from DNAC, can clone the repository (containing the executable)

```
git clone https://github.com/CiscoDevNet/DNAC-AURA.git
```
### Option 2. git clone via proxy
If DNAC needs a proxy to get to the internet, you will need to provide a proxy for git command.
NOTE:  please do not set a permanent environment variable as this will stop you from accessing some DNAC commands like maglev.

The example below uses an inline environment variable, just for the git command.  Make sure to put in the correct proxy url (including port) 
```
https_proxy=https//<your proxy> git clone https://github.com/CiscoDevNet/DNAC-AURA.git
```

### Option 3. Isolated environment.  
You will need to clone (using method 1 or 2) to an intermediate machine and copy to DNAC, using scp.  Remember to use port 2222 with the -P option to scp.
```
scp -P 2222 ./DNAC-AURA/dnac_aura  maglev@<mydnac>:
```

## To Run
There will be a directory called DNAC-AURA.  You can either change into directory, or run direct from the home directory.
You will be prompted for the admin username and password as well as the sudo password (maglev password).
```
$ ./DNAC-AURA/dnac_aura 

####################################################
###                                              ###
###   Welcome to the Cisco DNA Center AURA Tool  ###
###             version:1.0.2                    ###
###                                              ###
####################################################
###
###   All Cisco DNA Center based health,scale,upgrade readiness,Assurance & SDA checks will be run ###
###
 INFO:Performing maglev login...
[administration] username for 'https://kong-frontend.maglev-system.svc.cluster.local:443': admin
[administration] password for 'admin': 
 INFO:User 'admin' logged into 'kong-frontend.maglev-system.svc.cluster.local' successfully


#01:Checking:Determine Cisco DNA Center Product Type, Serial number, SW Version & Node IP
<snip>
```

After the script finishes the report and logs will be available.
```
******
Cisco DNA Center AURA tool has successfully completed.
Report and Logs can be found at:
 -- Cisco DNA Center AURA Report : /data/tmp/dnac_aura/reports/DNAC_AURA_Report_2020-07-07_04:20:09.pdf
 -- Cisco DNA Center AURA Logs : /data/tmp/dnac_aura/logs/2020-07-07_04:20:09/aura_op_file_2020-07-07_04:20:09.log
 -- Cisco DNA Center AURA tar file with all logs included : /data/tmp/dnac_aura/logs/DNAC_AURA_Logs_2020-07-07_04:20:09.tar.gz
 -- All relevant output logs for this run can also be found here : /data/tmp/dnac_aura/logs/2020-07-07_04:20:09
```

## Other Options
```
./DNAC-AURA/dnac_aura --help
usage: dnac_aura [-h] [-v] [-V] [-s] [-u U] [-n N] [-o] [-c]

Select options.

optional arguments:
  -h, --help  show this help message and exit
  -v          verbose
  -V          version information
  -s          Run additional SDA checks. To execute these checks, the tool
              will login to other devices in the fabric and collect show
              command outputs.
  -u U        Upload report and logs file to the SR. Please provide SR and
              password in the format sr_number:sr_password
  -n N        Add customer name to the PDF report on the first page (the
              summary page)
  -o          To collect CLI outputs from the network devices via the Cisco
              DNA Center. Ensure you have the captureFile.yaml in the same
              folder as this tool.
  -c          Compare configurations across multiple devices. You can choose 2
              timestamps from previous captures taken with the -o option. PDF
              Report will be generated with the diffs.
              
 ```

For release updates, see ChangeLog.md
