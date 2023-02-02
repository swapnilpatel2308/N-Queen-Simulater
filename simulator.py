
import pygame
import sys


pygame.init()
pygame.display.set_caption("N queen")
screen = pygame.display.set_mode((600, 650))
clock = pygame.time.Clock()
fps = 1

size = int(sys.argv[1])
#size = 7
one_box_w = int(600/size)

queen_img = pygame.image.load(
    "C:\\Users\\SWAPNIL\\Desktop\\my project\\n queen game\\q1.png")
queen_img = pygame.transform.scale(queen_img, (one_box_w, one_box_w))

x_pos = 0
y_pos = 0
run = True
queen_list = []
new_adder_list = []
flag = True


def chack_queen(x, y, size):
    chack_list = []
    for i in range(size):
        c = x + i
        d = y + i
        e = x - i
        f = y - i
        if(c < size):
            chack_list.append((c, y))
        if(d < size):
            chack_list.append((x, d))
        if(e > -1):
            chack_list.append((e, y))
        if(f > -1):
            chack_list.append((x, f))
        if(e > -1 and f > -1):
            chack_list.append((e, f))
        if(c < size and f > -1):
            chack_list.append((c, f))
        if(c < size and d < size):
            chack_list.append((c, d))
        if(e > -1 and d < size):
            chack_list.append((e, d))
    res = []
    [res.append(x) for x in chack_list if x not in res]
    res.remove((x, y))
    return res


def draw_box():
    k = 0
    for i in range(size):
        for j in range(size):
            if(i % 2 == k and j % 2 == k):
                pygame.draw.rect(screen, (175, 161, 84), pygame.Rect(
                    one_box_w*i, one_box_w*j, one_box_w, one_box_w))
            else:
                pygame.draw.rect(screen, (251, 239, 177), pygame.Rect(
                    one_box_w*i, one_box_w*j, one_box_w, one_box_w))
        if(k == 0):
            k = 1
        else:
            k = 0


def set_image(x, y, img):
    screen.blit(img, (x*one_box_w, y*one_box_w))


def issafe(x, y):
    b = []
    for i in range(len(queen_list)):
        a = chack_queen(queen_list[i][0], queen_list[i][1], size)
        for i in range(len(a)):
            b.append(a[i])
    for i in range(len(new_adder_list)):
        b.append(new_adder_list[i])

    if((x, y) in b):
        return False
    else:
        return True


def draw_queen():
    for i in range(len(queen_list)):
        set_image(queen_list[i][0], queen_list[i][1], queen_img)


font_color = (0, 150, 250)
font_obj = pygame.font.Font("C:\Windows\Fonts\segoeprb.ttf", 25)
text_obj = font_obj.render("Welcome to N Queen Simulator", True, font_color)

win_msg = font_obj.render("Completed....", True, (200, 0, 0))

while run:
    clock.tick(fps)
    screen.fill("#000000")

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    draw_box()
    if(flag == True):
        if(issafe(x_pos, y_pos)):
            queen_list.append((x_pos, y_pos))
            x_pos = x_pos + 1
            y_pos = 0
            set_image(x_pos, y_pos, queen_img)
        else:
            y_pos = y_pos + 1
            if(y_pos == size):
                x_pos = x_pos - 1
                y_pos = 0
                new_adder_list.append(queen_list[-1])
                queen_list.remove(queen_list[-1])
            set_image(x_pos, y_pos, queen_img)
        draw_queen()
        if(len(queen_list) == size):
            flag = False
    else:
        draw_queen()
        screen.blit(win_msg, (230, 300))

    screen.blit(text_obj, (100, 605))

    pygame.display.update()

pygame.quit()
