import cv2
import os

DATA_DIR = './data'
numbers = [str(i) for i in range(1, 21)] + ['40', '50', '60', '70', '80', '90', '100', '1000', '1MILLON']
dataset_size = 100  # Puedes ajustar este número si lo deseas

cap = cv2.VideoCapture(0)

for number in numbers:
    label_dir = os.path.join(DATA_DIR, number)

    # Solo forzar a recapturar si es '1' o '2'
    if number in ['1', '2']:
        if not os.path.exists(label_dir):
            os.makedirs(label_dir)
        print(f"\n🔄 Recolectando nuevamente imágenes para el número: {number}")
    else:
        # Para los demás números, solo si no existen
        if os.path.exists(label_dir):
            print(f"⚠️ Ya existen imágenes para '{number}', saltando...")
            continue
        os.makedirs(label_dir)

    print(f"\n💬 Preparándote para capturar imágenes del número: {number}")
    print(f"👉 Coloca tu mano haciendo la seña para '{number}' y presiona 'q' para comenzar...")

    while True:
        ret, frame = cap.read()
        cv2.putText(frame, f'Número: {number} - Presiona "Q" para comenzar',
                    (30, 50), cv2.FONT_HERSHEY_SIMPLEX,
                    1, (0, 255, 0), 2)
        cv2.imshow('Preparación', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    cv2.destroyWindow('Preparación')

    counter = 0
    print("🎬 Capturando imágenes...")
    while counter < dataset_size:
        ret, frame = cap.read()
        img_path = os.path.join(label_dir, f'{counter}.jpg')
        cv2.imwrite(img_path, frame)
        cv2.putText(frame, f'Capturando {counter + 1}/{dataset_size}', (10, 30),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
        cv2.imshow('Capturando', frame)
        counter += 1
        if cv2.waitKey(1) & 0xFF == 27:  # ESC para salir
            break
    cv2.destroyWindow('Capturando')

print("✅ Captura de números completada.")
cap.release()
cv2.destroyAllWindows()
