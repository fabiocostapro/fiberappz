import os
import paramiko as pmk
import re
import time


class InSsh:

    def __init__(self):
        self.ssh = pmk.SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(pmk.AutoAddPolicy())
        self.ssh.connect(hostname="fibra.redetelenew.com.br", port=2222, username="72fcosta", password=os.environ.get(
            "PASSWORD_SSH_FIBERAPP"), look_for_keys=False, allow_agent=False)
        self.shell = self.ssh.invoke_shell()

    def __del__(self):
        self.ssh.close()

    def run_commands(self, commands):
        time.sleep(4)
        for command in commands:
            self.shell.send(command + "\n")
        time.sleep(4)
        shell_output = str(self.shell.recv(5000))
        if len(shell_output) > 1:
            return shell_output
        else:
            error = []
            error.append("error")
            return error

    # def run_commands(self):
    #     with open("output.txt", "r") as file:
    #         shell_output = file.read()
    #     return shell_output

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

    def test_connection(self):
        open("output.txt", "w").close()
        shell_output = self.run_commands(["enable", "config"])
        check_output = self.check_ouput(shell_output)
        if check_output:
            return check_output

        def write_file():
            with open("output.txt", "w") as file:
                file.write(shell_output)
        write_file()
        config_q = (r"(config)")
        config_ret = re.findall(config_q, shell_output)
        c = 0
        for item in config_ret:
            c += 1
        if c > 1:
            test_connection = "True"
        else:
            test_connection = "False"
        return test_connection

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

    def authorize_ont(self, sn, f, s, p, vendorId, description, vlan, scriptType, gemPort):
        # open("output.txt", "w").close()
        # shell_output = self.run_commands(
        #     ["enable", "config", "scroll 512", "interface gpon {}/{}".format(f, s), "display ont info {} all".format(p)]
        # )
        shell_output = self.run_commands()
        check_output = self.check_ouput(shell_output)
        if check_output:
            return check_output

        busy_id = []
        busy_q = (r"(\d?\d)\s*[^ ]*\s*active")
        busy_ret = re.findall(busy_q, shell_output)
        c = 0
        for item in busy_ret:
            busy_id.append(int(item.strip()))
            item = int(item)
            c += 1
        print(busy_id)
        free_places = []
        all_places = (range(0, 124))
        for item in all_places:
            if item not in busy_id:
                free_places.append(item)
        print(free_places)
        next_ont_id = min(free_places)
        print(next_ont_id)
        authorize_command = ["ont add {} {} sn-auth {} omci {} desc {}".format(p, next_ont_id, sn, scriptType, description), "ont port native-vlan {} {} eth 1 vlan {} priority 0".format(
            p, next_ont_id, vlan), "quit", "service-port vlan {} gpon {}/{}/{} ont {} gemport {} multi-service user-vlan {} tag-transform translate".format(vlan, f, s, p, gemPort, next_ont_id, vlan)]

        shell_output = self.run_commands(authorize_command)

        def write_file():
            with open("output.txt", "w") as file:
                file.write(shell_output)
        write_file()
        print(authorize_command)
        return next_ont_id
