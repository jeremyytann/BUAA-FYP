import subprocess
import os
from PyQt6.QtCore import QThread

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

walker_list = world.get_actors().filter('walker.pedestrian.*')
vehicle_list = world.get_actors().filter('vehicle.*')

for walker in walker_list:
    walker.destroy()
    
if len(vehicle_list) == 0:
  settings = world.get_settings()
  settings.synchronous_mode = False
  settings.no_rendering_mode = False
  settings.fixed_delta_seconds = None
  world.apply_settings(settings)
"""

class RemoveAllWalkersThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    with open("remove_all_walkers_script.py", "w") as f:
      f.write(script_code)

    try:
      subprocess.run(["python", "remove_all_walkers_script.py"])
    except KeyboardInterrupt:
      pass
    finally:
      os.remove("remove_all_walkers_script.py")
      
      if os.path.exists("generate_walkers_script.py"):
        os.remove("generate_walkers_script.py")
      
      self.MainWindow.ui.generate_walkers_button.setEnabled(True)
      self.MainWindow.ui.walker_list_widget.clear()
      self.MainWindow.ui.walker_count_label.setText("0")