# 🎮 Animação com Estados em Pygame

Este projeto é uma simulação interativa em Python usando Pygame, que representa um personagem animado com diversos estados (parado, andando, pulando, usando poder especial) controlado por teclado. O personagem utiliza sprites individuais para cada ação e direção, simulando um autômato finito determinístico (AFD) visual.

## 📌 Funcionalidades

- ✅ Animação inicial de introdução automática
- ✅ Movimentação para esquerda (`A`) e direita (`D`) com animações dedicadas
- ✅ Pulo (`Espaço`) com física de gravidade e animação separada para cada direção
- ✅ Estados de espera (parado olhando para a esquerda ou direita)
- ✅ Poder especial (`Z`) com animações exclusivas (esquerda e direita)
- ✅ Transições entre estados visuais baseadas em teclas pressionadas
- ✅ Controle suave de animações com FPS regulado

## 🎮 Controles

| Tecla       | Ação                                |
|-------------|-------------------------------------|
| `A`         | Andar para a esquerda               |
| `D`         | Andar para a direita                |
| `Espaço`    | Pular                               |
| `Z`         | Ativar poder especial               |
| `ESC`       | Encerrar o jogo (fechar a janela)   |

## 📁 Estrutura do Projeto

```
projeto/
│
├── main.py
├── README.md
├── assets/
│   ├── cenario.png
│   └── sprites/
│       ├── animation/      # animation1.png ... animation20.png
│       ├── walkL/          # walkL_1.png ... walkL_10.png
│       ├── walkR/          # walkR_1.png ... walkR_10.png
│       ├── standL/         # std_1.png ... std_13.png
│       ├── standR/         # std_1.png ... std_13.png
│       ├── jmpL/           # jmp_1.png ... jmp_11.png
│       ├── jmpR/           # jmp_1.png ... jmp_11.png
│       ├── hit1L/          # hit_1.png ... hit_18.png
│       └── hit1R/          # hit_1.png ... hit_18.png
```

## ⚙️ Como Executar

1. **Instale o Python 3.10+**
   - Você pode baixá-lo em https://www.python.org/downloads/

2. **Instale o Pygame**
   ```bash
   pip install pygame
   ```

3. **Execute o jogo**
   No terminal (na pasta do projeto):
   ```bash
   python game.py
   ```

## 🧠 Como Funciona

### 🧱 Estados do Personagem

O personagem possui os seguintes estados, tratados como um autômato:

- `intro`: animação inicial automática
- `walkL`, `walkR`: andando para os lados
- `stdL`, `stdR`: parado virado para a esquerda/direita
- `jmpL`, `jmpR`: pulando para os lados
- `hitL`, `hitR`: atacando com o poder especial

### ⏱️ Sistema de Animação

Cada estado possui uma lista de sprites. A cada X frames (controlado por `tempo_entre_frames`), o próximo sprite da lista é exibido.

### 🧲 Física Simples

- Gravidade simulada com incremento da velocidade vertical (`velocidade_y`).
- Detecção de chão pelo valor de `y` (posição vertical).
- O pulo é um impulso para cima com força controlada por `forca_pulo`.

### 🔁 Fluxo

1. Ao iniciar, o personagem exibe uma animação de entrada.
2. Depois, espera comandos do usuário para mover, pular ou usar o poder.
3. Cada ação muda o `estado`, que define qual conjunto de sprites deve ser animado.

## 🛠️ Tecnologias

- **Python 3.10+**
- **Pygame 2.0+**

## 📌 Possíveis Expansões

- Adicionar colisão com elementos do cenário
- Incluir inimigos ou obstáculos
- Melhorar o sistema de física com aceleração e fricção
- Implementar mais poderes e animações

## 👨‍💻 Autor

Desenvolvido até versão 1.0 por **Matheus Garcia**  
Faculdade: Ciência da Computação – IFMG  

## 📝 Licença

Este projeto está sob a licença MIT. Sinta-se livre para modificar, estudar e reutilizar com créditos ao autor.

## 🖼️ Créditos dos Sprites

Os sprites utilizados neste projeto foram extraídos do site **The Spriters Resource**, especificamente da folha de sprites do jogo *Marvel vs. Capcom*. Todos os créditos pelos sprites pertencem aos criadores originais e à equipe do site:

🔗 [Marvel vs. Capcom - War Machine](https://www.spriters-resource.com/arcade/marvelvscapcom/sheet/74176/)
