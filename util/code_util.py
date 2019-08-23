from selenium import webdriver
from PIL import Image
import pytesseract
from util.ShowapiRequest import ShowapiRequest
# driver = webdriver.Chrome()
#
# driver.get("https://www.showapi.com/auth/reg")
# driver.maximize_window()
# driver.save_screenshot('1.png')
#
# code_element = driver.find_element_by_id('checkImg')
# left = code_element.location['x']
# top = code_element.location['y']
# right = code_element.size['width']+left
# height = code_element.size['height']+top
# print(left,top,right,height)
# im = Image.open('1.png')
# # print(im)
# # img = im.crop((left,top,right,height))
# # print(img)
# # img.save('2.png')
t1=Image.open('3.png')
text = pytesseract.image_to_string(t1)
print("t",text)
# python3.6.5
# 需要引入requests包 ：运行终端->进入python/Scripts ->输入：pip install requests

# r = ShowapiRequest("http://route.showapi.com/184-4","62626","d61950be50dc4dbd9969f741b8e730f5" )
# r.addFilePara("image", '2.png')
# r.addBodyPara("typeId", "35")
# r.addBodyPara("convert_to_jpg", "0")
# r.addBodyPara("needMorePrecise", "0")
# res = r.post()
# print(res.text) # 返回信息




# driver.quit()
