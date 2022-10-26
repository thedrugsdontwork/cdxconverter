import os
import sys
from .enumconverter import *
from .datatypes import INT8,UINT8,INT16,UINT16,INT32,UINT32,FLOAT64


##############config log
import logging
LOG=logging.getLogger(__name__)
LOG.addHandler(
    logging.StreamHandler(
        sys.stdout
    )
)
LOG.setLevel(
    logging.DEBUG
)
#####################config log end

#####Exception

class NotCDXException(Exception):...

#####Ecxeption end




## parse main stack
class stack:
    def __init__(self):
        self.stack=list()

    def put(self,data:dict):
        """

        :param data:{object:str,counter:int}
        :return:
        """
        self.stack.append(data)

    def get_top(self):
        return self.stack[-1]

    def pop(self):
        self.stack.pop(-1)

    def get_size(self):
        return len(self.stack)

    def is_empty(self):
        return len(self.stack)==0

class cdx_object(dict):
    def __init___(self,**kwargs):
        super().__init__(**kwargs)



def cdx_reader(file):
    cdx_stack = stack()
    cdx_obj = dict()
    stack_top = cdx_obj
    fp=open(file,"rb")
    # read header and match cdx header
    buffer=fp.read(8)
    if not match_header(buffer):
        LOG.error("This file is not a cdx file")
        fp.close()
        raise NotCDXException(f"This file is not a cdx file {file}")
    # ignore cdx reserve bytes
    fp.seek(kCDX_HeaderLength)
    while buffer:
        #Read tag fom stream
        buffer=fp.read(2)
        #Tag identifier
        target=UINT16(QUADCONST(*buffer,0,0))
        item=CDXDatumID.find(target)
        #Get identifier name
        tag_type=get_type(item)

        if item ==None:
            tag_type=f"unknow_target_{target}"
            if target&kCDXTag_UserDefined>0:
                LOG.warnning(f"Unkonw user defined prop ")
            else:
                # raise Exception(f"Unkonw target identify number {target}")
                LOG.error(f"Unknow target id in cdx file ignore it :[{target}]")
        # its an cdx obj
        if item in CDX_Objects:
            #get obj id 4 bytes
            buffer=fp.read(4)
            obj_id=UINT32(QUADCONST(*buffer))
            if stack_top.get(obj_id):
                LOG.warnning(f"Get same id [{obj_id}] {stack_top}")
            cdx=cdx_object(type=tag_type,id=obj_id)
            if not stack_top.get(tag_type):
                stack_top[tag_type]=[]
            stack_top[tag_type].append(cdx)
            cdx_stack.put(cdx)
            stack_top=cdx_stack.get_top()
        #get cdx obj end identifier
        elif item==CDXDatumID.kCDXProp_EndObject:
            cdx_stack.pop()
            if cdx_stack.is_empty():
                break
            stack_top=cdx_stack.get_top()

        # its prop
        else:
            buffer=fp.read(2)
            length=UINT16(QUADCONST(*buffer,0,0))
            # A length of 0xFFFF is a special value that indicates the object is greater than 65534 bytes in size.
            # In this case it is followed immediately by an additional 4-byte Length item to specify the actual length.
            if length==kCDXLengthOver:
                buffer = fp.read(4)
                length = UINT32(QUADCONST(*buffer))
            prop=fp.read(length)
            val=get_value(prop,tag_type)
            stack_top[tag_type]=val
    fp.close()
    LOG.info("Parse complete.")
    return cdx_obj



def get_type(item):
    return CDX_TAG_TYPE.get(item,None)

