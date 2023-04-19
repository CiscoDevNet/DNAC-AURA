# Change Log
- version 1.6.9 (19th April 2023)   
   -  capture DR state
    -  fixes for DR execution
    -  Added validation for CSCwa89160,CSCwe91959
    -  Look for postgres Primary vs Master in 2.3.4 and greater

- version 1.6.8 (12th January 2023)
    - fix mongo cpu utilization to account for multiple cpu and utilization > 100%
    - Fixed 2 issues – DR check failing for some releases & Hooks check output in the report was blank.  Also, reachability checks will print the IPs pinged.
    - Scale numbers updated for 2.3.3.x
    - Upgrade Path & Fabric compatibility updated to 2.3.3.x release. Added check for bug CSCvy50820.
    - support for versions  2.3.5.0, 2.3.4.0, 2.3.4.3
    - OSCP rerevoation change id  CSCvz40210 ->CSCvz27866
    - versions  2.3.3.6, 2.3.3.5
    - New check for upgrade failure CSCwc14612
    - Replace SSID Scale check with Fabric SSID Scale check
    - OCSP revocation check for swim
    - catch ProxyError in check_ise_connection
    - sanitize postgres password in Postgres Cluster Status
    - mulitple whitespace for /etc/fstab entries in check_disk_partition_mounts
- version 1.6.7 (17th September 2022)
    -  check for ISO build for DR
    - robustness in new version recognition.  Fix empty version corner case

- version 1.6.6 (25th August 2022)
    - cscwc59080 for 2.x releases and maglev hook installer bug
    - checking for etcd cert_expiry_notify key - CSCwc56327
    - check for default admin password
    - get dnac version natively before looking at package cache.  due to 2.3.3.3/4 same packages
    - support for version 2.3.3.4
    - support for version  2.2.3.6
    
