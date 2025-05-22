from otkt.instrument import instrument
from time import sleep

@instrument
def func_c():
    sleep(1)
    print("func_c")