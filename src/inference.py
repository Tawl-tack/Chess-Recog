from ultralytics import YOLO
import cv2
import os

if __name__ == "__main__":

    """model = YOLO(r"C:\dev\Chess-Vision-AI\runs\detect\train\weights\best.pt")"""
    model = YOLO(r"C:\dev\Chess-Vision-AI\runs\detect\train\weights\best.pt")
    folder_path = r"C:\dev\Chess-Vision-AI\data\pos_train"

    for arquivo in os.listdir(folder_path): # Lista todos os arquivos da pasta e pega 1/1

        if arquivo.endswith(".jpg") or arquivo.endswith(".png"): # Seleciona apenas as imgs dentro dele

            img_path = os.path.join(folder_path, arquivo) # Junta o nome do arquivo com o caminho dele
            img = cv2.imread(img_path)
            img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converte a imagem para tons de cinza
            img_grey2 = cv2.cvtColor(img_grey, cv2.COLOR_GRAY2RGB) # Coloca ela no padrão RGB
            result = model(img_grey2, save=True, project="runs\detect")
           