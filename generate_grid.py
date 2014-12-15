import random #找隨機的數


def get_int(msg, minimum, default): #取出三個引數 (訊息字串，最小值， 預設值)
    while True: 
        try:
            line = input(msg) #輸入line的值
            if not line and default is not None: #判斷是否有設預設值
                return default #如果有預設值，返回函式
            i = int(line) #如果沒有預設值，i = line
            if i < minimum: #如果i小於最小值
                print("must be >=", minimum) #輸出字串 must be >= 最小值
            else:
                return i #回到i = line
        except ValueError as err: #輸入錯誤時
            print(err) #跑出錯誤訊息


rows = get_int("rows: ", 1, None) #輸入一個符合條件的整數
columns = get_int("columns: ", 1, None) #輸入一個符合條件的整數
minimum = get_int("minimum (or Enter for 0): ", -1000000, 0) #輸入一個符合條件的整數

default = 1000 #預設值 = 1000
if default < minimum: #如果預設值小於最小值
    default = 2 * minimum #預設值等於兩倍的最小值
maximum = get_int("maximum (or Enter for " + str(default) + "): ", 
                  minimum, default) #輸入一個符合條件的整數

row = 0 
while row < rows: #當row小於rows時
    line = "" #line是空字串
    column = 0 
    while column < columns: #當column小於columns
        i = random.randint(minimum, maximum) #i等於介於最大值與最小值間的亂數
        s = str(i) #把i轉成字串
        while len(s) < 10: #當s的長度小於10
            s = " " + s #s等於空字串加s
        line += s #line = line + s
        column += 1 #column = column + 1
    print(line) #輸出line
    row += 1 #row = row + 1
