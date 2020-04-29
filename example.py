from imagesearch import *

# Search for the github logo on the whole screen
# note that the search only works on your primary screen.

# This is intended to be used as examples to be copy pasted, do not run the whole file at once

#pos = imagesearch("github.png")


# search for the github logo continuously :



#print("image found ", pos[0], pos[1])

# search for the logo on the 0,0,800,600 region
#  (a rectangle starting from the top left going 800 pixels to the right and down 600 pixels)
'''
pos = imagesearcharea("github.png", 0, 0, 800, 600)
if pos[0] != -1:
    print("position : ", pos[0], pos[1])
    pyautogui.moveTo(pos[0], pos[1])
else:
    print("image not found")

# the im parameter is usefull if you plan on looking for several different images without the need for recapturing the screen
# the screen capture being one of the most time consuming function it's a good way to optimize

# non -optimized way :
time1 = time.clock()
for i in range(10):
    imagesearcharea("github.png", 0, 0, 800, 600)
    imagesearcharea("panda.png", 0, 0, 800, 600)
print(str(time.clock() - time1) + " seconds (non optimized)")

# optimized way :

time1 = time.clock()
im = region_grabber((0, 0, 1920, 1080))
for i in range(10):
    imagesearcharea("github.png", 0, 0, 800, 600, 0.8, im)
    imagesearcharea("panda.png", 0, 0, 800, 600, 0.8, im)
print(str(time.clock() - time1) + " seconds (optimized)")

# sample output :

# 1.6233619831305721 seconds (non optimized)
# 0.4075934110084374 seconds (optimized)


# click image is to be used after having found the image

pos = imagesearch("github.png")
if pos[0] != -1:
    click_image("github.png", pos, "right", 0.2, offset=5)
'''

digitList = ["0.png","1.png","2.png","3.png","4.png","5.png","6.png","7.png","8.png","9.png"]
def chkPrice(dollarPos):
    dList = []
    for a in digitList:
        digitPos = imagesearcharea(a, dollarPos[0] + 25 ,dollarPos[1], dollarPos[0] + 48, dollarPos[1] + 32)
        if digitPos[0] != -1:
            dList.append(digitList.index(a))
            for b in digitList:
                digitPos2 = imagesearcharea(b, digitPos[0] + 25 ,digitPos[1], digitPos[0] + 48, digitPos[1] + 32)
                if digitPos2 != -1:
                    dList.append(digitList.index(b))
                    digitPos3 = imagesearcharea("Comma.png", digitPos[0] + 25, digitPos[1], digitPos[0] + 45, digitPos[1] + 32)

    print(dList)
    return dList[0] * 10 + dList[1]


isOn = True
chestPos = (960, 540)
buyPos = (800, 360)
def Sell(x):
    pyautogui.press("/")
    pyautogui.typewrite('ah sell {}'.format(x))
    pyautogui.press("enter")
    click_image("Pickaxe.png",buyPos,"left", 0.2, offset=0)
while isOn:
    pickPos = imagesearch_loop("Pickaxe.png", 0.5)
    scrollPos = imagesearch_loop("Scroll.png", 0.5)
    if pickPos[0] != -1:
        pyautogui.moveTo(pickPos)
        silkTextPos = imagesearch("SilkText.png", 0.5)
        dollarPos = imagesearch("Dollar.png", 0.5)
        price = chkPrice(dollarPos)
        print(price)
        if silkTextPos[0] != -1 and price < 55:
            click_image("Pickaxe.png", pickPos, "left", 0.2, offset=0)
            time.sleep(0.3)
            click_image("Pickaxe.png",buyPos,"left", 0.2, offset=0)
            pyautogui.press("esc")
            time.sleep(0.3)
            Sell(65000)

    if scrollPos[0] != -1:
        pyautogui.moveTo(scrollPos)
        scrollTextPos = imagesearch("ScrollText.png", 0.8)
        dollarPos = imagesearch("Dollar.png", 0.5)
        price = chkPrice(dollarPos)
        if scrollTextPos[0] != -1 and price < 95:
            click_image("Scroll.png", scrollPos, "left", 0.2, offset=0)
            click_image("Pickaxe.png", buyPos, "left", 0.2, offset=0)
            click_image("Pickaxe.png", buyPos, "left", 0.2, offset=0)
            Sell(100000)

        print("image not founn")
        pyautogui.moveTo(chestPos)
        click_image("Pickaxe.png", chestPos, "left", 0.2, offset=0)
        time.sleep(0.3)
        pyautogui.typewrite("/ah")
