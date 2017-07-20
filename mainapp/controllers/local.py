import re


class InsideLocal:

    def run_commands(self):
        with open("output.txt", "r") as file:
            shell_output = file.read()
        return shell_output

    def check_ouput(self, shell_output):
        request_error_q = (r"Unknown")
        request_error_ret = re.findall(request_error_q, shell_output)
        print("REQUEST_ERROR:{}".format(request_error_ret))
        if len(request_error_ret) == 0:
            request_error = "ok"
        else:
            request_error = "error"
        return request_error

    def status_onts(self):
        shell_output = self.run_commands()
        request_error = self.check_ouput(shell_output)

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
        status_onts = {}
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

        def write_file():
            with open("output.txt", "w") as file:
                file.write(shell_output)
        write_file()
        next_ont_id = {shell_output}
        self.check_ouput()
        ont_q = (r"(\d?\d)\s*[^ ]*\s*active")
        ont_ret = re.findall(ont_q, shell_output)
        c = 0
        for item in ont_ret:
            next_ont_id["{}".format(c)] = [item.strip()]
            item = int(item)
            c += 1
        print(next_ont_id)

        return next_ont_id
