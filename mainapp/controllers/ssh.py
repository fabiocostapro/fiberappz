import paramiko as pmk
import json
import re
import time


class StatusOnts:

    # def __init__(self):
    #     self.ssh = pmk.SSHClient()
    #     self.ssh.load_system_host_keys()
    #     self.ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
    #     self.ssh.connect(hostname="fibra.redetelenew.com.br", port=2222, username="sergio",
    #                      password="sugar222", look_for_keys=False, allow_agent=False)

    # def __del__(self):
    #     self.ssh.close()

    # def in_json(self, commands):
        # shell = self.ssh.invoke_shell()
        # for command in commands:
        #     shell.send(command + "\n")
        # time.sleep(2)
        # shell_output = str(shell.recv(5000))

    def in_json(self):
        def read_file():
            with open("output.txt", "r") as file:
                datafile = file.read()
            return datafile

        shell_output = read_file()
        print(shell_output)

        def write_file():
            with open("output.txt", "w") as file:
                file.write(shell_output)
        write_file()

        id_q = (r"Number\s*:\s(\d)")
        SN_q = (r"SN\s*:\s(\S{16})")
        F_q = (r"F\/S\/P\s*:\s(\d)")
        S_q = (r"F\/S\/P\s*:\s\d.(\d)")
        P_q = (r"F\/S\/P\s*:\s\d.\d.(\d)")
        VendorID_q = (r"VendorID\s*:\s(\S{4})")
        id_ret = re.findall(id_q, shell_output)
        SN_ret = re.findall(SN_q, shell_output)
        F_ret = re.findall(F_q, shell_output)
        S_ret = re.findall(S_q, shell_output)
        P_ret = re.findall(P_q, shell_output)
        VendorID_ret = re.findall(VendorID_q, shell_output)
        print(S_ret)

        c = 0
        ont_info = {}
        for item in id_ret:
            ont_info["{}".format(c)] = [item.strip(), SN_ret[c].strip(), F_ret[c].strip(),
                                        S_ret[c].strip(), P_ret[c].strip(), VendorID_ret[c].strip()]
            c += 1
        return ont_info
