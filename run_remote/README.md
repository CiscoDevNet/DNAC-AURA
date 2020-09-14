# Remote execution of AURA
This script allows you to lanch the AURA on a remote Cisco DNA Center.  It uses paramiko and scp libraries.

## Installing
To install, it is recommended that you use a virtual environment.  The following lines will create a python3 virtual 
environment, activate it, upgrade pip, and install the required libraaries

```buildoutcfg
python3 -m venv env3
source env3/bin/activate
pip install --upgrade pip
pip install -r requirements.txt
```
## Note about remote execution (session timeout)
Later versions (2.1+) of Cisco DNA Center have an ssh idle timeout.  This can impact AURA being run from an ssh session
either directly on DNAC, or indirectly via the run_remote script or ansible.

The work around is simple.  For an ssh connection, the "-o ServerAliveInterval=3" flag will send keepalives
and maintain the session.  This is used in this script, and can also be used for direct ssh connection as well as 
ansible

## Using the script
The script requires three arguments:
- dnac
- admin password (also available as an environment variable DNAC_ADMIN_PASS)
- maglev password (also available as an environment variable DNAC_MAGLEV_PASS)

the simplest way to run the script with arguments (see later section on environment vars) is
```buildoutcfg
./run_remote.py --dnac 1.1.1.1 --admin-pass passwd --maglev-pass passwd
```

If you are familiar with shell environment variables, this can be simplified further

```buildoutcfg
export DNAC_ADMIN_PASS="passwd"
export DNAC_MAGLEV_PASS="passwd"
./run_remote.py --dnac 10.1.1.1
```

## Passing AURA options (--)
To pass AURA specific arguments (for example -s to run SDA tests) you need to do the following:
```buildoutcfg
## note the extra --, due to a qwirk in the way argparse library works
./run_remote.py --dnac 10.1.1.1 -- -s
```

Make sure you include any run_remote options, such as --local-dir, all-cluster and --no-pull BEFORE the "--"

AURA specific options such as -n, --syslog, -d, -s need to be after the "--"

## Storing aura output locally.
AURA script supports the --json-summaary option. This produces a json summary of the test results as well as the 
location of the report and log file on DNAC.  When run_remote is supplied with the --local-dir option, the 
log and report files will be moved back to DNAC.  A json-summary file will be created.
A directory for the DNAC is created

```buildoutcfg
/home/aradford/RUN_REMOTE/run_remote.py --dnac 10.1.1.1  --local-dir /home/aradford/RUN_REMOTE/logs
```
after this completes, the /home/aradford/RUN_REMOTE/logs directory will contain:
```buildoutcfg
ls RUN_REMOTE/logs/10.1.1.1
DNAC_AURA_Logs_2020-09-08_23_20_11.tar.gz
DNAC_AURA_Report_2020-09-08_23_20_11.json
DNAC_AURA_Report_2020-09-08_23_20_11.pdf
```

the json file contains:
```buildoutcfg
cat RUN_REMOTE/logs/*/DNAC_AURA_Report_2020-09-08_23_20_11.json
{
  "json-summary": {
    "check_count": 64,
    "report-name": "/data/tmp/dnac_aura/reports/DNAC_AURA_Report_2020-09-08_23_20_11.pdf",
    "logfile-name": "/data/tmp/dnac_aura/logs/DNAC_AURA_Logs_2020-09-08_23_20_11.tar.gz",
    "ur_check_count": 19,
    "ur_error_count": 0,
    "warning_count": 5,
    "assur_warning_count": 2,
    "error_count": 5,
    "ur_warning_count": 3,
    "assur_check_count": 14,
    "assur_error_count": 0
  }
}
```
## Cluster execution
If using the --all-cluster option, the script will find all memebers of the cluster and run AURA on each one.  
Currently this is a serial execution.  Can be used with --local-dir to copy the report, logfile and json-summary
back from DNAC.

Either a VIP or physical address can be provided.  The script will connect and look for all physical IP in the 
same subnet as the IP used to connect.

## Other options
The script can also be run with the --no-pull option.  This stops the git pull to update to the 
latest version of AURA, but assumes you have copied aura to the home directory on DNA Center.

## CRON
Cron is a challenge for AURA due to the lack of PTY. It also requires editing the DNA Center crontab.

run_remote probably a better way of running AURA, as it solves the PTY issue and removes the need to edit the local 
DNA Center crontab.  Running remotely combined with --local-path means all DNA Center logs are in the same on an external
server.

Here is a sample crontab entry for running AURA on a DNAC every hour.
Need to supply the python interpreter explicitly to pick up the virtual environment contain paramiko and scp libraries.

```buildoutcfg
00 * * * * /home/aradford/RUN_REMOTE/env3/bin/python /home/aradford/RUN_REMOTE/run_remote.py --dnac 10.1.1.1 --admin-pass passwd --maglev-pass passwd --local-dir /home/aradford/RUN_REMOTE/logs > /tmp/run
```

This can be wrapped further by a shell script to protect the credentials from being stored in plain text.
