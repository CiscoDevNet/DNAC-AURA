# DNAC-AURA

The Cisco DNA Center AURA (Audit & Upgrade Readiness) command line tool performs a variety of health, scale & upgrade readiness checks for the DNA Center and the rest of the Fabric network. The tool is extremely simple to run and is executed on the DNA Center. The tool uses API calls, DB reads & show commands (read only operations) and hence, doesn't affect performance or cause impact to the DNA Center or the networking devices.

## Note about remote execution (session timeout)
Later versions (2.1+, 1.3.3.8+) of Cisco DNA Center have an ssh idle timeout. This can impact AURA being run from an ssh session either directly on DNAC, or indirectly via the run_remote script or ansible.

The work around is simple. For an ssh connection, the "-o ServerAliveInterval=3" flag will send keepalives and maintain the session. This is used in the run_remote script, and can also be used for direct ssh connection as well as ansible

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
https_proxy=https://<your proxy> git clone https://github.com/CiscoDevNet/DNAC-AURA.git
```

### Option 3. Isolated environment.  
You will need to clone (using method 1 or 2) to an intermediate machine and copy to DNAC, using scp.  Remember to use port 2222 with the -P option to scp.
```
scp -P 2222 ./DNAC-AURA/dnac_aura  maglev@<mydnac>:
```
## To get the latest version
We are adding new features quite often.  If you have downloaded an older version, it is very easy to get the latest.  Provided you used option #1 or #2, you can simply change directory into the DNAC-AURA directory and use git pull, instead of git clone.  You might need to provide proxy as in option #2.
```
$ cd ./DNAC-AURA
$ git pull
```

##AURA Versions - Change Log
For release updates, see ChangeLog.md

https://github.com/CiscoDevNet/DNAC-AURA/blob/master/ChangeLog.md
 


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

## Cisco DNA Center AURA Options
|  | No Options (default) | -s | -d | -o | -c |
| :---: | :---: | :---: | :---: | :---: | :---: |
| DNA Center Infra Health Checks | X | X | X |  |  |
| DNA Center Assurance Health Checks | X | X |  |  |  |
| WLC/eWLC Assurance Health Checks | X | X |  |  |  |
| Basic SDA Checks (Inventory check) DNAC-ISE Integration (only if ISE is integrated) | X | X |  |  |  |
| SDA(Fabric Device CLI collection, Control Plane & Security Plane Audit and Compatibility Check) |  | X |  |  |  |
| Upgrade Readiness Checks (including bugs) | X | X |  |  |  |
| DNA Center Scale (Fabric & Non Fabric scale parameters) | X | X | X |  |  |
| Capture CLI Outputs from the fabric devices and store locally on the DNA Center - command and device list provided via file captureFile.yaml |  |  |  | X |  |
| Compare configurations across multiple devices (based on outputs captured using -o option) |  |  |  |  | X |



## Command Line Options
```
./DNAC-AURA/dnac_aura --help
usage: dnac_aura [-h] [-v] [-V] [-s] [-u U] [-n N] [--syslog SYSLOG]
                 [--admin-pass ADMIN_PASS] [--maglev-pass MAGLEV_PASS] [-o]
                 [-c]

Select options.