def get_value(byte_arr,tag_type):
    if tag_type in ("Bond_Begin","Bond_End"):#unint32
        # fill=4-len(byte_arr)
        # print(byte_arr)
        return UINT32(QUADCONST(*byte_arr))
    elif tag_type in ("2DPosition","Window_Size","Window_Position"):#int32
        # In CDX files, a CDXPoin t2D is an x- and a y-CDXCoordinate stored as a pair of INT32s, y coordinate followed by x coordinate.
        # 以埃为单位 根据cdx提供的CDXPOINT2d 文档进行转换，
        # 额外将y坐标反转并将坐标等比缩放10
        y,x=INT32(QUADCONST(*byte_arr[:4])),\
            INT32(QUADCONST(*byte_arr[4:8]))
        x=round(x /1000000,2)
        y=-1*round(y /1000000,2)
        return dict(x=x,y=y)
    elif tag_type in ("BoundingBox","PrintMargins"):
        # http://www.cambridgesoft.com/services/documentation/sdk/chemdraw/cdx/DataType/CDXCoordinates.htm
        x,y,z,w=INT32(QUADCONST(*byte_arr[:4])),\
                INT32(QUADCONST(*byte_arr[4:8])),\
                INT32(QUADCONST(*byte_arr[8:12])),\
                INT32(QUADCONST(*byte_arr[12:]))
        x = round(x / 1000000, 2)
        y = round(y / 1000000, 2)
        z = round(z / 1000000, 2)
        w = round(w / 1000000, 2)
        return dict(top=x,left=y,bottom=z,right=w)

    elif tag_type in ('CreationProgram','Name','Text'):
        return byte_arr.decode("utf-8",'ignore')
    elif tag_type in ("Node_Type","ZOrder","Node_Element","CaptionLineHeight","LabelLineHeight","Bond_Order","Bond_Display"):#int16
        # if tag_type=="Node_Element":
            # LOG.debug(f"parse Node ele:{INT16(QUADCONST(*byte_arr,0,0))}")
        return INT16(QUADCONST(*byte_arr,0,0))
    elif tag_type in ("Atom_NumHydrogens"):#uint16
        return UINT16(QUADCONST(*byte_arr,0,0))
    elif tag_type in ("Atom_CIPStereochemistry","Bond_CIPStereochemistry","LabelJustification","Atom_Charge"):#int8
        return INT8(QUADCONST(*byte_arr,0, 0, 0))
    elif tag_type  in ('FontTable'):
        return parse_font_table(byte_arr)
    elif tag_type in ("CaptionStyle"):
        return get_font_style(byte_arr)
    elif tag_type in ("BondSpacing"):#int16
        # In CDX files, this value is stored as (10 * the bond spacing as a percent of length), so 18% of length = 180.
        return INT16(QUADCONST(*byte_arr,0, 0))//10
    # elif tag_type in ("LabelJustification"):#int8
    #     return QUADCONST(*byte_arr,0,0, 0)
    elif tag_type=="MacPrintInfo":
        fmt_str="%02d"*(len(byte_arr))
        t=tuple(byte_arr)
        return fmt_str%t
    elif tag_type in ("HashSpacing","MarginWidth","LineWidth","BoldWidth","BondLength"):#int 32
        return round(INT32(QUADCONST(*byte_arr))/100000,2)
    elif tag_type in ("ChainAngle"):
        return INT32(QUADCONST(*byte_arr))/65536
    elif tag_type in ("Bond_ShowStereo","Bond_ShowQuery","Atom_ShowAtomNumber","Atom_ShowStereo","Atom_ShowQuery"):#boolean
        return QUADCONST(*byte_arr,0,0,0)>0
    elif tag_type=="ColorTable":
        return parse_color_table(byte_arr)
    else:
        return list(byte_arr)

def parse_core():...

def match_header(buffer):
    """

    :param buffer: b bytes array
    :return:
    """
    cdx_header=bytes(kCDX_HeaderString,"utf-8")
    return (False,True)[buffer==cdx_header]

def parse_color_table(byte_arr):
    # http://www.cambridgesoft.com/services/documentation/sdk/chemdraw/cdx/properties/ColorTable.htm
    length=UINT16(QUADCONST(*byte_arr[:2],0,0))
    tmp_arr=byte_arr[2:]
    res=[]
    for i in range(length):
        r=INT16(QUADCONST(*tmp_arr[:2],0,0))//256
        g=INT16(QUADCONST(*tmp_arr[2:4],0,0))//256
        b=INT16(QUADCONST(*tmp_arr[4:6],0,0))//256
        tmp_arr=tmp_arr[6:]
        res.append(dict(r=r,g=g,b=b))
    return res

def parse_font_table(byte_arr):
    p_index=QUADCONST(*byte_arr[:2],0,0)
    #warn if p_index>=2
    platform=("Macintosh","Windows")[p_index]
    run_count=QUADCONST(*byte_arr[2:4],0,0)
    tmp_arr=byte_arr[4:]
    res=dict(platform=platform,fonttable=[])
    for i in range(run_count):
        # print(tmp_arr)
        font_id=QUADCONST(*tmp_arr[:2],0,0)
        char_set=QUADCONST(*tmp_arr[2:4],0,0)
        char_set=str(CDXCharSet.find(char_set))
        # print(char_set)
        name_len=QUADCONST(*tmp_arr[4:6],0,0)
        name=tmp_arr[6:6+name_len].decode("utf-8")
        dic=dict(
            id=font_id,
            charset=char_set,
            name=name
        )
        res["fonttable"].append(dic)
        tmp_arr=tmp_arr[name_len+6:]
    return res

def get_font_style(byte_arr):
    return list(byte_arr)


if __name__=='__main__':
    file=""
    cdx_json=cdx_reader()