import time
microwaveON = True
minutes = 5
seconds = 1
temperature = 100

def powerONOFF() :
    start = False
    timeArray = [0, 0, 0, 0]
    minutes = (timeArray[0] * 10 + timeArray[1])
    seconds = (timeArray[2] * 10 + timeArray[3])
    tempArray = ['','','']
    temperature = ''
    if microwaveON :
        microwaveON = False
    else :
        microwaveON = True
    updateDisplay()

def updateDisplay() :
    if microwaveON :
        timeDisplay = f"{minutes:02d}:{seconds:02d}"
        tempDisplay = str(temperature) + '°C'
        print(f"{timeDisplay} | {tempDisplay}")

def microwaveStart():
    if temperature != "":
        if seconds > 60:
            minutes += seconds // 60
            seconds = seconds % 60
        if minutes > 0 and seconds == 0 and start:
            seconds = 60
            minutes -= 1
        if minutes == 0 and seconds == 0:
            start = False
            temperature = ""
            temp_array = ['', '', '']
            updateDisplay()
        if seconds > 0 and start:
            seconds -= 1
            updateDisplay()
            time.sleep(1)
            microwaveStart()

while True :
    pencet = input("")
    if pencet == "ON/OFF" :
        powerONOFF()
    if pencet != "ON/OFF" and (not microwaveON) :
        print("Microwave belum dinyalakan!")
    else :
        if pencet in ['0','1','2','3','4','5','6','7','8','9'] :
            setTime(int(pencet))
        if pencet == "START" :
            microwaveStart()
        if pencet == "SET TEMP" :
            setTemp()
        if pencet == "SELESAI" :
            break

    
