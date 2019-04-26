import pygame

pygame.init()

sizex = 310
sizey = 310

win = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption("TicTacToe")


class field():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.color = (255, 255, 255)

        self.line1 = ((self.x + 10, self.y + 10), (self.x + 90, self.y + 90))
        self.line2 = ((self.x + 90, self.y + 10), (self.x + 10, self.y + 90))

        self.status = 0

    def draw(self): # draws fields and cross or circle
        # drawing rectangle
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        # drawing cross
        if self.status == 1:
            pygame.draw.line(win, (0, 0, 0), self.line1[0], self.line1[1], 4)
            pygame.draw.line(win, (0, 0, 0), self.line2[0], self.line2[1], 4)

        # drawing circle
        if self.status == 2:
            pygame.draw.circle(win, (0, 0, 0), (self.x + 50, self.y + 50), 40, 4)

    def hover(self): # checks if cursor is over the field
        pos = pygame.mouse.get_pos()
        if self.status == 0:
            if pos[0] >= (self.x) and pos[0] <= (self.x + 100) and pos[1] >= (self.y) and pos[1] <= (self.y + 100):
                self.color = (200, 200, 200)
            else:
                self.color = (255, 255, 255)
        else:
            self.color = (255, 255, 255)

    def pick(self): # switches status if field is clicked
        if self.status == 0:
            pos = pygame.mouse.get_pos()
            button = pygame.mouse.get_pressed()[0]
            if pos[0] >= (self.x) and pos[0] <= (self.x + 100) and pos[1] >= (self.y) and pos[1] <= (self.y + 100):
                if button:
                    self.status = 1
                else:
                    self.status = 0

field0_0 = field(0,   0)
field0_1 = field(106, 0)
field0_2 = field(211, 0)
field1_0 = field(0,   106)
field1_1 = field(106, 106)
field1_2 = field(211, 106)
field2_0 = field(0,   211)
field2_1 = field(106, 211)
field2_2 = field(211, 211)

fields = [field0_0, field0_1, field0_2, # 0
          field1_0, field1_1, field1_2, # 1
          field2_0, field2_1, field2_2] # 2
          # 0       # 1       # 2
run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    pygame.time.delay(15)

    win.fill((0,0,0)) # BLACK

    for field in fields:
        field.hover()
        field.pick()
        field.draw()

    pygame.display.update()

pygame.quit()
