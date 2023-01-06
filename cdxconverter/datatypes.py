# INT8, UINT8, INT16, UINT16, INT32, UINT32,FLOAT64
#little ending
import struct

class byteOverFlow(Exception):...

def UNSIGNED(func):
    bit = func()
    def wapper(val):
        return val&((1<<bit)-1)
    return wapper

def SIGNED(func):
    bit     = func()
    flag    = (1<<bit)-1
    tag     = 1<<(bit-1)
    effect  = flag^tag
    def wapper(val):
        tmp = val & flag
        if tmp == tag:
            raise byteOverFlow(f"INT{bit} overflow {val}->fmt:{tmp}")
        if tmp & tag > 0:
            # <0
            tmp = tmp & effect
            tmp = (tmp - 1) ^ effect
            return -1 * tmp
        else:
            return tmp
    return wapper

@SIGNED
def INT8():
    return 8

@UNSIGNED
def UINT8():
    return 8

@SIGNED
def INT16():
    return 16

@UNSIGNED
def UINT16():
    return 16

@SIGNED
def INT32():
    return 32

@UNSIGNED
def UINT32():
    return 32

def FLOAT64(val):
    tmp = val&0xffff_ffff_ffff_ffff
    tmp = struct.unpack(
        'd',
        tmp.to_bytes(8,'little')
    )[0]
    return tmp











if __name__=="__main__":
    print(INT32(0x01_EC_0000))