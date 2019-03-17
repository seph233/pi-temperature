from flask import Flask
from time import sleep

app = Flask(__name__)

@app.route("/gettemperature")
def gettemperature():
    tempStore = open("/sys/bus/w1/devices/28-01131bb90da8/w1_slave")
    data = tempStore.read()
    tempStore.close()
    tempData = data.split("\n")[1].split(" ")[9]
    temperature = float(tempData[2:])
    temperature = temperature/1000
    return str(temperature)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=12001)
    while(1==1):
        print(gettemperature())
        sleep(2)
