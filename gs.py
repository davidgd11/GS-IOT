import cv2
import mediapipe as mp

mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
mp_selfie_segmentation = mp.solutions.selfie_segmentation

hands = mp_hands.Hands(max_num_hands=1, min_detection_confidence=0.7)
segmentacao = mp_selfie_segmentation.SelfieSegmentation(model_selection=1)

comandos = {
    0: "Nenhum dedo levantado",
    1: "Corrosao detectada",
    2: "Objeto intruso detectado",
    3: "Vegetacao proxima detectada",
    4: "Falha estrutural detectada",
    5: "Tudo normal"
}

imagem_fundo = cv2.imread("subestacao.jpg")

def contar_dedos(hand_landmarks, handedness):
    dedos_levantados = 0
    ponta_dedos = [4, 8, 12, 16, 20]
    juntas = [2, 6, 10, 14, 18]

    if handedness == "Right":
        if hand_landmarks.landmark[ponta_dedos[0]].x < hand_landmarks.landmark[juntas[0]].x:
            dedos_levantados += 1
    else:
        if hand_landmarks.landmark[ponta_dedos[0]].x > hand_landmarks.landmark[juntas[0]].x:
            dedos_levantados += 1

    for i in range(1, 5):
        if hand_landmarks.landmark[ponta_dedos[i]].y < hand_landmarks.landmark[juntas[i]].y:
            dedos_levantados += 1

    return dedos_levantados

def main():
    cap = cv2.VideoCapture("sinalizacao.mp4")

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame = cv2.flip(frame, 1)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

        imagem_fundo_redimensionada = cv2.resize(imagem_fundo, (frame.shape[1], frame.shape[0]))

        resultado_segmentacao = segmentacao.process(frame_rgb)
        mask = resultado_segmentacao.segmentation_mask > 0.1

        frame_com_fundo = imagem_fundo_redimensionada.copy()
        frame_com_fundo[mask] = frame[mask]

        resultado = hands.process(frame_rgb)

        if resultado.multi_hand_landmarks and resultado.multi_handedness:
            for i in range(len(resultado.multi_hand_landmarks)):
                mao = resultado.multi_hand_landmarks[i]
                tipo_mao = resultado.multi_handedness[i].classification[0].label
                dedos = contar_dedos(mao, tipo_mao)
                comando = comandos.get(dedos, "Comando desconhecido")

                mp_drawing.draw_landmarks(frame_com_fundo, mao, mp_hands.HAND_CONNECTIONS)

                texto = f"{dedos} dedo(s): {comando}"
                font = cv2.FONT_HERSHEY_SIMPLEX
                scale = 0.9
                thickness = 2
                cor_texto = (0, 0, 0)
                (w, h), _ = cv2.getTextSize(texto, font, scale, thickness)
                x, y = 10, 50

                cv2.rectangle(frame_com_fundo, (x - 5, y - h - 10), (x + w + 5, y + 10), (255, 255, 255), -1)
                cv2.putText(frame_com_fundo, texto, (x, y), font, scale, cor_texto, thickness, cv2.LINE_AA)

        cv2.imshow("DroneGrid com fundo", frame_com_fundo)

        if cv2.waitKey(10) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()