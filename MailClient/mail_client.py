from System.Net.Mail import SmtpClient, MailMessage, Attachment
from System.Net import NetworkCredential
from settings import Settings

class MailClient(object):

    def __init__(self, host, address, password):
        self.settings = Settings()
        self.client = SmtpClient(host)
        self.authenticate(address, password)
        self.send_complete_subscribers = []

    def authenticate(self, address, password):
        self.address = address
        self.client.UseDefaultCredentials = False
        self.client.EnableSsl = True
        self.client.Credentials = NetworkCredential(address, password)

    def add_list(self, sourceList, destList):
        if sourceList:
            for item in destList:
                if item:
                    destList.Add(item)

    def send(self, recipients, subject, contents, cclist=None, bcclist=None, attachlist=None):
        message = MailMessage(self.address, recipients, subject, contents)
        self.add_list(message.CC, cclist)
        self.add_list(message.Bcc, bcclist)
        if attachlist:
            for attach in attachlist:
                att = Attachment(attach)
                message.Attachments.Add(att)
        
        message.IsBodyHtml = True
        self.send_token = "Async Send From Mail Client."
        self.client.SendCompleted += self.on_send_completed
        self.client.SendAsync(message, self.send_token)

    def on_send_completed(self, sender, args):
        for subscriber in self.send_complete_subscribers:
            subscriber()
