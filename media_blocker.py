import time
from datetime import datetime
import os
import fileinput
import re
import secrets

class Blocker:
    def __init__(self):
        # starting with an initial set of sites that the user can modify
        self.blocked_sites = ["www.youtube.com", "www.facebook.com", "www.reddit.com", "www.linkedin.com"]

    def current_sites(self):
        print("Current sites include:")
        print(self.blocked_sites)

    def add_sites(self, new_site):

        # basic website format validation
        if re.match(r"www\..*.com", new_site):
            self.blocked_sites.append(new_site)
            print("Added " + new_site + " to blocked sites.")

        else:
            print("Invalid site format. Please input sites as 'www.insertsitename.com.'")

    def action_block(self, status):

        # block
        if status == False:
            with open('/etc/hosts', 'rt') as original_host_file:
                copy_host_file = original_host_file.read()
                with open('/tmp/etc_hosts.tmp', 'a+') as outf:
                    outf.write(copy_host_file)
                    for site in self.blocked_sites:
                        # print(site)
                        if site in copy_host_file:
                        # print(site)
                            pass
                        else:
                            # print(site)
                            outf.write('\n' + '127.0.0.1' + " " + site)

                    os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')

        # unblock
        else:
            with open('/etc/hosts', 'rt') as original_host_file:
                copy_host_file = original_host_file.read()

            lines = copy_host_file.splitlines()

            with open('/tmp/etc_hosts.tmp', 'a+') as outf:
                for line in lines:
                    if not any(site in line for site in self.blocked_sites):
                        if line != '':
                            outf.write(line + '\n')
                    else:
                        # print(line)
                        pass
                outf.close()

            os.system('sudo mv /tmp/etc_hosts.tmp /etc/hosts')

if __name__ == "__main__":
    new_blocker = Blocker()

# tests
# -----
# new_blocker.current_sites()
# new_blocker.add_sites('www.9gag.com')
# new_blocker.action_block(True)
# -----
