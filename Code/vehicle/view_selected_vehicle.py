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

  # Set the spectator view to the vehicle's location and rotation
  spectator = world.get_spectator()
  vehicle_transform = vehicle.get_transform()
  vehicle_transform.location.z += 3
  spectator.set_transform(vehicle_transform)
except RuntimeError:
  print('CARLA Simulator not detected')
"""

class ViewSelectedVehicleThread(QThread):
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
    
      with open("view_selected_vehicle.py", "w") as f:
        f.write(script_code_formatted)

      try:
        subprocess.run(["python", "view_selected_vehicle.py"])
      except KeyboardInterrupt:
        pass
      finally:
        os.remove("view_selected_vehicle.py")