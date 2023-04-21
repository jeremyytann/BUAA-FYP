import subprocess
import os
from PyQt6.QtCore import QThread

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

current_weather = world.get_weather()

weather = carla.WeatherParameters(
  fog_density = current_weather.fog_density,
  precipitation = 0.0,
  sun_altitude_angle = current_weather.sun_altitude_angle,
)

world.set_weather(weather)
"""

class RainNoneThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    with open("rain_none_script.py", "w") as f:
      f.write(script_code)

    try:
      subprocess.run(["python", "rain_none_script.py"]) 
    except KeyboardInterrupt:
      pass
    finally:
      os.remove("rain_none_script.py")