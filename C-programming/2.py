from turtle import position
from ursina import *
import math

# Planet data dictionary
planet_data = {
    'Mercury': {
        'distance': '57.9 million km',
        'diameter': '4,879 km',
        'orbital_period': '88 days',
        'rotation_period': '59 days',
        'moons': '0',
        'description': 'The smallest and closest planet to the Sun'
    },
    'Venus': {
        'distance': '108.2 million km',
        'diameter': '12,104 km',
        'orbital_period': '225 days',
        'rotation_period': '243 days',
        'moons': '0',
        'description': 'The hottest planet with a thick toxic atmosphere'
    },
    'Earth': {
        'distance': '149.6 million km',
        'diameter': '12,742 km',
        'orbital_period': '365.25 days',
        'rotation_period': '24 hours',
        'moons': '1 (Moon)',
        'description': 'Our home planet, the only known planet with life'
    },
    'Mars': {
        'distance': '227.9 million km',
        'diameter': '6,779 km',
        'orbital_period': '687 days',
        'rotation_period': '24.6 hours',
        'moons': '2 (Phobos, Deimos)',
        'description': 'The Red Planet with the largest volcano in the solar system'
    },
    'Jupiter': {
        'distance': '778.5 million km',
        'diameter': '139,820 km',
        'orbital_period': '11.86 years',
        'rotation_period': '9.9 hours',
        'moons': '95+',
        'description': 'The largest planet with a massive storm called the Great Red Spot'
    },
    'Saturn': {
        'distance': '1.43 billion km',
        'diameter': '116,460 km',
        'orbital_period': '29.46 years',
        'rotation_period': '10.7 hours',
        'moons': '146+',
        'description': 'Famous for its spectacular ring system'
    },
    'Uranus': {
        'distance': '2.87 billion km',
        'diameter': '50,724 km',
        'orbital_period': '84 years',
        'rotation_period': '17.2 hours',
        'moons': '27',
        'description': 'Rotates on its side and orbits anti-clockwise (retrograde)'
    },
    'Neptune': {
        'distance': '4.50 billion km',
        'diameter': '49,244 km',
        'orbital_period': '164.8 years',
        'rotation_period': '16.1 hours',
        'moons': '14',
        'description': 'The windiest planet in the solar system'
    },
    'Pluto': {
        'distance': '5.91 billion km',
        'diameter': '2,377 km',
        'orbital_period': '248 years',
        'rotation_period': '6.4 days',
        'moons': '5 (Charon, Nix, Hydra, Kerberos, Styx)',
        'description': 'A dwarf planet in the Kuiper Belt'
    },
    'Sun': {
        'distance': '0 km (Center)',
        'diameter': '1,391,000 km',
        'composition': 'Hydrogen and Helium',
        'surface_temp': '5,500°C',
        'core_temp': '15 million°C',
        'description': 'The star at the center of our solar system'
    }
}

# Global variable to track selected planet
selected_planet = None
info_panel = None

def create_info_panel():
    """Creates an information panel to display planet details"""
    panel = Entity(
        model='quad',
        scale=(0.4, 0.3),
        color=color.rgba(0, 0, 0, 200),
        position=window.top_left + Vec3(0.22, -0.2, 0),
        parent=camera.ui,
        enabled=False
    )
    
    # Title text
    panel.title_text = Text(
        parent=panel,
        text='',
        position=(-0.18, 0.12),
        scale=2,
        origin=(-0.5, 0),
        color=color.yellow
    )
    
    # Info text
    panel.info_text = Text(
        parent=panel,
        text='',
        position=(-0.18, 0.08),
        scale=2,
        origin=(-0.5, 0.5),
        color=color.white
    )
    
    return panel

def show_planet_info(planet_name):
    """Display information about the selected planet"""
    global info_panel
    
    if planet_name in planet_data:
        data = planet_data[planet_name]
        info_panel.enabled = True
        info_panel.title_text.text = planet_name
        
        # Format the information text
        info_text = f"Distance from Sun: {data['distance']}\n"
        info_text += f"Diameter: {data['diameter']}\n"
        
        if 'orbital_period' in data:
            info_text += f"Orbital Period: {data['orbital_period']}\n"
            info_text += f"Rotation Period: {data['rotation_period']}\n"
            info_text += f"Moons: {data['moons']}\n"
        elif 'composition' in data:
            info_text += f"Composition: {data['composition']}\n"
            info_text += f"Surface Temp: {data['surface_temp']}\n"
        
        info_text += f"\n{data['description']}"
        
        info_panel.info_text.text = info_text

def hide_planet_info():
    """Hide the information panel"""
    global info_panel
    info_panel.enabled = False

