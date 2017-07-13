from paramiko import SSHClient
import paramiko


class SSH:

    def __init__(self):
        self.ssh = SSHClient()
        self.ssh.load_system_host_keys()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(hostname="45.33.23.219", username="diple", timeout=10)

    def exec_cmd(self, cmd):
        stdin, stdout, stderr = self.ssh.exec_command(cmd)
        if stderr.channel.recv_exit_status() != 0:
            output = (stderr.readlines())
        else:
            output = (stdout.readlines())
        return output


def uptime(command):
    ssh = SSH()
    output = ssh.exec_cmd(command)
    return output


def ls(command):
    ssh = SSH()
    output = ssh.exec_cmd(command)
    return output
