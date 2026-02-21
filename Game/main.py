import pygame as pg
import random

def is_crash():
    for x in range(player_rect.x, player_rect.topright[0], 1):
        for y in range(player_rect.y, player_rect.bottomleft[1], 1):
            try:
                if screen.get_at((x,y)) == (220, 215, 177, 255):
                    print('color is crash')
                    return True
            except:
                print("oops")


    if hotel_rect.colliderect(player_rect):
        print("hotel_is_crash")
        return True

    return False


width, height = 700, 450

FPS = 60

BLACK = (0, 0, 0)

x_direction = 0
y_direction = 0
player_speed = 2

image_dict = {
    "bg": pg.image.load('img/Background.png'),
    "player": {
        "rear": pg.image.load('img/cab_rear.png'),
        "left": pg.image.load('img/cab_left.png'),
        "right": pg.image.load('img/cab_right.png'),
        "front": pg.image.load('img/cab_front.png'),
    },
    "hole": pg.image.load('img/hole.png'),
    "hotel": pg.transform.scale(pg.image.load('img/hotel.png'), (80,80)),
    "passenger": pg.image.load('img/passenger.png'),
    "taxi_background": pg.transform.scale(pg.image.load('img/taxi_background.png'), (80, 32)),
    "parking": pg.transform.scale(pg.image.load('img/parking.png'), (80,32))
}
player_view = 'rear'
player_rect = image_dict["player"][player_view].get_rect()
player_rect.x = 300
player_rect.y = 300

hotel_img = image_dict["hotel"]
hotel_rect = hotel_img.get_rect()
hotel_positions = [
    (60, 30),
    (60, 300),
    (430, 300),
    (561, 30),
]
hotel_rect.x, hotel_rect.y = random.choice(hotel_positions)

#parking_img = image_dict["taxi_background"]
parking_img = image_dict["parking"]

parking_rect = parking_img.get_rect()
parking_rect.x, parking_rect.y = hotel_rect.x, hotel_rect.y + hotel_rect.height

passenger_img = image_dict["passenger"]
passenger_rect = passenger_img.get_rect()
passenger_rect.x, passenger_rect.y = hotel_rect.x, hotel_rect.y + hotel_rect.height


pg.init()

screen = pg.display.set_mode((width, height))

timer = pg.time.Clock()

run = True

while run:
    timer.tick(FPS)
    for event in pg.event.get():
        if event.type == pg.QUIT:
            run = False
        if event.type == pg.MOUSEBUTTONDOWN:
            mouse_x, mouse_y =pg.mouse.get_pos()
            pixel_color = screen.get_at((mouse_x, mouse_y))
            print(mouse_x, mouse_y)
            print(pixel_color)


        # if event.type == pg.KEYDOWN:
        #     if event.key == pg.K_RIGHT:
        #         x_direction = 1
        #     elif event.key == pg.K_LEFT:
        #         x_direction = -1
        #     elif event.key == pg.K_UP:
        #         y_direction = -1
        #     elif event.key == pg.K_DOWN:
        #         y_direction = 1
    keys_klava = pg.key.get_pressed()

    if keys_klava[pg.K_RIGHT]:
        x_direction = 1
        player_view = 'right'
    elif keys_klava[pg.K_LEFT]:
        x_direction = -1
        player_view = 'left'
    elif keys_klava[pg.K_UP]:
        y_direction = -1
        player_view = 'rear'
    elif keys_klava[pg.K_DOWN]:
        y_direction = 1
        player_view = 'front'




    # Обновление
    player_rect.x += player_speed * x_direction
    player_rect.y += player_speed * y_direction
    x_direction = 0
    y_direction = 0
    is_crash()
    # Визуализация
    screen.fill(BLACK)
    screen.blit(image_dict["bg"], (0,0))
    screen.blit(image_dict["player"][player_view], player_rect)

    # прорисовка
    screen.blit(image_dict["hotel"], hotel_rect)
    screen.blit(parking_img, parking_rect)
    screen.blit(passenger_img, passenger_rect)
    screen.blit(image_dict["player"][player_view], player_rect)

    pg.display.flip()
pg.quit()

