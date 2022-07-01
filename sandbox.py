import pgzrun
import random
import pygame
HEIGHT = 500
WIDTH = 1000
#____________________________________
pygame.mouse.set_visible(False)
wood_blocks = []
stone_blocks = []
dirt_blocks = []
water_blocks = []
grass_blocks = []
eaters = []
human_blocks = []
prey = []
animals = []
houses = []
elfHut = []
seas = []
forests = []
mountains =[]
HardDirt = []
leafs = []
elf_blocks = []
pop_blocks = []
fire_blocks = []
ice_blocks = []
lake_blocks = []
dragon_blocks = []
idragon_blocks = []
#____________________________________
humans_wood = 0
humans_stone = 0
food = 0
humans_water = 0
#____________________________________
elf_wood = 0
elf_stone = 0
elf_food = 0
elf_water = 0
beep = tone.create('C4', 0.1)
#____________________________________
cursor = Actor("cursor")
#____________________________________
def on_mouse_move(pos):
    cursor.pos = pos
#____________________________________cursor move
music.play('theme')
    
#____________________________________element code
def draw():
    
    global humans_wood
    global humans_stone
    global food
    global humans_water
    global elf_food
    global elf_water
    global elf_wood
    global elf_stone
    screen.fill("sky blue")
    cursor.draw()
    screen.draw.text("Human Wood: " + str(humans_wood) + " Human Stone: " + str(humans_stone) + " Human houses: " + str(len(houses)), topleft=(0,10),color=(255,255,255))
    screen.draw.text(" Elf Stone: " + str(elf_stone) + " Elf Houses: " + str(len(elfHut)), topleft=(0,30),color=(255,255,255))
    screen.draw.text("Human Food: " + str(food) + " Human Water: " + str(humans_water), topright=(WIDTH-20,10),color=(255,255,255))
    screen.draw.text("Elf Food: " + str(elf_food) + " Elf Water: " + str(elf_water), topright=(WIDTH-20,30),color=(255,255,255))
    #---------------------------------wood.basic
    for wood in wood_blocks:
        wood.draw()
        if len(fire_blocks) != 0:
            if wood.collidepoint(fire_blocks[0].pos):
                wood_blocks.remove(wood)
        if wood.y < HEIGHT - 30:
            wood.y += .5
        if random.randint(1,1000) == 50:
            elf = Actor("elf")
            elf_blocks.append(elf)
            elf.pos = wood.pos
            leaf = Actor("leaf")
            leafs.append(leaf)
            leaf.x = wood.x
            leaf.y = wood.y - 16
    
    #---------------------------------stone.basic
    for stone in stone_blocks:
        stone.draw()
        if len(fire_blocks) != 0:
            if stone.collidepoint(fire_blocks[0].pos):
                stone_blocks.remove(stone)
        if stone.y < HEIGHT - 30:
            stone.y += .5

    for leaf in leafs:
        leaf.draw()
        if len(fire_blocks) != 0:
            if leaf.collidepoint(fire_blocks[0].pos):
                leafs.remove(leaf)
        if leaf.y < HEIGHT - 46:
            leaf.y += .5
    #--------------------------------ground
    for dirt in dirt_blocks:
        dirt.draw()
        if len(fire_blocks) != 0:
            if dirt.collidepoint(fire_blocks[0].pos):
                dirt_blocks.remove(dirt)
        if dirt.y < HEIGHT - 10:
            dirt.y += .5
            grassed = False
            if random.randint(1,100) == 4 and grassed == False:
                grass = Actor("grass")
                grass_blocks.append(grass)
                grass.x = dirt.x
                grass.y = dirt.y - 5
                grassed = True
                
    for dirt in HardDirt:
        dirt.draw()
        if dirt.y < HEIGHT - 10:
            dirt.y += .5
    #--------------------------------water.basic
    for water in water_blocks:
        water.draw()
        if water.y < HEIGHT - 18:
            water.y += .5
    #--------------------------------water.lake
    for lake in lake_blocks:
        lake.draw()
        if lake.y < HEIGHT - 10:
            lake.y += .5
