from mail_client import MailClient
from login import Login
import wpf

from System.Text import Encoding
from System.IO import MemoryStream
from System.Windows import *
from System.Windows.Documents import TextRange
#from System.Windows.Forms import OpenFileDialog

class MailForm(Window):
    splitChar = ","
    
    def __init__(self):
        wpf.LoadComponent(self, 'mail_form.xaml')
        #self.buttonSend.Click += self.send_button_click
        self.Loaded += self.window_loaded
        self.attachlist = []

    @property
    def cclist(self):
        return self.textBoxCc.Text.split(MailForm.splitChar)

    @property
    def bcclist(self):
        return self.textBoxBcc.Text.split(MailForm.splitChar)

    
    def send_button_click(self, sender, args):
        self.send_email()

    def get_rich_text(self):
        contentRange = TextRange(self.richTextBoxContent.Document.ContentStart, self.richTextBoxContent.Document.ContentEnd)
        #stream = MemoryStream()
        #contentRange.Save(stream, DataFormats.Rtf)
        #content = Encoding.UTF8.GetString(stream.ToArray())
        return contentRange.Text

    def send_email(self):
        self.progressBarSend.Visibility = Visibility.Visible
        content = self.get_rich_text()
        self.client.send(self.textBoxTo.Text, self.textBoxSubject.Text, content, self.cclist, self.bcclist, self.attachlist)

    def window_loaded(self, sender, args):
        self.authenticate()

    def authenticate(self):
        login = Login()
        login.ShowDialog()
        self.client = MailClient(login.host, login.email, login.password)
        self.client.send_complete_subscribers.append(self.send_complete)

    def send_complete(self):
        self.progressBarSend.Visibility = Visibility.Hidden
    
    def buttonAttach_Click(self, sender, e):
        pass
        #openFile = OpenFileDialog()
        #openFile.ShowDialog()
        
try:
    form = MailForm()
    app = Application()
    app.Run(form)
except Exception, e:
    MessageBox.Show(e.message)