
# 🛰️ DroneGrid – Monitoramento Inteligente em Falta de Energia

## ⚠️ Descrição do Problema

A falta de energia elétrica compromete o funcionamento de hospitais, centros de comando, indústrias e serviços essenciais. Atualmente, as inspeções em infraestruturas elétricas são manuais, demoradas e colocam técnicos em risco.  
Há uma demanda urgente por soluções tecnológicas que auxiliem na identificação rápida de falhas, especialmente em situações de emergência ou baixa visibilidade.

## ✅ Visão Geral da Solução

**DroneGrid** é um sistema de monitoramento inteligente que utiliza Python e MediaPipe para interpretar **gestos manuais** realizados por operadores em campo, simulando a comunicação visual em inspeções de subestações e linhas de transmissão.

O sistema reconhece a quantidade de dedos levantados, associando cada gesto a um tipo de falha (ou status). O fundo do vídeo é substituído por uma imagem de subestação para simular o ambiente real.

## 🎯 Comandos por Gestos

| Dedos Levantados | Interpretação                     |
|------------------|-----------------------------------|
| 0 dedos          | Verificação concluída             |
| 1 dedo           | Corrosão detectada                |
| 2 dedos          | Objeto intruso detectado          |
| 3 dedos          | Vegetação próxima à rede          |
| 4 dedos          | Falha estrutural detectada        |
| 5 dedos          | Tudo normal                       |

## 🛠️ Tecnologias Utilizadas

- **Python 3.10+**
- **MediaPipe (Google)** – detecção de mãos e segmentação
- **OpenCV** – vídeo, desenho e manipulação de imagens
- **cv2.VideoWriter** – gravação do vídeo processado com legendas

## 📸 Instruções de Uso

1. Instale as dependências:
   ```bash
   pip install mediapipe opencv-python
   ```

2. Certifique-se de ter:
   - Um vídeo de entrada (`sinalizacao.mp4`)
   - Uma imagem de fundo (`subestacao.jpg`)

3. Rode o script principal:

   ```bash
   python gs.py
   ```

## 🎥 Vídeo Demonstrativo

🔗 Assista ao vídeo: [📺 DroneGrid - Demonstração do Projeto](https://www.youtube.com/watch?v=SEU-LINK-AQUI)

## 📂 Código Fonte

```
📁 dronegrid/
├── dronegrid.py
├── sinalizacao.mp4
├── subestacao.jpg
└── video_saida.mp4
```

## 👥 Integrantes

| Nome               | RM       |
|--------------------|----------|
| David G. B. Denunci| RM98603  |
| Lucas P. de Toledo | RM97913  |

## 📝 Licença

Este projeto foi desenvolvido para fins educacionais no contexto da disciplina de IoT aplicada com Python e Visão Computacional.