#___________________________fire block
    for poper in pop_blocks:
        poper.draw()
        if poper.y < HEIGHT - 18:
            poper.y += .5
        if len(fire_blocks) != 0:
            if poper.collidepoint(fire_blocks[0].pos):
                pop_blocks.remove(poper)
                
        
#___________________________fire block
    for fire in fire_blocks:
        fire.draw()
        if fire.y < HEIGHT - 18:
            fire.y += .9
        else:
            del fire_blocks[0]
        
#___________________________fire block
    for ice in ice_blocks:
        ice.draw()
        if ice.y > HEIGHT - 400:
            ice.y -= .5
        else:
            del ice_blocks[0]
            
    #--------------------------------grass
    for grass in grass_blocks:
        grass.draw()
        if len(fire_blocks) != 0:
            if grass.collidepoint(fire_blocks[0].pos):
                grass_blocks.remove(grass)
        if grass.y < HEIGHT - 18:
            grass.y += .5
        spawn= random.randint(1,50000)
        if spawn == 10:
            sheep = Actor("fox")
            animals.append(sheep)
            sheep.x = grass.x
            sheep.y = grass.y - 10
        elif spawn == 20:
            if len(eaters) < 3:
                fox = Actor("fox")
                eaters.append(fox)
                fox.x = grass.x
                fox.y = grass.y - 10
        elif spawn == 30:
            chicken = Actor("chicken")
            prey.append(chicken)
            chicken.x = grass.x
            chicken.y = grass.y - 10
        elif spawn == 40:
            human = Actor("human")
            human_blocks.append(human)
            human.x = grass.x
            human.y = grass.y - 10
        elif spawn == 50:
            wood = Actor("wood")
            wood_blocks.append(wood)
            wood.x = grass.x
            wood.y = grass.y - 10
        elif spawn == 60:
            stone = Actor("stone")
            stone_blocks.append(stone)
            stone.x = grass.x
            stone.y = grass.y - 10
        rain= random.randint(1,5000)
        if rain == 10:
            water = Actor("rain")
            water_blocks.append(water)
            water.x = random.randint(1,1000)
            water.y = 80
     #--------------------------------animal.hunt_True
    for fox in eaters:
        fox.draw()
        if fox.y < HEIGHT - 30:
            fox.y += .5
        move = random.randint(-1,2)
        if move == 0:
            fox.x += .9
        elif move == 1:
            fox.x -= .9
        if len(prey) > 0:
            eat_or_meet = random.randint(1,1000)
            if  eat_or_meet == 5:
                del prey[0]
                
     #--------------------------------humanoide
    for human in human_blocks:
        human.draw()
        if len(fire_blocks) != 0:
            if human.collidepoint(fire_blocks[0].pos):
                human_blocks.remove(human)
        if  human.y < HEIGHT - 30:
            human.y += .5
        moves = random.randint(-1,2)
        if moves == 0:
            human.x += .9
        elif moves == 1:
            human.x -= .9
        action =  random.randint(1,100)
        if action == 1:
            if len(prey) > 0:
                food += 1
                del prey[0]
        elif action == 2:
            if len(water_blocks) > 0:
                humans_water += 1
                del water_blocks[0]
        else:
            if food > 0:
                if humans_water > 0:
                    if random.randint(-1,2) == 0:
                        if len(wood_blocks) > 0:
                            humans_wood += 1
                            del wood_blocks[0]
                            if len(leafs) > 0:
                                del leafs[0]
                            food -= 1
                            humans_water  -= 2
                    else:
                        if len(stone_blocks) > 0 and len(stone_blocks) < 100:
                            humans_stone += 1
                            del stone_blocks[0]
                            food -= 1
                            humans_water -= 2
            if humans_stone > 9 and humans_wood > 9:
                house = Actor("house")
                houses.append(house)
                house.pos = human.pos
                humans_wood -= 10 
                humans_stone -= 10
   #--------------------------------elf          
    for elf in elf_blocks:
        elf.draw()
        if  elf.y < HEIGHT - 30:
            elf.y += .5
        moves = random.randint(-1,2)
        if moves == 0:
            elf.x += .9
        elif moves == 1:
            elf.x -= .9
        elfaction =  random.randint(1,100)
        if elfaction == 1:
            if len(prey) > 0:
                elf_food += 1
                del prey[0]
        elif elfaction == 2:
            if len(water_blocks) > 0:
                elf_water += 1
                del water_blocks[0]
        else:
            if elf_food > 0:
                if elf_water > 0:
                        if len(stone_blocks) > 0:
                            elf_stone += 1
                            del stone_blocks[0]
                            elf_food -= 1
                            elf_water -= 2
            if elf_stone > 9:
                if len(wood_blocks) > 0:
                    hut = Actor("elfhut")
                    elfHut.append(hut)
                    hut.pos = wood_blocks[0].pos
                    elf_stone -= 10
                    del wood_blocks[0]
                    if len(leafs) > 0:
                                del leafs[0]


 
