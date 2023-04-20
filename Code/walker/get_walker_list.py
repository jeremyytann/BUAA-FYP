import subprocess
import os
from PyQt6.QtCore import QThread

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

walker_list = world.get_actors().filter('walker.pedestrian.*')

output = ''

for walker in walker_list:
    output = output + str(walker.id) + "-" + walker.type_id + " "
    
print(output)
"""

class GetWalkerListThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    with open("get_walker_list_script.py", "w") as f:
      f.write(script_code)

    try:
      result = subprocess.run(["python", "get_walker_list_script.py"], capture_output=True, text=True)
      output = result.stdout.strip()
      
      outputs = output.split(' ')
      
      print(outputs)
      
      for walker_name in outputs:
          self.MainWindow.ui.walker_list_widget.addItem(walker_name)
      
      walker_list_count = self.MainWindow.ui.walker_list_widget.count()
      
      self.MainWindow.ui.walker_count_label.setText(str(walker_list_count))
      
      if walker_list_count > 0:
        self.MainWindow.ui.generate_walkers_button.setEnabled(False)
    except KeyboardInterrupt:
      pass
    finally:
      os.remove("get_walker_list_script.py")