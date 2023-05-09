import subprocess
import os
from PyQt6.QtCore import QThread

vehicle_id = 0

script_code = """
import carla

vehicle_id = {vehicle_id}

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

try:
  vehicle = world.get_actor(vehicle_id)
  vehicle.destroy()
except RuntimeError:
  print('CARLA Simulator not detected')
"""

class RemoveSelectedVehicleThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global vehicle_id
    selected_vehicles = self.MainWindow.ui.vehicle_list_widget.selectedItems()
    
    if len(selected_vehicles) > 0:
      for selected_vehicle in selected_vehicles:
        vehicle_name = selected_vehicle.text()
        
      vehicle_id = int(vehicle_name.split('-')[0])
      
      script_code_formatted = script_code.format(vehicle_id=vehicle_id)
    
      with open("remove_selected_vehicle.py", "w") as f:
        f.write(script_code_formatted)

      try:
        subprocess.run(["python", "remove_selected_vehicle.py"])
      except KeyboardInterrupt:
        pass
      finally:
        self.MainWindow.ui.vehicle_list_widget.takeItem(self.MainWindow.ui.vehicle_list_widget.row(selected_vehicles[0]))
        
        car_count = int(self.MainWindow.ui.vehicle_count_label.text()) - 1
        self.MainWindow.ui.vehicle_count_label.setText(str(car_count))
        
        os.remove("remove_selected_vehicle.py")