- version 1.6.5 (22nd June 2022)
    - change etcd location of ntp server in 2.3.3.x
    - change etcd location of ntp server in 2.3.3.x
    - support for versions 2.3.2.3, 2.2.2.9, 2.3.3.1
    - check kubelet root ca cert
    - ping_address retry limit reduced from default of 20
    - check kubelet cert expiry
    - suport for version 2.3.3.0

 - version 1.6.4 (26th April 2022)
    -  support version 2.2.3.5
    -  Updated Scale limits for 2.2.3.x
    -  check for ntp config before testing ntp servers
    -  Fixing error on ZK Epoch check
    -  catch ISE setup error
    -  fake test for sda setup issue to appear
    -  catch exceptions setting up sda tests and skip them
    -  Network assurance check, allow Enabled and True
    -  updated spec for hidden imports
    
 - version 1.6.3 (8th March 2022)
     - adding support for 2.3.2.1
    - 2min timeout for nodescale status
    - added  CSCvs83964 for redis OOM
    - new error message naming scheme
    - Modified Secondary Interface Status check, CSCvz07674 is not applicable to 2.2.2.x & beyond
    - Added New Check for Standard Interface Mapping
    - updated docker path for registry CA Expiry check as per CSCvy55791
    
 - version 1.6.2 (3rd February 2022)
     - skip down for taskmgr-assurance-4
     - skip down for taskmgr-assurance-3
    - Minor fix - Subnet  Overlap check
    - Log4j vulnerability check
    - catch exact proxyerror in commandrunner when multiple instances running
    - updated Diskspace validations
    - fixed for multiple redis instances in OOM check
    - check for a file in /data/tmp that prevents dnac_aura dir being created
    
 - version 1.6.1 (18th January 2022)
    - Tweaked SearchLog for journalctl logs, Added additional log validation in ssl_intercept check
    - added support for 2.1.2.8, 2.2.3.4, 2.3.2.0, 2.2.2.8
    - move cluster overlap check to main tests


 - version 1.6.0 (8th December 2021)
    - Fix exception in SDA ISE check when postgres is not responsive
    - Additional DNAC version checks for s/w bugs
    - catch exception when rca dir empty
    - Version checking for checks related to bugs
    - Changed CSCvv05807 to CSCvs35184

 - version 1.5.9 (29th October 2021)
    - check for extra serivces in the default namespace
    - Updated error messages for Check_Config when execution fails
    - updated error message for Transient Mounts Check
    - support version 2.2.2.6
    - Modified the description of the bundle mode check
    - Added 2.2.2.6 to upgrade path and 17.6.* to comp matrix
    
 - version 1.5.8 (12th October 2021)
     - ignore CSCvy55791 for versions before 2.1.2
    - Enhanced upgrade path check with version 2.2.2.5
    - support for 2.2.3.3
    - support for 2.2.2.5
    - catch ResourceNotFoundError in device health
    - add cron avc-te-job check for 2.3.2
    - skip ETCD for unknown as well as 2.x
    - catch connectionerror in devicehealth - 2.3.2
    - fix curl -s for 2.3.2 in rabbitmq cluster status
    - fix Mongo DB size check on 2.3.2
    
 - version 1.5.7 (23rd September 2021)
     - Skipping CSCvu77846 for fixed versions
    - Minor change to ISE error msg
    - upgrade path updated with 2.2.2.4
    - Cleanup code to avoid exceptions when DNAC version is not determined
    - fix logic n secondary interface check
    - catch EndpointConnectionError in BAPI check
    - Exiting relevant checks when model is not determined
    - make zookeepeer ruok more robust
    - check for empty model - CSCvy96229
    - skip localhost for versions 2.x - CSCvs24346
    - check for etcd certs - CSCvw23564
    - 
 - version 1.5.6 (27th August 2021)
    - skipping non maglev-system glusterfs-server endpoints
    - Moved Lisp component constraint violation & Stale reachability DB ent…
    - Fixed exception in overlapping IP upgrade check
    - check presence of docker Registry CA cert
    - Modified Bundle mode check as SWIM stopped from 2.2.2.x onwards
    - Moved Lisp component constraint violation & Stale reachability DB entries to SDA section
    - Skipping NDP purge check if 2.2.3.x upwards as not applicable
    - Fixed exception in Count of Scalable Groups check
    - SDA-Compatibility Matrix Check updated to 2.2.2.x release
    - Frey support - replacing ipcalc with ipaddress
    - update tenantid check to use real admin user
    - added versionss 2.2.2.4 2.2.3.0
    - backout ur_check_backup_size
    
 - version 1.5.5 (26th July 2021)
     - estimate backup size
    - fix null fileid
    - Upgrade path to 2.2.2.3
    - Minor Commit - Secondary intf check
    
 - version 1.5.4 (22nd July 2021)
     - Check status of secondary intfs for XL
    - Fix crashes in sda_all_checks caused by cmd dumps that are None
    - catch null fileid
    - Updated GBAC Sync Check to ignore Access Contracts for the moment
    - remove false endpoint error for gluster-fs in different namespace
    - added diff for .pki and docker filesystem for registry ca cert
    - tweak to reg ca check
    - Registry CA cert expiry check - CSCvy55791
    - fix log for packages in rca check
    - tweak Recent updates and RCA files
    - look for updates and rca
    - modify zookeeper from nc to zkServer.sh
    
 - version 1.5.3 (17th June 2021)
    - support version 2.1.2.7
    - fixed sg/pol count check to handle 0 return for non-sda setups
    - SDA compatibility matrix check updated
    - Support for Fabric sites with unicode characters
    - Changed upgrade path check to reflect 2.1.2.7
    - Only affected versions are checked for 'WLC correct telemetry API call' issue
    - Fix LISP Table Size exception when Fabric dev on 16.6.x
    - support for DNAC 2.2.2.3
    - ignore node-operator-merics
    - Added new check for Pleg Errors in Syslog, Included Taint check in Node status
    - Added NFS stale file handle check
    - Corrected the incorrect truncation of the check headline in summary of errors
    
 - version 1.5.2 (27th May 2021)
     -  Download test - Changed from tesseractcloud.com to ciscoconnectdna.com

 - version 1.5.1 (24th May 2021)
     - version 2.2.2.x support
    - Added check for Duplicate Group Based Policies in DNAC DB
    - Display summarized list of APs
    - Added note to SDA Detailed page to use -s option if there is a need to run all SDA checks
    - Added validation for CSCvw20926 in Catalog Package check
    - Added new check to validate GBAC Migration/Sync Status
    - catch invalid json in catalog settings
    - timeout for maglev backup
    - timeout for Catalog hook bundles
    - timeout for Catalog packages
    
 - version 1.5.0 (5th May 2021)
     - convert dns connectdna query to dig
    - Image Download test stand alone option (--download-test)
    - Test Image Download check in Upgrade Readiness
    - Minor Tweak to ES NDP check reporting

 - version 1.4.9 (24th April 2021)
     - Handling wireless device command runner exception
    - Summary of Errors Table
    - timeout ffor system update package check
    - tweak maglev login message
    - fix timeout on release channel
    - ES NDP Check - changed validation for 3 node to match unassigned with active shards
    - Changed SDA comp matrix from 1.3.3.9 to 2.1.2.6
    
 - version 1.4.8 (8th April 2021)
      - check for proxy encoding in Kernel 5.4.0-52-generic - CSCvx89597
      - versions 2.1.2.6 and 2.2.1.3
      - timeout for broken catalog commands
      - Bundle mode device check
      - ES NDP Check - Changed status for 44/56c for <1.3.x in 3x-node cluster to "Yellow"
      - Fixed ES-NDP check to validate Node Count and Status as per table in TZ
      - fix Checking MongoDB CPU join
      - Bundle mode SWIM check
      - updated upgrade path check for 2.1.2.6
      
 - 1.4.7 (16th March 2021)
    - Added new check for Zookeeper Epoch Validation on Cluster
    - updated elasticsearch ndp check to also validate for ret code 6 - seen on 3 node setups
    - fixed logic in elasticsearch checks for validation on XL appliances
    - Added 2 new checks for ElasticSearch Cluster Status on maglev-system and ndp
    - Added new checks(INFO only - No Validation) for Release Channel, System Update Packages, catalog package display and hook bundles
    - add warning for non DN appliance
    - fixed seconds in remedyctl start (total_seconds)
    
