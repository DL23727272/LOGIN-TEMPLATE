from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.card import MDCard
from kivymd.uix.label import MDLabel
from kivymd.uix.textfield import MDTextFieldRect
from kivy.lang import Builder

class Login(MDApp):
    def build(self):
        return Builder.load_file("login.kv")                                                                    # WAG NIYO KOPYAHINNNNNNNN  
# WAG NIYO KOPYAHINNNNNNNN
    def login(self):                                                                    # WAG NIYO KOPYAHINNNNNNNN  
        entered_username = self.root.ids.username_input.text                                                                    # WAG NIYO KOPYAHINNNNNNNN  
        entered_password = self.root.ids.password_input.text
        error_label = self.root.ids.error_label
                                                                    # WAG NIYO KOPYAHINNNNNNNN  
        username = 'DL'
        password = '123'

        if entered_username == '' and entered_password == '':                                                                    # WAG NIYO KOPYAHINNNNNNNN  
            error_label.text = 'Empty username and password!'                                                                    # WAG NIYO KOPYAHINNNNNNNN  
        elif entered_username == '':
            error_label.text = 'Empty username!'                                                                    # WAG NIYO KOPYAHINNNNNNNN  
        elif entered_password == '':
            error_label.text = 'Empty password!'
        elif entered_username == username and entered_password == password:                                                                    # WAG NIYO KOPYAHINNNNNNNN  
            error_label.text = 'Success!'
        elif entered_username != 'DL' or entered_password != '123':                                                                    # WAG NIYO KOPYAHINNNNNNNN  
            error_label.text = 'Wrong username or password!'                                                                    # WAG NIYO KOPYAHINNNNNNNN  
        else:
            error_label.text = 'Failed.' 
                                                                                                    # WAG NIYO KOPYAHINNNNNNNN
if __name__ == "__main__":
    app = Login()
    app.run()
