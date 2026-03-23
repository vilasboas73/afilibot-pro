import cv2
import numpy as np
import os

def criar_video(produto):
    print("Criando vídeo...")

    if not os.path.exists("videos"):
        os.makedirs("videos")

    largura = 720
    altura = 1280

    video = cv2.VideoWriter(
        "videos/teste.mp4",
        cv2.VideoWriter_fourcc(*'mp4v'),
        24,
        (largura, altura)
    )

    for i in range(120):
        frame = np.zeros((altura, largura, 3), dtype=np.uint8)

        cv2.putText(frame, "🔥 PROMOCAO HOJE", (50, 400),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,255), 3)

        cv2.putText(frame, produto["nome"], (50, 550),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        cv2.putText(frame, produto["preco"], (50, 650),
                    cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0,255,0), 3)

        cv2.putText(frame, "COMENTA LINK 👇", (50, 800),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255,255,255), 2)

        video.write(frame)

    video.release()

    print("Vídeo criado com sucesso!")