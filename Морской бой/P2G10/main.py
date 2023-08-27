import pygame
import modules.path as path
import modules.data_base as data
import modules.draw_module as draw
import modules.place_player_ships as place
import modules.click_and_shoot as shoot
import modules.ship as ship
import modules.bot as bot
import modules.win_check as win
import modules.button as button

pygame.init()
bot.place_bot_ship()
data.unplaced_ship = ship.Ship(type_ = "large", cell = [0,0,0], state = None, angle = 0, side = "player")
screen = pygame.display.set_mode((1200, 700))
pygame.display.set_caption("Боевой корабль!")
bf = "other\\background"
pygame.display.set_icon(pygame.image.load(path.path_to_file("images\\iccon.png")))
data.unplaced_ship = ship.Ship("large", [0, 0, 0], None, 0, "player")
FPS = 60
clock = pygame.time.Clock()
game = True
repeat = 0
step = "player"
winner = None
reset_button = button.Button(x = 1080, y = 20)
while game:
    mouse_state = "hover"
    screen.fill((255,255,255))
    draw.draw_all(screen,bf)
    if place.ship_number < 11: 
        place.blit_unplaced_ship_unchoosed(screen)
    else:
        if winner == None:
            winner = win.win(repeat)
        else:
            screen.blit(pygame.transform.scale(pygame.image.load(path.path_to_file(f"images\\other\\{winner}_table.png")), (500, 300)), (350, 200))
    for event in pygame.event.get():          
        if event.type == pygame.QUIT:
            game = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if place.ship_number < 11:
                print("MBD SN<11")
                place.choose_ship()
            mouse_state = "click"
        if event.type == pygame.MOUSEBUTTONUP: 
            if place.ship_number < 11:
                place.place_finish()
            mouse_state = "up"
        if place.ship_number < 11: 
            place.place_ship()
        if place.ship_number < 11:
            place.rotate_ship(repeat) 
    if (reset_button.X < pygame.mouse.get_pos()[0] < reset_button.X + reset_button.WIDTH and
        reset_button.Y < pygame.mouse.get_pos()[1] < reset_button.Y + reset_button.HEIGHT and
        reset_button.STATE != None):
        if mouse_state == "click":
            reset_button.STATE = "click"
        elif mouse_state == "up":
            reset_button.STATE = "up"
            data.player_map = data.map()
            data.enemy_map = data.map()
            place.ship_number = 1
            data.ships = []
            bot.place_bot_ship()
            data.unplaced_ship = ship.Ship(type_ = "large", cell = [0,0,0], state = None, angle = 0, side = "player")
            winner = None
            step = "player"
            repeat = 0 
            reset_button.STATE = "hover"
    reset_button.blit_button(screen)
    if place.ship_number >= 11 and winner == None:
        if step == "player" and shoot.check_click(mouse_state):
            step = "enemy"
        elif step == "enemy" and bot.bot_shoot(repeat):
            step = "player"
    clock.tick(FPS)
    pygame.display.flip()
    repeat += 1