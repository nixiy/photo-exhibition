# photo-exhibition

[![CodeQL](https://github.com/nixiy/photo-exhibition/actions/workflows/codeql-analysis.yml/badge.svg)](https://github.com/nixiy/photo-exhibition/actions/workflows/codeql-analysis.yml)

入力画像に正方形になるような余白を加えて、任意で撮影情報も付与する現像ツール

## 環境
- WMware Workstation 16 Player
    - Ubuntu 20.04LTS
- Python 3.8.5
    - Pillow 7.0.0
    - opencv-python 4.5.1.48

## 実装予定
- 画像の解像度を認識して適当な比率で余白を与える
- 撮影情報を余白に吐き出す
    - Exif情報から取ってこれる
- SNS投稿しやすいように軽量化する(5BM以下くらい?)
    - がんばる
- 思いつき次第便利な機能つける

## 対象機種
- RICOH GRIII

## 認識できるExif情報
- カメラの製造元
- カメラのモデル
- 解像度
- 35mm焦点距離
- ISO
- 絞り値
- 露出時間
- 露出プログラム
- 焦点距離
- コントラスト
- ホワイトバランス
- 撮影シーン
- 色空間
- 個別画像処理

## 完成図 (おそらく余白も含めて正方形になる予想)
![feature](https://user-images.githubusercontent.com/12169300/109020279-2e44db00-76fd-11eb-8530-4ba9c4d7f236.jpg)

---

A development tool that adds a square margin to the input image and optionally adds shooting information

## Scheduled to be implemented
- Recognize the resolution of the image and give a margin at an appropriate ratio
- Spit out shooting information in the margin
     - Get from Exif information
- Reduce the weight to make it easier to post on SNS (about 5BM or less?)
     - Work hard
- Add useful functions as soon as you come up with them

## Target model
- RICOH GR III
