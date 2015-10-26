import wpf

from System.Windows import Window, Application

class Login(Window):
    def __init__(self):
        wpf.LoadComponent(self, 'login.xaml')
        self.textBoxHost.Focus()
        self.buttonLogin.IsDefault = True

    @property
    def host(self):
        return self.textBoxHost.Text

    @property
    def email(self):
        return self.textBoxEmail.Text

    @property
    def password(self):
        return self.passwordBox.Password

    def validate(self):
        return self.host and self.email and self.password

    def highlight(self, label, property):
        req = "*"
        if not property:
            if not label.Content.endswith(req):
                label.Content += req
        else:
            label.Content = label.Content.replace(req, "")

    def highlight_required(self):
        req = "*"
        self.highlight(self.labelHost, self.host)
        self.highlight(self.labelEmail, self.email)
        self.highlight(self.labelPassword, self.password)


    def login_click(self, sender, event):
        if self.validate():
            self.DialogResult = True
            self.Close()
        else:
            self.highlight_required()
    
    def buttonCancel_Click(self, sender, e):
        self.DialogResult = False
        self.Close()

    def mouse_down(self, sender, e):
        self.DragMove()