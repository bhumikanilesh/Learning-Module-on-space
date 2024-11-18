from ursina import *
from info import *

able_text = True

def sol_info():
    
    app = Ursina(borderless=False)

    window.title = 'Ursina Solar System Simulation'
    window.fps_counter.enabled = False
    fps = 60
    window.fps_counter.max = 60
    
    window.exit_button.enabled=True
    
    music = Audio(sound_file_name='hb/music.mp3', loop=True, autoplay=True, volume=2)
    
    able_text = True

    class Planet(Entity):
   
        def __init__(self, x, y, z, s, texture, name):
            
            
            super().__init__()
            self.model = 'sphere'
            self.collider = 'sphere'
            self.x = x
            self.y = y
            self.z = z
            self.scale = s
            self.texture = texture
            self.name = name

        
        def input(self, key):
            def text_abler():
                global able_text
                able_text = True
            global able_text

            if self.hovered and able_text:
                name_text = Text(text=self.name,scale=0.75,font='pixel.ttf',resolution=100*Text.size)
                able_text = False
                name_text.appear(speed=0.01)
                destroy(name_text, delay=18)
                invoke(text_abler, delay=18)
                
                
    
    
    sun = Planet(0, 0, 0,280,'hb/sun.jpg',name=Sun_info)
    
    earth = Planet(370,0,0, 10, 'hb/earth.jpg',Earth_info)
    
    mars = Planet(430,20,0, 6, 'hb/mars.jpg',Mars_info)
    
    mercury = Planet(250,-30,0,5,'hb/mercury.jpg',Mercury_info)
    
    venus = Planet(300,0,0, 10, 'hb/venus.jpg',Venus_info)
    
    jupiter = Planet(570,0,100, 40, 'hb/jupiter.jpg',Jupiter_info)
    
    saturn = Planet(-680,0,450, 45, 'hb/saturn.jpg',Saturn_info)
    

    uranus = Planet(790,0,0,37.5, 'hb/uranus.jpg',Uranus_info)
    
    neptune = Planet(70,0,1000, 30, 'hb/neptune.jpg',Neptune_info)
        

    
    for i in range(0,11,5):
        
        rad=500-i
        x=500-i
        z=0
        while x>=0 and z!=rad:
            Asteroid=Entity(model='sphere',texture='hb/asteroid.jpg',scale=1.5,position=Vec3(x,0,z))
            x-=2
            z=math.sqrt(rad**2-x**2)
        while x>(-rad) and z!=0:
            Asteroid=Entity(model='sphere',texture='hb/asteroid.jpg',scale=1.5,position=Vec3(x,0,z))
            x-=2
            z=math.sqrt(rad**2-x**2)
        while x<0 and z!=(-rad):
            Asteroid=Entity(model='sphere',texture='hb/asteroid.jpg',scale=1.5,position=Vec3(x,0,z))
            x+=2
            z=-(math.sqrt(rad**2-x**2))
        while x<=rad and z!=0:
            Asteroid=Entity(model='sphere',texture='hb/asteroid.jpg',scale=1.5,position=Vec3(x,0,z))
            x+=2
            z=-(math.sqrt(rad**2-x**2))

        
    ring=Entity(model=load_model('hb/torusblend.obj'),scale=45)   
    ring.position=(-680,0,450)
    ring.scale_y=1
    ring.reparent_to(saturn)
    ring.rotation_x=45
    
        
    cam=EditorCamera()
    camera.position = Vec3(368,3,2)
    camera.clip_plane_far=60000
    cam.rotation_x=90
    bg=Sky()
    bg.texture='hb/space.png'

    app.run()
#sol_info()

