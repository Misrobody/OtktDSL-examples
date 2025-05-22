from otkt.tools.instrument import instrument
from otkt.instrument import instrument
from c import func_c
from time import sleep

@instrument
@instrument
def func_b():
    print("func_b")
    sleep(1)
    func_c()