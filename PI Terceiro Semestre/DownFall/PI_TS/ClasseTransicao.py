import pygame

class Transisao():
    def __init__(self, tela, personagem):
        self.inimigos = True
        self.porta = (605,90,64,64)
        self.f_1 = True
        self.f_2 = False
        self.tela = tela
        self.vermelho = (255, 0, 0)
        self.personagem = personagem


    def Nivel_2(self,jorges):

        if jorge_0 <= 0 and jorge_1 <= 0 and jorge_2 <= 0:
            pygame.draw.rect(self.tela,self.vermelho,self.porta)
            if self.porta[1] + 64 >= self.personagem.jogador_y and self.porta[1] <= self.personagem.jogador_y + 64:
                if self.porta[0] + 64 >= self.personagem.jogador_x and self.porta[0] <= self.personagem.jogador_x + 64:
                    self.f_1 = False
                    self.f_2 = True
                    self.personagem.jogador_x = 605
                    self.personagem.jogador_y = 610
                    print("bateu")