#--------------------------------------------------------------------------------------------------------
# Importando Bibliotecas

# É necessária instalar:
# Digite "pip install pygame" no seu console, se você usa windows
import pygame
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# Definindo Constantes

# Dimensões da Tela do Jogo

# As medidas foram feitas de acordo com o meu notebook.
# Se elas superarem o tamanho da sua tela, teremos um problema.
# Se elas foram menores que as dimensões da sua tela, não há problema.

LARGURA_TELA = 1366
ALTURA_TELA = 728

# Imagens

# Todas as imagens foram feitas com base nas dimensões da tela.

IMAGEM_FUNDO = pygame.image.load('imagens/fundo.jpg')
IMAGEM_ESTRADA_MOVE = pygame.image.load('imagens/estrada-move.png')
IMAGEM_MOVE = pygame.image.load('imagens/move.png')
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# Classes (ou objetos)

# ônibus move
class move:

    # posição do ônibus (x,y)
    def __init__(self, x, y):
        self.imagem = IMAGEM_MOVE
        self.x = x
        self.y = y
        self.velocidade = 5

    def desenhar(self, tela):
        tela.blit(self.imagem, (self.x, self.y))

    def  andar_frente(self):
        # andar pra frente é incrementar a posição x em que o busão é desenhado na tela
        self.x += self.velocidade
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# Funções

# Desenha a tela do jogo
# Recebe como parâmetro a tela que será desenhada
def desenhar_tela(tela, onibus_move):
    
    # Desenha a imagem de fundo na tela do jogo, dando a posição inicial (x,y) como parâmetro
    tela.blit(IMAGEM_FUNDO, (0,0))

    # Desenha a estrada do move na tela do jogo, dando a posição inicial (x,y) como parâmetro
    tela.blit(IMAGEM_ESTRADA_MOVE, (0,0))

    # Desenha o ônibus move na tela do jogo, utilizando sua própria função de se desenhar
    onibus_move.desenhar(tela)

    # Atualiza a tela
    pygame.display.update()

# Função principal
# Ela chama todas as outras funções
def main():

    # Criando a tela do jogo
    # É passado um par de números relativos às dimensões da tela (x,y)
    tela  = pygame.display.set_mode( (LARGURA_TELA, ALTURA_TELA) )

    # Criando o objeto do ônibus move
    # (100,600) -> posição inicial
    onibus_move = move(345,651)

    # O jogo está rodando
    rodando = True

    while rodando:

        # pygame.event.get() retorna uma lista de eventos
        # examplo: apertar uma tecla é um evento
        for event in pygame.event.get():

            # Se apertou o "x" da janela
            if event.type == pygame.QUIT:
                rodando = False
                # fecha a janela (o jogo)
                pygame.quit()
                # finaliza o código
                quit()

        # Chaves é um vetor que guardara o estado de todas as teclas permitidas de serem analisadas
        # esse estado será 1 ou 0, para está sendo pressionada ou não está sendo pressionada
        chaves = pygame.key.get_pressed()

        # caso o estado da tecla "d" seja 1, então ela está sendo pressionada
        if chaves[pygame.K_d]:
            # vai ser atualizada a posição x do busão antes dele ser desenhado na tela
            onibus_move.andar_frente()

        desenhar_tela(tela, onibus_move)
#--------------------------------------------------------------------------------------------------------

#--------------------------------------------------------------------------------------------------------
# Executa a função principal
main()
#--------------------------------------------------------------------------------------------------------
