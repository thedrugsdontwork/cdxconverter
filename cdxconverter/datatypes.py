# INT8, UINT8, INT16, UINT16, INT32, UINT32,FLOAT64
#little ending
import struct

class byteOverFlow(Exception):...

def UNSIGNED(func):
    bit=func()
    def wapper(val):
        return val&((1<<bit)-1)
    return wapper

def SIGNED(func):
    bit=func()
    flag=(1<<bit)-1
    tag=1<<(bit-1)
    effect=flag^tag
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

# def INT8(val):
#     tmp=val&0xff
#     if tmp==0x80:
#         raise byteOverFlow(f"INT8 overflow {val}->fmt:{tmp}")
#     if tmp&0x80>0:
#         #<0
#         tmp=tmp&0x7f
#         tmp=(tmp-1)^0x7f
#         return -1*tmp
#     else:
#         return tmp
#
# def UINT8(val):
#     return val&0xff
#
# def INT16(val):
#     tmp=val&0xff_ff
#     if tmp==0x80_00:
#         raise byteOverFlow(f"INT16 overflow {val}->fmt:{tmp}")
#     if tmp&0x80_00:
#         tmp=tmp&0x7f_ff
#         tmp = (tmp - 1) ^ 0x7f_ff
#         return -1*tmp
#     else:
#         return tmp
#
# def UINT16(val):
#     return val&0xff_ff
#
# def INT32(val):
#     tmp=val&0xff_ff_ff_ff
#     if tmp==0x80_00_00_00:
#         raise byteOverFlow(f"INT16 overflow {val}->fmt:{tmp}")
#     if tmp&0x80_00_00_00>0:
#         tmp = tmp & 0x7f_ff_ff_ff
#         tmp = (tmp - 1) ^ 0x7f_ff_ff_ff
#         return -1 * tmp
#     else:
#         return tmp
#
# def UINT32(val):
#     return val&0xff_ff_ff_ff

def FLOAT64(val):
    tmp=val&0xffff_ffff_ffff_ffff
    tmp=struct.unpack(
        'd',
        tmp.to_bytes(8,'little')
    )[0]
    return tmp











if __name__=="__main__":
    print(INT32(0x01_EC_0000))