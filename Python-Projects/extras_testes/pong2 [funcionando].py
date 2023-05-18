import pygame
import random

# Inicialização do Pygame
pygame.init()

# Definição das dimensões da janela do jogo
largura_janela = 800
altura_janela = 400
tela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Pong")

# Cores
cor_branca = (255, 255, 255)
cor_vermelha = (255, 0, 0)

# Variáveis do jogo
largura_raquete = 10
altura_raquete = 60
raquete_velocidade = 5
bola_raio = 10
bola_velocidade_x = 3
bola_velocidade_y = 3

# Posição inicial das raquetes
posicao_raquete_esquerda = altura_janela // 2 - altura_raquete // 2
posicao_raquete_direita = altura_janela // 2 - altura_raquete // 2

# Posição inicial da bola
posicao_bola_x = largura_janela // 2
posicao_bola_y = altura_janela // 2

# Pontuação inicial
pontuacao_esquerda = 0
pontuacao_direita = 0

# Loop principal do jogo
jogo_ativo = True
clock = pygame.time.Clock()

while jogo_ativo:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jogo_ativo = False

    # Movimentação das raquetes
    teclas_pressionadas = pygame.key.get_pressed()
    if teclas_pressionadas[pygame.K_w] and posicao_raquete_esquerda > 0:
        posicao_raquete_esquerda -= raquete_velocidade
    if teclas_pressionadas[pygame.K_s] and posicao_raquete_esquerda < altura_janela - altura_raquete:
        posicao_raquete_esquerda += raquete_velocidade
    if teclas_pressionadas[pygame.K_UP] and posicao_raquete_direita > 0:
        posicao_raquete_direita -= raquete_velocidade
    if teclas_pressionadas[pygame.K_DOWN] and posicao_raquete_direita < altura_janela - altura_raquete:
        posicao_raquete_direita += raquete_velocidade

    # Movimentação da bola
    posicao_bola_x += bola_velocidade_x
    posicao_bola_y += bola_velocidade_y

    # Verificação de colisão com as bordas da janela
    if posicao_bola_y > altura_janela - bola_raio or posicao_bola_y < bola_raio:
        bola_velocidade_y *= -1
    if posicao_bola_x > largura_janela - bola_raio or posicao_bola_x < bola_raio:
        bola_velocidade_x *= -1

    # Verificação de colisão com as raquetes
    if posicao_bola_x - bola_raio <= largura_raquete and \
            posicao_raquete_esquerda <= posicao_bola_y <= posicao_raquete_esquerda + altura_raquete:
        bola_velocidade_x *= -1
    elif posicao_bola_x + bola_raio >= largura_janela - largura_raquete and \
            posicao_raquete_direita <= posicao_bola_y <= posicao_raquete_direita + altura_raquete:
        bola_velocidade_x *= -1

    # Verificação de pontuação
    if posicao_bola_x < bola_raio:
        pontuacao_direita += 1
        posicao_bola_x = largura_janela // 2
        posicao_bola_y = altura_janela // 2
        bola_velocidade_x *= random.choice([-1, 1])
        bola_velocidade_y *= random.choice([-1, 1])
    elif posicao_bola_x > largura_janela - bola_raio:
        pontuacao_esquerda += 1
        posicao_bola_x = largura_janela // 2
        posicao_bola_y = altura_janela // 2
        bola_velocidade_x *= random.choice([-1, 1])
        bola_velocidade_y *= random.choice([-1, 1])

    # Preenchimento da tela
    tela.fill(cor_branca)

    # Desenho das raquetes
    pygame.draw.rect(tela, cor_vermelha, (0, posicao_raquete_esquerda, largura_raquete, altura_raquete))
    pygame.draw.rect(tela, cor_vermelha,
                     (largura_janela - largura_raquete, posicao_raquete_direita, largura_raquete, altura_raquete))

    # Desenho da bola
    pygame.draw.circle(tela, cor_vermelha, (posicao_bola_x, posicao_bola_y), bola_raio)

    # Desenho da pontuação
    fonte = pygame.font.Font(None, 36)
    texto_esquerda = fonte.render(str(pontuacao_esquerda), True, cor_vermelha)
    texto_direita = fonte.render(str(pontuacao_direita), True, cor_vermelha)
    tela.blit(texto_esquerda, (largura_janela // 4, 10))
    tela.blit(texto_direita, (largura_janela // 4 * 3, 10))

    # Atualização da tela
    pygame.display.flip()
    clock.tick(60)

# Encerramento do Pygame
pygame.quit()
