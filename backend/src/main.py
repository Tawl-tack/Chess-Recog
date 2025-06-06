import fen_converter as fc
import os

# import chess
if __name__ == "__main__":
    try:
        FEN = fc.convert_to_fen()
    except ValueError as e:
        print(f"Erro: {e}")




     
