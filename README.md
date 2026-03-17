# 🪟 i3wm Dotfiles & Scripts

Minha configuração pessoal do **i3 Window Manager**, incluindo scripts utilitários para controle de brilho, mouse, players de mídia e um timer Pomodoro para o terminal.

---

## 📁 Estrutura do Projeto

```
i3wm/
├── config              # Arquivo de configuração principal do i3wm
├── brightness/
│   └── brightness.sh   # Controle de brilho da tela
├── mouse/
│   └── mouse_control.sh # Controle do mouse via teclado
├── play/
│   ├── play.py          # Script para alternar entre players de mídia
│   └── player_control.sh # Controle de reprodução via playerctl
└── pomato/
    ├── pomato.py        # Timer Pomodoro para o terminal
    ├── fonts.py         # Fontes ASCII para o timer
    ├── analise.py       # Análise de sessões de foco
    └── alert.ogg        # Som de alerta ao fim do timer
```

---

## ✨ Funcionalidades

### 🖥️ Configuração do i3 (`config`)

- **Mod Key:** `Super` (Mod4)
- **Font:** JetBrains Mono Medium Nerd Font
- **Status bar:** i3blocks
- Workspaces numerados de 1 a 10
- Atalhos para navegação, redimensionamento e movimentação de janelas
- `focus_follows_mouse` desativado

### 💡 Controle de Brilho (`brightness/brightness.sh`)

Controla o brilho do monitor usando `brightnessctl`.

```bash
./brightness.sh incress   # Aumenta 5%
./brightness.sh decress   # Diminui 5%
```

Mapeado no i3 para as teclas de função de brilho:
```
XF86MonBrightnessUp   → aumenta brilho
XF86MonBrightnessDown → diminui brilho
```

---

### 🖱️ Controle do Mouse pelo Teclado (`mouse/mouse_control.sh`)

Permite mover o cursor e clicar sem usar o mouse físico, usando `xdotool`.

```bash
./mouse_control.sh up         # Move 50px para cima
./mouse_control.sh down       # Move 50px para baixo
./mouse_control.sh left       # Move 50px para esquerda
./mouse_control.sh right      # Move 50px para direita
./mouse_control.sh up-slow    # Move 10px para cima
./mouse_control.sh down-slow  # Move 10px para baixo
./mouse_control.sh left-slow  # Move 10px para esquerda
./mouse_control.sh right-slow # Move 10px para direita
./mouse_control.sh click      # Clique esquerdo
./mouse_control.sh rightclick # Clique direito
```

Ativado no i3 com `Super+M` (entra no `mouse_mode`):

| Tecla | Ação |
|-------|------|
| `h/j/k/l` | Mover (esq/baixo/cima/dir) rápido |
| `s/f/d/g` | Mover devagar |
| `n / c` | Clique esquerdo |
| `m / v / x` | Clique direito |
| `Esc` | Sair do mouse_mode |

---

### 🎵 Controle de Players de Mídia (`play/`)

Gerencia múltiplos players de mídia simultaneamente via `playerctl`, permitindo alternar entre eles dinamicamente.

**`play.py`** — detecta os players ativos e alterna entre eles via um contador salvo em arquivo.

**`player_control.sh`** — interface de controle:

```bash
./player_control.sh toggle-player  # Alterna o player ativo (+ notificação)
./player_control.sh play-pause     # Play/Pause no player atual
./player_control.sh play           # Play
./player_control.sh pause          # Pause
./player_control.sh next           # Próxima faixa
./player_control.sh previous       # Faixa anterior
```

Atalhos no i3:

| Atalho | Ação |
|--------|------|
| `Super+Shift+M` | Alternar player ativo |
| `Super+P` | Play/Pause |
| `Super+,` | Faixa anterior |
| `Super+.` | Próxima faixa |

---

### 🍅 Pomato — Timer Pomodoro no Terminal (`pomato/`)

Timer Pomodoro minimalista para o terminal, com display em ASCII art e alerta sonoro ao final.

```bash
python3 pomato/pomato.py [-w 25] [-f tty-clock]
```

| Opção | Descrição | Padrão |
|-------|-----------|--------|
| `-w`  | Duração do período de trabalho (minutos) | 5 |
| `-f`  | Fonte do display (`tty-clock` ou `braille-y`) | tty-clock |

- Pressione **Ctrl+C** para sair a qualquer momento
- Requer terminal com no mínimo **8 linhas** e **34 colunas**
- Toca `alert.ogg` ao fim do timer (requer `paplay`)

---

## ⌨️ Atalhos Principais do i3

| Atalho | Ação |
|--------|------|
| `Super+Enter` | Abrir terminal |
| `Super+Q` | Fechar janela |
| `Super+D` | dmenu (lançador de apps) |
| `Super+F` | Fullscreen |
| `Super+Shift+Space` | Alternar janela flutuante |
| `Super+Shift+?` | Alternar layout |
| `Super+Setas` | Mover foco |
| `Super+Shift+Setas` | Mover janela |
| `Super+1~0` | Ir para workspace |
| `Super+Shift+1~0` | Mover janela para workspace |
| `Super+Shift+C` | Recarregar config |
| `Super+Shift+R` | Reiniciar i3 |
| `Super+Shift+Q` | Sair do i3 |

---

## 🔧 Dependências

| Ferramenta | Uso |
|------------|-----|
| `i3wm` | Window manager |
| `i3blocks` | Status bar |
| `brightnessctl` | Controle de brilho |
| `xdotool` | Controle do mouse via teclado |
| `playerctl` | Controle de players de mídia |
| `pactl` | Controle de volume (PulseAudio) |
| `paplay` | Reprodução de áudio (alerta do Pomato) |
| `xss-lock` + `i3lock` | Bloqueio de tela |
| `nm-applet` | Gerenciamento de redes |
| `dex` | Autostart de apps XDG |
| `JetBrains Mono Nerd Font` | Fonte da interface |
| Python 3 | Scripts `play.py` e `pomato.py` |

---

## 🚀 Instalação

1. Clone o repositório:
   ```bash
   git clone https://github.com/Michel-Rooney/i3wm.git ~/.config/i3
   ```

2. Instale as dependências (Debian/Ubuntu):
   ```bash
   sudo apt install i3 i3blocks brightnessctl xdotool playerctl pulseaudio-utils i3lock xss-lock network-manager-gnome dex
   ```

3. Reinicie o i3 com `Super+Shift+R` ou faça logout/login.

---

## 📝 Licença

Este projeto é de uso pessoal. Sinta-se livre para usar e adaptar conforme sua necessidade.
