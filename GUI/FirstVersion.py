import kivy
from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from MainFileForGUI import MainFileGUI
import os
kivy.require("1.11.1")

class ConnectPage(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 2

        if os.path.isfile("prev_details.txt"):
            with open("prev_details.txt", "r") as f:
                d = f.read().split(",")
                prev_project_name = d[0]
                prev_LayuppNumber = d[1]
                prev_Timestamp = d[2]
                prev_Angle = d[3]
        else: 
            prev_project_name = ""
            prev_LayuppNumber = ""
            prev_Timestamp = ""
            prev_Angle = ""


        self.add_widget(Label(text="Project name:"))

        self.project_name = TextInput(text = prev_project_name, multiline=False)
        self.add_widget(self.project_name)

        self.add_widget(Label(text="Layupp Number:"))
        
        self.LayuppNumber = TextInput(text = prev_LayuppNumber, multiline=False)
        self.add_widget(self.LayuppNumber)

        self.add_widget(Label(text="Timestamp yes/no : 1/0"))
        
        self.Timestamp = TextInput(text = prev_Timestamp, multiline=False)
        self.add_widget(self.Timestamp)

        self.add_widget(Label(text="Include Angle yes/no : 1/0"))
        
        self.Angle = TextInput(text = prev_Angle, multiline=False)
        self.add_widget(self.Angle)


        self.RunAnalysis = Button(text = 'RunAnalysis')
        self.RunAnalysis.bind(on_press = self.RunAnalysis_button)
        self.RunAnalysis.bind(on_press = self.TEST)
        self.add_widget(Label())
        self.add_widget(self.RunAnalysis)

    def RunAnalysis_button(self, instance):
        project_name = self.project_name.text
        LayuppNumber = self.LayuppNumber.text
        Timestamp = self.Timestamp.text
        Angle = self.Angle.text

        #print(f"Attempting to join {ip}:{port} as {Timestamp}")

        with open("prev_details.txt", "w")  as f:
            f.write(f"{project_name},{LayuppNumber},{Timestamp},{Angle}")
    
    def TEST(self, instance):
        project_name = self.project_name.text
        LayuppNumber = self.LayuppNumber.text
        Timestamp = self.Timestamp.text
        Angle = self.Angle.text

        #Runing the python script for the composite analysis
        MainFileGUI(project_name,LayuppNumber,Timestamp,Angle)

        print('Test worked')
        print(f"{project_name}")

class CompositAssistant(App):
    def build(self):
        return ConnectPage()

if __name__ == "__main__":
    CompositAssistant().run()
