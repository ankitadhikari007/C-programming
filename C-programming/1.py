from turtle import position
from ursina import *
import math

def update():
   
    global t
    t = t + 0.02  
    angle = math.pi * 40 / 180  

    # ORBITAL MOTION: Using circular motion formulas
    radius_1 = 2
    mercury.x = math.cos(t) * radius_1
    mercury.z = math.sin(t) * radius_1

    radius_2 = 2.8
    venus.x = math.cos(t + angle) * radius_2
    venus.z = math.sin(t + angle) * radius_2
    
    radius_3 = 3.6
    earth.x = math.cos(t + angle * 2) * radius_3
    earth.z = math.sin(t + angle * 2) * radius_3
    
    radius_4 = 4.4
    mars.x = math.cos(t + angle * 3) * radius_4
    mars.z = math.sin(t + angle * 3) * radius_4

    radius_5 = 6.0
    jupiter.x = math.cos(t + angle * 4) * radius_5
    jupiter.z = math.sin(t + angle * 4) * radius_5
    
    radius_6 = 7.2
    saturn.x = math.cos(t + angle * 5) * radius_6
    saturn.z = math.sin(t + angle * 5) * radius_6
    
    radius_7 = 8.6
    uranus.x = math.cos(t + angle * 6) * radius_7
    uranus.z = math.sin(t + angle * 6) * radius_7
    
    radius_8 = 10.2
    neptune.x = math.cos(t + angle * 7) * radius_8
    neptune.z = math.sin(t + angle * 7) * radius_8
    
    radius_9 = 11.8
    pluto.x = math.cos(t + angle * 8) * radius_9
    pluto.z = math.sin(t + angle * 8) * radius_9

    # Move Saturn's rings with Saturn
    saturn_ring.position = saturn.position
    saturn_ring.rotation_y += time.dt * 10
    
    # ROTATION: Make planets spin on their own axis
    sun.rotation_y += time.dt * 28
    mercury.rotation_y += time.dt * 20
    earth.rotation_y += time.dt * 20
    venus.rotation_y += time.dt * 20
    mars.rotation_y += time.dt * 20
    jupiter.rotation_y += time.dt * 20
    saturn.rotation_y += time.dt * 20
    uranus.rotation_y += time.dt * 20
    neptune.rotation_y += time.dt * 20
    pluto.rotation_y += time.dt * 20
    
    # CAMERA CONTROLS
    # Zoom in/out with mouse wheel or Q/E keys
    if held_keys['q'] or held_keys['scroll up']:
        camera.z += time.dt * 10
    if held_keys['e'] or held_keys['scroll down']:
        camera.z -= time.dt * 10
    
    # Move left/right with A/D keys
    if held_keys['a']:
        camera.x -= time.dt * 10
    if held_keys['d']:
        camera.x += time.dt * 10
    
    # Move up/down with W/S keys
    if held_keys['w']:
        camera.y += time.dt * 10
    if held_keys['s']:
        camera.y -= time.dt * 10

def input(key):
    """Handle mouse wheel for zooming"""
    if key == 'scroll up':
        camera.z += 2
    elif key == 'scroll down':
        camera.z -= 2

def create_orbit(radius, orbit_color=color.white, thickness=1):
    """Creates a circular orbit line to show planetary paths"""
    segments = 64
    points = []
    
    for i in range(segments + 1):
        angle = (i / segments) * 2 * math.pi
        x = math.cos(angle) * radius
        z = math.sin(angle) * radius
        points.append((x, 0, z))
    
    orbit = Entity(
        model=Mesh(vertices=points, mode='line', thickness=thickness),
        color=orbit_color,
        unlit=True
    )
    return orbit

def create_saturn_ring_with_texture():
    """Creates Saturn's ring with texture"""
    segments = 128
    inner_radius = 1.3
    outer_radius = 2.2
    vertices = []
    triangles = []
    uvs = []
    
    for i in range(segments + 1):
        angle = (i / segments) * 2 * math.pi
        
        # Inner vertex
        x_inner = math.cos(angle) * inner_radius
        z_inner = math.sin(angle) * inner_radius
        vertices.append((x_inner, 0, z_inner))
        uvs.append((0, i / segments))
        
        # Outer vertex
        x_outer = math.cos(angle) * outer_radius
        z_outer = math.sin(angle) * outer_radius
        vertices.append((x_outer, 0, z_outer))
        uvs.append((1, i / segments))
    
    # Create triangles
    for i in range(0, len(vertices) - 2, 2):
        triangles.append((i, i+1, i+2))
        triangles.append((i+1, i+3, i+2))
    
    ring_mesh = Mesh(vertices=vertices, triangles=triangles, uvs=uvs)
    
    ring = Entity(
        model=ring_mesh,
        texture='textures/2k_saturn_ring_alpha.png',
        double_sided=True,
        rotation_x=90,
        alpha=0.8
    )
    
    return ring