- 1.4.6  (21 February 2021)
    - Formatted Mongo Sizes Output to align values
    - New Check for Mongo DB Sizes
    - Removed "sizeOnly" from NDP DB size cmd in Mongo Collector check - Fails on Magneto
    - Handled None Return for DNAC version on Influx check
    - remove legacy 2.2.1.0 package description

- 1.4.5  (19 February 2021)
    - Fixed Catalog Settings Check check to handle None return for proxy
    - updated package versions for 2.2.1
    - Log cleaner exception fix
    - tweaked error message for Influx OOM check
    - Updated Influx OOM Check to include new validations for CSCvw50984
    
- 1.4.4  (01 February 2021)
    - add both PRE POST hooks
    - added logging for LogCLeaner Cronjob check
    - dump out hook versions applied
    - lisp component constraint violation - CSCvx10390
    - add percentages to traffic errors
    
- 1.4.3  (20 January 2021)
    - Modified upgrade path check to include 2.1.2.5
    - addded support for 2.1.2.5
    - Fixed upgrade path checks
    
- 1.4.2  (12 January 2021)
    - Option to skip the SDA Device Check
    - updated error message for log cleaner check
    - Added New Check for Log Cleaner Cronjob if file exists(CSCvw89770) - Applicable to 2.1.2.x only
    - fixed typo
    - Skipping Diskspace validation for /mnt/install-artifacts
    - check external auth flag
    - added CSCvv37918 for MTU issue
    - fix placeement of redis messages
    - fixed incorrect info tag for assur_show_health check
    - change CA cert expiry from warning to error <100days
    - fix exception in retry of disk check
    
- 1.4.1  (09 December 2020)
    - Modified the welcome message
    - typo in remedyctl info
    - add support for 1.3.3.9
    - Upgrade path check to 2.1.2.x patches
    - Fix Exception in Compatibility check with Cat2k device
    - Modify Compatibility and Upgrade path checks to include 1.3.3.9
    - typeo update history message
    - 3 DNS issue resolved in 1.3.3.8
    
- 1.4.0  (30 November 2020)
   -  Fixed Query to sort correctly for top 10 largest tables in Postgres
    - add proxy for pull
    - skip swap check for L/XL
    - Added reporting of top 10 largest tables data to postgres size check
    - Add AURA result in json to the log file
    - Tweaked maglev login to retry thrice and report partial AURA op collection if it fails
    - add support for version 2.1.2.4 of DNAC
    - Detailed SDA Checks for the Edges increased to 50 Edges per site with -s option
    - move AURA self version check
    - New check to validate Shell Env Vars for any proxy configs
    - Added compatibility check to maglev backup display
    - tweak backup history message

