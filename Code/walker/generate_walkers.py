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

print(len(spawn_points))

# Spawn walkers
batch = []
walker_speed = []
random.shuffle(spawn_points)

for spawn_point in spawn_points:
  if len(batch) == num_walkers:
    print(len(batch))
    break

  blueprint = random.choice(blueprints)
  
  if blueprint.has_attribute('is_invincible'):
    blueprint.set_attribute('is_invincible', 'false')
  
  # if blueprint.has_attribute('speed'):
  #   walker_speed.append(blueprint.get_attribute('speed').recommended_values[1])

  batch.append(SpawnActor(blueprint, spawn_point))
  
results = client.apply_batch_sync(batch, True)

# new_walker_speed = []

# for i in range(len(results)):
#   if results[i].error:
#     print(results[i].error)
#   else:
#     walkers_list.append({{"id": results[i].actor_id}})
#     new_walker_speed.append(walker_speed[i])
  
# walker_speed = new_walker_speed

# batch = []
# all_id = []
# blueprint_controller = world.get_blueprint_library().find('controller.ai.walker')

# for i in range(len(walkers_list)):
#   batch.append(SpawnActor(blueprint_controller, carla.Transform(), walkers_list[i]["id"]))

# results = client.apply_batch_sync(batch, True)

# for i in range(len(results)):
#   if results[i].error:
#     print(results[i].error)
#   else:
#     walkers_list[i]["con"] = results[i].actor_id

# for i in range(len(walkers_list)):
#   all_id.append(walkers_list[i]["con"])
#   all_id.append(walkers_list[i]["id"])
# all_actors = world.get_actors(all_id)
  
# for i in range(0, len(all_id), 2):
#   all_actors[i].start()
#   all_actors[i].go_to_location(world.get_random_location_from_navigation())
#   all_actors[i].set_max_speed(float(walker_speed[int(i/2)]))

# traffic_manager.global_percentage_speed_difference(30.0)

# while True:
#   world.tick()
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