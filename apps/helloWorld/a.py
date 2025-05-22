from otkt.instrument import instrument
from b import func_b
from time import sleep

@instrument
def func_a():
    print("func_a")
    sleep(1)
    func_b()