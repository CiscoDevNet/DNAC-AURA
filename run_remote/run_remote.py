#!/usr/bin/env python
from __future__ import print_function
from paramiko import  SSHClient, AutoAddPolicy,AuthenticationException
from scp import SCPClient
import json
import os
from ipaddress import IPv4Interface
from argparse import ArgumentParser, REMAINDER

def connect(ip, password):
    try:
        ssh = SSHClient()
        ssh.set_missing_host_key_policy(AutoAddPolicy())

        print('Initiating SSH to {}...'.format(ip))
        ssh.connect(ip, port=2222, username="maglev", password=password ,look_for_keys=False)

        # use keepalive to keep connection open to DNAC with idle timeout=5mins
        t = ssh.get_transport()
        t.set_keepalive(5)
        return ssh
    except AuthenticationException:
        print("Unable to SSH to the device {} due to an Authentication Exception".format(ip))

def validate_op(stdout, stderr):
    stderr._set_mode('rb')
    status = stderr.read().decode('ascii').strip("\n")
    if not status:
        stdout._set_mode('rb')
        opstatus = stdout.read().decode('ascii').strip("\n")
        print(opstatus)
    else:
        print(status)

def get_cluster_members(dnac, maglev):
    print("Getting other cluster members..")
    with  connect(dnac, maglev) as conn:
        cmd = "etcdctl ls /maglev/config | grep node | sed -e 's#$#/network#' | xargs -n1 etcdctl get | jq -r '"
        jq = '.[] |.inet | .host_ip + "/" + .netmask'
        final = "' | grep -v '^[/]$' "
        full_cmd = cmd + jq + final
        #print(full_cmd)
        stdin, stdout, stderr = conn.exec_command(full_cmd)
        iplist = stdout.readlines()

        for ip in iplist:
            ipa = IPv4Interface(ip.strip())
            print(ipa)
            if dnac == str(ipa.ip):
                network = ipa.network
        targets =[]
        for ip in iplist:
            ipa = IPv4Interface(ip.strip())
            if ipa.network == network:
                targets.append(str(ipa.ip))

    return targets


def copy_files(conn, dnac, json_summary, dir):
    path = "{}/{}".format(dir, dnac)
    print("\n**** Checking local destination folder: {}".format(path))
    if not os.path.isdir(path):
        try:
            os.mkdir(path)
        except OSError:
            print("Creation of the directory %s failed" % path)
        else:
            print("Successfully created the directory %s " % path)

    print("\n**** Copy logfiles and report files back to {}".format(path))
    scp = SCPClient(conn.get_transport())
    scp.get(json_summary['json-summary']['report-name'], local_path=path)
    scp.get(json_summary['json-summary']['logfile-name'], local_path=path)

def run_aura(dnac, maglev, admin, nopull, dir, rest):
    #print (dnac, maglev, admin, rest)
    others = ''
    if rest != []:
        others = ' '.join(rest[1:])


    with connect(dnac, maglev) as conn:

        if not nopull :
            print("\nCollecting proxy info...")
            try:
                stdin, stdout, stderr = conn.exec_command("cat /etc/systemd/system/docker.service.d/http*-proxy.conf | awk '/HTTPS_PROXY/ {print}'")
                stdout._set_mode('rb')
                proxy = stdout.read().decode('ascii').strip("\n")
                proxy = proxy.split("=")[2]
            except IndexError:
                print("no proxy found")
                proxy = ''

            print("\nCloning/Pulling latest AURA Code...\n")
            stdin, stdout, stderr= conn.exec_command("https_proxy={} git clone https://github.com/CiscoDevNet/DNAC-AURA.git".format(proxy))
            validate_op(stdout, stderr)
            stdin, stdout, stderr = conn.exec_command("cd DNAC-AURA; git pull")
            validate_op(stdout, stderr)

        json_summary = {}
        print("\n\n****** EXECUTING AURA ON NODE : {} ******\n\n".format(dnac))
        json_flag = "--json-summary" if dir is not None else ""
        cmd = "/home/maglev/DNAC-AURA/dnac_aura --admin-pass {} --maglev-pass {} {} {}".format(admin,maglev, json_flag, others)
        stdin, stdout, stderr = conn.exec_command(cmd,get_pty=True)
        while True:
            line = stdout.readline()
            print(line, end='')
            if "json-summary" in line:
                json_summary = json.loads(line)
            if not line: break
        #print(json.dumps(json_summary, indent=2))

        if dir is not None:
            if json_summary == {}:
                print("No json summary cannot copy logfiles and report")
                return

            copy_files(conn, dnac, json_summary, dir)

            # copy a summary
            print("\n******* WRITING JSON SUMMARYS ******")
            base = os.path.splitext(os.path.basename(json_summary['json-summary']['report-name']))[0]
            with open("{}/{}/{}.json".format(dir, dnac,base), "w") as f:
                json.dump(json_summary, f, indent=2)

            ### cleaning up remote files
            print("\n******* CLEANING IP REMOTE REPORT AND LOGFILES ******")
            cmd = "rm {} {}".format(json_summary['json-summary']['report-name'], json_summary['json-summary']['logfile-name'])
            stdin, stdout, stderr = conn.exec_command(cmd)
            validate_op(stdout, stderr)

if __name__ == "__main__":
    parser = ArgumentParser(description='Select options.')
    parser.add_argument('--dnac', type=str, required=True,
                        help="dnac to connect to")
    parser.add_argument('--maglev-pass', type=str, default=os.environ.get('DNAC_MAGLEV_PASS','password'),
                        help="maglev password")
    parser.add_argument('--admin-pass', type=str,default=os.environ.get('DNAC_ADMIN_PASS','password'),
                        help="admin (WEBUI) password")
    parser.add_argument('--no-pull', action='store_true', default=False,
                        help="do not pull down new copy of aura")
    parser.add_argument('--all-cluster', action='store_true', default=False,
                        help="all cluster members")
    parser.add_argument('--local-dir', type=str,
                        help="local directory to store report/logs")
    parser.add_argument('rest', nargs=REMAINDER)
    args = parser.parse_args()

    if args.maglev_pass == "password":
        print("\n** Warning, using default maglev password, use DNAC_MAGLEV_PASS environment var or --maglev-pass")
    if args.maglev_pass == "password":
        print("\n** Warning, using default admin password, use DNAC_ADMIN_PASS environment var or --admin-pass")

    if args.all_cluster:
        targets = get_cluster_members(args.dnac, args.maglev_pass)
    else:
        targets = [args.dnac]

    for target in targets:
        print("target:{}:".format(target))
        run_aura(target, args.maglev_pass, args.admin_pass, args.no_pull, args.local_dir, args.rest)