- 1.3.9  (21 November 2020)
    - CSCvu46056 CSCvs82235 and CSCvu46056 added to sidecar check
    - eWLC -> IOSXE WLC in assurance checks
    - tweak backup errors/info/warnings
    - sidecar check
    - Fixed reporting for VIP Toggle Check, Minor tweaks to Log Search funcs
    - handle remedy log file appearing as binary
    - utf-8 in site breakkdown
    - remover duplicate swap message
    - New Check for Gluster Volume Heal Stats , minor tweak to service distribution check
    
- 1.3.8  (16 November 2020)
    - avoid 1.2 for stale reachability test
    - fix stale reachability error
    - wlc kong error matching with assurnace
    
- 1.3.7  (15 November 2020)
    - stale reachabilty DB - CSCvs68227
    - Fixed fabric scale checks when multiple levels are present in a fabric site
    - certificate update job failing - CSCvv55243
    - logging for empty sites - only show first 15 in report
    
- 1.3.6  (12 November 2020)
    - break down of sites by type, show empty building/floors
    - check swap on 2.x builds, CSCvw31167
    - catch bad json in tennantid
    
- 1.3.5  (10 November 2020)
    - check VIP toggle -  CSCvo95706
    - catch memberid error messaage and display
    - Minor Tweak - Renamed Transient Mounts check
    
- 1.3.4  (09 November 2020)
    - check for pending workflows
    - Added new check for Transient Mounts
    - Check for cluster hostname
    - fix false success if DNS ping fails
    - Change parent catalog var from warning to error
    - added check for DNAC CA cert on Aireos
    - Fixed incomplete model name for XL
    - catch error in logtofile, logging for I/O check
                                                       
- 1.3.3  (31 October 2020)
     - retry disk IO failures
     - Uncommented and Tweaked Service Distribution Check
     - Fixed Scale checks for VN and Fabric Devices,Borders,CPs to handle Unicode Site Names

- 1.3.2  (21 October 2020)
     -  timeout for cassandra health
     -  Compatibility & upgrade path checks updated with 1.3.3.8
     -  add version cache for 1.3.3.8
     -  verify cassandra container before check

- 1.3.1  (19 October 2020)
     - Fixed Catalog Settings Validate Check for Cyclops - 2 steps to validate status
     - Added versions for 1.2.6(1)
     - Fixed exceptions with Secondary ISE PAN checks
     -  packages for 2.1.2.3
     - check for CSCvv86302 - WLC telemetry API call
     - remove CSCvu68204 check - elasticsearch
     - show expired WLC cert
     - only check extenal_auth <2.x
     - run_remote binary, run on all nodes of cluster and logs moved to central location
     
- 1.3.0  (12 October 2020)
    - added CSCvo23455 to parent repo var check
    - added DB check for tenantid
    - check for manual repository settings
    - tweaks to rabbitmq check to only show queue diffs
    
- 1.2.9  (04 October 2020)
    - Added root ca expiry check - CSCvv95329, tweak real cert expiry
    - catch ISE API timeout, and device health API failure
    - check_ping returns status
    - Warning check for CSCvu68204
    - Fixed timezone check failing
    - Fixed NTP Time Sync check to also validate bit buffer for reach discrepancies
    - explimitvar catchall
    - addedd errors to json-summary
    - Added reference to CSCvt22551 for inodes check
    
- 1.2.8  (27 September 2020)
     -  Add L2 sessions to the ISIS check
     -  added container for rabbitQ check to avoid warning message
     -  ISE pxgrid check for pxgrid process on PANs only
     -  refactored update history, just use system_update_package status
     -  magneto version
     -  timeout x for kubectl curl
     -  put in timeout for memberid in case telemetry-agent down
     -  Fixed cached MTU check error for magneto
     -  fixed rabbit queue validation for magneto, minor tweaks to reporting on other checks
     -  config ntp servers, test unique configured
     -  remove 1.3.3.6+ from CSCvu83230 description
     -  remedyctl check
     -  Added Diskspace Utilization validation to Glusterfs mount check
     -  catch BAPI error on 1.2.x installs
     -  New Check for Node Diagnosis , Tweaked logic to find primary mongo instance in  stale connections check
     
