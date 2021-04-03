import pygame
import random
tempo = 0

pygame.init()


class jogador(): #Classecom tudo que envolve o jogador
    def __init__(self, jogador_x, jogador_y):

        self.jogadori = pygame.image.load('Sheet_Jogador.png')
        self.jogador_x = jogador_x
        self.jogador_y = jogador_y
        self.arma = (self.jogador_x + 17, self.jogador_y - 60, 30, 60)
        self.vel = 5
        self.vida_jogador = 3
        self.disney = (-200,-200,-200,-200)
        self.hitbox = (self.jogador_x, self.jogador_y, 64, 64)
        self.colidiu = False
        self.cont_invencibilidade = 0
        self.vida_jogadori = pygame.image.load('vida_jogado.png')
        self.x_imagem_vida = 0
        self.x_imagem_jogador = 0
        self.cont_animacao = 0

    def desenhar_jogador(self):
        if self.vida_jogador > 0:
            self.hitbox = ((self.jogador_x + 10), (self.jogador_y + 4), 42, 58) #para ficar junto do jogador
            tela.blit(self.jogadori,(self.jogador_x+11, self.jogador_y+5),(self.x_imagem_jogador, 0, 40, 58))
            pygame.draw.rect(tela, vermelho, self.hitbox, 1)
        if self.vida_jogador < 0:
            self.hitbox = self.disney

    def hud_vida(self):
        if self.vida_jogador == 3:
            tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 128, 39))
        if self.vida_jogador == 2:
            self.x_imagem_vida = 42
            tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 128, 39))
        if self.vida_jogador == 1:
            self.x_imagem_vida = 84
            tela.blit(self.vida_jogadori, (50, 10), (self.x_imagem_vida, 0, 128, 39))


    def movimento_jogador(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            self.jogador_x -= self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador= 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_d]:
            self.jogador_x += self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_w]:
            self.jogador_y -= self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_s]:
            self.jogador_y += self.vel
            self.cont_animacao += 1
            if self.cont_animacao == 10:
                if self.x_imagem_jogador == 420:
                    self.x_imagem_jogador = 0
                    self.cont_animacao = 0
                self.x_imagem_jogador += 42
                self.cont_animacao = 0

        if keys[pygame.K_s] == False and keys[pygame.K_w] == False and keys[pygame.K_d] == False and keys[pygame.K_a]==False:
            self.x_imagem_jogador = 0
            self.cont_animacao = 0

    def colisao_jogador_parede(self):
        if self.jogador_x == 1100:
            self.jogador_x -= self.vel
        if self.jogador_x == 115:
            self.jogador_x += self.vel
        if self.jogador_y == 645:
            self.jogador_y -= self.vel
        if self.jogador_y == 205:
            self.jogador_y += self.vel

    def colisao_jogador_inimigo(self,inimigo_hitbox):
        self.cont_invencibilidade += 1

        if self.colidiu == False:
                   #y              altura           y                  y                   y                      altura
            if self.hitbox[1] + self.hitbox[3] >= inimigo_hitbox[1] and self.hitbox[1] <= inimigo_hitbox[1] + inimigo_hitbox[3]:
                if self.hitbox[0] + self.hitbox[2] >= inimigo_hitbox[0] and self.hitbox[0] <= inimigo_hitbox[0] + inimigo_hitbox[2]:
                    print(self.vida_jogador)
                    self.vida_jogador -= 1
                    self.colidiu = True
                    self.cont_invencibilidade = 0
        if self.cont_invencibilidade >120:
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
        self.disney = (-200,-200,-200,-200) # Disney é uma variavel que retica as coisa da tela.
        self.dano = 1
        self.buff_dano = False
        self.nova_espada = (605, 390, 64, 64)
        self.pegou = False



    def hora_de_desenhar(self, cont): #ferifica se o jogador não está espando o espaço, e depois libera para desenhar
        if cont > 80:
            self.desenhar = True


    def desenhar_espada(self, x_jogador, y_jogador):
        if self.contador <= 60 and self.desenhar:
            self.hitbox = (x_jogador + 16, y_jogador - 60, 32, 64)
            pygame.draw.rect(tela, vermelho, self.hitbox, 1)
            tela.blit(self.arma,(x_jogador + 2,y_jogador - 60))
            self.contador += 1 #contador que faz a espada ficar na tela por 1 segundo = 60 FPS

        elif self.contador >= 60:
            self.hitbox = self.disney #nesse caso a disney esta removendo a hit.box da espada, tivemos alguns erros aqui.
            self.desenhar = False
            self.contador = 0

    def melhorias (self,jorge_0,jorge_1,jorge_2,jogador_x,jogador_y):
        if jorge_0 <= 0 and jorge_1 <= 0 and jorge_2 <= 0 and self.pegou ==False:
            pygame.draw.rect(tela,vermelho,self.nova_espada)
            if self.nova_espada[1] + 64 >= jogador_y and self.nova_espada[1] <= jogador_y + 64:
                if self.nova_espada[0] + 64 >= jogador_x and self.nova_espada[0] <= jogador_x + 64:
                    self.dano = 3
                    self.pegou = True


