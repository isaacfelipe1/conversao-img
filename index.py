import cv2
import os

diretorio = "C:\\testesIsaac\\"

for filename in os.listdir(diretorio):
    if filename.lower().endswith((".jpg", ".jpeg", ".png")):
        filepath = os.path.join(diretorio, filename)
        image = cv2.imread(filepath)
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        extensao = os.path.splitext(filename)[1]
        output_path = os.path.join(diretorio, filename.split(".")[0] + "" + extensao)
        cv2.imwrite(output_path, gray_image)
        print(f"Imagem em escala de cinza salva em: {output_path}")

print("Conversão concluída.")
