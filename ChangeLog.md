# Change Log
- 1.1.5  (5th August 2020)
  - Added SY5 to Compatibility
  - Fix ISE ver to accomodate root version
  - updated Mongo collector check to print Bug ID as Info
  - check dns resolution - under 2sec response for all DNS servers
  - Fetching SGTs & SGACLs from ISE PAN
  - Added top 10 pods utilization in /var to iNodes Check (with names)
  
- 1.1.4  (29th July 2020)
  - Fixed Backup Display check to handle missing server config
  - Check truststore ISE cert expiry and duplication - CSCvu23957
  - New check for CSCvs24346 - CHECK IF ETCD BINDING IS TO LOOPBACK (LOCALHOST/127.0.0.1)
  - add 1.3.3.6 to CSCvu83230 - change default behaviour for external DNAC auth
  - Added new Upgrade Readiness Check for Last Successful Backup
  - Added check for CSCvt27360 - DNAC-ISE Integration issue, bad credentials
  - Added check for CSCvu77846  After upgrade to 2.1, switch provision is blocked if it is not running 16.12.2 and newer code
  
- 1.1.3  (25th July 2020)
  - Files uploading to the SR
  - Added Bug ID ref to NTP Service Check
  - Fixed DNAC Version retrieval
  - fixed ur_info for non running pods check
  - count /etc/network/interfaces dns entrie
  - catch error for all Upgrade Readiness checks
  - add description for CSCvr63900 for dns >3
  - Added Check for Cached MTU
  - fix dns formatting
  - count dns etcd per node; display per interface dns entries
  - Fabric device compatibility check for 1.3.3.6

- 1.1.2  (22nd July 2020)
  - fix ntp config perms on /etc/ntpd.conf
  - catcherror modifed to create a specific error
  - Fixed Mongo Lock and Influx Health Check
  - fixed purge check to take care of older output format in 1.2.10
  - Added New Checks, Fix for Mongo CPU check
  - Assurance Pipelines check
  - dump out network config to logs
  - disk IO checks for degraded RAID controller
  - platform-ui version for 1.3.3.6
  
- 1.1.1  (20th July 2020)
  - ISE checks 
  - Commenting out unused imports
  - Added error logging to include Bug IDs for a few checks
  - check for external auth - CSCvu83230
  - add package, platform numbers for 2.1.1.3
  - Added check for CSCvq46058
  - Added memory, disk and process checks for ISE
  - change resolve.conf from 3->4 as extra kube-dns entry
  - collect memberid
  - added insecure option to cxd curl and fixed resolv.conf crash
  - ISE Check - checking for inactive & Bad passwords in ISE
  - Adding check for CSCvp60100
  - logging of resolv.conf

- 1.1.0  (15th July 2020)
  - ISE connectivity, version and health cheacks
  - cassandra checks
  - fileId missing in fileservice check
  - stale mount check - CSCvt95075
  - maglev and kube certs validity - CSCvr26534
  
- 1.0.4  (14th July 2020)
  - count /etc/resolv.conf entries
  - fix bug with unknown device role
  - dns count check (not resolv.conf)
  - mongo stale connection check
  - LISP enhancements
  - influx DB size
  
- 1.0.3 (10th July 2020)
  - remove appliance check
  - Check count of SGT, Contracts and Policies in DNAC DB
  - ntp fix
  
- 1.0.2 (7th July 2020)
  - add interface IP display
  - added -V for version
  - match version for 2.1.x
  
- 1.0.1 - first release 
