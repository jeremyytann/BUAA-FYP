import subprocess
import os
from PyQt6.QtCore import QThread
# from vehicle.get_vehicle_list import GetVehicleListThread

walker_count = 0

script_code = """
import time
import os
import carla
from numpy import random

num_walkers = {walker_count}

client = carla.Client('127.0.0.1', 2000)
client.set_timeout(10.0)
synchronous_master = False

walkers_list = []
walker_controller_list = []
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

blueprints = world.get_blueprint_library().filter('walker.pedestrian.*')
spawn_points = []

while len(spawn_points) < num_walkers * 2:
  spawn_point = carla.Transform()
  loc = world.get_random_location_from_navigation()
  if (loc != None):
    spawn_point.location = loc
    spawn_points.append(spawn_point)

SpawnActor = carla.command.SpawnActor

# Spawn walkers
batch = []
walker_speed = []
random.shuffle(spawn_points)

for spawn_point in spawn_points:
  if len(batch) == num_walkers:
    break

  blueprint = random.choice(blueprints)
  
  if blueprint.has_attribute('is_invincible'):
    blueprint.set_attribute('is_invincible', 'false')
  
  # if blueprint.has_attribute('speed'):
  #   walker_speed.append(blueprint.get_attribute('speed').recommended_values[1])

  batch.append(SpawnActor(blueprint, spawn_point))
  
results = client.apply_batch_sync(batch, True)
"""

class GenerateWalkersThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global walker_count
    walker_count_text = self.MainWindow.ui.walker_slider_count_label.text()
    
    if walker_count_text.isdigit():
      # Parse the text to an integer
      walker_count = int(walker_count_text)
      
    script_code_formatted = script_code.format(walker_count=walker_count)
    
    with open("generate_walkers_script.py", "w") as f:
      f.write(script_code_formatted)

    try:
      self.MainWindow.ui.generate_walkers_button.setEnabled(False)
      subprocess.run(["python", "generate_walkers_script.py"])
    except KeyboardInterrupt:
      pass