- 1.2.7  (19 September 2020)
    - tweak check_tenantintsegment_overflow to only run on primary mongo node
    - both upgraded and attempted versions
    - change IO to 100M for /tmp
    - fix dump of ise serials for certs
    - TenantId is wapping int - CSCvr19226
    - Added compatibility check for 3560-cx
    - Improved reporting for NTP Time Sync Check
    - Skipping DRAM & Processor checks if VM
    - Added new check for Disk Partition Mounts - CSCvv62098
    - log ISE cert serials+issuer
    - sort upate history
    - added --admin-user (default admin) to both aura and run_remote
    - modified errors - LISP edge session to include VN Anchoring & active telemetry error eWLC to include PI
    - fixed null object exception while getting version

- 1.2.6  (14 September 2020)
    -  added explicit check for timezone change on DNAC
    -  add ok message for DNS config on interfaces, using coredns
    -  print OK message if no ISE truststore expried certs
    -  skip maglev login check when command line arg provided
    -  change gluster mount to explicit check, to avoid nfs timeout
    -  flag no upgrade history
    -  catch error in old versions if no upgrade history
    
- 1.2.5  (12 September 2020)
    - added history of versions upgraded from in the past
    - Speeded up checks that use fabric site hierarchy
    - Command Capture with -o option is now site aware
    - Check pxGrid status on dedicated pxGrid node and more details provided in error for CSCvu77846
    - log ISE serials for truststore debug
    - Fixed diskspace checks to use df-l , Added new check to see if glusterfs mounted
    - added --all-cluster to run_remote on run all nodes in the cluster
    - flag ISE cert as expired - error
    - remove redis MacNameSpace count check, as redis can crash when low in memory
    - tweak duplicate test to ignore _third_party alias
    - Check for bug CSCvr06877 - LAN automation


- 1.2.4  (09 September 2020)
    - README for run_remote
    - fill out all check/error/warning in json-summary
    - single digit GB/s io ok
    - check for 30 fabric sites in the domain - CSCvv30308
    - new package_cache
    - directory for run_remote
    - Fixed etcd binding check to handle nxdomain return and false positive for ipv6
    - --no-pull option for run_remote
    - activate refactored rabbit check
    - fix df hang, non responsive nfs, added chcek for non responsive nfs - CSCvs93317
    - added --json-summary option for AURA
    - check to ensure running aura as user maglev, not as root
    - refactor rabbit status
    - added versions for 2.2.1 - magneto
    - added keepalive for run_remote for ssh idle timeout
    
- 1.2.3  (05 September 2020)
    - fix for error in redis check, where no redis running
    - dcbx test look in kern.log.1 as well as kern.log
    - added interface error warning
    - Push Comp Matrix full results to a file and summry in the report
    
- 1.2.2  (04 September 2020)
   - correct scale for totDevices for 131, 211
   - check kern.log for errors
   - fixed tarfile crash with -o option
   - check redis memory util and MacNameSpace entries - CSCvs83964
   - ewlc & wlc server url IP address check
   - ewlc network-assurance summary checks added
   - Adding DNAC Scale checks to -d option
   - Enhanced the Processor cores table display
   - ewlc assurance checks for DNAC-CA & sdn-network-infra-iwan truststores and certificates
   - Fixed DNAC test results are seen twice in the pdf report
   
- 1.2.1  (01 September 2020)
    - Added links to Section Titles on Summary page to Detailed Results of each
    - skip device/client health for older DNAC < 1.3
    - comment out old version_cache, add 2.1.2.0 system + ui versions
    - fix for remaining args, no proxy - run_remote.py
    - added GB/s as valid I/O throughput, so IO test does not fail
    - Tweaked Mongo stale conns check - Warning if > 100k but < 1 mil
    - New check for CSCvi73428 - Checking if SSL Intercept is configured in the Network
    - minor fix to Searchlog
    - Fixed Scale Limit parser to pick expected limits based on DNAC version
    - Scale parameters included for 2.1.x and 1.3.3.x release
    - Tweak to influx db check - mention limit check of > 20G in Error
    - Refactored Influx Check to report last terminated time for OOM and always display db size
    
