import subprocess
import os
from PyQt6.QtCore import QThread

prop_id = 0

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

prop_id = {prop_id}

prop_actor = world.get_actor(prop_id)

prop_transform = prop_actor.get_transform()

prop_transform.rotation.yaw -= 45

prop_actor.set_transform(prop_transform)
"""

class PropRotateLeftThread(QThread):
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
    
      with open("prop_rotate_left_script.py", "w") as f:
        f.write(script_code_formatted)

      try:
        subprocess.run(["python", "prop_rotate_left_script.py"])
      except KeyboardInterrupt:
        pass
      finally:
        os.remove("prop_rotate_left_script.py")