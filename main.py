#importing packages
import pygame

#initializing packages
pygame.init()

#setting screen dimension
screenWidth = 800
screenHeight = int(screenWidth * 0.8)
#displaying the main screen and setting caption
screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("Client 1")

#set framerate
clock = pygame.time.Clock()
FPS = 60

#defining player actions
moving_left = False
moving_right = False

#defining colours
BG = (144, 201, 120)

#assigning colours
def draw_bg():
    screen.fill(BG)


#making a class playerEntity(Soldier) which defines actions related to the player
class playerEntity(pygame.sprite.Sprite):
    def __init__(self,char_type ,x, y, scale, speed):
        pygame.sprite.Sprite.__init__(self)
        self.char_type = char_type
        self.speed = speed
        self.direction = 1
        self.flip = False
        self.animation_list = []
        self.frame_index = 0
        self.update_time = pygame.time.get_ticks()
        for i in range(5):
            self.img = pygame.image.load(f'media/img/{self.char_type}/Idle/{i}.png')
            self.img = pygame.transform.scale(self.img, (int(self.img.get_width() * scale), int(self.img.get_height() * scale)))
            self.animation_list.append(self.img)
        self.image = self.animation_list[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y) 
    
    def move(self, moving_left, moving_right):
        #defining a command for movement
        #resetting movement
        dx = 0
        dy = 0
        
        #assigning variables to move left and right
        if moving_left:
            dx = -self.speed
            self.flip = True
            self.direction = -1
        if moving_right:
            dx = self.speed
            self.flip = False
            self.direction = 1

        #changing the actual rectangle position
        self.rect.x += dx
        self.rect.y += dy


    def update_animation(self):
        #updating the animation
        ANIMATION_COOLDOWN = 100
        #update image
        self.image = self.animation_list[self.frame_index]
        #check if enough time has passed from the last animation
        if pygame.time.get_ticks() - self.update_time > ANIMATION_COOLDOWN:
           self.update_time = pygame.time.get_ticks() 
           self.frame_index += 1
        elif self.frame_index >= len(self.animation_list):
           self.frame_index = 0

        
    def draw(self):
        #defining a command to draw
        screen.blit(pygame.transform.flip(self.img, self.flip , False), self.rect)

#printing player with type, co-ords and scale
p1 = playerEntity('Player', 200, 200, 2, 5)
enemy = playerEntity('Enemy', 300, 200, 2, 5)

run = True
while run:

    #clicking the clock
    clock.tick(FPS)

    #background colour
    draw_bg()

    #update the animation
    p1.update_animation()
    enemy.update_animation()


    #drawing players
    p1.draw()
    enemy.draw()


    #moving players
    p1.move(moving_left, moving_right)

    for event in pygame.event.get():
        #quitting game with QUIT button
        if event.type == pygame.QUIT:
            run = False
        #key presses
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_ESCAPE:
                run = False

        #key releases
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_d:
                moving_right = False
    

    pygame.display.update()