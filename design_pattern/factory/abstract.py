# 抽象产品接口 - 按钮
class Button:
     def paint(self):
        pass

# 具体产品类 - WindowsButton
class WindowsButton(Button):
    def paint(self):
        return "Render a Windows button"

# 具体产品类 - MacButton
class MacButton(Button):
    def paint(self):
        return "Render a Mac button"

# 抽象产品接口 - 文本框
class TextBox:
    def paint(self):
        pass

# 具体产品类 - WindowsTextBox
class WindowsTextBox(TextBox):
    def paint(self):
        return "Render a Windows text box"

# 具体产品类 - MacTextBox
class MacTextBox(TextBox):
    def paint(self):
        return "Render a Mac text box"

# 抽象工厂接口
class GUIFactory:
    def create_button(self):
        pass

    def create_text_box(self):
        pass

# 具体工厂类 - WindowsGUIFactory
class WindowsGUIFactory(GUIFactory):
    def create_button(self):
        return WindowsButton()

    def create_text_box(self):
        return WindowsTextBox()

# 具体工厂类 - MacGUIFactory
class MacGUIFactory(GUIFactory):
    def create_button(self):
        return MacButton()

    def create_text_box(self):
        return MacTextBox()
class Gui(Button,TextBox):
    def __init__(self,Button,TextBox):
        self.button = Button
        self.textbox = TextBox
    def pick(self):
        print(self.button.paint())
    def pop_up(self):
        print(self.button.paint())

# 客户端代码

def create_gui(factory):
    button = factory.create_button()
    text_box = factory.create_text_box()
    return Gui(button,text_box)



windows_gui = create_gui(WindowsGUIFactory())
mac_gui = create_gui(MacGUIFactory())

windows_gui.pick()
windows_gui.pop_up()

mac_gui.pick()
mac_gui.pop_up()
