import requests
import base64
with open('left.png', 'rb') as f:
    left = f.read()
with open('right.png', 'rb') as f:
    right = f.read()
len(left)
len(right)
r = requests.post('http://159.203.98.104:3000/send', data={'sendTo': 'dubchill', 'sendFrom': 'wchill', 'image_left': base64.b64encode(left), 'image_right': base64.b64encode(right)})
print r.text
