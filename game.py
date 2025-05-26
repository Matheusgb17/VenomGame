import pygame
import sys
import os

pygame.init()

# Tamanho da tela
LARGURA, ALTURA = 1000, 563
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("This that pink venom")

# Função para carregar imagens
def carregar_animacoes(caminho, prefixo, quantidade):
    imagens = []
    for i in range(1, quantidade + 1):
        caminho_imagem = os.path.join(caminho, f"{prefixo}{i}.png")
        imagem = pygame.image.load(caminho_imagem).convert_alpha()
        imagens.append(imagem)
    return imagens

# Fundo
fundo = pygame.image.load("assets/cenario.png").convert()

# Animações
anim_intro = carregar_animacoes("assets/sprites/animation", "animation", 20)
anim_walkL = carregar_animacoes("assets/sprites/walkL", "walkL_", 10)
anim_walkR = carregar_animacoes("assets/sprites/walkR", "walkR_", 10)
anim_stdL = carregar_animacoes("assets/sprites/standL", "std_", 13)
anim_stdR = carregar_animacoes("assets/sprites/standR", "std_", 13)
anim_jmpL = carregar_animacoes("assets/sprites/jmpL", "jmp_", 11)
anim_jmpR = carregar_animacoes("assets/sprites/jmpR", "jmp_", 11)
anim_hitL = carregar_animacoes("assets/sprites/hit1L", "hit_", 18)
anim_hitR = carregar_animacoes("assets/sprites/hit1R", "hit_", 18)

# Classe Jogador
class JogadorAnimado:
    def __init__(self):
        self.estado = "intro"
        self.direcao = "right"
        self.frame_atual = 0
        self.contador_frames = 0
        self.tempo_entre_frames = 5
        self.x = LARGURA // 2
        self.y_base = ALTURA - 75
        self.y = self.y_base
        self.velocidade = 4
        self.velocidade_y = 0
        self.gravidade = 1
        self.forca_pulo = -18
        self.em_pulo = False
        self.usando_poder = False
        self.animacoes = {
            "intro": anim_intro,
            "walkL": anim_walkL,
            "walkR": anim_walkR,
            "stdL": anim_stdL,
            "stdR": anim_stdR,
            "jmpL": anim_jmpL,
            "jmpR": anim_jmpR,
            "hitL": anim_hitL,
            "hitR": anim_hitR,
        }

    def atualizar_estado(self, teclas):
        if self.estado == "intro":
            return

        # Se está usando o poder, ignora entrada de teclas até a animação acabar
        if self.usando_poder:
            return

        estado_anterior = self.estado

        # Poder especial
        if teclas[pygame.K_z] and not self.em_pulo:
            self.estado = "hitL" if self.direcao == "left" else "hitR"
            self.usando_poder = True
            self.frame_atual = 0
            self.contador_frames = 0
            return

        # Detecção de pulo
        if teclas[pygame.K_SPACE] and not self.em_pulo:
            self.velocidade_y = self.forca_pulo
            self.em_pulo = True

        # Movimento horizontal
        movendo = False
        if teclas[pygame.K_a]:
            self.x -= self.velocidade
            self.direcao = "left"
            movendo = True
        elif teclas[pygame.K_d]:
            self.x += self.velocidade
            self.direcao = "right"
            movendo = True

        # Estado com base no movimento e pulo
        if self.em_pulo:
            self.estado = "jmpL" if self.direcao == "left" else "jmpR"
        elif movendo:
            self.estado = "walkL" if self.direcao == "left" else "walkR"
        else:
            self.estado = "stdL" if self.direcao == "left" else "stdR"

        if self.estado != estado_anterior:
            self.frame_atual = 0
            self.contador_frames = 0

    def atualizar_animacao(self):
        self.contador_frames += 1
        if self.contador_frames >= self.tempo_entre_frames:
            self.contador_frames = 0
            self.frame_atual += 1

            if self.estado == "intro":
                if self.frame_atual >= len(self.animacoes["intro"]):
                    self.estado = "stdR"
                    self.direcao = "right"
                    self.frame_atual = 0
            else:
                anim = self.animacoes[self.estado]
                if self.frame_atual >= len(anim):
                    if "jmp" in self.estado:
                        self.frame_atual = len(anim) - 1
                    elif "hit" in self.estado:
                        self.usando_poder = False
                        self.frame_atual = 0
                        self.estado = "stdL" if self.direcao == "left" else "stdR"
                    else:
                        self.frame_atual = 0

        # Gravidade
        if self.em_pulo:
            self.velocidade_y += self.gravidade
            self.y += self.velocidade_y
            if self.y >= self.y_base:
                self.y = self.y_base
                self.velocidade_y = 0
                self.em_pulo = False
                self.frame_atual = 0
                self.contador_frames = 0

    def desenhar(self, tela):
        animacao = self.animacoes[self.estado]
        frame_index = self.frame_atual % len(animacao)
        imagem = animacao[frame_index]
        tela.blit(imagem, (self.x - imagem.get_width() // 2, self.y - imagem.get_height()))

# Instanciar jogador
jogador = JogadorAnimado()

# Loop principal
relogio = pygame.time.Clock()
executando = True

while executando:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False

    teclas = pygame.key.get_pressed()

    tela.blit(fundo, (0, 0))

    jogador.atualizar_estado(teclas)
    jogador.atualizar_animacao()
    jogador.desenhar(tela)

    pygame.display.flip()
    relogio.tick(60)

pygame.quit()
sys.exit()
