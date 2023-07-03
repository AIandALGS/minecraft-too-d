    os.environ["SDL_VIDEO_CENTERED"] = "1"

    pygame.init()

    flags = DOUBLEBUF
    screen = pygame.display.set_mode(
        (WINDOW_DISPLAY_WIDTH, WINDOW_DISPLAY_HEIGHT), flags, 16
    )

    event_manager = EventManager()

    player = Player()
    camera = Camera(player)
    mouse = Mouse()

    world = World(player, camera, mouse)

    # Profiling
    with cProfile.Profile() as profile:
        main(event_manager, screen, pygame.time.Clock())