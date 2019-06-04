import pygame

pygame.init()

sizex = 310
sizey = 310

win = pygame.display.set_mode((sizex, sizey))
pygame.display.set_caption("TicTacToe")

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)


player = 1
class field():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.color = WHITE

        self.line1 = ((self.x + 10, self.y + 10), (self.x + 90, self.y + 90))
        self.line2 = ((self.x + 90, self.y + 10), (self.x + 10, self.y + 90))

        self.status = 0

    def draw(self): # draws fields and cross or circle
        # drawing rectangle
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        # drawing cross
        if self.status == 1:
            pygame.draw.line(win, (0, 0, 0), self.line1[0], self.line1[1], 6)
            pygame.draw.line(win, (0, 0, 0), self.line2[0], self.line2[1], 6)
        # drawing circle
        elif self.status == 2:
            pygame.draw.circle(win, (0, 0, 0), (self.x + 50, self.y + 50), 43, 4)

    def hover(self): # checks if cursor is over the field
        global player
        pos = pygame.mouse.get_pos()
        if player <= 2 :
            if self.status == 0:
                if pos[0] >= (self.x) and pos[0] <= (self.x + 100) and pos[1] >= (self.y) and pos[1] <= (self.y + 100):
                    self.color = GREY
                else:
                    self.color = WHITE
            else:
                self.color = WHITE

    def pick(self): # switches status if field is clicked
        global player
        if self.status == 0:
            pos = pygame.mouse.get_pos()
            button1 = pygame.mouse.get_pressed()[0]
            if pos[0] >= (self.x) and pos[0] <= (self.x + 100) and pos[1] >= (self.y) and pos[1] <= (self.y + 100):
                if player == 1:
                    if button1:
                        self.status = 1
                        player = 2
                    else:
                        pass
                elif player == 2:
                    if button1:
                        self.status = 2
                        player = 1
                    else:
                        pass



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

row1 = [fields[0], fields[1], fields[2]] # ---
row2 = [fields[3], fields[4], fields[5]] # ---
row3 = [fields[6], fields[7], fields[8]] # ---
row4 = [fields[0], fields[3], fields[6]] # |
row5 = [fields[1], fields[4], fields[7]] # |
row6 = [fields[2], fields[5], fields[8]] # |
row7 = [fields[0], fields[4], fields[8]] # \
row8 = [fields[6], fields[4], fields[2]] # /

rows = [row1, row2, row3, row4, row5, row6, row7, row8]


def reset():
    global player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        player = 1
        for field in fields:
            field.status = 0

def winner():
    global rows
    global player
    for row in rows:
        if row[0].status == (1) and row[1].status == (1) and row[2].status == (1):
            for field in row:
                field.color = (255, 0, 0)
            player = 3


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

    winner()

    reset()

    pygame.display.update()

pygame.quit()
