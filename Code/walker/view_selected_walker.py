import subprocess
import os
from PyQt6.QtCore import QThread

walker_id = 0

script_code = """
import carla

walker_id = {walker_id}

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

try:
  walker = world.get_actor(walker_id)

  spectator = world.get_spectator()
  walker_transform = walker.get_transform()
  walker_transform.location.x += 3
  walker_transform.location.z += 1
  walker_transform.rotation.yaw += 180
  spectator.set_transform(walker_transform)
except RuntimeError:
  print('CARLA Simulator not detected')
"""

class ViewSelectedWalkerThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global walker_id
    selected_walkers = self.MainWindow.ui.walker_list_widget.selectedItems()
    
    if len(selected_walkers) > 0:
      for selected_walker in selected_walkers:
        walker_name = selected_walker.text()
        
      walker_id = int(walker_name.split('-')[0])
      
      script_code_formatted = script_code.format(walker_id=walker_id)
    
      with open("view_selected_walker.py", "w") as f:
        f.write(script_code_formatted)

      try:
        subprocess.run(["python", "view_selected_walker.py"])
      except KeyboardInterrupt:
        pass
      finally:
        os.remove("view_selected_walker.py")