#---------------------------------------------------------------Hearts
    for sea in seas:
        sea.draw()
        if random.randint(1,100) == 100:
            water = Actor("water")
            water_blocks.append(water)
            water.y = sea.y
            water.x =   random.randint(sea.x - 32,sea.x + 32)

        
    for forest in forests:
        forest.draw()
        if random.randint(1,100) == 100:
            wood = Actor("wood")
            wood_blocks.append(wood)
            wood.pos = forest.pos
            wood.y = forest.y
            wood.x =   random.randint(wood.x - 32,wood.x + 32)
        
    for mountain in mountains:
        mountain.draw()        
        if random.randint(1,100) == 100:
            stone = Actor("stone")
            stone_blocks.append(stone)
            stone.pos = mountain.pos
            stone.y = mountain.y
            stone.x =   random.randint(stone.x - 32,stone.x + 32)
    #----------------------------prey
    for preys in prey:
        preys.draw()
        if preys.y < HEIGHT - 30:
            preys.y += .5
        movess = random.randint(-1,2)
        if movess == 0:
            preys.x += .9
        elif movess == 1:
            preys.x -= .9
        meet = random.randint(1,500)
        if meet == 10:
            chicken = Actor("chicken")
            prey.append(chicken)
            chicken.pos = preys.pos
    #--------------------------------anamal of peace
    for sheep in animals:
        sheep.draw()
        if sheep.y < HEIGHT - 30:
            sheep.y += .5
        smove = random.randint(-1,2)
        if smove == 0:
            sheep.x += .9
        elif smove == 1:
            sheep.x -= .9

    #--------------------------------dragons!
    for dragon in dragon_blocks:
        dragon.draw()
        if len(ice_blocks) != 0:
            if dragon.collidepoint(ice_blocks[0].pos):
                dragon_blocks.remove(dragon)
        if dragon.y > HEIGHT - 400:
            dragon.y -= .5
        smove = random.randint(-1,2)
        if smove == 0:
            dragon.x += .9
        elif smove == 1:
            dragon.x -= .9
        do = random.randint(1,200)
        if do == 2:
            fire = Actor("fire")
            fire_blocks.append(fire)
            fire.pos = dragon.pos
    #--------------------------------dragons!
    for idragon in idragon_blocks:
        idragon.draw()
        if len(fire_blocks) != 0:
            if idragon.collidepoint(fire_blocks[0].pos):
                idragon_blocks.remove(idragon)
        if idragon.y < HEIGHT - 30:
            idragon.y += .5
        smove = random.randint(-1,2)
        if smove == 0:
            idragon.x += .9
        elif smove == 1:
            idragon.x -= .9
        ices = random.randint(1,200)
        if ices == 2:
            ice = Actor("ice")
            ice_blocks.append(ice)
            ice.pos = idragon.pos
    #------------------------------------house
    for home in houses:
        home.draw()
        if len(fire_blocks) != 0:
            if home.collidepoint(fire_blocks[0].pos):
                houses.remove(home)
        if home.y < HEIGHT - 30:
            home.y += .5
        do = random.randint(1,100)
        if do == 50:
             human = Actor("human")
             human_blocks.append(human)
             human.pos = home.pos
        elif do == 70:
            food += 10
        elif do == 20:
            humans_water += 10

    #------------------------------------elfhut
    for hut in elfHut:
        hut.draw()
        if len(fire_blocks) != 0:
            if hut.collidepoint(fire_blocks[0].pos):
                elfHut.remove(hut)
        if hut.y < HEIGHT - 30:
            hut.y += .5
        do = random.randint(1,100)
        if do == 50:
             elf = Actor("elf")
             elf_blocks.append(elf)
             elf.pos = hut.pos
        elif do == 70:
            elf_food += 10
        elif do == 20:
            elf_water += 10
