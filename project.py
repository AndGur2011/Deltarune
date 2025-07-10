import pygame
pygame.init()
window = pygame.display.set_mode((500, 500)) #
zmina_bg = pygame.image.load("jevil_bg.jpg")                                    #загрузка заднего фона
zmina_bg = pygame.transform.scale(zmina_bg, (500, 500))
game = 1

before_game = pygame.image.load("deltarune.webp")                               #экран перед игрой
before_game = pygame.transform.scale(before_game, (500,500))
window.blit(before_game, (0,0))
text = '''Нажми на союзника (слева) после нажатия'''                            #инструкция
text2 = "появятся враги и их надо будет убить нажатием"
font = pygame.font.Font("Intro.otf", 15)
text_image = font.render(text, True , (255,255,255) )
text_image2 = font.render(text2 , True , (255,255,255))
window.blit(text_image,(50,250))
window.blit(text_image2, (50,275))

location = "menu"

class Kartinka():                                                                #класс картинка
    def __init__(self, width, height, file, x, y):
        self.image = pygame.image.load(file)
        self.image = pygame.transform.scale(self.image, (width, height))
        self.rect = pygame.Rect(x, y, width, height)
        self.visible = False

    def draw(self):
        if self.visible:
            window.blit(self.image, (self.rect.x, self.rect.y))                 
            
knopka_kr = Kartinka(100, 100, "kris_back.png", 80, 120)                        #кнопки-персонажи                                   
knopka_kr.visible = True
knopka_spm = Kartinka(150, 150, "spamtone.png", 250, 70)
knopka_jevil = Kartinka(80, 80, "jevil.png", 270, 200)
knopka_tenna = Kartinka(80,130, "tenna.png", 270, 270)
knopka_sus = Kartinka(100, 100, "susie_back.png", 70, 200)
knopka_sus.visible = False
knopka_rals = Kartinka(100,100, "ralsei_dlt.png", 80, 300)
knopka_kng = Kartinka(150,150, "knight.png", 270,180)
kng_hp = 3

spm_jevil_active = False
                                                                                #игровой цикл
while game:
    if location == "game":
        window.blit(zmina_bg, (0, 0))

        knopka_kr.draw()
        knopka_spm.draw()
        knopka_jevil.draw()
        knopka_sus.draw()
        knopka_kng.draw()
        knopka_rals.draw()
        knopka_tenna.draw()
        if spm_jevil_active and not knopka_spm.visible and not knopka_jevil.visible and not knopka_tenna.visible:
            knopka_sus.visible = True
            knopka_rals.visible = True
    for iw in pygame.event.get():
        if iw.type == pygame.QUIT:
            game = 0
            pygame.quit()

        if iw.type == pygame.MOUSEBUTTONDOWN:                                   #работа кнопки криса
            x, y = pygame.mouse.get_pos()
            if knopka_kr.visible and knopka_kr.rect.collidepoint(x, y):
                pygame.mixer.music.load("School.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                knopka_spm.visible = True
                knopka_jevil.visible = True
                knopka_tenna.visible = True
                spm_jevil_active = True
                knopka_sus.visible = False
                knopka_rals.visible = False
            if location == "menu":
                location = "game"
            
            if knopka_spm.visible and knopka_spm.rect.collidepoint(x, y):        #работа кнопки спамтона
                knopka_spm.visible = False
                pygame.mixer.music.load("attack_slash.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(0)

            if knopka_jevil.visible and knopka_jevil.rect.collidepoint(x, y):    #работа кнопки джевила
                knopka_jevil.visible = False
                pygame.mixer.music.load("attack_slash.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(0)
            if knopka_tenna.visible and knopka_tenna.rect.collidepoint(x, y):    #работа кнопки тенна
                knopka_tenna.visible = False
                pygame.mixer.music.load("attack_slash.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(0)
                
        if iw.type == pygame.MOUSEBUTTONDOWN:                                    #работа кнопки сьюзи и ралзей
            x, y = pygame.mouse.get_pos()
            if knopka_sus.visible and knopka_sus.rect.collidepoint(x, y)or knopka_rals.visible and knopka_rals.rect.collidepoint(x, y):
                pygame.mixer.music.load("The_Chase.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(-1)
                knopka_kng.visible = True
            if knopka_kng.visible and knopka_kng.rect.collidepoint(x, y):        #работа кнопки рыцаря
                pygame.mixer.music.load("attack_slash.mp3")
                pygame.mixer.music.set_volume(0.4)
                pygame.mixer.music.play(0)
                kng_hp -= 1
            if kng_hp == 0:
                knopka_kng.visible = False
    
        
    pygame.display.update()