def create_planet_with_shader(model_name, scale, day_texture, has_night=False, night_texture=None):
    """Creates a planet with day-night shader effect"""
    
    # Create the main planet entity
    planet = Entity(
        model='sphere',
        scale=scale,
        texture=day_texture
    )
    
    if has_night and night_texture:
        # Create a shader that blends day and night textures based on light direction
        planet.shader = lit_with_shadows_shader
        
        # Create night side overlay
        night_side = Entity(
            model='sphere',
            scale=scale * 1.001,  # Slightly larger to avoid z-fighting
            texture=night_texture,
            parent=planet,
            alpha=0.5,
            shader=lit_with_shadows_shader
        )
        planet.night_side = night_side
    
    return planet

# Initialize the Ursina application
app = Ursina()

class Sky(Entity):
    """Creates a large sphere around the scene to show stars"""
    def __init__(self):
        super().__init__(
            model='sphere',
            texture='textures/2k_stars_milky_way.jpg',
            parent=scene,
            scale=150,
            double_sided=True
        )

# Create the starry sky
sky = Sky()

# FIXED LIGHT (shadows enabled)
sun_light = PointLight(
    parent=scene,
    position=(0, 0, 0),
    color=color.white,
    shadows=True
)
sun_light.intensity = 14
# ADD LIGHTING for day-night effect
# Main sun light
# sun_light = DirectionalLight()
# sun_light.look_at(Vec3(1, -1, 1))
# sun_light.color = color.rgb(255, 253, 250)
# sun_light.intensity = 10
# # Ambient light (soft overall illumination)
# ambient = AmbientLight(color=color.rgba(50, 50, 80, 50))

# CREATE CELESTIAL BODIES
# Sun doesn't need lighting effects
sun = Entity(
    model='sphere', 
    scale=3, 
    texture='textures/2k_sun.jpg',
    unlit=True  # Sun emits light, doesn't receive it
)

# Create planets with day-night effects
mercury = Entity(model='sphere', scale=0.38, texture='textures/2k_mercury.jpg')
venus = Entity(model='sphere', scale=0.95, texture='textures/2k_venus_surface.jpg')

# Earth with night lights
earth = Entity(model='sphere', scale=1.00, texture='textures/2k_earth_daymap.jpg')

mars = Entity(model='sphere', scale=0.53, texture='textures/2k_mars.jpg')
jupiter = Entity(model='sphere', scale=2.5, texture='textures/2k_jupiter.jpg')
saturn = Entity(model='sphere', scale=2.00, texture='textures/2k_saturn.jpg')
uranus = Entity(model='sphere', scale=1.4, texture='textures/2k_uranus.jpg')
neptune = Entity(model='sphere', scale=1.3, texture='textures/2k_neptune.jpg')
pluto = Entity(model='sphere', scale=0.28, texture='textures/plutomap1k.jpg')

# CREATE SATURN'S RING WITH TEXTURE
saturn_ring = create_saturn_ring_with_texture()

# CREATE ORBITS WITH DIRECT COLOR NAMES
orbit_mercury = create_orbit(2.2, color.gray, 2)
orbit_venus   = create_orbit(2.8, color.orange, 2)
orbit_earth   = create_orbit(3.6, color.blue, 2)
orbit_mars    = create_orbit(4.4, color.red, 2)
orbit_jupiter = create_orbit(6.0, color.brown, 2)
orbit_saturn  = create_orbit(7.2, color.yellow, 2)
orbit_uranus  = create_orbit(8.6, color.cyan, 2)
orbit_neptune = create_orbit(10.2, color.azure, 2)
orbit_pluto   = create_orbit(11.8, color.light_gray, 2)

# Initialize time variable for orbital motion
t = -math.pi

# Set initial camera position
camera.position = (0, 15, -25)
camera.rotation_x = 30

# Start the application
app.run()