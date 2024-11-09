import pyxel, random

class JeuSnake:

    TITLE = 'Jeu Snake'
    WIDTH, HEIGHT = 200,160
    CASE =20
    FRAME_REFRESH = 15

    def __init__(self):
        pyxel.init(self.WIDTH, self.HEIGHT,title=self.TITLE)
        self.snake = [[3,3],[2,3],[1,3]]
        self.score = 0
        self.direction = [1,0]
        self.food = [20,20]
        pyxel.run(self.update, self.draw)

    def move(self):
        if pyxel.btn(pyxel.KEY_ESCAPE):
            pyxel.quit()
        elif pyxel.btn(pyxel.KEY_UP) and self.direction in ([1,0],[-1,0]):
            self.direction = [0,-1]
        elif pyxel.btn(pyxel.KEY_DOWN) and self.direction in ([1,0],[-1,0]):
            self.direction = [0,1]
        elif pyxel.btn(pyxel.KEY_LEFT) and self.direction in ([0,1],[0,-1]):
            self.direction = [-1,0]
        elif pyxel.btn(pyxel.KEY_RIGHT) and self.direction in ([0,1],[0,-1]):
            self.direction = [1,0]

    def food_(self):
        if self.food in self.snake:
            self.score += 1
        while self.food in self.snake:
            self.food = [random.randint(0,self.WIDTH/self.CASE-1),random.randint(0,self.HEIGHT/self.CASE-1)]
    def update(self):
        if pyxel.frame_count % self.FRAME_REFRESH == 0:
            head = [self.snake[0][0]+self.direction[0], self.snake[0][1]+self.direction[1]]
            self.snake.insert(0,head)
            self.snake.pop(-1)
            self.move()
            self.food_()
            if head in self.snake[1:] or head[0]<0 or head[0]>self.WIDTH/self.CASE -1 or head[1]<0 or head[1]>self.HEIGHT/self.CASE -1:
                pyxel.quit()

    def draw(self):
        pyxel.cls(0)
        x_head, y_head = self.snake[0]
        pyxel.rect(x_head*self.CASE, y_head*self.CASE, self.CASE,self.CASE,10)
        pyxel.rect(self.food[0], self.food[1], self.CASE,self.CASE,8)
        for ring in self.snake[1:]:
            x, y = ring[0], ring[1]
            pyxel.rect(x*self.CASE, y*self.CASE, self.CASE,self.CASE,9)
        pyxel.text(5, 5, f"SCORE : {self.score}", 7)
jeu = JeuSnake()