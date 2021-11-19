import pygame
import threading


def quit_pygame():
    pygame.quit()


class View:
    def __init__(self):
        self.screen = None
        thread = threading.Thread(target=self.run_pygame)
        thread.start()

    def run_pygame(self):
        pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode([500, 500])
        self.screen.fill((255, 255, 255))
        # Run until the user asks to quit
        running = True
        while running:
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Draw a solid blue circle in the center
            pygame.draw.circle(self.screen, (0, 0, 255), (250, 250), 75)
            # Flip the display
            pygame.display.flip()
        pygame.quit()

    def add_element(self):
        pygame.draw.circle(self.screen, (0, 0, 255), (100, 100), 75)
        pygame.display.flip()
