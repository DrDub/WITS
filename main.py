#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pygame

from pygame.locals import *

from Star import Star, StarsCalification
from Button import Button, ButtonNextLevel
from Text import Text
from Timer import Timer

from CfgUtils import CfgUtils
print "Modules imported"

'''
####################################################
#                  SCENES                          #
####################################################
'''     
class Menu():
    def __init__(self):
        self.image = pygame.image.load('resources/background_menu.png')

        self.button_play = Button('resources/Button1.png',SCREEN_WIDTH/2,300)
        self.button_options = Button('resources/Button1.png',SCREEN_WIDTH/2,425)
        self.button_credits = Button('resources/Button1.png',SCREEN_WIDTH/2,550)
        self.button_exit = Button('resources/Button1.png',SCREEN_WIDTH/2,675)

        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.button_play)
        self.buttons.add(self.button_options)
        self.buttons.add(self.button_credits)
        self.buttons.add(self.button_exit)
        
        self.configuration = CfgUtils('configuration.cfg')
        self.language = self.configuration.read('Options', 'language')

        self.font = pygame.font.Font('resources/ThrowMyHandsUpintheAirBold.ttf',85)      

        self.text_play = Text(self.font,self.configuration.read(self.language,'play'),(255,255,255),512,300)
        self.text_options = Text(self.font,self.configuration.read(self.language,'options'),(255,255,255),512,425)
        self.text_credits = Text(self.font,self.configuration.read(self.language,'credits'),(255,255,255),512,550)
        self.text_exit = Text(self.font,self.configuration.read(self.language,'exit'),(255,255,255),512,675)

        print "Menu() created"

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
        
            if event.type == MOUSEBUTTONDOWN:
                if self.button_play.rect.collidepoint(event.pos[0],event.pos[1]):
                    difficult_start()
                if self.button_options.rect.collidepoint(event.pos[0],event.pos[1]):
                    options_start()
                if self.button_credits.rect.collidepoint(event.pos[0],event.pos[1]):
                    print "credits"
                if self.button_exit.rect.collidepoint(event.pos[0],event.pos[1]):
                    exit()  

    def draw(self,screen):
        screen.blit(self.image,(0,0))
        self.buttons.draw(screen)
        self.text_play.draw(screen)
        self.text_options.draw(screen)
        self.text_credits.draw(screen)
        self.text_exit.draw(screen)
        pygame.display.flip();

class Difficult():
    def __init__(self):
        self.image = pygame.image.load('resources/background_easy.jpg')

        self.button_easy = Button('resources/Boton_dificultad1.png',512,250)
        self.button_medium = Button('resources/Boton_dificultad2.png',512,375)
        self.button_hard = Button('resources/Boton_dificultad3.png',512,500)

        self.buttons = pygame.sprite.Group()
        self.buttons.add(self.button_easy)
        self.buttons.add(self.button_medium)
        self.buttons.add(self.button_hard)

        self.configuration = CfgUtils('configuration.cfg')
        self.language = self.configuration.read('Options', 'language')

        self.font = pygame.font.Font('resources/ThrowMyHandsUpintheAirBold.ttf',85)    

        self.title = Text(self.font,self.configuration.read(self.language,'dificult'),(255,255,255),512,70)
        self.text_easy = Text(self.font,self.configuration.read(self.language,'easy'),(255,255,255),512,250)
        self.text_medium = Text(self.font,self.configuration.read(self.language,'medium'),(255,255,255),512,375)
        self.text_hard = Text(self.font,self.configuration.read(self.language,'hard'),(255,255,255),512,500)

        print "Difficult() created"

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.button_easy.rect.collidepoint(event.pos[0],event.pos[1]):
                    leveleasy_start()
                if self.button_medium.rect.collidepoint(event.pos[0],event.pos[1]):
                    levelmedium_start()
                if self.button_hard.rect.collidepoint(event.pos[0],event.pos[1]):
                    levelhard_start()

    def draw(self,screen):
        screen.blit(self.image,(0,0))
        self.buttons.draw(screen)
        self.title.draw(screen)
        self.text_easy.draw(screen)
        self.text_medium.draw(screen)
        self.text_hard.draw(screen)
        pygame.display.flip()

