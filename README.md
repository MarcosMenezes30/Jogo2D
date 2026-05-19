# Alien Invasion Game

## 🎮 O que é o Projeto?

**Alien Invasion** é um jogo 2D desenvolvido em **Python** usando a biblioteca **Pygame**. É um projeto feito durante a disciplina de **AQS (Análise e Qualidade de Software)** na faculdade.

### Objetivo do Jogo
- O jogador controla uma nave espacial na base da tela
- Deve disparar projéteis contra alienígenas que descem do topo
- Alienígenas se movem horizontalmente e descem progressivamente
- O jogo é baseado no clássico "Space Invaders"

---

## 📁 Estrutura do Projeto

```
Jogo2D/
├── README.md                  # Documentação básica
├── .gitignore                 # Configuração do Git
├── venv/                      # Virtual environment (já existe)
├── src/                       # Código-fonte do jogo
│   ├── alien_invasion.py      # Classe principal que gerencia o jogo
│   ├── settings.py            # Configurações do jogo (tamanho, cores, velocidades)
│   ├── ship.py                # Classe da nave do jogador
│   ├── bullet.py              # Classe dos projéteis
│   ├── alien.py               # Classe dos alienígenas
│   ├── heranca.py             # Classe base com herança (ABC)
│   └── monkeytype.sqlite3     # Banco de dados (provavelmente de testes)
└── images/                    # Recursos gráficos
    └── ship.bmp               # Imagem da nave
```

---

## 🔧 Dependências do Projeto

O projeto usa **uma única dependência externa**:

- **pygame** - Biblioteca para desenvolvimento de jogos 2D em Python

Outras dependências são da **biblioteca padrão do Python**:
- `sys` - Controle do sistema
- `abc` - Abstract Base Classes (herança)

---

## 📋 Arquivos Principais

### 1. **alien_invasion.py** (Arquivo Principal)
- Classe `AlienInvasion` - Gerencia o jogo inteiro
- Inicializa o Pygame
- Cria a tela do jogo (1200x800 px)
- Gerencia grupos de objetos: nave, projéteis, alienígenas
- Implementa a lógica principal do jogo (criação de frotas, colisões, etc)
- **Para rodar o jogo**, execute este arquivo

### 2. **settings.py** (Configurações)
Armazena todas as constantes do jogo:
- Tamanho da tela: 1200x800 pixels
- Cor de fundo: RGB(230, 230, 230) - cinza claro
- Velocidades:
  - Nave: 1.5 unidades
  - Projéteis: 1.0 unidades
  - Alienígenas: 0.3 unidades
  - Frota desce: 10 unidades por volta
- Configurações de projéteis (cor, tamanho, limite)

### 3. **ship.py** (Nave do Jogador)
- Carrega imagem `ship.bmp`
- Gerencia posição e movimento da nave
- Controla movimento esquerdo/direito
- Métodos: `blitme()` (desenhar), `update()` (atualizar posição)

### 4. **bullet.py** (Projéteis)
- Cria projéteis disparados pela nave
- Gerencia velocidade e posição
- Remove projéteis quando saem da tela

### 5. **alien.py** (Alienígenas)
- Define o sprite do alienígena
- Gerencia movimento horizontal e vertical
- Usa `pygame.sprite.Sprite` para facilitar colisões

### 6. **heranca.py** (Classe Base)
- Implementa herança com `ABC` (Abstract Base Class)
- Pode ser a base para outras classes do jogo

---

## 🚀 Como Instalar e Rodar (Mac M1 com Python 3 e venv)

### **Pré-requisitos**
- macOS em Mac M1 (ou Intel)
- Python 3.x instalado
- Terminal (zsh é padrão em Macs recentes)

### **Passo 1: Navegar para o diretório do projeto**
```bash
cd /Users/marcao/Programing/Jogo2D
```

### **Passo 2: Ativar o Virtual Environment (venv)**
```bash
source venv/bin/activate
```
Você saberá que o venv está ativo quando aparecer `(venv)` no início da linha do terminal.

### **Passo 3: Verificar a versão do Python**
```bash
python --version
```
Você deve ver Python 3.x (exemplo: Python 3.10.x, Python 3.11.x, etc)

### **Passo 4: Instalar o Pygame**
```bash
pip install pygame
```
Ou se quiser versão específica:
```bash
pip install pygame==2.1.3
```

> **Nota M1**: O Pygame é totalmente compatível com Mac M1 em arquitetura nativa. A instalação via `pip` vai automaticamente baixar a versão correta para ARM64.

### **Passo 5: Verificar Instalação**
```bash
python -c "import pygame; print(pygame.__version__)"
```
Se funcionar sem erros, o Pygame está instalado corretamente.

### **Passo 6: Rodar o Jogo**
```bash
cd src
python alien_invasion.py
```

Ou diretamente do diretório raiz:
```bash
python src/alien_invasion.py
```

---

## 🎮 Controles do Jogo

| Ação | Controle |
|------|----------|
| Mover nave para esquerda | Seta esquerda (`←`) ou tecla `A` |
| Mover nave para direita | Seta direita (`→`) ou tecla `D` |
| Disparar projéteis | Espaço (`SPACE`) |
| Sair do jogo | Fechar a janela ou `ESC` |

---

## 🛠️ Comandos Úteis

### Desativar o venv
```bash
deactivate
```

### Listar pacotes instalados
```bash
pip list
```

### Criar arquivo requirements.txt (recomendado)
```bash
pip freeze > requirements.txt
```

### Instalar de um requirements.txt existente
```bash
pip install -r requirements.txt
```

---

## 📝 Resumo Rápido

```bash
# 1. Ativar venv
source venv/bin/activate

# 2. Instalar pygame
pip install pygame

# 3. Rodar o jogo
python src/alien_invasion.py
```