class inimigos(): # Classe para definir movimento e imprirmir os inimigo
    def __init__(self, bixo_x, bixo_y,vida):

        self.bixo_x = bixo_x
        self.bixo_y = bixo_y
        self.hitbox = (0, 0, 0, 0)
        self.bixo_hit = False  # Faz com que o bixo vá para tras quando é atingido
        self.disney = (-200,-200,-200,-200)
        #Variaveis Jorge
        self.bateu = False
        self.vida_inimigo = vida
        self.cont = 0 #cont para não dar hit.kill no inimigo, fazendo muitas colisões ela serve para mandar o inimigo para tras tbm
        self.jorgei_frente = pygame.image.load('JorgeSheet.png')
        self.jorgei_costas = pygame.image.load('JorgeSheetContas.png')
        self.x_animacao_jorge = 0
        self.cont_animacao = 0
        #--------------------------------------Divisão de Variaveis-----------------------------------------------------------
        #Variaveis Roberto
        self.campo_visao = (self.bixo_x-125, self.bixo_y-125, 250, 250)
        self.robertoi = pygame.image.load('Cachorro_Sheet.png')
        self.x_animacao_roberto = 0
        self.avistado = False

        #Variaveis Jeorgia
        #Buff Jogador


    def desenhar_inimigo_jorge(self):
        if self.vida_inimigo > 0:
            self.hitbox = (self.bixo_x -24, self.bixo_y -32, 46, 64)
            pygame.draw.rect(tela,vermelho,self.hitbox,1)
            self.cont_animacao +=1
            if self.bateu == False:
                tela.blit(self.jorgei_frente, (self.bixo_x - 26, self.bixo_y - 32), (self.x_animacao_jorge, 0, 49, 64))
                if self.cont_animacao == 10:
                    if self.x_animacao_jorge == 400:
                        self.x_animacao_jorge = 0
                        self.cont_animacao = 0
                    self.x_animacao_jorge += 50
                    self.cont_animacao = 0
            if self.bateu == True:
                tela.blit(self.jorgei_costas, (self.bixo_x - 26, self.bixo_y - 32), (self.x_animacao_jorge, 0, 49, 64))
                if self.cont_animacao == 10:
                    if self.x_animacao_jorge == 400:
                        self.x_animacao_jorge = 0
                        self.cont_animacao = 0
                    self.x_animacao_jorge += 50
                    self.cont_animacao = 0
        else:
            self.hitbox = self.disney


    def movimento_inimigo_jorge(self):
        if self.bixo_y == 668:
            self.bateu = True

        if self.bateu == True:
            self.bixo_y -= 2
            if self.bixo_hit:
                self.bixo_y -=20


        if self.bateu == False:
            self.bixo_y += 2
            if self.bixo_hit:
                self.bixo_y -=20

        if self.bixo_y == 240 or self.bixo_y < 240:
            self.bateu = False


    def colisao_espada(self,espada_hitbox,dano):
        self.cont+=1
        if self.hitbox[1] + self.hitbox[3] >= espada_hitbox[1] and self.hitbox[1] +espada_hitbox[3] <= espada_hitbox[1] + espada_hitbox[3] and self.cont>60:
            if self.hitbox[0] + self.hitbox[2] >= espada_hitbox[0] and self.hitbox[0] + espada_hitbox[2] <= espada_hitbox[0] + espada_hitbox[2]:
                self.vida_inimigo -= dano
                self.bixo_hit = True
                self.cont = 0
                print(self.vida_inimigo)
        if self.cont>5:
            self.bixo_hit = False


    def desenhar_inimigo_roberto(self):
        if self.vida_inimigo > 0:
            self.hitbox = (self.bixo_x -32, self.bixo_y -32, 62, 44)
            self.campo_visao = (self.bixo_x - 125, self.bixo_y - 125, 250, 250)
            tela.blit(self.robertoi, (self.bixo_x - 32, self.bixo_y - 32), (self.x_animacao_roberto, 0, 60, 44))
            #tela.blit(self.robertoi, (self.bixo_x - 32, self.bixo_y - 32))
            pygame.draw.rect(tela,vermelho,self.hitbox,1)
            pygame.draw.rect(tela, vermelho, self.campo_visao, 1)
            if self.avistado == True:
                self.cont_animacao += 1
                if self.cont_animacao == 10:
                    if self.x_animacao_roberto == 549:
                        self.x_animacao_roberto = 0
                        self.cont_animacao = 0
                    self.x_animacao_roberto += 61
                    self.cont_animacao = 0
        else:
            self.hitbox = self.disney
            print('Foi Para a Disney')


    def movimento_inmigo_roberto(self,x_jogador,y_jogador):
        if self.campo_visao[1] + 250 >= y_jogador and self.campo_visao[1] <= y_jogador + 64:
            if self.campo_visao[0] + 250 >= x_jogador and self.campo_visao[0] <= x_jogador + 64:
                if x_jogador + 32 > self.bixo_x:
                    self.bixo_x += 1
                if x_jogador + 32 < self.bixo_x:
                    self.bixo_x -= 1
                if y_jogador + 32 > self.bixo_y:
                    self.bixo_y += 1
                if y_jogador + 32 < self.bixo_y:
                    self.bixo_y -= 1
                self.avistado = True
            else:
                self.avistado = False
        else:
            self.avistado = False

    def desenhar_inimigo_jeorgia(self):
        if self.vida_inimigo > 0:
            self.hitbox = ((self.bixo_x -32), (self.bixo_y -32), 64, 64)
            pygame.draw.rect(tela,vermelho,self.hitbox,1)
            pygame.draw.circle(tela, verde, (self.bixo_x, self.bixo_y), 32)
        else:
            self.hitbox = self.disney

    def movimento_inimigo_jeorgia(self):
        if self.bixo_x == 1100:
            self.bateu = True

        if self.bateu == True:
            self.bixo_x -= 4
            if self.bixo_hit and self.bixo_y > 200:
                self.bixo_y -=20

        if self.bateu == False:
            self.bixo_x += 4
            if self.bixo_hit and self.bixo_y > 200:
                self.bixo_y -=20

        if self.bixo_x == 180:
            self.bateu = False


