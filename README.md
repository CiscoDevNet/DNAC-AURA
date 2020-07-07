# DNAC-AURA

The Cisco DNA Center AURA (Audit & Upgrade Readiness) command line tool performs a variety of health, scale & upgrade readiness checks for the DNA Center and the rest of the Fabric network. The tool is extremely simple to run and is executed on the DNA Center. The tool uses API calls, DB reads & show commands (read only operations) and hence, doesn't affect performance or cause impact to the DNA Center or the networking devices.

## To Run
This script needs to be downloaded onto Cisco DNA Center.  First ssh to DNAC.

```
ssh -p2222 maglev@<dnacIP>
```

The next step is to download to Cisco DNA Center. 

```
git clone https://github.com/CiscoDevNet/DNAC-AURA.git
```

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


