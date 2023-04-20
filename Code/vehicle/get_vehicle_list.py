import subprocess
import os
from PyQt6.QtCore import QThread

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

vehicle_list = world.get_actors().filter('vehicle.*')

output = ''

for vehicle in vehicle_list:
    output = output + str(vehicle.id) + "-" + vehicle.type_id + " "
    
print(output)
"""

class GetVehicleListThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    with open("get_vehicle_list_script.py", "w") as f:
      f.write(script_code)

    try:
      result = subprocess.run(["python", "get_vehicle_list_script.py"], capture_output=True, text=True)
      output = result.stdout.strip()
      
      outputs = output.split(' ')
      
      for vehicle_name in outputs:
          self.MainWindow.ui.vehicle_list_widget.addItem(vehicle_name)
      
      vehicle_list_count = self.MainWindow.ui.vehicle_list_widget.count()
      
      self.MainWindow.ui.vehicle_count_label.setText(str(vehicle_list_count))
      
      if vehicle_list_count > 0:
        self.MainWindow.ui.generate_vehicles_button.setEnabled(False)
    except KeyboardInterrupt:
      pass
    finally:
      os.remove("get_vehicle_list_script.py")