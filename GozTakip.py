import cv2
import mediapipe as mp
import numpy as np

cap = cv2.VideoCapture(0)
mp_face = mp.solutions.face_mesh
face_mesh = mp_face.FaceMesh(refine_landmarks=True, max_num_faces=1)

# Basit arayüz harfleri
letters = ['A', 'B', 'C', 'D', 'E']
selected_index = 0
typed_text = ''

def get_eye_ratio(landmarks, eye_indices):
    # Göz dikey ve yatay mesafe oranı
    eye = [landmarks[i] for i in eye_indices]
    hor_line = np.linalg.norm(np.array([eye[0].x, eye[0].y]) - np.array([eye[3].x, eye[3].y]))
    ver_line = np.linalg.norm(np.array([eye[1].x, eye[1].y]) - np.array([eye[5].x, eye[5].y]))
    ratio = ver_line / hor_line
    return ratio

while True:
    ret, frame = cap.read()
    if not ret:
        break

    frame = cv2.flip(frame, 1)
    rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    results = face_mesh.process(rgb)

    if results.multi_face_landmarks:
        face_landmarks = results.multi_face_landmarks[0].landmark

        # Sol göz (bizim sağ tarafımıza düşüyor)
        left_eye_indices = [362, 385, 387, 263, 373, 380]
        left_eye_ratio = get_eye_ratio(face_landmarks, left_eye_indices)

        # Sağ göz
        right_eye_indices = [33, 160, 158, 133, 153, 144]
        right_eye_ratio = get_eye_ratio(face_landmarks, right_eye_indices)

        # Ortalama göz kırpma oranı
        blink_ratio = (left_eye_ratio + right_eye_ratio) / 2

        # Göz merkezleri (sol)
        left_eye_center_x = np.mean([face_landmarks[i].x for i in left_eye_indices])

        # Göz yönü
        if left_eye_center_x < 0.4:
            selected_index = max(0, selected_index - 1)
        elif left_eye_center_x > 0.6:
            selected_index = min(len(letters) -1, selected_index +1)

        # Kırpma tespiti (kısa göz kapama)
        if blink_ratio < 0.25:
            typed_text += letters[selected_index]
            cv2.waitKey(500)  # Kırpmayı spamlamasın diye beklet

    # Arayüz çizimi
    h, w, _ = frame.shape
    for idx, letter in enumerate(letters):
        color = (0,255,0) if idx == selected_index else (255,255,255)
        cv2.putText(frame, letter, (50 + idx*60, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 3)

    cv2.putText(frame, 'Typed: ' + typed_text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, (0,0,255), 2)

    cv2.imshow('Eye Writer', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()