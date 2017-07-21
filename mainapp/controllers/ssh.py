import os
import paramiko as pmk
import re
import time


class Inside:

    # def __init__(self):
    #     self.ssh = pmk.SSHClient()
    #     self.ssh.load_system_host_keys()
    #     self.ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
    #     self.ssh.connect(hostname="fibra.redetelenew.com.br", port=2222, username="72fcosta", password=os.environ.get(
    #         "PASSWORD_SSH_FIBERAPP"), look_for_keys=False, allow_agent=False)
    #     self.shell = self.ssh.invoke_shell()

    # def __del__(self):
    #     self.ssh.close()

    # def run_commands(self, commands):
    #     time.sleep(4)
    #     for command in commands:
    #         self.shell.send(command + "\n")
    #     time.sleep(4)
    #     shell_output = str(self.shell.recv(5000))
    #     if len(shell_output) > 1:
    #         return shell_output
    #     else:
    #         error = []
    #         error.append("error")
    #         return error

    def run_commands(self):
        with open("output.txt", "r") as file:
            shell_output = file.read()
        return shell_output

    def check_ouput(self, shell_output):
        # prompt_q = [r"(#')"]
        # prompt_ret = re.findall(prompt_q, shell_output)
        # if len(prompt_ret) < 1:
        #     prompt_ret.append("error")
        #     print(prompt_ret)
        #     return prompt_ret
        welcome = [r"(#)"]
        for pattern in welcome:
            pattern_q = pattern
            pattern_ret = re.findall(pattern_q, shell_output)
            if len(pattern_ret) < 2:
                pattern_ret.append("error")
                print(pattern_ret)
                return pattern_ret
        not_welcome = [r"(Unknown)", r"(#[A-z 0-9 _]{1,}')"]
        for pattern in not_welcome:
            pattern_q = pattern
            pattern_ret = re.findall(pattern_q, shell_output)
            if len(pattern_ret) > 0:
                pattern_ret.append("error")
                print(pattern_ret)
                return pattern_ret

    def status_onts(self):
        # open("output.txt", "w").close()
        # shell_output = self.run_commands(["enable", "config", "scroll 512", "display ont autofind all"])
        shell_output = self.run_commands()
        check_output = self.check_ouput(shell_output)
        if check_output:
            return check_output

        def write_file():
            with open("output.txt", "w") as file:
                file.write(shell_output)
        write_file()
        status_onts = {}
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
        c = 0
        for item in id_ret:
            status_onts["{}".format(c)] = [item.strip(), SN_ret[c].strip(), F_ret[c].strip(),
                                           S_ret[c].strip(), P_ret[c].strip(), VendorID_ret[c].strip()]
            c += 1
        return status_onts

    def next_ont_id(self, f, s, p):
        open("output.txt", "w").close()
        shell_output = self.run_commands(
            ["enable", "config", "scroll 512", "interface gpon {}/{}".format(f, s), "display ont info {} all".format(p)]
        )
        check_output = self.check_ouput(shell_output)
        if check_output:
            return check_output

        def write_file():
            with open("output.txt", "w") as file:
                file.write(shell_output)
        write_file()
        next_ont_id = []
        ont_q = (r"(\d?\d)\s*[^ ]*\s*active")
        ont_ret = re.findall(ont_q, shell_output)
        c = 0
        for item in ont_ret:
            next_ont_id.append(int(item.strip()))
            item = int(item)
            c += 1
        print(next_ont_id)
        free_places = []
        all_places = (range(0, 124))
        for item in all_places:
            if item not in next_ont_id:
                free_places.append(item)
        print(free_places)

        return next_ont_id
