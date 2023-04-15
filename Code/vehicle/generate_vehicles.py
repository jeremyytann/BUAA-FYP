import subprocess
import os
from PyQt6.QtCore import QThread

vehicle_count = 0

script_code = """
import time
import os
import carla
from numpy import random

num_traffics = {vehicle_count}

client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False

vehicles_list = []
world = client.get_world()

traffic_manager = client.get_trafficmanager(8000)
traffic_manager.set_global_distance_to_leading_vehicle(2.0)
traffic_manager.set_synchronous_mode(True)

settings = world.get_settings()

if not settings.synchronous_mode:
  synchronous_master = True
  settings.synchronous_mode = True
  settings.fixed_delta_seconds = 0.05
else:
  synchronous_master = False

blueprints = world.get_blueprint_library().filter('vehicle.*')
spawn_points = world.get_map().get_spawn_points()

SpawnActor = carla.command.SpawnActor
SetAutopilot = carla.command.SetAutopilot
FutureActor = carla.command.FutureActor

# Spawn vehicles
batch = []
random.shuffle(spawn_points)

for n, transform in enumerate(spawn_points):
  if n >= num_traffics:
    break
  blueprint = random.choice(blueprints)
  blueprint.set_attribute('role_name', 'autopilot')
  
  if blueprint.has_attribute('color'):
    color = random.choice(blueprint.get_attribute('color').recommended_values)
    blueprint.set_attribute('color', color)
  if blueprint.has_attribute('driver_id'):
    driver_id = random.choice(blueprint.get_attribute('driver_id').recommended_values)
    blueprint.set_attribute('driver_id', driver_id)

  batch.append(SpawnActor(blueprint, transform)
    .then(SetAutopilot(FutureActor, True, traffic_manager.get_port())))
  
client.apply_batch_sync(batch, synchronous_master)

print('Generated {vehicle_count} vehicles.')

traffic_manager.global_percentage_speed_difference(25.0)

while True:
  world.tick()
"""

class GenerateVehiclesThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global vehicle_count
    vehicle_count_text = self.MainWindow.ui.vehicle_slider_count_label.text()
    
    if vehicle_count_text.isdigit():
      # Parse the text to an integer
      vehicle_count = int(vehicle_count_text)
      
    script_code_formatted = script_code.format(vehicle_count=vehicle_count)
    
    with open("generate_vehicles_script.py", "w") as f:
      f.write(script_code_formatted)

    try:
      self.MainWindow.ui.generate_vehicles_button.setEnabled(False)
      subprocess.run(["python", "generate_vehicles_script.py"])
    except KeyboardInterrupt:
      pass