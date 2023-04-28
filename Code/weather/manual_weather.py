import subprocess
import os
from PyQt6.QtCore import QThread

sun_altitude_angle = 0
precipitation = 0
fog_density = 0

script_code = """
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

weather = carla.WeatherParameters(
  fog_density = {fog_density}.0,
  precipitation = {precipitation}.0,
  sun_altitude_angle = {sun_altitude_angle}.0,
)

world.set_weather(weather)
"""

class ManualWeatherThread(QThread):
  def __init__(self, MainWindow, parent=None):
    super().__init__(parent)
    self.MainWindow = MainWindow
  
  def run(self):
    global sun_altitude_angle
    sun_altitude_angle = self.MainWindow.ui.sun_slider_label.text()
    global precipitation
    precipitation = self.MainWindow.ui.rain_slider_label.text()
    global fog_density
    fog_density = self.MainWindow.ui.fog_slider_label.text()
    
    script_code_formatted = script_code.format(sun_altitude_angle=sun_altitude_angle, precipitation=precipitation, fog_density=fog_density)
    
    with open("manual_weather_script.py", "w") as f:
      f.write(script_code_formatted)

    try:
      subprocess.run(["python", "manual_weather_script.py"]) 
    except KeyboardInterrupt:
      pass
    finally:
      os.remove("manual_weather_script.py")