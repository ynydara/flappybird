import pygame as p
import random
screenWidth = 340
screenHeight = 680
BLACK = (0, 0, 0)

class Pipe(p.sprite.Sprite):
    def __init__(self, x, height, is_upper=True):
        super().__init__()
        self.passed = False
        if is_upper:
            self.image = p.image.load("images\\top.png")
        else:
            self.image = p.image.load("images\\bottom.png")
        self.rect = self.image.get_rect()
        self.rect.x = x
        if is_upper:
            self.rect.y = height - self.rect.height
        else:
            self.rect.y = height

    def update(self,screen):
        self.rect.x -= 3
        if self.rect.right < 0:
            self.kill()

def generate_pipe_height(lastPipeHeight,lastPipeX):
    gap_height = 200
    min_height = 50
    max_height = screenHeight - gap_height - min_height
    new_height = random.randint(min_height, max_height)
    new_x = lastPipeX + random.randint(150, 300)
    while abs(new_height - lastPipeHeight) < 100 or abs(new_x - lastPipeX) < 150:
        new_height = random.randint(min_height, max_height)
        new_x = lastPipeX + random.randint(150, 300)

    return new_height, new_x

    
class Player(p.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.frames = [p.image.load("images\\birdR.png"),
                       p.image.load("images\\birdU.png"),
                       p.image.load("images\\birdD.png")]

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.x = x
        self.y = y
        self.animation_speed = 50
        self.clock = p.time.Clock()
        self.elapsed_time = 0
        self.gravity = 0.3
        self.speed = 30
        self.game_over_played = False
        self.score =0
       
    def update(self,screen):
        self.rect.y += 3 
        # self.rect.y += self.gravity 
        keys = p.key.get_pressed()
        if not self.game_over_played:
            if self.rect.y > 580 or (self.rect.y > 680):
                self.alive = False
                self.show_game_over_screen(screen)
                self.game_over_played = True
            # background_image = p.image.load('images\gameover.png')
            # screen.blit(background_image, (0, 0))
            # p.mixer.music.load("sounds\sfx_die.wav")
            # p.mixer.music.play(1)
           
            
        if (keys[p.K_SPACE]) or (keys[p.MOUSEBUTTONDOWN]):
            # print("?????")
            self.elapsed_time += self.clock.tick(60)
            if self.elapsed_time >= self.animation_speed:
                self.elapsed_time = 0
                self.frame_index = (self.frame_index + 1) % len(self.frames)
                self.rect.y -=100
                self.rect.y -= self.gravity
                self.image = self.frames[self.frame_index]
                p.mixer.music.load("sounds\sfx_wing.wav")
                p.mixer.music.play(1)
       
    def show_game_over_screen(self, screen):
        background_image = p.image.load('images\gameOverrre.png')
        screen.blit(background_image, (0, 0))
        p.mixer.music.load("sounds\sfx_die.wav")
        
        p.mixer.music.play()
            
def main():
    p.init()
    size = (screenWidth, screenHeight)
    screen = p.display.set_mode(size)
    p.display.set_caption("Alyssa's Flappy Bird")
    running = True
    clock = p.time.Clock()

    allSprites = p.sprite.Group()
    pipes = p.sprite.Group()
    animatedSprites = Player(100, 100)
    allSprites.add(animatedSprites)
    
    # lastPipeHeight = screenHeight // 2
    lastPipeHeight, lastPipeX = screenHeight // 2, screenWidth

    while running:
        for event in p.event.get():
            if event.type == p.QUIT:
                    running = False
            elif event.type == p.MOUSEBUTTONDOWN:
                animatedSprites.rect.y -=100
                p.mixer.music.load("sounds\sfx_wing.wav")
                p.mixer.music.play(1)
                # print(f"Mouse Click at ({event.pos[0]}, {event.pos[1]})")
        for event in p.event.get():
            if event.type == p.QUIT:
                running = False
        key = p.key.get_pressed()

        if key[p.K_ESCAPE]:
            running = False
       
        allSprites.update(screen)
        if p.time.get_ticks() % 120 == 0:
            pipe_height, pipe_x = generate_pipe_height(lastPipeHeight,lastPipeX)
            a = random.randint(0, 99)  
            if a % 3 == 0:
                a += 100
            a = random.randint(0,100)
            upper_pipe = Pipe(pipe_x, pipe_height, True)
            lower_pipe = Pipe(pipe_x, pipe_height + 200, False)
            pipes.add(upper_pipe, lower_pipe)
            allSprites.add(upper_pipe, lower_pipe)
            lastPipeX = pipe_x
            lastPipeHeight = pipe_height
        if p.sprite.spritecollide(animatedSprites, pipes, False):
            animatedSprites.alive = False
            animatedSprites.show_game_over_screen(screen)
        for pipe in pipes:
            if isinstance(pipe, Pipe)and not pipe.passed:
                if pipe.rect.right < animatedSprites.rect.x:
                    pipe.passed = True
                    p.mixer.music.load("sounds\sfx_point.wav")
                    p.mixer.music.play(1)
                    animatedSprites.score += 1
        screen.fill(BLACK)
        font = p.font.SysFont(None, 24)
        img = font.render('Score: ' + str(animatedSprites.score), True, BLACK)
        background_image = p.image.load('images\\background.png')
        ground = p.image.load("images\\ground.png")

        screen.blit(background_image, (0, 0))
        screen.blit(ground, (0, 600))
        screen.blit(img, (40, 40))
        allSprites.draw(screen)
          
        if not animatedSprites.alive:
             background_image = p.image.load('images\gameOverrre.png')
             screen.blit(background_image, (0, 0))
             font = p.font.SysFont(None, 50)
             img = font.render('Score: '+ str(animatedSprites.score), True, BLACK)
             screen.blit(img, (100, 40))
             p.time.wait(2000)
             
        #     animatedSprites.show_game_over_screen(screen)
            # running = False
        p.display.flip()
        clock.tick(60)


    p.quit()

if __name__ == "__main__":
    main()
