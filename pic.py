from PIL import Image
from PIL.ExifTags import TAGS
from PIL.MpoImagePlugin import MpoImageFile

# コントラストをkey->value変換する
def decodeContrast(key):
    contrast = {
        2:"ハード"
    }
    if key in contrast:
        return contrast[key]
    else:
        return None

# 露出プログラムをkey->value変換する
def decodeExposureProgram(key):
    exposureProgram = {
        4:"シャッター優先",
    }
    if key in exposureProgram:
        return exposureProgram[key]
    else:
        return None

# ホワイトバランスをkey->value変換する
def decodeWhiteBalance(key):
    whiteBalance = {
        0:"自動"
    }
    if key in whiteBalance:
        return whiteBalance[key]
    else:
        return None

# 撮影シーンタイプを変換する
def decodeSceneCaptureType(key):
    sceneCaptureType = {
        0:"標準",
        1:"風景",
        2:"人物",
        3:"夜景",
    }
    if key in sceneCaptureType:
        return sceneCaptureType[key]
    else:
        return None    

# 色空間を変換する
def decodeColorSpace(key):
    colorSpace = {
        1:"sRGB",
        0xFFFF:"Uncalibrated"
    }
    if key in colorSpace:
        return colorSpace[key]
    else:
        return None

# 個別画像処理
def decodeCustomRendered(key):
    customRendered = {
        0:"通常処理",
        1:"特殊処理",
    }
    if key in customRendered:
        return customRendered[key]
    else:
        return None

def main():
    imagePath = "./resource/test.JPG"
    im:MpoImageFile = Image.open(imagePath)
    exif = im.getexif()

    exifDic = {}

    # create exif dictionary
    for tag_id, value in exif.items():
        tag = TAGS.get(tag_id, tag_id)
        exifDic[tag] = value

    # sample print
    print("############# RICOH #############")
    print("カメラの製造元:➤➤➤", exifDic["Make"])
    print("カメラのモデル:➤➤➤", exifDic["Model"])
    print("Version:➤➤➤", exifDic["Software"])

    print("解像度:➤➤➤",exifDic["ExifImageWidth"],"x",exifDic["ExifImageHeight"])
    print("35mm焦点距離:➤➤➤",exifDic["FocalLengthIn35mmFilm"],"mm")
    print("ISO:➤➤➤", exifDic["ISOSpeedRatings"])
    print("絞り値:➤➤➤ f",exifDic["FNumber"][0]/exifDic["FNumber"][1])
    print("露出時間:➤➤➤", exifDic["ExposureTime"][0],"/",exifDic["ExposureTime"][1])
    print("露出プログラム:➤➤➤", decodeExposureProgram(exifDic["ExposureProgram"]))
    print("焦点距離:➤➤➤", exifDic["FocalLength"][0]/exifDic["FocalLength"][1],"mm")
    print("コントラスト:➤➤➤", decodeContrast(exifDic["Contrast"]))
    print("ホワイトバランス:➤➤➤", decodeWhiteBalance(exifDic["WhiteBalance"]))
    print("撮影シーン:➤➤➤", decodeSceneCaptureType(exifDic["SceneCaptureType"]))
    print("色空間:➤➤➤", decodeColorSpace(exifDic["ColorSpace"]))
    print("個別画像処理:➤➤➤", decodeCustomRendered(exifDic["CustomRendered"]))
    print("############# GRiii #############")

if __name__ == "__main__":
    main()
