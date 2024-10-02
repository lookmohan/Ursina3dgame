from ursina import *
from ursina.prefabs.first_person_controller import FirstPersonController

app=Ursina()
for z in range(10):
    for x in range(10):
        Entity(
            model="cube",texture="white_cube",collider="box",ignore=True,color=color.dark_gray,
            position=(x,0,z),
            parent=scene,
            origin_y=0.5,
            #texture="white_cube"

            )
class TextureBox(Button):
    def __init__(self,position=(5,2,5)):
        super().__init__(
            parent=scene,
            position=position,model="cube",origin_y=0.5,
            texture="material_baseColor.jpeg",
            color=color.hsv(0,0,1)
            )
        self.texture_choice=0
        self.textures=['rentgf.jpg','mickey.jpg','tr.jpg','trm.jpg','boruto.jpg','guy.jpg','naruto.jpg']

    def input(self,key):
        if self.hovered:
            if key == "left mouse down":
                self.texture_choice+=1
                self.texture_choice%=len(self.textures)
                self.texture=self.textures[self.texture_choice]
TextureBox()

player=FirstPersonController()

app.run()