#
#____________________________________element add
def update():

        
    #________________________________
    if len(eaters) > 25:
        del eaters[-1]
        
    if len(fire_blocks) > 5:
        del fire_blocks[-1]
    if len(ice_blocks) > 5:
        del ice_blocks[-1]
    #________________________________
    if keyboard.K_3:
        wood = Actor("wood")
        wood_blocks.append(wood)
        wood.pos = cursor.pos
        #-------------------------------wood
    if keyboard.K_4:
        stone = Actor("stone")
        stone_blocks.append(stone)
        stone.pos = cursor.pos
        #-------------------------------stone
    if keyboard.K_1:
        dirt = Actor("dirt")
        dirt_blocks.append(dirt)
        dirt.pos = cursor.pos
        #-------------------------------dirt
    if keyboard.K_2:
        water = Actor("water")
        lake_blocks.append(water)
        water.pos = cursor.pos
        #-------------------------------water
    if keyboard.K_5:
        grass = Actor("grass")
        grass_blocks.append(grass)
        grass.pos = cursor.pos
        #-------------------------------grass
    if keyboard.K_6:
        fox = Actor("fox")
        eaters.append(fox)
        fox.pos = cursor.pos
        #-------------------------------fox
    if keyboard.K_7:
        human = Actor("human")
        human_blocks.append(human)
        human.pos = cursor.pos
        #-------------------------------human
    if keyboard.K_8:
       sheep = Actor("sheep")
       animals.append(sheep)
       sheep.pos = cursor.pos
        #-------------------------------sheep
    if keyboard.K_9:
       chicken = Actor("chicken")
       prey.append(chicken)
       chicken.pos = cursor.pos
        #-------------------------------chicken
    if keyboard.q:
       sea = Actor("sea")
       seas.append(sea)
       sea.pos = cursor.pos
        #-------------------------------heart of the sea
    if keyboard.w:
       forest = Actor("forest")
       forests.append(forest)
       forest.pos = cursor.pos
        #-------------------------------heart of the forest
    if keyboard.e:
       mountain = Actor("mount")
       mountains.append(mountain)
       mountain.pos = cursor.pos
        #-------------------------------heart of the mountans
    if keyboard.K_0:
       elf = Actor("elf")
       elf_blocks.append(elf)
       elf.pos = cursor.pos
        #-------------------------------elf
    if keyboard.o:
       pop = Actor("dirt")
       pop_blocks.append(pop)
       pop.pos = cursor.pos
        #-------------------------------elf

    if keyboard.p:
       fire = Actor("fire")
       fire_blocks.append(fire)
       fire.pos = cursor.pos
        #-------------------------------elf
    if keyboard.r:
       dragon = Actor("dragon")
       dragon_blocks.append(dragon)
       dragon.pos = cursor.pos
        #-------------------------------elf
    if keyboard.t:
       idragon = Actor("icedragon")
       idragon_blocks.append(idragon)
       idragon.pos = cursor.pos
        #-------------------------------elf
    if keyboard.BACKQUOTE:
       hard = Actor("dirt")
       HardDirt.append(hard)
       hard.pos = cursor.pos
    if keyboard.l:
        if len(human_blocks) > 0:
            del human_blocks[0]
        elif len(eaters) > 0:
            del eaters[0]
        elif len(prey) > 0:
            del prey[0]
        elif len(animals) > 0:
            del animals[0]
    if keyboard.q:
        if len(prey) > 0:
            del prey[0]
    if keyboard.b:
        human_blocks.clear()
        eaters.clear()
        animals.clear()
        prey.clear()
        elf_blocks.clear()
        idragon_blocks.clear()
        dragon_blocks.clear()
    if keyboard.c:
        human_blocks.clear()
pgzrun.go()
