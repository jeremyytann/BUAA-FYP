import subprocess
import os
from PyQt6.QtCore import QThread

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

prop_list = world.get_actors().filter('static.prop.*')

output = ''

for prop in prop_list:
    output = output + str(prop.id) + "-" + prop.type_id + " "
    
print(output)
"""

class GetPropListThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    with open("get_prop_list_script.py", "w") as f:
      f.write(script_code)

    try:
      result = subprocess.run(["python", "get_prop_list_script.py"], capture_output=True, text=True)
      output = result.stdout.strip()
      
      outputs = output.split(' ')
      
      for prop_name in outputs:
        if len(prop_name) > 0:
          self.MainWindow.ui.existing_props_list_widget.addItem(prop_name)

    except KeyboardInterrupt:
      pass
    finally:
      os.remove("get_prop_list_script.py")