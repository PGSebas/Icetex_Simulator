import sys
sys.path.append("src")
import os, sys
from kivy.resources import resource_add_path, resource_find
from view.gui.console_kivy import Icetex_Calculator

def main():
   
    view = Icetex_Calculator()
    view.run()

if __name__ == "__main__":
    if hasattr(sys, '_MEIPASS'):
        resource_add_path(os.path.join(sys._MEIPASS))
    main()
    