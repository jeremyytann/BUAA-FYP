import subprocess
import os
from PyQt6.QtCore import QThread

prop_id = 0

script_code = """
import carla

prop_id = {prop_id}

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

try:
  prop = world.get_actor(prop_id)
  prop.destroy()
except RuntimeError:
  print('CARLA Simulator not detected')
"""

class RemoveSelectedPropThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global prop_id
    selected_props = self.MainWindow.ui.existing_props_list_widget.selectedItems()
    
    if len(selected_props) > 0:
      for selected_prop in selected_props:
        prop_name = selected_prop.text()
        
      prop_id = int(prop_name.split('-')[0])
      
      script_code_formatted = script_code.format(prop_id=prop_id)
    
      with open("remove_selected_prop.py", "w") as f:
        f.write(script_code_formatted)

      try:
        subprocess.run(["python", "remove_selected_prop.py"])
      except KeyboardInterrupt:
        pass
      finally:
        self.MainWindow.ui.existing_props_list_widget.takeItem(self.MainWindow.ui.existing_props_list_widget.row(selected_props[0]))
        
        os.remove("remove_selected_prop.py")