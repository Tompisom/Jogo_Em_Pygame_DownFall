import pygame
import threading
import time
tempo = 0

pygame.init()

tela = pygame.display.set_mode((720, 480))
pygame.display.set_caption("DOWNFALL")

preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0,0,255)
cont = 0


class jogador(): #Classecom tudo que envolve o jogador
    def __init__(self, jogador_x, jogador_y):

        self.jogadori = pygame.image.load('jogado.png')
        self.jogador_x = jogador_x
        self.jogador_y = jogador_y
        self.arma = (self.jogador_x + 17, self.jogador_y - 60, 30, 60)
        self.vel = 5
        self.vida_jogador = 3

    def desenhar_jogador(self):
        if self.vida_jogador > 0:
            self.hitbox = (self.jogador_x , self.jogador_y, 64, 64)
            tela.blit(self.jogadori,(self.jogador_x, self.jogador_y))
            pygame.draw.rect(tela, vermelho, self.hitbox, 1)

    def movimento_jogador(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.jogador_x -= self.vel

        if keys[pygame.K_d]:
            self.jogador_x += self.vel

        if keys[pygame.K_w]:
            self.jogador_y -= self.vel

        if keys[pygame.K_s]:
            self.jogador_y += self.vel

    def colisao_jogador_parede(self):
        if self.jogador_x == 665:
            self.jogador_x -= self.vel
        if self.jogador_x == -5:
            self.jogador_x += self.vel
        if self.jogador_y == 420:
            self.jogador_y -= self.vel
        if self.jogador_y == 0:
            self.jogador_y += self.vel


class armamentos(pygame.sprite.Sprite): #Classe para as armas do jogador
    def __init__(self):
        self.x = 0
        self.y = 0
        self.arma = pygame.image.load('espada.png')
        self.espaco = False
        self.hitbox = (0,0,0,0)
        self.contador = 0
        self.desenhar = False

    def ataque_espada(self, contador):
        keys = pygame.key.get_pressed()
        self.espaco = False

        if keys[pygame.K_SPACE]:
            contador += 1
            print("contador: ", contador)
            if contador < 30:
                self.espaco = True

        else:
            contador = 0

        return contador

    def desenhar_espada(self, x_jogador, y_jogador):

        if self.espaco:
            self.hitbox = (x_jogador + 16, y_jogador - 60, 32, 64)
            pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            tela.blit(self.arma,(x_jogador + 2,y_jogador - 60))
            self.contador += 1





class inimigos(): # Classe para definir movimento e imprirmir os inimigos
    def __init__(self, bixo_x, bixo_y):
        self.bixo_x = bixo_x
        self.bixo_y = bixo_y
        self.bateu = False
        self.hitbox = (self.bixo_x,self.bixo_y,64,64)
        self.vida_inimigo = 3

    def desenhar_inimigo(self):
        if self.vida_inimigo > 0:
            self.hitbox = (self.bixo_x -32, self.bixo_y -32, 64, 64)
            pygame.draw.circle(tela, azul, (self.bixo_x, self.bixo_y), 32)
            pygame.draw.rect(tela,vermelho,self.hitbox,1)

    def movimento_inimigo(self):
        if self.bixo_y == 444:
            self.bateu = True

        if self.bateu == True:
            self.bixo_y -= 2

        if self.bateu == False:
            self.bixo_y += 2

        if self.bixo_y == 20:
            self.bateu = False
    def colisao_inimigo(self):
        if personagem.hitbox[1] + 64 >= self.hitbox[1] and personagem.hitbox[1] <= self.hitbox[1]+ 64:
            if personagem.hitbox[0] + 64 >= self.hitbox[0] and personagem.hitbox[0] <= self.hitbox[0] + 64:
                print(personagem.vida_jogador)
                personagem.vida_jogador -= 1
    def colisao_espada(self):
            if self.hitbox[1] + 64 >= combate.hitbox[1] and self.hitbox[1] +64 <= combate.hitbox[1] + 64:
                if self.hitbox[0] + 64 >= combate.hitbox[0] and self.hitbox[0] +32 <= combate.hitbox[0] + 64:
                    print(self.vida_inimigo)
                    self.vida_inimigo -= 1





run = True
personagem = jogador(50, 50) #Variavel que recebe a classe Jogador
jorge = inimigos(360, 20)    #Variavel que recebe a classe Inimigos
combate = armamentos()       # Classe das Armas

clock = pygame.time.Clock()
frame = 60

while run:

    tela.fill(preto)  # Pinta a tela de preto
    clock.tick(frame)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #Detectar as Teclas




    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas




    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede() #Colisao do jogador

         #Verifica se o espaco foi pressionado

        personagem.desenhar_jogador() #



    if jorge.vida_inimigo > 0:
        jorge.movimento_inimigo() # Movimento do Inimigo (Vertical)
        jorge.desenhar_inimigo()  # Imprime o inimigo
        jorge.colisao_inimigo()
        jorge.colisao_espada()

    cont = combate.ataque_espada(cont)

    pygame.display.update() #Update em tudo

pygame.quit()
