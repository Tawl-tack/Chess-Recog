# Chess Vision AI

## Chess Vision – Extensão de navegador para reconhecimento de tabuleiros virtuais

**Descrição do projeto:**

O *Chess Vision* é uma extensão para o Google Chrome que usa IA para reconhecer tabuleiros de xadrez virtuais diretamente da tela do usuário. O público-alvo são pessoas que assistem partidas em vídeo (YouTube, etc.) e querem analisar uma posição sem recriá-la manualmente.

Funcionalidade principal: ao clicar em "escanear", a extensão captura a tela, identifica o tabuleiro e as peças (2D), converte a posição para notação FEN e mostra uma mini-interface com uma engine de análise (ex: Stockfish). Também pode gerar link direto para abrir a posição no chess.com ou lichess.

**Objetivos:**

* Detectar tabuleiros virtuais exibidos na tela.
* Reconhecer posição e tipo de cada peça.
* Gerar notação FEN correspondente.
* Exibir interface leve com Stockfish.
* Evitar reconstrução manual do tabuleiro.

**Diferenciais:**

* Foco em vídeos: basta uma print.
* Compatível com o visual do chess.com e lichess.
* Integração com engine de análise.
* Interface simples e rápida.

---

### ADR

**Divisão vs. detecção total:** decidi analisar a imagem como um todo ao invés de dividir a imagem em 64 quadrados e classificar cada um.
**YOLOv8 vs. YOLOv4:** Optei pelo YOLOv8 pela sua velocidade e precisão, apesar da documentação abrangente do YOLOv4.

---

### Atualização (04/04/2025)

* Organização das pastas finalizada.
* Modelo retreinado localmente.
* Overfitting detectado após 20 epochs.
* Testes em imagens reais funcionaram com fundo padrão.
* Erros começaram com fundos menos previsíveis.
* Solução: treinar com imagens em preto e branco para evitar dependência de cor.

---

### Atualização (05/04/2025)

* Problema com cores resolvido.
* Modelo agora funciona para tabuleiros de chess.com e lichess.
* Ainda falha com tabuleiros de livros.
* Testes com Histogram Equalization e Gaussian Blur não ajudaram.
* Organização de chamadas de arquivos melhorada com `os` e `cv2`.
* Pipeline atual: detecta → corta → redimensiona → pré-processa → envia para modelo.

**Próximo passo:** começar a integração com a extensão do navegador.

