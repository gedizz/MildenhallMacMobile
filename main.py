from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.widget import Widget
from kivy.clock import Clock


class LeftTop(GridLayout):

    oneReserve = TextInput(multiline=False)
    oneMain = TextInput(multiline=False)
    twoMain = TextInput(multiline=False)

    def __init__(self, **kwargs):
        super(LeftTop, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 2
        #self.size_hint = (0.33, 0.33)

        self.add_widget(Label(text='#1 Reserve'))
        self.add_widget(Label(text='#1 Main'))
        self.add_widget(Label(text='#2 Main'))

        self.add_widget(self.oneReserve)
        self.add_widget(self.oneMain)
        self.add_widget(self.twoMain)


class MiddleTop(GridLayout):
    forwardBody = TextInput(multiline=False)
    centerWing = TextInput(multiline=False)
    aftBody = TextInput(multiline=False)
    upperDeck = TextInput(multiline=False)

    def __init__(self, **kwargs):
        super(MiddleTop, self).__init__(**kwargs)
        self.rows = 8
        #self.size_hint = (0.33, 0.33)

        self.add_widget(Label(text='Forward Body', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.forwardBody)

        self.add_widget(Label(text='Center Wing', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.centerWing)

        self.add_widget(Label(text='Aft Body', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.aftBody)

        self.add_widget(Label(text='Upper Deck', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.upperDeck)


class RightTop(GridLayout):
    threeMain = TextInput(multiline=False)
    fourMain = TextInput(multiline=False)
    fourReserve = TextInput(multiline=False)

    def __init__(self, **kwargs):
        super(RightTop, self).__init__(**kwargs)
        self.cols = 3
        self.rows = 2
        #self.size_hint = (0.33, 0.33)

        self.add_widget(Label(text='#3 Main'))
        self.add_widget(Label(text='#4 Main'))
        self.add_widget(Label(text='#4 Reserve'))

        self.add_widget(self.threeMain)
        self.add_widget(self.fourMain)
        self.add_widget(self.fourReserve)


class BasicInputs(GridLayout):

    basicWeight = TextInput(multiline=False)
    basicMoment = TextInput(multiline=False)
    fuelDensity = TextInput(multiline=False)

    def __init__(self, **kwargs):
        super(BasicInputs, self).__init__(**kwargs)
        self.cols = 3
       # self.rows = 2
        self.size_hint = (0.2, 0.2)

        self.add_widget(Label(text='Basic Weight', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.basicWeight)

        self.add_widget(Label(text='Basic Moment', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.basicMoment)

        self.add_widget(Label(text='Fuel Density', size_hint_x=0.33, size_hint_y=0.33))
        self.add_widget(self.fuelDensity)



    #def update(self):
        #text = FuelLoad.oneMain.text
        #FuelLoad.oneReserve.text = text


class MainBody(BoxLayout):
    def __init__(self, **kwargs):
        super(MainBody, self).__init__(**kwargs)
        # Anchor Layout1
        topLeft = AnchorLayout(anchor_x='left', anchor_y='top', padding=5)
        topLeft.add_widget(LeftTop(size_hint_x=1, size_hint_y=0.1))
        # Anchor Layout2
        topMiddle = AnchorLayout(anchor_x='center', anchor_y='top')
        topMiddle.add_widget(MiddleTop(size_hint_x=1, size_hint_y=0.33))
        # Anchor Layout3
        topRight = AnchorLayout(anchor_x="right", anchor_y="top")
        topRight.add_widget(RightTop(size_hint_x=1, size_hint_y=0.1))
        # Create a box layout
        # Add both the anchor layouts to the box layout
        self.add_widget(topLeft)
        self.add_widget(topMiddle)
        self.add_widget(topRight)
        # Return the boxlayout widget


class MyApp(App):

    def build(self):
        #anchor1 = AnchorLayout(anchor_x='left', anchor_y='bottom')
        #button1 = Button(text='Bottom-Left', size_hint=(0.3, 0.3), background_color=(1.0, 0.0, 0.0, 1.0))
        #anchor1.add_widget(button1)
        #Clock.schedule_interval(FuelLoad.update, 1.0 / 60.0)
        return MainBody()


if __name__ == '__main__':
    MyApp().run()
