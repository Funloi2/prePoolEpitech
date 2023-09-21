import pygame
import csv
from Hangman import button


# import button


# initialize pygame
def main():
    pygame.init()
    screen_width = 1000
    screen_height = 600
    side_margin = 500
    lower_margin = 100
    level = 0
    hmWindow = pygame.display.set_mode((screen_width + side_margin, screen_height + lower_margin))
    pygame.display.set_caption("Hangman Editor")
    run = True

    # define game variables
    clock = pygame.time.Clock()
    FPS = 60
    scroll_left = False
    scroll_right = False
    scroll = 0
    scroll_speed = 1
    cols = 150
    rows = 16
    tile_size = screen_height // rows
    current_tile = 0
    tile_types = 21

    # load images
    pine1 = pygame.image.load('Assets/img/Background/pine1.png').convert_alpha()
    pine2 = pygame.image.load('Assets/img/Background/pine2.png').convert_alpha()
    mountain = pygame.image.load('Assets/img/Background/mountain.png').convert_alpha()
    sky_img = pygame.image.load('Assets/img/Background/sky_cloud.png').convert_alpha()

    # stor tiles in list
    letter_list = []
    img_list = []
    for x in range(tile_types):
        img = pygame.image.load(f'Assets/img/Tile/{x}.png')
        img = pygame.transform.scale(img, (tile_size, tile_size))
        img_list.append(img)
    for x in range(1,26):
        img = pygame.image.load(f'Assets/img/letters/{x}.png')
        img = pygame.transform.scale(img, (tile_size, tile_size))
        letter_list.append(img)

    # define buttons
    button_list = []
    button_col = 0
    button_row = 0
    for i in range(len(img_list)):
        tile_button = button.Button(screen_width + (75 * button_col) + 50, 75 * button_row + 50, img_list[i], 1)
        button_list.append(tile_button)
        button_col += 1
        if button_col == 6:
            button_row += 1
            button_col = 0

    for i in range(len(letter_list)):
        tile_button = button.Button(screen_width + (75 * button_col) + 50, 75 * button_row + 50, letter_list[i], 1)
        button_list.append(tile_button)
        button_col += 1
        if button_col == 6:
            button_row += 1
            button_col = 0

    # define colors
    Green = (0, 255, 0)
    White = (255, 255, 255)
    Black = (0, 0, 0)
    Red = (255, 0, 0)

    # draw images
    width = pine1.get_width()
    font = pygame.font.SysFont('Futura', 30)

    def draw_text(text, font, text_col, x, y):
        img = font.render(text, True, text_col)
        hmWindow.blit(img, (x, y))
    def draw_bg():
        hmWindow.fill(Green)

        for x in range(4):
            hmWindow.blit(sky_img, ((x * width) - scroll * .5, 0))
            hmWindow.blit(mountain, ((x * width) - scroll * .6, screen_height - mountain.get_height() - 300))
            hmWindow.blit(pine1, ((x * width) - scroll * .7, screen_height - pine1.get_height() - 150))
            hmWindow.blit(pine2, ((x * width) - scroll * .8, screen_height - pine2.get_height()- 10))

    def draw_grid():
        # vertical lines
        for c in range(cols):
            pygame.draw.line(hmWindow, White, (c * tile_size - scroll, 0), (c * tile_size - scroll, screen_height-10))
        # horizontal lines
        for c in range(rows ):
            pygame.draw.line(hmWindow, White, (0, c * tile_size), (screen_width, c * tile_size))

    world_data = []
    for row in range(rows):
        r = [-1] * cols
        world_data.append(r)

    #create ground
    for tile in range(0, cols):
        world_data[rows - 1][tile] = 0

    #func to draw world tiles
    def draw_world():
        for y, row in enumerate(world_data):
            for x, tile in enumerate(row):
                if tile >= 0:
                    hmWindow.blit(img_list[tile], (x * tile_size - scroll, y * tile_size))

    save_img = pygame.image.load('Assets/img/save_btn.png').convert_alpha()
    load_img = pygame.image.load('Assets/img/load_btn.png').convert_alpha()
    save_button = button.Button(screen_width // 2, screen_height+ lower_margin - 50, save_img, 1)
    load_button = button.Button(screen_width // 2 + 200, screen_height+ lower_margin - 50, load_img, 1)



    while run:
        clock.tick(FPS)
        draw_bg()
        draw_grid()
        draw_world()
        pygame.draw.rect(hmWindow, Green, (screen_width, 0, side_margin, screen_height))
        if save_button.draw(hmWindow) :
            # save level data
            with open(f'level{level}_data.csv', 'w', newline='') as csvfile:
                writer = csv.writer(csvfile, delimiter=',')
                for row in world_data:
                    writer.writerow(row)
        if load_button.draw(hmWindow):
            # load in level data
            with open(f'level{level}_data.csv', newline='') as csvfile:
                reader = csv.reader(csvfile, delimiter=',')
                for x, row in enumerate(reader):
                    for y, tile in enumerate(row):
                        world_data[x][y] = int(tile)
        draw_text(('Level : ' + str(level)), font, Black, 10, screen_height + lower_margin - 90)
        draw_text("Press UP or DOWN to change level", font, Black, 10, screen_height + lower_margin - 60)



        # add new tiles to screen
        # get mouse position
        pos = pygame.mouse.get_pos()
        x = (pos[0] + scroll) // tile_size
        y = pos[1] // tile_size

        # check that the coordinates are within the tile area


        # draw tile panel and tiles
        button_count = 0
        for button_count,i in enumerate(button_list):
            if i.draw(hmWindow):
                current_tile = button_count

        #highlight selected tile
        pygame.draw.rect(hmWindow, Red, button_list[current_tile].rect, 3)

        # scroll background
        if scroll_left == True and scroll > 0:
            scroll -= 5 * scroll_speed
        if scroll_right == True and scroll < (cols * tile_size) - screen_width:
            scroll += 5 * scroll_speed

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            if pos[0] < screen_width and pos[1] < screen_height:
                # update tile value
                if pygame.mouse.get_pressed()[0] == 1:
                    if current_tile <= tile_types:
                        world_data[y][x] = current_tile
                if pygame.mouse.get_pressed()[2] == 1:
                    world_data[y][x] = -1

            # keyboard presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level += 1
                if event.key == pygame.K_DOWN and level > 0:
                    level -= 1
                if event.key == pygame.K_LEFT:
                    scroll_left = True
                if event.key == pygame.K_RIGHT:
                    scroll_right = True
                if event.key == pygame.K_RSHIFT:
                    scroll_speed = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    scroll_left = False
                if event.key == pygame.K_RIGHT:
                    scroll_right = False
                if event.key == pygame.K_RSHIFT:
                    scroll_speed = 1

        pygame.display.update()

    pygame.quit()
