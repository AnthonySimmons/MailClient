import sys
from mail_client import MailClient

class MailConsole(object):
    
    def __init__(self):
        self.options = ["-to", "-from", "-password", "-host", "-subject", "-contents"]
        self.get_options = {}

    def print_usage(self):
        usage = "ipy.exe mail_console.py -to <Address> -from <Address> -password <Password> -host <Server> -subject <Subject> -contents <Contents>"
        print(usage)

    @property
    def receipients(self):
        return self.get_options["-to"]

    @property
    def sender(self):
        return self.get_options["-from"]

    @property
    def password(self):
        return self.get_options["-password"]

    @property
    def host(self):
        return self.get_options["-host"]

    @property
    def subject(self):
        return self.get_options["-subject"]

    @property
    def contents(self):
        return self.get_options["-contents"]

    def parse_options(self, args):
        argv = args

        for i in range(len(argv)-1):
            arg = argv[i]
            if arg in self.options:                
                option = argv[i+1]
                self.get_options[arg] = option

    
    def prompt(self):
        for option in self.options:
            prompt = "{}: ".format(option.replace("-", ""))
            opt = raw_input(prompt)
            self.get_options[option] = opt

    def run(self):
        argc = len(sys.argv)
        if argc == 1:
            self.prompt()
        else:
            self.parse_options(sys.argv)


console = MailConsole()
console.run()
client = MailClient(console.host, console.sender, console.password)
client.send(console.receipients, console.subject, console.contents)