class LevelsSelector():
    def __init__(self, selector, difficult):
        self.selector = selector
        self.difficult = difficult

        if self.difficult == "Easy":
            self.image = pygame.image.load('resources/background_easy.jpg')
            self.level_button = 'resources/Boton_nivel1.png'
        elif self.difficult == "Medium":
            self.image = pygame.image.load('resources/background_medium.jpg')
            self.level_button = 'resources/Boton_nivel2.png'
        elif self.difficult == "Hard":
            self.image = pygame.image.load('resources/background_hard.jpg')
            self.level_button = 'resources/Boton_nivel3.png'

        self.levels = []
        self.numbers = []
        self.text_numbers = []
        self.starscalification = []

        self.configuration = CfgUtils('configuration.cfg')
        self.language = self.configuration.read('Options', 'language')

        self.levels_cfg = CfgUtils('levels.cfg')

        self.font = pygame.font.Font('resources/ThrowMyHandsUpintheAirBold.ttf',85)    

        self.buttons_levels = pygame.sprite.Group()
        self.califications_levels = pygame.sprite.Group()

        self.title = Text(self.font,self.configuration.read(self.language,'levels'),(255,255,255),512,70)

        for i in range(0,15):
            self.numbers.append(i+1)
            self.calification_level = self.levels_cfg.read(self.difficult,str(i+1+self.selector))
            if i <5:
                self.levels.append(Button(self.level_button,174+175*i,250))
                self.text_numbers.append(Text(self.font,self.numbers[i]+self.selector,(255,255,255),174+175*i,250))
                self.starscalification.append(StarsCalification(int(self.calification_level),174+175*i,305))
            elif i>=5 and i<10:
                self.levels.append(Button(self.level_button,174+175*i-875,425))
                self.text_numbers.append(Text(self.font,self.numbers[i]+self.selector,(255,255,255),174+175*i-875,425))
                self.starscalification.append(StarsCalification(int(self.calification_level),174+175*i-875,480))
            elif i>=10:
                self.levels.append(Button(self.level_button,174+175*i-1750,+600))
                self.text_numbers.append(Text(self.font,self.numbers[i]+self.selector,(255,255,255),174+175*i-1750,600))
                self.starscalification.append(StarsCalification(int(self.calification_level),174+175*i-1750,655))
            self.buttons_levels.add(self.levels[i])
            self.califications_levels.add(self.starscalification[i])

        print "LevelsSelector() created"

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                for i in range(0,15):  
                    if self.levels[i].rect.collidepoint(event.pos[0],event.pos[1]):
                        game_start(i+1,self.difficult)

    def draw(self,screen):
        screen.blit(self.image,(0,0))
        self.buttons_levels.draw(screen)
        self.califications_levels.draw(screen)
        for i in range(0,15):
            self.text_numbers[i].draw(screen)
        self.title.draw(screen)
        pygame.display.flip()      
        

class Options():
    def __init__(self):
        self.configuracion = CfgUtils('configuracion.cfg')
        self.lenguaje = self.configuracion.leer('Options', 'lenguaje')

        self.fuente = pygame.font.Font('resources/ThrowMyHandsUpintheAirBold.ttf',85)

        self.title = Texto(self.fuente,self.configuracion.leer(self.lenguaje,'options'),(255,255,255),512,70)

    def update(self):
        for event in pygame.event.get():
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    exit()
    
    def draw(self,screen):
        screen.fill((0,0,0))
        self.title.draw(screen)
        pygame.display.flip()   
        
        
