
import carla

client = carla.Client('localhost', 2000)
client.set_timeout(5.0)
world = client.get_world()

spectator = world.get_spectator()
spectator_transform = spectator.get_transform()

prop_distance = 3 
prop_location = spectator_transform.location + (spectator_transform.get_forward_vector() * prop_distance)

prop_location.z = 0

prop_blueprint = world.get_blueprint_library().find('static.prop.briefcase')

prop_transform = carla.Transform(prop_location)

prop_actor = world.spawn_actor(prop_blueprint, prop_transform)

print(str(prop_actor.id) + "-" + prop_actor.type_id)