- 1.2.0  (24 August 2020)
   - Assurance checks for non fabric IOSXE WLCs
   - Added -d option for DNAC Infra checks only
   - minor fix - logging util for diskspace
   - Added --maglev-pass and --admin-pass as command line options. Simplify remote launch or crontab launch
   - Tweak to diskspace check reporting
   - refactored check_build and get_dnac_version to use PackageCache
   - fix float issue for disk IO failure to execute error
   - support for --syslog option to log errors to remote syslog server
   - check for Data Center Bridging Exchange Protocol (DCBX)on upstream switch - CSCvq32094
   - Fixed nodeupdater check to only run if there is an upgrade failure in node update phase
   - Merged Diskspace and iNodes Check, Fixed validation for Service Restarts Check
   
- 1.1.9  (19 August 2020)
    - Hyperlinks for Comp Matrix and all Bugs
    - Fixed docker proxy check false positive due to username in field
    - BGP Checks are now site aware
    - Tweaked high util on /data/nfs(backup server) to be reported as warning instead of error
    - Added new check for AAA Servers Status Info, modified psql query func to add additional param to include header in op
    - tightend ISE ccert check, duplicate serial from same issuer
    - correct logfile for maglev catalog settings display
    - Fixed High Restarts check - handled terminated services in Completed State
    - tweak error when IO test fails to execute
    - ISE Scale check should include only Active connections
    
- 1.1.8  (15 August 2020)
    - SDA Border/CP/Edge captures are now site aware with seperate log file per site
    - Added Bug ID to Duplicate SGT tag check
    - tweaked error reporting for Cassandra check
    - Fixed Cert Validity check to handle error for -ve return(Already expired certs)
    - Fixed ETCD Binding Check to only validate loopback IP
    - added logging to etcd binding check
    - trapped empty device health data
    - Check REST API - BAPI - CSCvr70208
    - tweaks to reporting for exited containers and non running pods
    - added missing comma
    - catch DB exception when collecting fabric data
    - refactored appstack check and added endpoint check to detect more down services
       
- 1.1.7  (12 August 2020)
  - version display on PDF 1st page
  - Avoiding AURA crash if command runner times out
  - Displaying 1st 100 SGTs & SGACLs from ISE... logging it too...
  - Added 3 retries to command runner if its busy
  - Fixes to Mongo CPU check , Influx Memory check 
  - Fixed ETCD Binding False Positive, Added Cassandra Key distribution check, Added AURA version to report header
  - logtofile and used it for truststore and assurnace summary data
  - Added logging for DRAM check and fixed wrong reference in check_installer_hook
  - Added 1.3.3.7 to compatibility and upgrade path
  - Display device and client health counts in assurance
  - Adding 1.3.3.7 version
  - trap exception in File-service for missing FileID mappings 
  - placeholder for new SDA  role 18
  - catch missing SDA role
  - pmtu check - CSCvs22065
  - DRAM and Processor verifications
  - Fixed Mongo Sync Status check
  - Fixed NodeUpdater check to look for CSCvu93288 
  - Added New Check for High Restart Counts
  
- 1.1.6  (7th August 2020)
  - Missed adding upgrade readiness to the overall count in report
  - Fixed IP pool migration check to skip if DNAC version is 1.2.x
  - corrected node display check for Cyclops
  - included ewlc telemetry connection new format
  - Fixed Error messages for Cmd Exec Failures
  - Upgrade path to 1.3.3.6, directories & files will now have mode 755
  - Fixed NTP Check to error out for offset > 300 ms
  - Fixed Mongo Sync Check to throw error only if more than 60secs behinid primary
  - tweak error for IO retry
  - clarified message for IO failure
  - clarified internal AURA exceptions
  - WLC/eWLC Assurance checks are now moved to default run
  - Check Docker Daemon proxy settings
  - Added New Check for IP Pool Migration Issue
  - Fixed diskspace check logging to capture top 10 dirs util info in error condition 
  - change bugid for ISE trust store from CSCvu23957  to CSCvv05807
  - Fixed Node Status Check to validate exact string, Added debug logging to FileService Check 
  - Node Updater and Hook Installer Service Check 
  - fixed dns etcd error in format string leading to exception
  - Adding Product Details and Count to Total Devices Scale Check
  - display DNAC certificate SAN entries
  - Fixed Stale Mounts Check to handle stderr, fixed run_shell func to return correct error code and output
  - Fixed diskspace check to validate <=2G
  
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
