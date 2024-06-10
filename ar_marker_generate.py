import cv2
import numpy as np

#ArUco辞書を取得
#DICT_4X4_50...4×4のArUcoマーカーを含む50個のマーカーセット
dictionary = cv2.aruco.getPredefinedDictionary(cv2.aruco.DICT_4X4_50)

#マーカーサイズの指定
# ---> 一辺400ピクセルのマーカーが生成
marker_size = 400

#---4つのArUcoマーカーの生成---
#IDが0から3までの4つのArUcoマーカーを生成したいためrange(0,4)と指定
for i in range(0, 4):
    
    #ArUcoマーカーの画像の初期化
    marker_image = np.zeros((marker_size, marker_size), dtype=np.uint8)
    #ArUcoマーカーの生成
    arker_image = cv2.aruco.generateImageMarker(dictionary, i, marker_size, marker_image, 1)
    #生成された#ArUcoマーカーの画像の保存
    cv2.imwrite(f"marker_{i}.jpg", marker_image)

