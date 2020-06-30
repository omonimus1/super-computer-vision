## 


## Installation

### LInux
```
sudo apt-get update
sudo apt-get install libleptonica-dev 
sudo apt-get install tesseract-ocr 
sudo apt-get install libtesseract-dev
```

### Mac
```
brew install tesseract

```

### On Windows
download binary from https://github.com/UB-Mannheim/tesseract/wiki. then add pytesseract.pytesseract.tesseract_cmd = 'C:\Program Files (x86)\Tesseract-OCR\tesseract.exe' to your script.

### Then you should install python package using pip:
pip install tesseract
pip install tesseract-ocr

## Troubleshooting

* [No path set for terresact, impossible to import](https://stackoverflow.com/questions/50951955/pytesseract-tesseractnotfound-error-tesseract-is-not-installed-or-its-not-i)
*[Tesseract Documentation / FAQ](https://github.com/tesseract-ocr/tessdoc)