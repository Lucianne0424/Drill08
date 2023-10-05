from pico2d import *
import random

# Game object class here

class Grass:
    def __init__(self):  # 생성자 함수 - 객체가 생성될 때 자동으로 호출되는 함수 - / self : 생성된 객체 자신을 가르키는 변수
        self.image = load_image('grass.png')

    def draw(self):  # 멤버 함수 첫번째는 항상 self이어야 함.
        self.image.draw(400, 30)

    def update(self):  # 잔디의 변화가 없어도 이걸 만든 이유가 있다고 함.
        pass


class Boy:
    def __init__(self):
        self.x, self.y = random.randint(100,700), 90
        self.frame = random.randint(0,7)
        self.image = load_image('run_animation.png')

    def update(self):
        self.frame = (self.frame + 1) % 8
        self.x += 5

    def draw(self):
        self.image.clip_draw(self.frame * 100, 0, 100, 100, self.x, self.y)

class Ball:
    def __init__(self):
        if random.randint(0,1) == 0:
            self.image = load_image('ball21x21.png')
        else:
            self.image = load_image('ball41x41.png')

        self.x, self.y = random.randint(0,800), 599
        self.speed = random.randint(1,10)

    def update(self):
        if self.y > 60:
            self.y -= self.speed
        else:
            self.y = 60

    def draw(self):
        self.image.draw(self.x, self.y)



def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            running = False


def reset_world():
    global running
    global grass
    global team
    global balls
    global world
    running = True
    world = []
    grass = Grass()
    world.append(grass)

    team = [Boy() for i in range(11)]
    world += team

    balls = [Ball() for i in range(20)]
    world += balls


def render_world():
    clear_canvas()
    for o in world:
        o.draw()
    update_canvas()


def update_world():
    for o in world:
        o.update()
    pass


open_canvas()

# initialization code
reset_world()

# game main loop code
while running:
    handle_events()
    update_world()
    render_world()
    delay(0.05)

# finalization code

close_canvas()
