from pygame import *


WIDTH, HEIGHT = 750, 500
FPS = 50
score1 = 0
score2 = 0
needed_score = 3


screen = display.set_mode((WIDTH, HEIGHT))
display.set_caption("Awesome game")
background = transform.scale(image.load("background.png"),(WIDTH,HEIGHT))
clock = time.Clock()




mixer.init()
mixer.music.load("best music.mp3")
mixer.music.play()

font.init()
font1 = ()


class Image(sprite.Sprite):
    def __init__(self,img,x,y,w,h,s):
        super().__init__()
        self.image = transform.scale(image.load(img),(w,h))
        self.rect = self.image.get_rect()
        self.speed = s
        self.rect.x = x
        self.rect.y = y
        
    def paste(self):
        screen.blit(self.image,(self.rect.x,self.rect.y))

class Movement(Image):
    def __init__(self,img,x,y,w,h,s):
        super().__init__(img,x,y,w,h,s)


    def display_score(self, score):
        style = font.Font( None, 40)
        text = style.render("Score:"+str(score),True,(255,255,255))
        return text
        

    def win(self,p):
        style = font.Font( None, 40)
        congrat = style.render("Congratulations! Player "+str(p),True,(255,255,255))
        return congrat

    def player_one(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < HEIGHT-100:
            self.rect.y += self.speed


    def player_two(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < HEIGHT-100:
            self.rect.y += self.speed




ball = Movement("donald.png",WIDTH/2,HEIGHT/2,30,30,10)
p1 = Movement("pong_platform.png",10,HEIGHT/2,50,100,10)
p2 = Movement("pong_platform.png",WIDTH-35,HEIGHT/2,50,100,10)

ball_speed = [5,5]


run = True
end = False
while run:
    for e in event.get():
        if e.type == QUIT:
            quit()
            run = False

    if end != True:
        ball.rect.x += ball_speed[0]
        ball.rect.y += ball_speed[1]

        if ball.rect.colliderect(p1.rect) or ball.rect.colliderect(p2.rect):
            ball_speed[0] = -ball_speed[0]

        if ball.rect.top <= 0 or ball.rect.bottom >= HEIGHT:
            ball_speed[1] = -ball_speed[1]


        
        screen.blit(background,(0,0))
        ball.paste()
        p2.paste()
        p1.paste()
        p1.player_one()
        p2.player_two()
        p1_text = p1.display_score(score1)
        p2_text = p2.display_score(score2)
        screen.blit(p1_text,(25,25))
        screen.blit(p2_text, (600,25))







        if ball.rect.x <= 0:
            ball = Movement("donald.png",WIDTH/2,HEIGHT/2,30,30,10)
            time.delay(2000)
            score2 += 1

        if ball.rect.x >= WIDTH - 30:
            ball = Movement("donald.png",WIDTH/2,HEIGHT/2,30,30,10)
            time.delay(2000)
            score1 += 1

        if score1 >= 3:
            pt1 = p1.win(1)
            screen.blit(pt1,(200,200))
            end = True


        if score2 >= 3:
            pt2 = p2.win(2)
            screen.blit(pt2,(200,200))
            end = True
        display.update()

    
    else:
        end = False
        ball = Movement("donald.png",WIDTH/2,HEIGHT/2,30,30,10)
        p1 = Movement("pong_platform.png",10,HEIGHT/2,75,100,10)
        p2 = Movement("pong_platform.png",WIDTH-35,HEIGHT/2,75,100,10)
        score1 =0 
        score2 =0
        time.delay(10000)
        
    clock.tick(FPS)


