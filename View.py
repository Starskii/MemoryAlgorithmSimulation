import pygame
import threading


def quit_pygame():
    pygame.quit()


class View:
    def __init__(self):
        self.screen = None
        self.resources = []
        self.processes = []
        self.r_locations = []
        self.p_locations = []
        thread = threading.Thread(target=self.run_pygame)
        thread.start()

    def run_pygame(self):
        pygame.init()
        # Set up the drawing window
        self.screen = pygame.display.set_mode([500, 500], pygame.RESIZABLE)
        # Run until the user asks to quit
        running = True
        while running:
            self.screen.fill((255, 255, 255))
            # Did the user click the window close button?
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            # Draw a solid blue circle in the center
            self.draw_elements()
            # Flip the display
            pygame.display.flip()
        pygame.quit()

    def draw_elements(self):
        screen_width, screen_height = pygame.display.get_surface().get_size()
        size_denominator = 40

        # Draw Processes
        for index in range(0, len(self.processes)):
            # Set color to red if blocked, otherwise blue
            color = (0, 255, 255)
            # Get sum of res you are waiting on
            sum = 0
            for waiting_res in self.processes[index].waiting_res:
                sum += waiting_res
            if sum > 0:
                color = (255, 0, 0)
            # Make radius 1/20 of screen width and place 2x1/20width low on screen
            radius = int(screen_width / size_denominator)
            dist_from_top = 3 * radius
            dist_from_left = 4 * radius * (index+1)
            pygame.draw.circle(self.screen, color, (dist_from_left, dist_from_top), radius)

            if len(self.p_locations) < len(self.processes):
                # Save two process locations:
                self.p_locations.append(((dist_from_left - radius, dist_from_top + radius), (dist_from_left + radius, dist_from_top + radius)))

        # Draw Resources
        for index in range(0, len(self.resources)):
            # Set color to red if empty, otherwise blue
            color = (0, 255, 255)
            if self.resources[index].cur_r == 0:
                color = (255, 0, 0)
            # Make length of square 1/screen_denom of screen width and place 2x1/20width low on screen
            radius = int(screen_width / size_denominator)
            dist_from_top = screen_height - 3 * radius
            dist_from_left = 4 * radius * (index + 1)
            pygame.draw.rect(self.screen, color, pygame.Rect(dist_from_left, dist_from_top, radius, radius), radius)

            # Save two resource locations:
            if len(self.r_locations) < len(self.resources):
                self.r_locations.append(((dist_from_left - radius, dist_from_top - radius), (dist_from_left + radius, dist_from_top - radius)))

        # Draw Holding Res -> Proc
        for p_index in range(0, len(self.processes)):
            process = self.processes[p_index]
            for r_index in range(0, len(process.holding_res)):
                if process.holding_res[r_index] > 0:
                    self.draw_arrow(self.r_locations[r_index][0], self.p_locations[p_index][0], 1)

        # Draw Waiting Proc -> Proc
        for p_index in range(0, len(self.processes)):
            process = self.processes[p_index]
            for r_index in range(0, len(process.waiting_res)):
                if process.waiting_res[r_index] > 0:
                    self.draw_arrow(self.p_locations[p_index][1], self.r_locations[r_index][1], -1)

    def draw_arrow(self, origin, destination, arrow_multiplier):
        color = (255, 0, 0)
        if arrow_multiplier > 0:
            color = (0, 255, 255)
        pygame.draw.line(self.screen, color, origin, destination)
        x, y = destination
        pygame.draw.line(self.screen, color, destination, (x - arrow_multiplier * 10, y + arrow_multiplier * 10))
        pygame.draw.line(self.screen, color, destination, (x + arrow_multiplier * 10, y + arrow_multiplier * 10))

    def add_process(self, process):
        self.processes.append(process)

    def add_resource(self, resource):
        self.resources.append(resource)

    def modify_process(self, index, process):
        self.processes[index] = process

    def modify_resource(self, index, resource):
        self.resources[index] = resource
