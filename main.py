import pygame
from pygame.math import Vector2
import random
import os

pygame.init()


width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Game Snake")
score_font = pygame.font.Font(None, 36)

apple = pygame.transform.scale(pygame.image.load(os.path.join(r"D:\Proyectos\Prueba\img\apple.png")),(20,20))
snake_head = pygame.transform.scale(pygame.image.load(os.path.join(r"D:\Proyectos\Prueba\img\snake.png")),(20,20))
snake = []
for x in range(1,5):
    snake+=[pygame.transform.scale(pygame.image.load(os.path.join(r"D:\Proyectos\Prueba\img\snake"+str(x)+".png")),(20,20))]

class Snake:
    def __init__(self):
        self.body = [Vector2(20,100),Vector2(20,110),Vector2(20,120)]
        self.direction = Vector2(0,-20)
        self.add = False
    def draw(self):
        for block in self.body:
            screen.blit(snake_head,(block.x,block.y))
        if self.direction == Vector2(0,-20):
            screen.blit(snake[0],(self.body[0].x,self.body[0].y))
        if self.direction == Vector2(0,20):
            screen.blit(snake[2],(self.body[0].x,self.body[0].y))
        if self.direction == Vector2(20,0):
            screen.blit(snake[1],(self.body[0].x,self.body[0].y))
        if self.direction == Vector2(-20,0):
            screen.blit(snake[3],(self.body[0].x,self.body[0].y))
    
    def move(self):	
        if self.add == True:
            body_copy = self.body
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]
            self.add = False
        else:
            body_copy = self.body[:-1]
            body_copy.insert(0,body_copy[0]+self.direction)
            self.body = body_copy[:]

    def move_up(self):
        self.direction = Vector2(0,-20)

    def move_down(self):    
       self.direction = Vector2(0,20)

    def move_right(self):
       self.direction = Vector2(20,0)

    def move_left(self):
       self.direction = Vector2(-20,0)

    def die(self):
        if self.body[0].x >= width+20 or self.body[0].y >= height+20 or self.body[0].x <= -20 or self.body[0].y <= -20:
           return True
		#SNake se toca a si misma
        for i in self.body[1:]:
            if self.body[0] == i:
                return True
class Apple:
	def __init__(self):
		self.generate()


	def draw(self):
		screen.blit(apple,(self.pos.x,self.pos.y))


	def generate(self):
		self.x = random.randrange(0,int(width/20))
		self.y = random.randrange(0,int(height/20))
		self.pos = Vector2(self.x*20,self.y*20)

	def check_collision(self,snake):

		if snake[0] == self.pos:
			self.generate()
			snake.add = True
			return True

		for block in snake[1:]:
			if self.pos == block:
				self.generate()
		return False

try:
    def main():

        snake = Snake()
        apple = Apple()
        score = 0

        fps = pygame.time.Clock()

        while True:

            fps.tick(30)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()

                if event.type == pygame.KEYDOWN and snake.direction.y != 20:
                    if event.key == pygame.K_UP:
                        snake.move_up()

                if event.type == pygame.KEYDOWN and snake.direction.y != -20:
                    if event.key == pygame.K_DOWN:
                        snake.move_down()


                if event.type == pygame.KEYDOWN and snake.direction.x != -20:
                    if event.key == pygame.K_RIGHT:
                        snake.move_right()

                if event.type == pygame.KEYDOWN and snake.direction.x != 20:
                    if event.key == pygame.K_LEFT:
                        snake.move_left()

                            
            screen.fill((175,215,70))
            snake.draw()
            apple.draw()

            snake.move()

            snake.die()
            if snake.die():
                quit()


            text = score_font.render("Score: {}".format(score), 1, (255, 255, 255))
            screen.blit(text, (width - text.get_width() - 20, 20))

            pygame.display.update()
except Exception as e:
    print("Se produjo un error al ejecutar", str(e))
main()