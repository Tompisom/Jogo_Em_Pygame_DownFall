import pygame
import threading
import random
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
        self.disney = (-200,-200,-200,-200)
        self.hitbox = (self.jogador_x, self.jogador_y, 64, 64)
        self.colidiu = False
        self.cont_invencibilidade = 0

    def desenhar_jogador(self):
        if self.vida_jogador > 0:
            self.hitbox = (self.jogador_x , self.jogador_y, 64, 64)
            tela.blit(self.jogadori,(self.jogador_x, self.jogador_y))
            pygame.draw.rect(tela, vermelho, self.hitbox, 1)
        if self.vida_jogador < 0:
            self.hitbox = self.disney

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

    def colisao_jogador_inimigo(self,jorge_x, jorge_y):
        self.cont_invencibilidade += 1
        if self.colidiu == False:
            if self.hitbox[1] + 64 >= jorge_y and self.hitbox[1] <= jorge_y+ 64:
                if self.hitbox[0] + 64 >= jorge_x and self.hitbox[0] <= jorge_x + 64:
                    print(self.vida_jogador)
                    self.vida_jogador -= 1
                    self.colidiu = True
                    self.cont_invencibilidade = 0
        if self.cont_invencibilidade >80:
            self.colidiu = False


class armamentos(pygame.sprite.Sprite): #Classe para as armas do jogador
    def __init__(self):
        self.x = 0
        self.y = 0
        self.arma = pygame.image.load('espada.png')
        self.espaco = False
        self.hitbox = (0,0,0,0)
        self.contador = 0
        self.desenhar = False
        self.disney = (-200,-200,-200,-200)



    def hora_de_desenhar(self, cont):
        if cont > 80:
            self.desenhar = True


    def desenhar_espada(self, x_jogador, y_jogador):
        if self.contador <= 60 and self.desenhar:
            self.hitbox = (x_jogador + 16, y_jogador - 60, 32, 64)
            pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            tela.blit(self.arma,(x_jogador + 2,y_jogador - 60))
            self.contador += 1

        elif self.contador >= 60:
            self.hitbox = self.disney
            self.desenhar = False
            self.contador = 0


class inimigos(): # Classe para definir movimento e imprirmir os inimigos
    def __init__(self, bixo_x, bixo_y):
        self.bixo_x = bixo_x
        self.bixo_y = bixo_y
        self.bateu = False
        self.hitbox = (self.bixo_x,self.bixo_y,64,64)
        self.vida_inimigo = 3
        self.bixo_hit = False
        self.cont = 0

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
            if self.bixo_hit:
                self.bixo_y -=20


        if self.bateu == False:
            self.bixo_y += 2
            if self.bixo_hit:
                self.bixo_y -=20


        if self.bixo_y == 20:
            self.bateu = False


    def colisao_espada(self):
        self.cont+=1
        if self.hitbox[1] + 64 >= combate.hitbox[1] and self.hitbox[1] +64 <= combate.hitbox[1] + 64 and self.cont>60:
            if self.hitbox[0] + 64 >= combate.hitbox[0] and self.hitbox[0] +32 <= combate.hitbox[0] + 64:
                print(self.vida_inimigo)
                self.vida_inimigo -= 1
                self.bixo_hit = True
                self.cont = 0
        if self.cont>5:
            self.bixo_hit = False


run = True
personagem = jogador(360, 410)                     #Variavel que recebe a classe Jogador
jorge = inimigos(random.randrange(200,600), 20)    #Variavel que recebe a classe Inimigos
combate = armamentos()                             # Classe das Armas

clock = pygame.time.Clock()
frame = 60
chamou = False

while run:

    tela.fill(preto)  # Pinta a tela de preto
    clock.tick(frame)


    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        #Detectar as Teclas
        elif event.type == pygame.KEYDOWN:
        # verifica se as setas foram apertadas e muda a velocidade
            if event.key == pygame.K_SPACE and cont >80:
                combate.hora_de_desenhar(cont)
                cont = 0

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede() #Colisao do jogador
        personagem.colisao_jogador_inimigo(jorge.hitbox[0],jorge.hitbox[1])
         #Verifica se o espaco foi pressionado

        personagem.desenhar_jogador() #



    if jorge.vida_inimigo > 0:
        jorge.movimento_inimigo() # Movimento do Inimigo (Vertical)
        jorge.desenhar_inimigo()  # Imprime o inimigo
        jorge.colisao_espada()


    cont +=1

    pygame.display.update() #Update em tudo

pygame.quit()