import time
from datetime import datetime as dt
import os
import fileinput

websites=["www.youtube.com", "www.facebook.com", "www.reddit.com", "www.linkedin.com"]

def check_block(status):
    # block
    if status == True:
        with open('/etc/hosts', 'rt') as original_host_file:
            copy_host_file = original_host_file.read()
            # print(copy_host_file)
            with open('/tmp/etc_hosts.tmp', 'a+') as outf:
                outf.write(copy_host_file)
                for site in websites:
                    # print(site)
                    if site in copy_host_file:
                    # print(site)
                        pass
                    else:
                        print(site)
                        outf.write('\n' + '127.0.0.1' + " " + site)
                        # print(outf.read())

                os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')
    # unblock
    else:
        with open('/etc/hosts', 'rt') as original_host_file:
            copy_host_file = original_host_file.read()

            # print(copy_host_file)

        lines = copy_host_file.splitlines()

        with open('/tmp/etc_hosts.tmp', 'a+') as outf:
            for line in lines:
                if not any(site in line for site in websites):
                    if line != '':
                        outf.write(line + '\n')
                else:
                    # print(line)
                    pass
            outf.close()

        os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')

check_block(False)
#check_block(True)
test_file = open('/etc/hosts', 'rt')
print(test_file.read())