optional arguments:
  -h, --help            show this help message and exit
  -v                    verbose logging
  -V                    version information
  -s                    Run additional SDA checks. To execute these checks,
                        the tool will login to other devices in the fabric and
                        collect show command outputs.
  -u U                  Upload report and logs file to the SR. Please provide
                        SR and password in the format sr_number:sr_password
  -n N                  Add customer name to the PDF report on the first page
                        (the summary page)
  --syslog SYSLOG       destination syslog server
  --admin-pass ADMIN_PASS
                        maglev admin password (this is the UI password for
                        admin user
  --maglev-pass MAGLEV_PASS
                        maglev password (for sudo)
  -d                    Perform all DNA Center Infrastructure Health checks only
  -o                    To collect CLI outputs from the network devices via
                        the Cisco DNA Center. Ensure you have the
                        captureFile.yaml in the same folder as this tool.
  -c                    Compare configurations across multiple devices. You
                        can choose 2 timestamps from previous captures taken
                        with the -o option. PDF Report will be generated with
                        the diffs.     
 ```



## What does it check
Run it to find out.  Here is a sample of some of the checks that are run:

####Cisco DNA Center Health & Connectivity
``` 
#01:Checking:Determine Cisco DNA Center Product Type, Serial number, SW Version & Node IP
#02:Checking:Determine Cisco DNA Center memberid
#03:Checking:CPU Load Average
#04:Checking:Disk Layout
#05:Checking:Disk Space and iNodes Utilization
#06:Checking:Disk I/O throughput (>200MB/s)
#07:Checking:DRAM Total Available Memory
#08:Checking:DRAMs Installed in the appliance
#09:Checking:Processor Cores Enabled and Status
#10:Checking:Docker Status
#11:Checking:Docker Proxy settings
#12:Checking:Kubelet Status
#13:Checking:Version of Cisco DNA Center this was built from
#14:Checking:Cluster Node Reachability - nodes : []
#15:Checking:Interface Reachability - all nodes : []
#16:Checking:VIP Reachability - VIPs : []
#17:Checking:Number of DNS servers configured in etcd on nodes (<=3)
#18:Checking:Number of /etc/resolv.conf entries (<=4)
#19:Checking:DNS config - /etc/network/interfaces
#20:Checking:DNS Reachability - DNS : []
#21:Checking:DNS server can resolve www.ciscoconnectdna.com
#22:Checking:NTP server Sync : []
#23:Checking:DCBX upstream causing tx drops
#24:Checking:check kernel logs for errors
#25:Checking:Certificate Validity and Expiry
#26:Checking:Expiry of truststore certificates
#27:Checking:NTP Service status on the Cisco DNA Center
#28:Checking:NTP Server Time Sync
#29:Checking:Status of PMTU discovery
#30:Checking:Node Display
#31:Checking:Node Status
#32:Checking:Appstack Status
#33:Checking:Endpoint Status
#34:Checking:Check Services for High Restart Counts
#35:Checking:State of ISE states in DB
#36:Checking:External authentication configured for DNAC users
#37:Checking:Checking Count of Scalable Groups, Contracts and Access Policies in DNAC DB
#38:Checking:Glusterfs Instances
#39:Checking:Glusterfs NODE_NAME check
#40:Checking:Glusterfs Clustering
#41:Checking:ETCD Cluster Health
#42:Checking:ETCD Storage Size
#43:Checking:ETCD memory utilization
#44:Checking:ETCD binding to loopback(localhost/127.0.0.1)
#45:Checking:Postgres Cluster Status
#46:Checking:Postgres size
#47:Checking:MongoDB Cluster Health and Sync Status
#48:Checking:Checking MongoDB for Stale Connections from collector-manager
#49:Checking:Checking MongoDB CPU in docker stats
#50:Checking:Checking if MongoDB is locked
#51:Checking:InfluxDB Health
#52:Checking:InfluxDB Memory Utilization
#53:Checking:Cassandra Health
#54:Checking:Cassandra status
#55:Checking:Rabbitmq Cluster Health
#56:Checking:Rabbitmq Cluster Status
#57:Checking:Rabbitmq Queue Status
#58:Checking:Rabbitmq Queues with Unacknowledged messages
#59:Checking:Zookeeper Cluster Health
#60:Checking:Zookeeper Cluster Status
#61:Checking:REST API (BAPI) is responding
#62:Checking:Backup History
```

####Upgrade Readiness
```
#01:Checking:Cluster Subnet Overlap with Internal Addresses
#02:Checking:RCA Files Disk Usage
#03:Checking:Count of Exited containers
#04:Checking:Count of Non Running Pods
#05:Checking:Maglev Catalog Settings
#06:Checking:Proxy connect to ciscoconnectdna via:http://proxy.com:80 
#07:Checking:Checking File-service for missing FileID mappings
#08:Checking:Checking Expiry of Maglev Certs
#09:Checking:Checking for Stale Mount Points
#10:Checking:Collector-ISE config has been cleaned up after a previous upgrade
#11:Checking:Backup Display to find Last Successful Backup
#12:Checking:Provision fail due to invalid migration status parameter
#13:Checking:Maglev Hook Installer Service status on the Cisco DNA Center
#14:Checking:Checking if SSL Intercept is configured in the Network
#15:Checking:DNA Center Upgrade Path to the latest patch off 1.3.3.x
#16:Checking:ISE Compatibility check for ACA (Access Control Application)
#17:Checking:Fabric Devices Compatibility with DNA Center Version 1.3.3.7
#18:Checking:IP Pool Migration
#19:Checking:Configured AAA Servers and their Status
``` 

####Cisco DNA Center Assurance
``` 
#01:Checking:Assurance Partition Disk Space Usage
#02:Checking:Assurance Services Status
#03:Checking:Check Assurance Backend Purge Job
#04:Checking:Check Assurance NDP Purge Job that cleans up Redis DB
#05:Checking:Assurance Pipeline status
#06:Checking:Device health score summary
#07:Checking:Client health score summary
#08:Checking:Determine the SGTs & SGACLs via API on the Primary ISE Node
#09:Checking:Capturing Commands from the Wireless Controllers
#10:Checking:eWLC Telemetry Connection Status Check
#11:Checking:eWLC Netconf Yang Datastore Check
#12:Checking:eWLC sdn-network-infra-iwan Trustpoint & Certificates
#13:Checking:eWLC DNAC-CA Trustpoint & Certificate
#14:Checking:eWLC Device Network Assurance Status
#15:Checking:AIREOS WLC Telemetry Connection Status Check
``` 

####SD-Access Health
```
#01:Checking:Fabric device reachability inventory status
#02:Checking:Fabric inventory collection
#03:Checking:SDA:Cisco DNA Center & ISE integration status
#04:Checking:Verify the SSH connectivity between Cisco DNA Center and Cisco ISE
#05:Checking:Cisco ISE Nodes Memory Usage
#06:Checking:Cisco ISE Nodes Disks Usage
#07:Checking:Status of the Cisco ISE processes
#08:Checking:Determine the SGTs & SGACLs via API on the Primary ISE Node
#09:Checking:SDA:Capturing Commands from the Borders/CPs/Edges
#10:Checking:SDA:Software version and platform type count
#11:Checking:SDA:Fabric devices CPU Utilization Check
#12:Checking:SDA:Fabric devices Memory Utilization Check
#13:Checking:SDA:Verify the number of LISP Sessions on the Fabric devices
#14:Checking:SDA:Check the LISP IPv4 EID Table size on all Fabric devices
#15:Checking:SDA:Check the LISP IPv4 MAP Cache Table size on the Borders
#16:Checking:SDA:Check the ISIS Sessions state for the Fabric devices
#17:Checking:SDA: Ensure the Fabric devices have more than one ISIS Session - Redundancy check
#18:Checking:SDA:Borders Only:IPv4 BGP Sessions
#19:Checking:SDA:Borders Only:VPNv4 BGP Sessions
#20:Checking:SDA:AAA Server connectivity from the devices
#21:Checking:SDA:CTS PACS downloaded to the devices
#22:Checking:SDA:CTS SGTs downloaded to the devices
#23:Checking:SDA:eWLC CPU Utilization Check
#24:Checking:SDA:eWLC Memory Utilization Check
#25:Checking:eWLC Fabric AP Check
#26:Checking:eWLC Fabric WLAN Check
``` 

####Cisco DNA Center Scale
```
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
