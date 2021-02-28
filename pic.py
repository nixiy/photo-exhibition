from PIL import Image
from PIL.ExifTags import TAGS
from PIL.MpoImagePlugin import MpoImageFile

class ExifDecoder:
    exifDic = {}
    
    def __init__(self, exifRaw):
        # create exif dictionary
        for tag_id, value in exifRaw.items():
            tag = TAGS.get(tag_id, tag_id)
            self.exifDic[tag] = value

    # コントラストをkey->value変換する
    def getContrast(self):
        keyVal = self.exifDic["Contrast"]
        contrast = {
            2:"ハード"
        }
        return contrast[keyVal] if keyVal in contrast else None

    # 露出プログラムをkey->value変換する
    def getExposureProgram(self):
        keyVal = self.exifDic["ExposureProgram"]
        exposureProgram = {
            4:"シャッター優先",
        }
        return exposureProgram[keyVal] if keyVal in exposureProgram else None

    # ホワイトバランスをkey->value変換する
    def getWhiteBalance(self):
        keyVal = self.exifDic["WhiteBalance"]
        whiteBalance = {
            0:"自動"
        }
        return whiteBalance[keyVal] if keyVal in whiteBalance else None

    # 撮影シーンタイプを変換する
    def getSceneCaptureType(self):
        keyVal = self.exifDic["SceneCaptureType"]
        sceneCaptureType = {
            0:"標準",
            1:"風景",
            2:"人物",
            3:"夜景",
        }
        return sceneCaptureType[keyVal] if keyVal in sceneCaptureType else None

    # 色空間を変換する
    def getColorSpace(self):
        keyVal = self.exifDic["ColorSpace"]
        colorSpace = {
            1:"sRGB",
            0xFFFF:"Uncalibrated"
        }
        return colorSpace[keyVal] if keyVal in colorSpace else None

    # 個別画像処理
    def getCustomRendered(self):
        keyVal = self.exifDic["CustomRendered"]
        customRendered = {
            0:"通常処理",
            1:"特殊処理",
        }
        return customRendered[keyVal] if keyVal in customRendered else None

    #
    def getExifElem(self, key):
        return self.exifDic[key] if key in self.exifDic else None

    # 製造元を取得する
    def getMake(self):
        key = "Make"
        return self.getExifElem(key)
    
    # モデルを取得する
    def getModel(self):
        key = "Model"
        return self.getExifElem(key)
    
    # カメラバージョンを取得する
    def getVersion(self):
        key = "Software"
        return self.getExifElem(key)
    
    # 35mm焦点距離を取得する
    def getFocalLengthIn35mmFilm(self):
        key = "FocalLengthIn35mmFilm"
        return self.getExifElem(key)
    
    # ISOを取得する
    def getISO(self):
        key = "ISOSpeedRatings"
        return self.getExifElem(key)
    
    # 解像度を取得する
    def getResolution(self):
        widthKey = "ExifImageWidth"
        width = self.getExifElem(widthKey)
        heightKey = "ExifImageHeight"
        height = self.getExifElem(heightKey)
        if width is not None and height is not None:
            return str(width) + "x" + str(height)

    # Tuple要素を割って値出す系
    def multiConversion(self, key):
        keyVal = self.getExifElem(key)
        return keyVal[0] / keyVal[1] if keyVal is not None else None
        
    # F値を取得する
    def getFNumber(self):
        key = "FNumber"
        return self.multiConversion(key)
    
    # 露出時間を取得する
    def getExposureTime(self):
        key = "ExposureTime"
        return self.multiConversion(key)
    
    # 焦点距離を取得する
    def getFocalLength(self):
        key = "FocalLength"
        return self.multiConversion(key)
    
def main():
    imagePath = "./resource/test.JPG"
    im:MpoImageFile = Image.open(imagePath)
    exif = im.getexif()        
    exifDecoder = ExifDecoder(exif)

    # sample print
    print("############# RICOH #############")
    print("カメラの製造元:➤➤➤",  exifDecoder.getMake())
    print("カメラのモデル:➤➤➤",  exifDecoder.getModel())
    print("Version:➤➤➤",         exifDecoder.getVersion())

    print("解像度:➤➤➤",          exifDecoder.getResolution())
    print("35mm焦点距離:➤➤➤",    exifDecoder.getFocalLengthIn35mmFilm(),"mm")
    print("ISO:➤➤➤",             exifDecoder.getISO())
    print("絞り値:➤➤➤ f",        exifDecoder.getFNumber())
    print("露出時間:➤➤➤",        exifDecoder.getExposureTime())
    print("露出プログラム:➤➤➤",  exifDecoder.getExposureProgram())
    print("焦点距離:➤➤➤",        exifDecoder.getFocalLength(),"mm")
    print("コントラスト:➤➤➤",    exifDecoder.getContrast())
    print("ホワイトバランス:➤➤➤",exifDecoder.getWhiteBalance())
    print("撮影シーン:➤➤➤",      exifDecoder.getSceneCaptureType())
    print("色空間:➤➤➤",          exifDecoder.getColorSpace())
    print("個別画像処理:➤➤➤",    exifDecoder.getCustomRendered())
    print("############# GRiii #############")

if __name__ == "__main__":
    main()
