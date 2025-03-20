
import pygame
import string
import man
import enum
import server
import client
pygame.init()

class GameState(enum.Enum):
    RUNNING = 0
    LOST = 1
    MENU = 2
    WIN = 3
    QUIT = 100

class Game:
    def __init__(self):
        self.running = True
        self.server = None
        self.client = None


        self.font = pygame.font.Font("OpenSans-ExtraBold.ttf", 36)
        
        self.WIDTH = 600
        self.HEIGHT = 700
        self.screen = pygame.display.set_mode((self.WIDTH, self.HEIGHT))

        # Start Button
        self.start_button = self.font.render("START", True, (255, 255, 255), (0, 0, 0))
        self.start_button_rect = self.start_button.get_rect()
        self.start_button_rect.x = self.WIDTH/2-self.start_button_rect.w/2
        self.start_button_rect.y = self.HEIGHT/2-self.start_button_rect.h/2

        # Host Button
        self.host_button = self.font.render("HOST", True, (255, 255, 255), (0, 0, 0))
        self.host_button_rect = self.start_button.get_rect()
        self.host_button_rect.x = self.WIDTH/2-self.host_button_rect.w/2 - self.start_button_rect.w
        self.host_button_rect.y = self.HEIGHT/2-self.host_button_rect.h/2
        # Connect Button
        self.connect_button = self.font.render("CONNECT", True, (255, 255, 255), (0, 0, 0))
        self.connect_button_rect = self.connect_button.get_rect()
        self.connect_button_rect.x = self.WIDTH/2-self.connect_button_rect.w/2 + self.connect_button_rect.w
        self.connect_button_rect.y = self.HEIGHT/2-self.connect_button_rect.h/2

        self.string_to_guess = "i love you"
        self.guesses = []
        self.display_string = self.create_display_str(self.guesses) # the string that will be rendered to the text representing the string to guess

        self.guess_box_rect = pygame.Rect(0, self.WIDTH-50, self.WIDTH, self.HEIGHT-40)
        self.letter_rects = {}

        self.hangman = man.Hangman()
        self.alphabet = list(string.ascii_lowercase)
        self.wrong = []

        self.lost_message = self.font.render(f"YOU LOST!!!! The word was\n {self.string_to_guess}", True, (100, 0, 0))
        self.lost_message_rect = self.lost_message.get_rect()
        self.lost_message_rect.x = self.WIDTH/2 - self.lost_message_rect.w/2
        self.lost_message_rect.y = self.WIDTH/2
        self.lost = False
        self.gamestate = GameState.MENU

    def create_display_str(self, guesses):
        display_str = ""
        for char in self.string_to_guess:
            if char == " ":
                display_str += " "
                continue
            found = False
            for guess in guesses:
                if char == guess:
                    display_str += char
                    found = True
                    break
            if not found:
                display_str += "_ "  
        return display_str
    
    def draw_display_string(self):
        text = self.font.render(self.display_string, True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.x = 600/2 - text_rect.w/2
        text_rect.y = 100
        self.screen.blit(text, (text_rect.x, text_rect.y))

    def draw_guess_box(self):
        pygame.draw.rect(self.screen, (151, 151, 151), self.guess_box_rect)
        for i, letter in enumerate(self.alphabet):
            if i <= 12:
                text = self.font.render(letter, True, (100, 100, 100))
                text_rect = text.get_rect()
                text_rect.x = i*40+20
                text_rect.y = self.guess_box_rect.y + 20
            elif i > 12 and i <= 26:
                i -= 13
                text = self.font.render(letter, True, (100, 100, 100))
                text_rect = text.get_rect()
                text_rect.x = i*40+20
                text_rect.y = self.guess_box_rect.y + 60
            
            
            self.screen.blit(text, (text_rect.x, text_rect.y))
            self.letter_rects[letter] = text_rect


    def check_guess(self, guess, alphabet):
        print(guess, alphabet)
        if guess in self.string_to_guess:
            pass
        else:
            self.hangman.stage += 1
            if self.hangman.stage >= 7:
                self.gamestate = GameState.LOST
        return alphabet

    def start_menu(self):
        # this is too be called
        self.screen.blit(self.start_button, (self.start_button_rect.x, self.start_button_rect.y))
        self.screen.blit(self.host_button, (self.host_button_rect.x, self.host_button_rect.y))
        self.screen.blit(self.connect_button, (self.connect_button_rect.x, self.connect_button_rect.y))


    def loop(self):
        while self.gamestate is not GameState.QUIT:
            self.display_string = self.create_display_str(self.guesses)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.gamestate = GameState.QUIT
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()

                    if self.gamestate is GameState.MENU:
                        if self.start_button_rect.collidepoint(pos):
                            self.gamestate = GameState.RUNNING
                        if self.host_button_rect.collidepoint(pos):
                            i = input("Please enter the word: ")
                            self.server = server.Server(i)
                            self.server.threaded_start()
                            self.string_to_guess = i
                            self.gamestate = GameState.RUNNING

                    # check if letter was pressed
                    if self.gamestate is GameState.RUNNING:
                        for letter, rect in self.letter_rects.items():
                            if rect.collidepoint(pos):
                                self.alphabet = self.check_guess(letter, self.alphabet)
                                self.guesses.append(letter)


            # Draw Background Color
            self.screen.fill((51, 51, 51))

            if self.gamestate is GameState.MENU:
                self.start_menu()
            elif self.gamestate is GameState.RUNNING:
                self.draw_display_string()
                self.draw_guess_box()
                self.hangman.draw(self.screen)
            elif self.gamestate is GameState.LOST:
                self.draw_loss()

            pygame.display.flip() # clear the screen
            
    def draw_loss(self):
        if self.gamestate is GameState.LOST:
            self.screen.blit(self.lost_message, (self.lost_message_rect.x, self.lost_message_rect.y))

Game().loop()