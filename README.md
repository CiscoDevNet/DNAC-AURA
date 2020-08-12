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

## What does it check
Run it to find out.  Here is a sample of some of the checks that are run
```
****** Running Platform Checks ******
#03:Checking:CPU Load Average
#04:Checking:Disk Layout
#05:Checking:Disk Space Usage
#06:Checking:iNodes Utilization
#07:Checking:Disk I/O throughput (>200MB/s)
#08:Checking:DRAM Total Available Memory
#09:Checking:DRAMs Installed in the appliance
#10:Checking:Processor Cores Enabled and Status
#11:Checking:Docker Status
#12:Checking:Docker Proxy settings
#13:Checking:Kubelet Status
#14:Checking:Version of Cisco DNA Center this was built from
 INFO:Check completed successfully
#15:Checking:Cluster Node Reachability - nodes : [u'10.10.10.144']
#16:Checking:Interface Reachability - all nodes : [u'10.66.104.84', u'10.10.10.144']
#17:Checking:VIP Reachability - VIPs : []
#01:Checking:Cluster Subnet Overlap with Internal Addresses
INFO:Subnet Overlap Check Looks OK
#18:Checking:Number of DNS servers configured in etcd on nodes (<=3)
#19:Checking:Number of /etc/resolv.conf entries (<=4)
#20:Checking:DNS config - /etc/network/interfaces
#21:Checking:DNS Reachability - DNS : [u'171.70.168.183']
#22:Checking:DNS server can resolve www.ciscoconnectdna.com
#23:Checking:NTP server Sync : [u'ntp.esl.cisco.com']
#24:Checking:Certificate Validity and Expiry
 INFO:Certificate Validity Check looks OK. It is valid for 121 more days
#25:Checking:Expiry of truststore certificates
#26:Checking:NTP Service status on the Cisco DNA Center
#27:Checking:NTP Server Time Sync
#28:Checking:Status of PMTU discovery
#29:Checking:Node Display
#30:Checking:Node Status
 INFO:Checking Condition OutOfDisk
 INFO:Checking Condition MemoryPressure
 INFO:Checking Condition DiskPressure
 INFO:Checking Condition PIDPressure
 INFO:Checking Condition Ready
#31:Checking:Appstack Status
#32:Checking:Check Services for High Restart Counts
#33:Checking:State of ISE states in DB
#34:Checking:External authentication configured for DNAC users
#35:Checking:Checking Count of Scalable Groups, Contracts and Access Policies in DNAC DB
#36:Checking:Glusterfs Instances
#37:Checking:Glusterfs NODE_NAME check
#38:Checking:Glusterfs Clustering
#39:Checking:ETCD Cluster Health
#40:Checking:ETCD Storage Size
#41:Checking:ETCD memory utilization
#42:Checking:ETCD binding to loopback(localhost/127.0.0.1
#43:Checking:Postgres Cluster Status
#44:Checking:Postgres size
#45:Checking:MongoDB Cluster Health and Sync Status
#46:Checking:Checking MongoDB for Stale Connections from collector-manager
#47:Checking:Checking MongoDB CPU in docker stats
#48:Checking:Checking if MongoDB is locked
Checking if Mongodb is writeable...
#49:Checking:InfluxDB Health
#50:Checking:InfluxDB Memory Utilization
#51:Checking:Cassandra Health
#52:Checking:Cassandra status
#53:Checking:Rabbitmq Cluster Health
Checking health of node 'rabbit@rabbitmq-0.rabbitmq.maglev-system.svc.cluster.local' ...
#54:Checking:Rabbitmq Cluster Status
#55:Checking:Rabbitmq Queue Status
#56:Checking:Rabbitmq Queues with Unacknowledged messages
#57:Checking:Zookeeper Cluster Health
#58:Checking:Zookeeper Cluster Status
#59:Checking:Backup History
****** Upgrade Readiness Checks ******
#02:Checking:RCA Files Disk Usage
#03:Checking:Count of Exited containers
#04:Checking:Count of Non Running Pods
#05:Checking:Maglev Catalog Settings
#06:Checking:Direct connect to ciscoconnectdna
#07:Checking:Checking File-service for missing FileID mappings
#08:Checking:Checking Expiry of Maglev Certs
#09:Checking:Checking for Stale Mount Points
#10:Checking:Collector-ISE config has been cleaned up after a previous upgrade
#11:Checking:Backup Display to find Last Successful Backup
#12:Checking:Provision fail due to invalid migration status parameter
INFO:Check Passed
#13:Checking:Maglev Hook Installer Service status on the Cisco DNA Center
#14:Checking:Maglev Node Updater Service status on the Cisco DNA Center
#15:Checking:DNA Center Upgrade Path to the latest patch off 1.3.3.x
****** Running Assurance Checks ******
#01:Checking:Assurance Partition Disk Space Usage
#02:Checking:Assurance Services Status
#03:Checking:Check Assurance Backend Purge Job
#04:Checking:Check Assurance NDP Purge Job that cleans up Redis DB
#05:Checking:Assurance Pipeline status
#06:Checking:Device health score summary
#07:Checking:Client health score summary
****** Running SDA Checks ******
#01:Checking:Fabric device reachability inventory status
#02:Checking:Fabric inventory collection
#03:Checking:SDA:Cisco DNA Center & ISE integration status
#04:Checking:Verify the SSH connectivity between Cisco DNA Center and Cisco ISE
#16:Checking:ISE Compatibility check for ACA (Access Control Application)
#05:Checking:Cisco ISE Nodes Memory Usage
#06:Checking:Cisco ISE Nodes Disks Usage
#07:Checking:Status of the Cisco ISE processes
#08:Checking:Determine the SGTs & SGACLs via API on the Primary ISE Node
#09:Checking:SDA:Capturing Commands from the Borders/CPs/Edges/WLCs
#10:Checking:SDA:Software version and platform type count
#11:Checking:SDA:Fabric devices CPU Utilization Check
#12:Checking:SDA:Fabric devices Memory Utilization Check
#13:Checking:SDA:Verify the number of LISP Sessions Established on the Fabric devices
#14:Checking:SDA:Check the LISP IPv4 EID Table size on all Fabric devices
#15:Checking:SDA:Check the LISP IPv4 MAP Cache Table size on the Borders
#16:Checking:SDA:Check the ISIS Sessions state for the Fabric devices
#17:Checking:SDA: Ensure the Fabric devices have more than one ISIS Session - Redundancy check
#18:Checking:SDA:Borders Only:IPv4 BGP Sessions
#19:Checking:SDA:Borders Only:VPNv4 BGP Sessions
#20:Checking:SDA:AAA Server connectivity from the devices
#21:Checking:SDA:CTS PACS downloaded to the devices
#22:Checking:SDA:CTS SGTs downloaded to the devices
#08:Checking:eWLC Telemetry Connection Status Check
#09:Checking:eWLC Netconf Yang Datastore Check
#23:Checking:SDA:eWLC CPU Utilization Check
#24:Checking:SDA:eWLC Memory Utilization Check
#25:Checking:eWLC Fabric AP Check
#26:Checking:eWLC Fabric WLAN Check
****** Upgrade Readiness SDA Checks ******
#17:Checking:Fabric Devices Compatibility with DNA Center Version 1.3.3.7
INFO:Site Global/SYD - Compatibility Check passed for 3 devices (compatible versions:device count) - {u'16.12.3s': 2, u'8.10.112.0': 1}
#18:Checking:IP Pool Migration
****** Running Scale Checks ******
#01:Checking:Scale : Number of Sites
#02:Checking:Scale : Number of Access Control Policies
#03:Checking:Scale : Number of Access Contracts
#04:Checking:Scale : Total number of devices (switch, router, wireless controller)
#05:Checking:Scale : Number of Fabric Domains
#06:Checking:Scale : Number of Fabric Sites
#07:Checking:Scale : Number of Group SGTs
#08:Checking:Scale : Number of IP SuperPools
#09:Checking:Scale : Number of ISE connections
#10:Checking:Scale : Max number of AAA (Radius)
#11:Checking:Scale : Number of SSIDs
#12:Checking:Scale : Number of Virtual Networks per site
#13:Checking:Scale : Number of Wireless Access Points
#14:Checking:Scale : Number of Wireless LAN Controllers
#15:Checking:Scale : Number of Wireless Sensors
#16:Checking:Scale : Number of Fabric Devices per Site
#17:Checking:Scale : Number of Fabric Borders per Site
#18:Checking:Scale : Number of Fabric Control Plane Nodes per Site

```
