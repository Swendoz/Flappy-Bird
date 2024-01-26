import pygame

import assets
import configs
from objects.background import Background
from objects.floor import Floor
from objects.column import Column
from objects.bird import Bird
from objects.gamestart_message import GameStartMessage
from objects.gameover_message import GameOverMessage
from objects.score import Score

def play_game():
    pygame.init()

    assets.load_sprites()
    assets.load_audios()

    pygame.display.set_caption("Flappy Bird")
    game_icon = assets.get_sprite("bird-midflap")
    pygame.display.set_icon(game_icon)
    screen = pygame.display.set_mode((configs.SCREEN_WIDTH, configs.SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    column_create_event = pygame.USEREVENT
    running = True
    game_over = False
    game_started = False


    sprites = pygame.sprite.LayeredUpdates()


    def create_sprites():
        Background(0, sprites)
        Background(1, sprites)
        Floor(0, sprites)
        Floor(1, sprites)

        return Bird(sprites), GameStartMessage(sprites), Score(sprites)


    bird, game_start_message, score = create_sprites()


    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == column_create_event:
                Column(sprites)
            if event.type == pygame.MOUSEBUTTONDOWN and not game_started and not game_over:
                game_started = True
                game_start_message.kill()
                pygame.time.set_timer(column_create_event, 1500)
            if event.type == pygame.MOUSEBUTTONDOWN and game_over:
                print("Playing again")
                game_started = False
                game_over = False
                # score= 0
                sprites.empty()
                bird, game_start_message, score = create_sprites()

            bird.handle_event(event)

        screen.fill(0)

        sprites.draw(screen)

        if game_started and not game_over:
            sprites.update()

        if bird.check_collision(sprites) and not game_over:
            GameOverMessage(sprites)
            game_over = True
            game_started = False
            pygame.time.set_timer(column_create_event, 0)
            assets.play_audio("hit")

        for sprite in sprites:
            if type(sprite) is Column and sprite.is_passed():
                score.value += 1
                assets.play_audio("point")
                print(f"Score: {score}")

        pygame.display.flip()
        clock.tick(configs.FPS)

    pygame.quit()


# play_game()