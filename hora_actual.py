from datetime import datetime


def uno():
    timestap= 15
    date_time = datetime.fromtimestamp(timestap)
    d=date_time.strftime("%m/%d/%Y, %H:%M:%S")
    print(d)

def dos():
    now = datetime.now()
    fecha = now.strftime("%d/%m/%Y_%H:%M")
    print(fecha)

dos()