class Transisao():
    def __init__(self):
        self.inimigos = True
        self.porta = (605,150,64,64)
        self.f_1 = True
        self.f_2 = False
        self.jorge = []
        self.jeorgia = []
        self.roberto = []
        self.randomizador_jorge = [200,300,400,500,600,700,800,900,1000]
        self.randomizador_jeorgia = [200,300,400,500,564]


    def Nivel_2(self,jorge_0,jorge_1,jorge_2,jogador_x,jogador_y):

        if jorge_0 <= 0 and jorge_1 <= 0 and jorge_2 <= 0:
            pygame.draw.rect(tela,vermelho,self.porta)
            if self.porta[1] + 64 >= jogador_y and self.porta[1] <= jogador_y + 64:
                if self.porta[0] + 64 >= jogador_x and self.porta[0] <= jogador_x + 64:
                    self.f_1 = False
                    self.f_2 = True
                    personagem.jogador_x = 605
                    personagem.jogador_y = 610
                    print("bateu")

    def recarregar_f1(self):
        random.shuffle(self.randomizador_jorge)
        for zonas in range(3):
            self.jorge.append(inimigos(self.randomizador_jorge[zonas], 240,3))

    def recarregar_f2(self):
        self.jeorgia = []
        random.shuffle(self.randomizador_jeorgia)
        for zonas in range(2):
            self.jeorgia.append(inimigos(200, self.randomizador_jeorgia[zonas],3))

        self.jorge = []
        self.jorge.append(inimigos(600, 160,3))

        self.roberto = []
        self.roberto.append(inimigos(640, 400,5))
        self.roberto.append(inimigos(840, 400,5))


tela = pygame.display.set_mode((1280, 800))
pygame.display.set_caption("DOWNFALL")

