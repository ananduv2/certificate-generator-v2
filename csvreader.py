from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import time
import xlwt
from xlwt import Workbook
file1 = open('list.txt', 'r')
# code = time.time()
code = 1633880992
wb = Workbook()
sheet1 = wb.add_sheet('Sheet 1')
x=1
for line in file1:
    pre = "SAC"
    c_id = "%s_%d" % (pre,code)
    code = int(code) + 1
    # c_name = str("certificates/"+c_id+".pdf")
    i_name = str("images/"+c_id+".jpeg")
    img = Image.open("c1.jpg")
    draw = ImageDraw.Draw(img)
    selectFont = ImageFont.truetype("FiraSans-Black.ttf", size = 120)
    codeFont = ImageFont.truetype("overpass-mono-regular.otf", size = 50)
    draw.text( (1670,880), line, (255,255,255),anchor="ma",font=selectFont,align ="center")
    draw.text( (300,115), c_id, (255,255,255),anchor="ma",font=codeFont,align ="center")
    # sheet1.write(x, 0, line)
    # sheet1.write(x, 1, c_id)
    # x = x + 1
    # img.save( c_name, "PDF", resolution=72.0)
    img.save( i_name, "JPEG", resolution=72.0)
    # wb.save('certificate data.xls')
