import random

class Turtle:
    energy = 50
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    def __init__(self, name):
        self.name = name

    def moving(self):
        move = random.choice([-2,-1,1,2])
        direction = random.choice(['x','y'])
        print('Turtle{0} move {1}, on {2}'.format(self.name, move, direction))
        if direction == 'x':
            position = self.x + move
            if 0 <= position <= 10:
                self.x += move
            elif position < 0:
                self.x = - (self.x + move)
            elif position > 10:
                self.x = 10 + (10 - (self.x + move))

        if direction == 'y':
            position = self.y + move
            if 0 <= position <= 10:
                self.y += move
            elif position < 0:
                self.y = - (self.y + move)
            elif position > 10:
                self.y = 10 + (10 - (self.y + move))


        self.energy -= 1
        print('Turtle{0} Position: x={1}, y={2}, energy={3}, '.format(self.name,self.x, self.y, self.energy))


class Fish:
    x = random.randint(0, 10)
    y = random.randint(0, 10)

    def __init__(self, name):
        self.name = name

    def moving(self):
        move = random.choice([-1, 1])
        direction = random.choice(['x','y'])
        if direction == 'x':
            position = self.x + move
            if 0 <= position <= 10:
                self.x += move
            elif position < 0:
                self.x = - (self.x + move)
            elif position > 10:
                self.x = 10 + (10 - (self.x + move))

        if direction == 'y':
            position = self.y + move
            if 1 <= position <= 10:
                self.y += move
            elif position < 0:
                self.y = - (self.y + move)
            elif position > 10:
                self.y = 10 + (10 - (self.y + move))

        print('Fish{0} Position: x={1}, y={2}'.format(self.name, self.x, self.y))


class Pool:
    def __init__(self, turtle_num=2, fish_num=10):
        self.turtle_num = turtle_num
        self.fish_num = fish_num
        self.turtle_list = []
        for i in range(self.turtle_num):
            self.turtle_list.append(Turtle(str(i+1)))
        self.fish_list = []
        for i in range(self.fish_num):
            self.fish_list.append(Fish(str(i+1)))


pool = Pool(3,10)


while len(pool.turtle_list) > 0 and len(pool.fish_list) > 0:
    for each in pool.turtle_list:
        if each.energy > 0:
            each.moving()

        else:
            pool.turtle_list.remove(each)
            print('Turtle{0} have no energy!!!!'.format(each.name))

    for eachfish in pool.fish_list:
        eachfish.moving()
        for eachturtle in pool.turtle_list:
            if eachfish.x == eachturtle.x and eachfish.y == eachturtle.y:
                print('Turtle{0} catch Fish{1}!! It get 20 energy!!!'.format(eachturtle.name,eachfish.name))
                eachturtle.energy += 20
                pool.fish_list.remove(eachfish)

if len(pool.fish_list) == 0:
    print('There is no fish!! Game Over!!')


if len(pool.turtle_list) == 0:
    print('The turtles have no energy!! Game Over!!!')





#日志：
    #6月写的L37_t1_turtle.py.作业里，乌龟和10个fish的类对象都是手动建立的。
    #10月改进时增加的池子类，可以将乌龟和鱼的初始化在建立池对象的同时完成，
    #而在池子里发生的事件不需要对象的名称，所以不用纠结变量名的可视化，
    #把对象放进列表里迭代即可
