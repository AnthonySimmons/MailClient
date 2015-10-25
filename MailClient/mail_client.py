from System.Net.Mail import SmtpClient, MailMessage, Attachment
from System.Net import NetworkCredential

class MailClient(object):

    def __init__(self, host, address, password):
        self.client = SmtpClient(host)
        self.authenticate(address, password)
        self.send_complete_subscribers = []

    def authenticate(self, address, password):
        self.address = address
        self.client.UseDefaultCredentials = False
        self.client.EnableSsl = True
        self.client.Credentials = NetworkCredential(address, password)

    def send(self, recipients, subject, contents, cclist=None, bcclist=None, attachlist=None):
        message = MailMessage(self.address, recipients, subject, contents)
        if cclist:
            for cc in cclist:
                message.CC.Add(cc)
        if bcclist:
            for bcc in bcclist:
                message.Bcc.Add(bcc)
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
