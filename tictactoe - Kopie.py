import pygame
import numpy

n = int(input("Wie groß soll das Feld sein? (n muss eine natürliche Zahl sein!)"))
fields_to_win = int(input("Wie viele Felder werden zum Gewinnen benötigt?"))#

N = n  # In case some weirdo doesn't want a quadratic field.

field_size = 100
line_width = 5

total_width = n * field_size + (n - 1) * line_width

WHITE = (255, 255, 255)
GREY = (200, 200, 200)
RED = (255, 0, 0)
BLACK = (0, 0, 0)

player = 1

pygame.init()
win = pygame.display.set_mode((total_width, total_width))
pygame.display.set_caption("TicTacToe")


class Field:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.width = 100
        self.color = WHITE

        self.line1 = (
        (self.x + 0.1 * field_size, self.y + 0.1 * field_size), (self.x + 0.9 * field_size, self.y + 0.9 * field_size))
        self.line2 = (
        (self.x + 0.9 * field_size, self.y + 0.1 * field_size), (self.x + 0.1 * field_size, self.y + 0.9 * field_size))

        self.status = 0

    def draw(self):  # draws fields and cross or circle
        # drawing rectangle
        pygame.draw.rect(win, self.color, (self.x, self.y, self.width, self.width))

        # drawing cross
        if self.status == 1:
            pygame.draw.line(win, BLACK, self.line1[0], self.line1[1], 6)
            pygame.draw.line(win, BLACK, self.line2[0], self.line2[1], 6)
        # drawing circle
        elif self.status == 2:
            pygame.draw.circle(win, BLACK, (self.x + 0.5 * field_size, self.y + 0.5 * field_size),
                               int(0.43 * field_size), int(0.8 * line_width))

    def hover(self):  # checks if cursor is over the field
        global player
        pos = pygame.mouse.get_pos()
        if player <= 2:
            if self.status == 0:
                if self.x <= pos[0] <= (self.x + field_size) and self.y <= pos[1] <= (self.y + field_size):
                    self.color = GREY
                else:
                    self.color = WHITE
            else:
                self.color = WHITE

    def pick(self):  # switches status if field is clicked
        global player
        if self.status == 0:
            pos = pygame.mouse.get_pos()
            button1 = pygame.mouse.get_pressed()[0]
            if self.x <= pos[0] <= (self.x + field_size) and self.y <= pos[1] <= (
                    self.y + field_size):
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


fields = numpy.ndarray((n, N), dtype=Field)

for i in range(n):
    for j in range(N):
        x = j * field_size + (line_width * j)
        y = i * field_size + (line_width * i)
        fields[i][j] = Field(x, y)

fields_transposed = fields.T

rows_length = 2 * n + 2

rows = numpy.ndarray((rows_length, n), dtype=Field)
for i in range(rows_length):
    if i < n:
        rows[i] = fields[i]
    elif i < 2 * n:
        rows[i] = fields_transposed[i - n]
    elif i == rows_length - 2:
        rows[rows_length - 2] = rows.diagonal()
    elif i == rows_length - 1:
        rows[rows_length - 1] = numpy.fliplr(fields).diagonal()


# rows = [row1, row2, row3, row4, row5, row6, row7, row8]


def reset():
    global player
    keys = pygame.key.get_pressed()
    if keys[pygame.K_r]:
        print("Games has been reset.")
        player = 1
        for _field_row in fields:
            for _field in _field_row:
                _field.status = 0


def get_row_is_winner(row) -> bool:
    count = 0
    old_status = 0
    for t in row:
        if t.status == 0:
            count = 0
        elif t.status != old_status:
            count = 1
        elif t.status == old_status:
            count += 1
        else:
            raise Exception("get_row_is_winner(): There was an error with the field.status.")

        if count >= fields_to_win:
            return True
        else:
            old_status = t.status

    return False


def winner():
    global rows
    global player
    for row in rows:
        if get_row_is_winner(row):
            for field in row:
                field.color = RED
            player = 3


run = 1
while run:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = 0

    pygame.time.delay(15)

    win.fill(BLACK)  # BLACK

    for field_row in fields:
        for field in field_row:
            field.hover()
            field.pick()
            field.draw()

    winner()

    reset()

    pygame.display.update()

pygame.quit()
