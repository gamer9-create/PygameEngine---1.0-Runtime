import random

def makeBlock(table=None,on=None):
    blockProperties = []
    position = (0,0)
    size = (0,0)

    position = [random.randint(1,90),random.randint(1,30)]
    size = [50,50]
    blockProperties.append(position)
    blockProperties.append(size)
    return blockProperties
def load_world(world):
    return world.o
def makeWorld(worldData, worldNum):
    f = open(f"C:\\users\lalit\\PycharmProjects\\WorldSystem\\generate_files\\world.py", "w")
    f.write(f"o = {worldData}")
    f.close()
    return worldData
def make_world():
    world = []
    for r in range(50, 100):
        block =None
        if not r <= 1:
            block = makeBlock()
        else:
            block = makeBlock(world)
        append = True
        for worl in world:
            if worl:
                if worl[0][0] == block[0][0] and worl[0][1] == block[0][1]:
                    append = False
        block1 = makeBlock()
        block1[0][0] = block[0][0]*2
        block1[0][1] = block[0][1]
        if append:
            world.append(block)
            world.append(block1)
    return world












