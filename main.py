import time
import cv2
import mediapipe as mp

cam = cv2.VideoCapture(0)
pTime = 0


#mpDraw = mp.solutions.drawing_utils #outil qui dessine

mpFaceMesh = mp.solutions.face_mesh #outil qui detecte la tete

faceMesh = mpFaceMesh.FaceMesh(max_num_faces=2) #nombre de tetes detectables

#drawSpec = mpDraw.DrawingSpec(thickness=1, circle_radius=1) #maillage

frameWidth = 2200 # resolution de l'image

frameHeight = 1500





cam.set(3, frameWidth) #largeur de la fenetre

cam.set(4, frameHeight) #longueur de la fenetre

cam.set(10, 350)#luminosité de la fenêtre



while cam.isOpened():
    success, img = cam.read();
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB); #conversion BGR en RGB
    results = faceMesh.process(imgRGB); #analyse et detection du visage
    emoji = cv2.imread("monkey1.png", cv2.IMREAD_UNCHANGED) #importe l'emoji
    if results.multi_face_landmarks is not None and len(results.multi_face_landmarks) >= 1:  # si un visage est détecté
        for face_landmarks in results.multi_face_landmarks:  # Pour chaque visage
            # ==== 1. Calcul des coordonnées du rectangle autour du visage ====
            height, width, _ = img.shape
            x_min, y_min = width, height
            x_max, y_max = 0, 0

            # Trouver les points extrêmes du visage
            for landmark in face_landmarks.landmark:
                x = int(landmark.x * width)#landmark.x est compris entre [0,1]
                y = int(landmark.y * height)
                if x < x_min:
                    x_min = x
                if y < y_min:
                    y_min = y
                if x > x_max:
                    x_max = x
                if y > y_max:
                    y_max = y

            # Vérification que la zone du visage est valide
            if (x_max - x_min) > 0 and (y_max - y_min) > 0:
                try:
                    # Redimensionne l'emoji à la taille du visage
                    newWidth = x_max-x_min
                    newHeight = y_max-y_min

                    emoji_resized = cv2.resize(emoji, (newWidth, newHeight))

                    # Superposition (blending)


                    for c in range(0, 3):
                        img[y_min:y_max, x_min:x_max, c] = (
                                img[y_min:y_max, x_min:x_max, c] * (1-emoji_resized[:, :, 3]/ 255.0) + #masque de transparence de l'emoji (transparents)
                                emoji_resized[:, :, c] * (emoji_resized[:, :, 3]/ 255.0) #photo opaques
                        )
                except Exception as e:
                    print(f"Vous êtes sortis du cadre")

            # Dessine le maillage sur le visage (optionnel)
            # mpDraw.draw_landmarks(img, face_landmarks, mpFaceMesh.FACEMESH_CONTOURS, drawSpec, drawSpec)

        #cv2.rectangle(img, (x_min, y_min), (x_max, y_max), (0, 255, 0), 2)


    cTime = time.time(); # (mili)seconde actuelle (epoch linux)
    fps = 1/(cTime-pTime) #fps = 1/seconde actuelle-seconde passée

    pTime = cTime #la seconde actuelle devient la seconde passée

    cv2.putText(img, f'FPS: {int(fps)}', (20,70), cv2.FONT_ITALIC, 3, (255,10,10))
    cv2.imshow("Image", img)
    if cv2.waitKey(1)==ord('x'):
        break #"x"" pour quitter
cam.release()







