import cv2
import numpy as np
from tkinter import Tk, filedialog
from ultralytics import YOLO

def pre_processing():
        root = Tk()
        root.withdraw()
        file_path = filedialog.askopenfilename(
        title="Selecione a imagem de um Tabuleiro!",
        filetypes= [("imagens", "*.jpg *.jpeg .png")]
        )

        # img_path = os.path.join(folder_path, arquivo) # Junta o nome do arquivo com o caminho dele
        img = cv2.imread(file_path)
        img_grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # Converte a imagem para tons de cinza
        img_grey2 = cv2.cvtColor(img_grey, cv2.COLOR_GRAY2RGB) # Coloca ela no padrão RGB
        
        return img_grey2

def matrix(result):
    boxes = result[0].boxes 
    A = np.zeros((8, 8))

    for box in boxes:
        if int(box.cls[0].item() == 7) and box.conf > 0.8:
            board_x1, board_y1, board_x2, board_y2 = box.xyxy[0].tolist() # Essa trecho é só para achar as coordenadas da borda do tabuleiro.

    for box in boxes:
        if box.conf > 0.6:
            x1, y1, x2, y2 = box.xyxy[0].tolist()

            for index_y in range(0, 8):
                for index_x in range(0, 8):

                    point_y = (2 * (board_y2 - board_y1) * index_y + (board_y2 - board_y1)) / 16 # (y2 - y1) é o tamanho relativo do tabuleiro, só usei ele aqui para fazer a divisão pelo tabuleiro e n pela imagem.
                    point_x = (2 * (board_x2 - board_x1) * index_x + (board_x2 - board_x1)) / 16

                    if (y1 < point_y + board_y1 < y2) and (x1 < point_x + board_x1 < x2) and int(box.cls[0].item() != 7): # Esse + y1 é apenas para somar a parte que falta para os pontos relativos do tabuleiro virarem pontos na imagem em si.
                        if int(box.cls[0]) == 0:
                            A[index_y, index_x] = 13
                        else:  
                            A[index_y, index_x] = int(box.cls[0].item())
    return A

def fen(A):
    piece_name = {13:'B',
                1: 'K',
                2: 'N',
                3: 'P',
                4: 'Q',
                5: 'R',
                6: 'b',
                7: 'board',
                8: 'k',
                9: 'n',
                10: 'p',
                11: 'q',
                12: 'r'}
    count = 0
    fen = ""

    for i in range(0, 8):
        
        for j in range(0, 8):
            if A[i, j] != 0:
                    if count != 0:
                        fen += str(count)
                        count = 0
                    fen += piece_name[A[i, j]]
            else:
                 
                 count += 1
        if count != 0:
                        fen += str(count)
                        count = 0
        if i < 7:
            fen += "/"

    return fen


def convert_to_fen():
    
    img = pre_processing()
    model = YOLO(r"C:\dev\Chess-Vision-AI\runs\detect\train\weights\best.pt")
    result = model(img, save=True, project="runs\detect")
    A = matrix(result)

    FEN = fen(A)
    inv_FEN = fen(A[::-1])
    # https://lichess.org/editor/1kr1q3/pbpB4/1p3r2/4p2p/3nP1pN/2QP2P1/PPP4P/1KR2R2_w_-_-_0_1?color=white
    print("FEN para jogador de branca: https://lichess.org/editor/"+ FEN + "_w_-_-_0_1?color=white")
    print("FEN para jogador de preta: https://lichess.org/editor/" + inv_FEN + "_w_-_-_0_1?color=white")

    return FEN, inv_FEN
    

    
    