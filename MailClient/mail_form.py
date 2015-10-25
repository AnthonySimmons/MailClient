from mail_client import MailClient
from login import Login
import wpf

from System.Windows import Window, Application, MessageBox
from System.Windows.Documents import TextRange
#from System.Windows.Forms import OpenFileDialog

class MailForm(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'mail_form.xaml')
        #self.buttonSend.Click += self.send_button_click
        self.Loaded += self.window_loaded

    def send_button_click(self, sender, args):
        self.send_email()

    def send_email(self):
        contentRange = TextRange(self.richTextBoxContent.Document.ContentStart, self.richTextBoxContent.Document.ContentEnd)
        content = contentRange.Text
        self.client.send(self.textBoxTo.Text, self.textBoxSubject.Text, content)

    def window_loaded(self, sender, args):
        self.authenticate()

    def authenticate(self):
        login = Login()
        login.ShowDialog()
        self.client = MailClient(login.host, login.email, login.password)
    
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