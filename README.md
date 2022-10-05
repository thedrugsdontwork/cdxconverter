# cdxconverter
> convert chem file format cdx to mol (based on rdkit)

## Reference Document [CDX File Format](http://www.cambridgesoft.com/services/documentation/sdk/chemdraw/cdx/index.htm) , [Rdkit Source Code](https://github.com/rdkit/rdkit)


## Main Operations
- parse cdx atoms&bonds imformation to json(middle struct)
- convert it to mol format (based on rdkit)

## Defect
- Only convert to 2d now
- Some skeleton compounds can not be well converted

## Use
- Clone project and refer to  [example](./test/test.py)