class Game():
    def __init__(self,level,difficult):
        self.levels_names= [
                       "La Cibeles - Madrid(Spain)",
                       "Fontana di Trevi - Roma(Italy)",
                       "Kiosko - Tampico(Mexico)",
                       "Metropolitano -Tampico(Mexico)",
                       "Muralla China - China",
                       "Casa Blanca - Washington(USA)",
                       "Torre Eiffel - Paris (France)",
                       "Partenon - Atenas(Grece)",
                       "Arco del Triunfo - Francia(Paris)",
                       "Taj Mahal - Agra (India)",
                       "Gran Piramide - Giza(Egipto)",
                       "Estatua Libertad - N. York(USA)",
                       "Coliseo de Roma - Roma(Italy)",
                       "Chichen Itza - Yucatan(Mexico)",
                       "Cristo Rendentor - Rio(Brasil)",
                       "Opera Sydney - Sydney(Australia)",
                       "Lincoln M. - Washington(USA)",
                       "Puerta de Alcala - Madrid(Spain)",
                       "Esfinge - Giza(Egipto)",
                       "Big Ben - Londres(England)",
                       "London Eye - Londres(England)",
                       "Torre de Pisa - Pisa(Italy)",
                       "Moais - Pascua(Chile)",
                       "Machu Picchu - Urubamba(Peru)",
                       "Stonehenge - Wiltshire(U.K.)",
                       "Cat.S.Basilio - Moscu(Rusia)",
                       "Sirenita - Copenhague(Dinamarca)",
                       "Kiyomizu Dera - Kioto(Japon)",
                       "Monte Fuji - Honshu(Japon)",
                       "Piramides - Teotihuacan(Mexico)",
                       "Catedral - Santiago (Spain)",
                       "Acueducto - Segovia(Spain)",
                       "Cuevas - Altamira (Spain)"]

        self.level = level
        self.difficult = difficult 
        
        self.configuration = CfgUtils('configuration.cfg')
        self.language = self.configuration.read('Options', 'language')

        self.rating_level = CfgUtils('levels.cfg')
        self.current_rating_level = int(self.rating_level.read(self.difficult,str(self.level)))
        
        self.color = (0,0,0)
        
        #Level Creator
        for Level in range(1,31):
            if Level==self.level:
                self.image = pygame.image.load('resources/bgnivel'+str(Level)+'.jpg')
                self.name = self.levels_names[Level-1]
        
        self.font = pygame.font.Font('resources/ThrowMyHandsUpintheAirBold.ttf',35)        
        self.level_title = Text(self.font,self.name,self.color,SCREEN_WIDTH/2,30)

        #Timer 
        self.timer = Timer()
        self.timer.start()

        self.star = Star(self.difficult)        
        self.button_nextlevel = ButtonNextLevel()
        self.sprites = pygame.sprite.Group()
        self.sprites.add(self.star)
        self.sprites.add(self.button_nextlevel)

        self.posx_text_nextlevel = 1124

        if self.difficult == "Easy":
            self.title_shadow = pygame.image.load('resources/sombra_titulo_nivel1.png')
        elif self.difficult == "Medium":
            self.title_shadow = pygame.image.load('resources/sombra_titulo_nivel2.png')
        elif self.difficult == "Hard":
            self.title_shadow = pygame.image.load('resources/sombra_titulo_nivel3.png')

    def update(self):
        for event in pygame.event.get():
            if event.type == QUIT or event.type == KEYDOWN and event.key == K_ESCAPE:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                if self.star.rect.collidepoint(event.pos[0],event.pos[1]):
                    self.star.mover = True
                    if self.timer.time()<2:
                        self.rating_level.write(3)
                    elif self.timer.time()>=2 and self.timer.time()<= 4:
                        if self.current_rating_level == 3:
                            pass
                        else:
                            self.rating_level.write(2)
                    elif self.timer.time()> 4:
                        if self.current_rating_level == 2 or self.current_rating_level == 3:
                            pass
                        else:
                            self.rating_level.write(1)
                    self.timer.stop()
                if self.button_nextlevel.rect.collidepoint(event.pos[0],event.pos[1]):
                    game_start(self.level+1,self.difficult)
        
        self.star.update()

        if self.star.rect.x >= 1024:
            self.button_nextlevel.move=True
            self.posx_text_nextlevel -= 10
            if self.posx_text_nextlevel<=890:
                self.posx_text_nextlevel = 890

        if self.button_nextlevel.move:
            self.button_nextlevel.update()
            
    def draw(self,screen):
        #self.texto_temporizador para que no de error al draw.
        #self.texto_temporizador = Texto(self.fuente, self.temporizador.time(),self.color,SCREEN_WIDTH/2,60)
        self.text_nextlevel = Text(self.font,self.configuration.read(self.language,'nextlevel'),self.color,self.posx_text_nextlevel,650)

        screen.blit(self.image,(0,0))
        screen.blit(self.title_shadow,(0,0))
        self.level_title.draw(screen)
        #self.texto_temporizador.draw(screen)
        self.sprites.draw(screen)
        self.text_nextlevel.draw(screen)
        pygame.display.flip()

'''
####################################################
#               FUNCTIONS                          #
#              SCENE CHANGES                       #
####################################################
'''
def game_start(level,difficult):
    print "Changed scene to Game() Level: "+str(level)+ " Difficult: "+difficult
    global scene;
    scene = Game(level,difficult)

def options_start():
    print "Changed scene to Options()"
    global scene
    scene = Options()

def difficult_start():
    print "Changed scene to Difficult()"
    global scene
    scene = Difficult()

def leveleasy_start():
    print "Changed scene to LevelsSelector(Easy)"
    global scene
    scene = LevelsSelector(0,"Easy")

def levelmedium_start():
    print "Changed scene to LevelsSelector(Medium)"
    global scene
    scene = LevelsSelector(0,"Medium")  

def levelhard_start():
    print "Changed scene to LevelsSelector(Hard)"
    global scene
    scene = LevelsSelector(0,"Hard")
scene = None

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))
pygame.display.set_caption("WITS for PC v1.0")
pygame.display.set_icon(pygame.image.load("resources/star.png"))
print "Windows created"

'''
####################################################
#              MAIN LOOP                           #
####################################################
''' 
def main():
    global scene
    pygame.init()
    
    clock = pygame.time.Clock()

    scene=Menu()

    while True:
        clock.tick()
        scene.update()
        scene.draw(screen)
        
if __name__ == '__main__':
    main()
