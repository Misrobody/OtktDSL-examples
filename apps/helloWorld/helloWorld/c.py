from otkt.tools.instrument import instrument
from otkt.instrument import instrument
from time import sleep

@instrument
@instrument
def func_c():
    sleep(1)
    print("func_c")