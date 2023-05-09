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
  walker.destroy()
except RuntimeError:
  print('CARLA Simulator not detected')
"""

class RemoveSelectedWalkerThread(QThread):
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
    
      with open("remove_selected_walker.py", "w") as f:
        f.write(script_code_formatted)

      try:
        subprocess.run(["python", "remove_selected_walker.py"])
      except KeyboardInterrupt:
        pass
      finally:
        self.MainWindow.ui.walker_list_widget.takeItem(self.MainWindow.ui.walker_list_widget.row(selected_walkers[0]))
        
        car_count = int(self.MainWindow.ui.walker_count_label.text()) - 1
        self.MainWindow.ui.walker_count_label.setText(str(car_count))
        
        os.remove("remove_selected_walker.py")