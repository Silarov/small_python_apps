import urllib.request
import os
import time

urllib.request.urlretrieve("https://counterintuity.com/wp-content/uploads/2015/06/smiley-163510_1280-1280x640.jpg","smiley.jpg")
os.startfile('smiley.jpg')
time.sleep(5)
os.remove("smiley.jpg") 