fase_1 = pygame.image.load('Fase_1.png')
fase_2 = pygame.image.load('Fase_2.png')

preto = (0, 0, 0)
vermelho = (255, 0, 0)
azul = (0,0,255)
verde = (0,160,0)
cont = 0 #cont para o ataque do jogador serve para impedir que o jogador fique apertando espaço que nem um demente

run = True
personagem = jogador(605, 610)                              #Variavel que recebe a classe Jogador
nivel = Transisao()

nivel.recarregar_f1()

combate = armamentos()                                      #Classe das Armas            #Inimigo que persegue o jogador

clock = pygame.time.Clock()
frame = 60


def primeira_fase(tela, fase_1, personagem, combate):

    tela.blit(fase_1, (0, 0))  # Pinta a tela de preto

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.hud_vida()
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.colisao_jogador_inimigo(nivel.jorge[0].hitbox)  # verifica se o jogador foi atingido pelo inimigo
        print(nivel.jorge[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[2].hitbox)
        personagem.desenhar_jogador()



    for jorges in nivel.jorge:
        if jorges.vida_inimigo >=0:
            jorges.movimento_inimigo_jorge()  # Movimento do Inimigo (Vertical)
            jorges.desenhar_inimigo_jorge()  # Imprime o inimigo
            jorges.colisao_espada(combate.hitbox,combate.dano)

    nivel.Nivel_2(nivel.jorge[0].vida_inimigo,nivel.jorge[1].vida_inimigo
                  ,nivel.jorge[2].vida_inimigo,personagem.jogador_x,personagem.jogador_y)

    combate.melhorias(nivel.jorge[0].vida_inimigo,nivel.jorge[1].vida_inimigo
                  ,nivel.jorge[2].vida_inimigo,personagem.jogador_x,personagem.jogador_y)

    pygame.display.update()  # Update em tudo

    if nivel.f_2 == True:
        nivel.recarregar_f2()


def segunda_fase(tela, fase_2, personagem,combate):
    tela.blit(fase_2, (0, 0))  # Pinta a tela de preto

    combate.desenhar_espada(personagem.jogador_x, personagem.jogador_y)  # Imprime a espadas

    if personagem.vida_jogador > 0:
        personagem.movimento_jogador()  # Movimento do jogador
        personagem.colisao_jogador_parede()  # Colisao do jogador
        personagem.desenhar_jogador()
        personagem.colisao_jogador_inimigo(nivel.roberto[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.roberto[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[0].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jeorgia[1].hitbox)
        personagem.colisao_jogador_inimigo(nivel.jorge[0].hitbox)
        personagem.hud_vida()

    for robertos in nivel.roberto:
        if robertos.vida_inimigo >= 0:
            robertos.desenhar_inimigo_roberto()
            robertos.colisao_espada(combate.hitbox,combate.dano)
            robertos.movimento_inmigo_roberto(personagem.jogador_x, personagem.jogador_y)

    for jeorgias in nivel.jeorgia:
        if jeorgias.vida_inimigo >= 0:
            jeorgias.desenhar_inimigo_jeorgia()
            jeorgias.colisao_espada(combate.hitbox,combate.dano)
            jeorgias.movimento_inimigo_jeorgia()

    for jorges in nivel.jorge:
        if jorges.vida_inimigo >= 0:
            jorges.movimento_inimigo_jorge()  # Movimento do Inimigo (Vertical)
            jorges.desenhar_inimigo_jorge()  # Imprime o inimigo
            jorges.colisao_espada(combate.hitbox,combate.dano)




    pygame.display.update()  # Update em tudo


while run:

    clock.tick(frame)     # roda o game loop 60 vezes em 1 segundo

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Detectar as Teclas
        elif event.type == pygame.KEYDOWN:
            # verifica se as setas foram apertadas e muda a velocidade
            if event.key == pygame.K_SPACE and cont > 80:  # limita a espada/ataque do jogador
                combate.hora_de_desenhar(cont)
                cont = 0  # zeramos para conseguir obter um timer de quando o jogador poderá utilizar a espada novamente


    if nivel.f_1 == True:
        primeira_fase(tela, fase_1, personagem, combate)


    if nivel.f_2 == True:
        segunda_fase(tela, fase_2, personagem,combate)



    cont += 1  # incrementação do cont do ataque do jogador

pygame.quit()