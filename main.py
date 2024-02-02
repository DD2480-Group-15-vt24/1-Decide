from src.data_structures import Input
from src.cmv import CMV
from src.pum import generate_pum
from src.fuv import generate_fuv
from src.decide import decide

if __name__ == "__main__":
    cmv_factory = CMV([False for _ in range(15)])
    cmv_factory.check_LICs()
    cmv = cmv_factory.cmv

    pum = generate_pum(cmv, Input.LCM)
    fuv = generate_fuv(pum, Input.PUV)
    result = decide(fuv)
    print(result)
