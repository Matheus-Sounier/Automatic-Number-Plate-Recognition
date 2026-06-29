from ultralytics import YOLO
import cv2

imagem = "Resources/5.jpg"  # qualquer foto serve para testar

for caminho in ["models/vehiculos/best.pt", "models/yolov8n.pt", "models/yolov10n.pt"]:
    print(f"\nTestando: {caminho}")
    model = YOLO(caminho)
    results = model.predict(imagem, conf=0.1)
    
    print(f"  Classes do modelo: {model.names}")
    print(f"  Detecções encontradas: {len(results[0].boxes)}")
    
    for box in results[0].boxes:
        cls_id = int(box.cls)
        conf = float(box.conf)
        print(f"    → Classe: {model.names[cls_id]} | Confiança: {conf:.2f}")
    
    # Salva imagem anotada
    saida = f"resultado_{caminho.replace('/', '_').replace('.pt', '')}.jpg"
    results[0].save(filename=saida)
    print(f"  Imagem salva em: {saida}")