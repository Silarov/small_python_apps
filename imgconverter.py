from PIL import Image

for i in range(27):
    imgNumber = str(i)
    imgPath = "/Users/silarov/Documents/Dev/portfolio/img/images/denmark/"
    imgFileName = imgNumber + ".jpg"
    img = Image.open(imgPath + imgFileName).convert('RGB')
    
    outputFilePath = '/Users/silarov/Documents/Dev/portfolio/img/images/denmark_webp/' + imgNumber + '.webp'
    img.save(outputFilePath, 'webp', quality=50)
    
    print(f"Image {imgNumber} saved with 50% quality.")
