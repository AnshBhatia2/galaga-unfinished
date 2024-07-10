import pgzrun

HEIGHT = 700
WIDTH = 1200

white = (255,255,255)
blue = (0,0,255)

score = 0
direction = 1
enemies = []
bullets = []
speed = 5

ship = Actor("galaga")
ship.pos = (WIDTH // 2,HEIGHT - 60)
ship.dead = False
ship.countdown = 90

for x in range(8):
    for y in range(4):
        e = Actor("bug")
        enemies.append(e)
        enemies[-1].x = 100+ 50*x
        enemies[-1].y = 80+ 50*y

def game_over():
    screen.draw.text("GAME OVER", (250,350))

def display_score():
    screen.draw.text(str(score), (50,30))

def on_key_down(key):
    if ship.dead == False:
        if key == keys.SPACE:
            bullet = Actor("bullet")
            bullets.append(bullet)
            bullets[-1].x = ship.x
            bullets[-1].y = ship.y - 50

def draw():
    screen.clear()
    screen.fill(blue)
    if ship.dead == False:
        ship.draw()
    for enemy in enemies:
        enemy.draw()
    if len(enemies) == 0:
        game_over()


def update():
    pass

pgzrun.go()