def update():
    global t
    t = t + 0.01  
    angle = math.pi * 40 / 180  

    # ORBITAL MOTION: Using circular motion formulas
    radius_1 = 2
    mercury.x = math.cos(t) * radius_1
    mercury.z = math.sin(t) * radius_1

    radius_2 = 2.8
    venus.x = math.cos(t + angle) * radius_2
    venus.z = math.sin(t + angle) * radius_2
    
    radius_3 = 3.6
    earth.x = math.cos(-t + angle * 2) * radius_3
    earth.z = math.sin(-t + angle * 2) * radius_3
    
    radius_4 = 4.4
    mars.x = math.cos(t + angle * 3) * radius_4
    mars.z = math.sin(t + angle * 3) * radius_4

    radius_5 = 6.0
    jupiter.x = math.cos(t + angle * 4) * radius_5
    jupiter.z = math.sin(t + angle * 4) * radius_5
    
    radius_6 = 7.2
    saturn.x = math.cos(t + angle * 5) * radius_6
    saturn.z = math.sin(t + angle * 5) * radius_6
    
    # URANUS: Anti-clockwise motion (negative angle)
    radius_7 = 8.6
    uranus.x = math.cos(-t + angle * 6) * radius_7  # Note the negative t
    uranus.z = math.sin(-t + angle * 6) * radius_7
    
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
    
    # Highlight selected planet
    if selected_planet:
        # Add a subtle pulsing glow effect
        glow_scale = 1 + 0.1 * math.sin(time.time() * 3)
        if hasattr(selected_planet, 'original_scale'):
            selected_planet.scale = selected_planet.original_scale * glow_scale

def input(key):
    """Handle mouse wheel for zooming and ESC to close info panel"""
    if key == 'scroll up':
        camera.z += 2
    elif key == 'scroll down':
        camera.z -= 2
    elif key == 'escape':
        hide_planet_info()

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

def make_planet_clickable(planet, name):
    """Makes a planet clickable and stores its name"""
    planet.name = name
    planet.collider = 'sphere'
    planet.original_scale = planet.scale
    
    def on_click():
        global selected_planet
        # Deselect previous planet
        if selected_planet and selected_planet != planet:
            selected_planet.scale = selected_planet.original_scale
        
        selected_planet = planet
        show_planet_info(name)
        print(f"Clicked on {name}")
    
    planet.on_click = on_click
    
    def on_mouse_enter():
        if planet != selected_planet:
            planet.scale = planet.original_scale * 1.1
        mouse.visible = True
    
    def on_mouse_exit():
        if planet != selected_planet:
            planet.scale = planet.original_scale
    
    planet.on_mouse_enter = on_mouse_enter
    planet.on_mouse_exit = on_mouse_exit

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

# CREATE CELESTIAL BODIES
# Sun doesn't need lighting effects
sun = Entity(
    model='sphere', 
    scale=3, 
    texture='textures/2k_sun.jpg',
    unlit=True  # Sun emits light, doesn't receive it
)

# Create planets
mercury = Entity(model='sphere', scale=0.38, texture='textures/2k_mercury.jpg')
venus = Entity(model='sphere', scale=0.95, texture='textures/2k_venus_surface.jpg')
earth = Entity(model='sphere', scale=1.00, texture='textures/2k_earth_daymap.jpg')
mars = Entity(model='sphere', scale=0.53, texture='textures/2k_mars.jpg')
jupiter = Entity(model='sphere', scale=2.5, texture='textures/2k_jupiter.jpg')
saturn = Entity(model='sphere', scale=2.00, texture='textures/2k_saturn.jpg')
uranus = Entity(model='sphere', scale=1.4, texture='textures/2k_uranus.jpg')
neptune = Entity(model='sphere', scale=1.3, texture='textures/2k_neptune.jpg')
pluto = Entity(model='sphere', scale=0.28, texture='textures/plutomap1k.jpg')

# Make all planets clickable
make_planet_clickable(sun, 'Sun')
make_planet_clickable(mercury, 'Mercury')
make_planet_clickable(venus, 'Venus')
make_planet_clickable(earth, 'Earth')
make_planet_clickable(mars, 'Mars')
make_planet_clickable(jupiter, 'Jupiter')
make_planet_clickable(saturn, 'Saturn')
make_planet_clickable(uranus, 'Uranus')
make_planet_clickable(neptune, 'Neptune')
make_planet_clickable(pluto, 'Pluto')

# CREATE SATURN'S RING WITH TEXTURE
saturn_ring = create_saturn_ring_with_texture()

# CREATE ORBITS WITH DIRECT COLOR NAMES
orbit_mercury = create_orbit(2, color.gray, 2)
orbit_venus   = create_orbit(2.8, color.orange, 2)
orbit_earth   = create_orbit(3.6, color.blue, 2)
orbit_mars    = create_orbit(4.4, color.red, 2)
orbit_jupiter = create_orbit(6.0, color.brown, 2)
orbit_saturn  = create_orbit(7.2, color.yellow, 2)
orbit_uranus  = create_orbit(8.6, color.cyan, 2)
orbit_neptune = create_orbit(10.2, color.azure, 2)
orbit_pluto   = create_orbit(11.8, color.light_gray, 2)

# Create the info panel
info_panel = create_info_panel()

# Instructions text
instructions = Text(
    text='Click planets for info | WASD: Move | QE: Zoom | ESC: Close info',
    position=window.top_left + Vec3(0.02, -0.02, 0),
    scale=1,
    origin=(-0.5, 0.5),
    background=True
)

# Initialize time variable for orbital motion
t = -math.pi

# Set initial camera position
camera.position = (0, 15, -25)
camera.rotation_x = 30

# Start the application
app.run()