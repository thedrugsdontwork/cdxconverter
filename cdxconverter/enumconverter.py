"""
doc here
"""
from enum import Enum
from rdkit.Chem.rdchem import BondType,BondDir

kCDXLineHeight_Variable  	=0
kCDXLineHeight_Automatic 	=1
kCDXTagType_Unknown			="unknown"
kCDXTagType_Query			="query"
kCDXTagType_Rxn				="reaction"
kCDXTagType_Stereo			="stereo"
kCDXTagType_Number			="number"
kCDXTagType_Heading			="heading"
kCDXTagType_IDTerm			="idterm"
kCDXTagType_BracketUsage	="bracketusage"
kCDXTagType_PolymerRepeat	="polymerrepeat"
kCDXTagType_PolymerFlip		="polymerflip"
kCDXTagType_Deviation		="deviation"
kCDXTagType_Distance		="distance"
kCDXTagType_Angle			="angle"
kCDXTagType_Rf				="rf"
kCDXLengthOver				=0xFFFF

# set default little ending store

QUADCONST =lambda a, b, c, d: \
	 (( ((d) & 0xff) << 24)	\
	| ( ((c) & 0xff) << 16)	\
	| ( ((b) & 0xff) << 8)	\
	| ( ((a) & 0xff)))

# typedef UINT16 CDXTag;
# typedef INT32  CDXObjectID; // signed for now, due to mac compiler bug?
kCDXUndefinedId 		= -1

kCDX_HeaderStringLen 	= 8
kCDX_HeaderString 		="VjCD0100"
kCDX_Signature	   		=QUADCONST(ord('V'),ord('j'),ord('C'),ord('D'))
kCDX_HeaderLength		=28
kCDXML_HeaderString 	=\
	"<?xml version=\"1.0\" encoding=\"UTF-8\" ?>\n" +\
	"<!DOCTYPE CDXML SYSTEM \"http://www.cambridgesoft.com/xml/cdxml.dtd\" >\n"

kCDXTag_Object				= 0x8000
kCDXTag_UserDefined			= 0x4000
class  CDXDatumID(Enum):
	# General properties.
	kCDXProp_EndObject=0						# 0x0000 Marks end of object.
	kCDXProp_CreationUserName=1				# 0x0001 The name of the creator (program user's name) of the document. (CDXString)
	kCDXProp_CreationDate=2					# 0x0002 The time of object creation. (CDXDate)
	kCDXProp_CreationProgram=3				# 0x0003 The name of the program=3 including version and platform=3 that created the associated CDX object. ChemDraw 4.0 uses ChemDraw 4.0 as the value of CreationProgram. (CDXString)
	kCDXProp_ModificationUserName=4			# 0x0004 The name of the last modifier (program user's name) of the document. (CDXString)
	kCDXProp_ModificationDate=5				# 0x0005 Time of the last modification. (CDXDate)
	kCDXProp_ModificationProgram=6			# 0x0006 The name of the program=6 including version and platform=6 of the last program to perform a modification. ChemDraw 4.0 uses ChemDraw 4.0 as the value of CreationProgram. (CDXString)
	kCDXProp_Unused1=7						# 0x0007 Table of contents. (obsolete)
	kCDXProp_Name=8							# 0x0008 Name of an object. (CDXString)
	kCDXProp_Comment=9						# 0x0009 An arbitrary string intended to be meaningful to a user. (CDXString)
	kCDXProp_ZOrder=10						# 0x000A Back-to-front ordering index in 2D drawing. (INT16)
	kCDXProp_RegistryNumber=11				# 0x000B A registry or catalog number of a molecule object. (CDXString)
	kCDXProp_RegistryAuthority=12				# 0x000C A string that specifies the authority which issued a registry or catalog number. Some examples of registry authorities are CAS=12 Beilstein=12 Aldrich=12 and Merck. (CDXString)
	kCDXProp_Unused2=13						# 0x000D Indicates that this object (the reference object) is an alias to an object elsewhere in the document (the target object). The attributes and contained objects should be taken from the target object. (obsolete)
	kCDXProp_RepresentsProperty=14			# 0x000E Indicates that this object represents some property in some other object. (CDXRepresentsProperty)
	kCDXProp_IgnoreWarnings=15				# 0x000F Signifies whether chemical warnings should be suppressed on this object. (CDXBooleanImplied)
	kCDXProp_ChemicalWarning=16				# 0x0010 A warning concerning possible chemical problems with this object. (CDXString)
	kCDXProp_Visible=17						# 0x0011 The object is visible if non-zero. (CDXBoolean)

	# Fonts.
	kCDXProp_FontTable =256			# 0x0100 A list of fonts used in the document. (CDXFontTable)

	# Coordinates.
	kCDXProp_2DPosition =512			# 0x0200 The 2D location (in the order of vertical and horizontal locations) of an object. (CDXPoint2D)
	kCDXProp_3DPosition=513					# 0x0201 The 3D location (in the order of X-=513 Y-=513 and Z-locations in right-handed coordinate system) of an object in CDX coordinate units. The precise meaning of this attribute varies depending on the type of object. (CDXPoint3D)
	kCDXProp_2DExtent=514						# 0x0202 The width and height of an object in CDX coordinate units. The precise meaning of this attribute varies depending on the type of object. (CDXPoint2D)
	kCDXProp_3DExtent=515						# 0x0203 The width=515 height=515 and depth of an object in CDX coordinate units (right-handed coordinate system). The precise meaning of this attribute varies depending on the type of object. (CDXPoint3D)
	kCDXProp_BoundingBox=516					# 0x0204 The smallest rectangle that encloses the graphical representation of the object. (CDXRectangle)
	kCDXProp_RotationAngle=517					# 0x0205 The angular orientation of an object in degrees * 65536. (INT32)
	kCDXProp_BoundsInParent=518				# 0x0206 The bounds of this object in the coordinate system of its parent (used for pages within tables). (CDXRectangle)
	kCDXProp_3DHead=519						# 0x0207 The 3D location (in the order of X-=519 Y-=519 and Z-locations in right-handed coordinate system) of the head of an object in CDX coordinate units. The precise meaning of this attribute varies depending on the type of object. (CDXPoint3D)
	kCDXProp_3DTail=520						# 0x0208 The 3D location (in the order of X-=520 Y-=520 and Z-locations in right-handed coordinate system) of the tail of an object in CDX coordinate units. The precise meaning of this attribute varies depending on the type of object. (CDXPoint3D)
	kCDXProp_TopLeft=521						# 0x0209 The location of the top-left corner of a quadrilateral object=521 possibly in a rotated or skewed frame. (CDXPoint2D)
	kCDXProp_TopRight=522						# 0x020A The location of the top-right corner of a quadrilateral object=522 possibly in a rotated or skewed frame. (CDXPoint2D)
	kCDXProp_BottomRight=523					# 0x020B The location of the bottom-right corner of a quadrilateral object=523 possibly in a rotated or skewed frame. (CDXPoint2D)
	kCDXProp_BottomLeft=524					# 0x020C The location of the bottom-left corner of a quadrilateral object=524 possibly in a rotated or skewed frame. (CDXPoint2D)

	# Colors.
	kCDXProp_ColorTable =768			# 0x0300 The color palette used throughout the document. (CDXColorTable)
	kCDXProp_ForegroundColor=769				# 0x0301 The foreground color of an object represented as the two-based index into the object's color table. (UINT16)
	kCDXProp_BackgroundColor=770				# 0x0302 The background color of an object represented as the two-based index into the object's color table. (INT16)
	
	# Atom properties.
	kCDXProp_Node_Type =1024			# 0x0400 The type of a node object. (INT16)
	kCDXProp_Node_LabelDisplay=1025				# 0x0401 The characteristics of node label display. (INT8)
	kCDXProp_Node_Element=1026					# 0x0402 The atomic number of the atom representing this node. (INT16)
	kCDXProp_Atom_ElementList=1027				# 0x0403 A list of atomic numbers. (CDXElementList)
	kCDXProp_Atom_Formula=1028					# 0x0404 The composition of a node representing a fragment whose composition is known=1028 but whose connectivity is not. For example=1028 C<sub>4</sub>H<sub>9</sub> represents a mixture of the 4 butyl isomers. (CDXFormula)
	kCDXProp_Atom_Isotope =1056			# 0x0420 The absolute isotopic mass of an atom (2 for deuterium, 14 for carbon-14). (INT16)
	kCDXProp_Atom_Charge=1057					# 0x0421 The atomic charge of an atom. (INT8)
	kCDXProp_Atom_Radical=1058					# 0x0422 The atomic radical attribute of an atom. (UINT8)
	kCDXProp_Atom_RestrictFreeSites=1059		# 0x0423 Indicates that up to the specified number of additional substituents are permitted on this atom. (UINT8)
	kCDXProp_Atom_RestrictImplicitHydrogens=1060# 0x0424 Signifies that implicit hydrogens are not allowed on this atom. (CDXBooleanImplied)
	kCDXProp_Atom_RestrictRingBondCount=1061	# 0x0425 The number of ring bonds attached to an atom. (INT8)
	kCDXProp_Atom_RestrictUnsaturatedBonds=1062	# 0x0426 Indicates whether unsaturation should be present or absent. (INT8)
	kCDXProp_Atom_RestrictRxnChange=1063		# 0x0427 If present=1063 signifies that the reaction change of an atom must be as specified. (CDXBooleanImplied)
	kCDXProp_Atom_RestrictRxnStereo=1064		# 0x0428 The change of stereochemistry of an atom during a reaction. (INT8)
	kCDXProp_Atom_AbnormalValence=1065			# 0x0429 Signifies that an abnormal valence for an atom is permitted. (CDXBooleanImplied)
	kCDXProp_Unused3=1066						# 0x042A
	kCDXProp_Atom_NumHydrogens=1067				# 0x042B The number of (explicit) hydrogens in a labeled atom consisting of one heavy atom and (optionally) the symbol H (e.g.=1067 CH<sub>3</sub>). (UINT16)
	kCDXProp_Unused4=1068						# 0x042C
	kCDXProp_Unused5=1069						# 0x042D
	kCDXProp_Atom_HDot=1070						# 0x042E Signifies the presence of an implicit hydrogen with stereochemistry specified equivalent to an explicit H atom with a wedged bond. (CDXBooleanImplied)
	kCDXProp_Atom_HDash=1071					# 0x042F Signifies the presence of an implicit hydrogen with stereochemistry specified equivalent to an explicit H atom with a hashed bond. (CDXBooleanImplied)
	kCDXProp_Atom_Geometry=1072					# 0x0430 The geometry of the bonds about this atom. (INT8)
	kCDXProp_Atom_BondOrdering=1073				# 0x0431 An ordering of the bonds to this node=1073 used for stereocenters=1073 fragments=1073 and named alternative groups with more than one attachment. (CDXObjectIDArray)
	kCDXProp_Node_Attachments=1074				# 0x0432 For multicenter attachment nodes or variable attachment nodes=1074 a list of IDs of the nodes which are multiply or variably attached to this node. (CDXObjectIDArrayWithCounts)
	kCDXProp_Atom_GenericNickname=1075			# 0x0433 The name of the generic nickname. (CDXString)
	kCDXProp_Atom_AltGroupID=1076				# 0x0434 The ID of the alternative group object that describes this node. (CDXObjectID)
	kCDXProp_Atom_RestrictSubstituentsUpTo=1077	# 0x0435 Indicates that substitution is restricted to no more than the specified value. (UINT8)
	kCDXProp_Atom_RestrictSubstituentsExactly=1078	# 0x0436 Indicates that exactly the specified number of substituents must be present. (UINT8)
	kCDXProp_Atom_CIPStereochemistry=1079		# 0x0437 The node's absolute stereochemistry according to the Cahn-Ingold-Prelog system. (INT8)
	kCDXProp_Atom_Translation=1080				# 0x0438 Provides for restrictions on whether a given node may match other more- or less-general nodes. (INT8)
	kCDXProp_Atom_AtomNumber=1081				# 0x0439 Atom number=1081 as text. (CDXString)
	kCDXProp_Atom_ShowQuery=1082				# 0x043A Show the query indicator if non-zero. (CDXBoolean)
	kCDXProp_Atom_ShowStereo=1083				# 0x043B Show the stereochemistry indicator if non-zero. (CDXBoolean)
	kCDXProp_Atom_ShowAtomNumber=1084			# 0x043C Show the atom number if non-zero. (CDXBoolean)
	kCDXProp_Atom_LinkCountLow=1085				# 0x043D Low end of repeat count for link nodes. (INT16)
	kCDXProp_Atom_LinkCountHigh=1086			# 0x043E High end of repeat count for link nodes. (INT16)
	kCDXProp_Atom_IsotopicAbundance=1087		# 0x043F Isotopic abundance of this atom's isotope. (INT8)
	kCDXProp_Atom_ExternalConnectionType=1088	# 0x0440 Type of external connection=1088 for atoms of type kCDXNodeType_ExternalConnectionPoint. (INT8)

	# Molecule properties.
	kCDXProp_Mole_Racemic =1280			# 0x0500 Indicates that the molecule is a racemic mixture. (CDXBoolean)
	kCDXProp_Mole_Absolute=1281					# 0x0501 Indicates that the molecule has known absolute configuration. (CDXBoolean)
	kCDXProp_Mole_Relative=1282					# 0x0502 Indicates that the molecule has known relative stereochemistry=1282 but unknown absolute configuration. (CDXBoolean)
	kCDXProp_Mole_Formula=1283					# 0x0503 The molecular formula representation of a molecule object. (CDXFormula)
	kCDXProp_Mole_Weight=1284					# 0x0504 The average molecular weight of a molecule object. (FLOAT64)
	kCDXProp_Frag_ConnectionOrder=1285			# 0x0505 An ordered list of attachment points within a fragment. (CDXObjectIDArray)

	# Bond properties.
	kCDXProp_Bond_Order =1536			# 0x0600 The order of a bond object. (INT16)
	kCDXProp_Bond_Display=1537					# 0x0601 The display type of a bond object. (INT16)
	kCDXProp_Bond_Display2=1538					# 0x0602 The display type for the second line of a double bond. (INT16)
	kCDXProp_Bond_DoublePosition=1539			# 0x0603 The position of the second line of a double bond. (INT16)
	kCDXProp_Bond_Begin=1540					# 0x0604 The ID of the CDX node object at the first end of a bond. (CDXObjectID)
	kCDXProp_Bond_End=1541						# 0x0605 The ID of the CDX node object at the second end of a bond. (CDXObjectID)
	kCDXProp_Bond_RestrictTopology=1542			# 0x0606 Indicates the desired topology of a bond in a query. (INT8)
	kCDXProp_Bond_RestrictRxnParticipation=1543	# 0x0607 Specifies that a bond is affected by a reaction. (INT8)
	kCDXProp_Bond_BeginAttach=1544				# 0x0608 Indicates where within the Bond_Begin node a bond is attached. (UINT8)
	kCDXProp_Bond_EndAttach=1545				# 0x0609 Indicates where within the Bond_End node a bond is attached. (UINT8)
	kCDXProp_Bond_CIPStereochemistry=1546		# 0x060A The bond's absolute stereochemistry according to the Cahn-Ingold-Prelog system. (INT8)
	kCDXProp_Bond_BondOrdering=1547				# 0x060B Ordered list of attached bond IDs. (CDXObjectIDArray)
	kCDXProp_Bond_ShowQuery=1548				# 0x060C Show the query indicator if non-zero. (CDXBoolean)
	kCDXProp_Bond_ShowStereo=1549				# 0x060D Show the stereochemistry indicator if non-zero. (CDXBoolean)
	kCDXProp_Bond_CrossingBonds=1550			# 0x060E Unordered list of IDs of bonds that cross this one (either above or below). (CDXObjectIDArray)
	kCDXProp_Bond_ShowRxn=1551					# 0x060F Show the reaction-change indicator if non-zero. (CDXBoolean)

	# Text properties.
	kCDXProp_Text =1792					# 0x0700 The text of a text object. (CDXString)
	kCDXProp_Justification=1793					# 0x0701 The horizontal justification of a text object. (INT8)
	kCDXProp_LineHeight=1794					# 0x0702 The line height of a text object. (UINT16)
	kCDXProp_WordWrapWidth=1795					# 0x0703 The word-wrap width of a text object. (INT16)
	kCDXProp_LineStarts=1796					# 0x0704 The number of lines of a text object followed by that many values indicating the zero-based text position of each line start. (INT16ListWithCounts)
	kCDXProp_LabelAlignment=1797				# 0x0705 The alignment of the text with respect to the node position. (INT8)
	kCDXProp_LabelLineHeight=1798				# 0x0706 Text line height for atom labels (INT16)
	kCDXProp_CaptionLineHeight=1799				# 0x0707 Text line height for non-atomlabel text objects (INT16)
	kCDXProp_InterpretChemically=1800			# 0x0708 Signifies whether to the text label should be interpreted chemically (if possible). (CDXBooleanImplied)

	# Document properties.
	kCDXProp_MacPrintInfo =2048			# 0x0800 The 120 byte Macintosh TPrint data associated with the CDX document object. Refer to Macintosh Toolbox manual for detailed description. (Unformatted)
	kCDXProp_WinPrintInfo=2049					# 0x0801 The Windows DEVMODE structure associated with the CDX document object. (Unformatted)
	kCDXProp_PrintMargins=2050					# 0x0802 The outer margins of the Document. (CDXRectangle)
	kCDXProp_ChainAngle=2051					# 0x0803 The default chain angle setting in degrees * 65536. (INT32)
	kCDXProp_BondSpacing=2052					# 0x0804 The spacing between segments of a multiple bond=2052 measured relative to bond length. (INT16)
	kCDXProp_BondLength=2053					# 0x0805 The default bond length. (CDXCoordinate)
	kCDXProp_BoldWidth=2054						# 0x0806 The default bold bond width. (CDXCoordinate)
	kCDXProp_LineWidth=2055						# 0x0807 The default line width. (CDXCoordinate)
	kCDXProp_MarginWidth=2056					# 0x0808 The default amount of space surrounding atom labels. (CDXCoordinate)
	kCDXProp_HashSpacing=2057					# 0x0809 The default spacing between hashed lines used in wedged hashed bonds. (CDXCoordinate)
	kCDXProp_LabelStyle=2058					# 0x080A The default style for atom labels. (CDXFontStyle)
	kCDXProp_CaptionStyle=2059					# 0x080B The default style for non-atomlabel text objects. (CDXFontStyle)
	kCDXProp_CaptionJustification=2060			# 0x080C The horizontal justification of a caption (non-atomlabel text object) (INT8)
	kCDXProp_FractionalWidths=2061				# 0x080D Signifies whether to use fractional width information when drawing text. (CDXBooleanImplied)
	kCDXProp_Magnification=2062					# 0x080E The view magnification factor (INT16)
	kCDXProp_WidthPages=2063					# 0x080F The width of the document in pages. (INT16)
	kCDXProp_HeightPages=2064					# 0x0810 The height of the document in pages. (INT16)
	kCDXProp_DrawingSpaceType=2065				# 0x0811 The type of drawing space used for this document. (INT8)
	kCDXProp_Width=2066							# 0x0812 The width of an object in CDX coordinate units=2066 possibly in a rotated or skewed frame. (CDXCoordinate)
	kCDXProp_Height=2067						# 0x0813 The height of an object in CDX coordinate units=2067 possibly in a rotated or skewed frame. (CDXCoordinate)
	kCDXProp_PageOverlap=2068					# 0x0814 The amount of overlap of pages when a poster is tiled. (CDXCoordinate)
	kCDXProp_Header=2069						# 0x0815 The text of the header. (CDXString)
	kCDXProp_HeaderPosition=2070				# 0x0816 The vertical offset of the header baseline from the top of the page. (CDXCoordinate)
	kCDXProp_Footer=2071						# 0x0817 The text of the footer. (CDXString)
	kCDXProp_FooterPosition=2072				# 0x0818 The vertical offset of the footer baseline from the bottom of the page. (CDXCoordinate)
	kCDXProp_PrintTrimMarks=2073				# 0x0819 If present=2073 trim marks are to printed in the margins. (CDXBooleanImplied)
	kCDXProp_LabelStyleFont=2074				# 0x081A The default font family for atom labels. (INT16)
	kCDXProp_CaptionStyleFont=2075				# 0x081B The default font style for captions (non-atom-label text objects). (INT16)
	kCDXProp_LabelStyleSize=2076				# 0x081C The default font size for atom labels. (INT16)
	kCDXProp_CaptionStyleSize=2077				# 0x081D The default font size for captions (non-atom-label text objects). (INT16)
	kCDXProp_LabelStyleFace=2078				# 0x081E The default font style for atom labels. (INT16)
	kCDXProp_CaptionStyleFace=2079				# 0x081F The default font face for captions (non-atom-label text objects). (INT16)
	kCDXProp_LabelStyleColor=2080				# 0x0820 The default color for atom labels (INT16)
	kCDXProp_CaptionStyleColor=2081				# 0x0821 The default color for captions (non-atom-label text objects). (INT16)
	kCDXProp_BondSpacingAbs=2082				# 0x0822 The absolute distance between segments of a multiple bond. (CDXCoordinate)
	kCDXProp_LabelJustification=2083			# 0x0823 The default justification for atom labels. (INT8)
	kCDXProp_FixInplaceExtent=2084				# 0x0824 Defines a size for OLE In-Place editing. (CDXPoint2D)
	kCDXProp_Side=2085							# 0x0825 A specific side of an object (rectangle). (INT16)
	kCDXProp_FixInplaceGap=2086					# 0x0826 Defines a padding for OLE In-Place editing. (CDXPoint2D)

	# Window properties.
	kCDXProp_Window_IsZoomed =2304		# 0x0900 Signifies whether the main viewing window is zoomed (maximized). (CDXBooleanImplied)
	kCDXProp_Window_Position=2305				# 0x0901 The top-left position of the main viewing window. (CDXPoint2D)
	kCDXProp_Window_Size=2306					# 0x0902 Height and width of the document window. (CDXPoint2D)
	
	# Graphic object properties.
	kCDXProp_Graphic_Type = 0x0A00			# 0x0A00 The type of graphical object. (INT16)
	kCDXProp_Line_Type=2561						# 0x0A01 The type of a line object. (INT16)
	kCDXProp_Arrow_Type=2562					# 0x0A02 The type of arrow object=2562 which represents line=2562 arrow=2562 arc=2562 rectangle=2562 or orbital. (INT16)
	kCDXProp_Rectangle_Type=2563				# 0x0A03 The type of a rectangle object. (INT16)
	kCDXProp_Oval_Type=2564						# 0x0A04 The type of an arrow object that represents a circle or ellipse. (INT16)
	kCDXProp_Orbital_Type=2565					# 0x0A05 The type of orbital object. (INT16)
	kCDXProp_Bracket_Type=2566					# 0x0A06 The type of symbol object. (INT16)
	kCDXProp_Symbol_Type=2567					# 0x0A07 The type of symbol object. (INT16)
	kCDXProp_Curve_Type=2568					# 0x0A08 The type of curve object. (INT16)
	kCDXProp_Arrow_HeadSize = 0x0A20	# 0x0A20 The size of the arrow's head. (INT16)
	kCDXProp_Arc_AngularSize=2593				# 0x0A21 The size of an arc (in degrees * 10=2593 so 90 degrees = 900). (INT16)
	kCDXProp_Bracket_LipSize=2594				# 0x0A22 The size of a bracket. (INT16)
	kCDXProp_Curve_Points=2595					# 0x0A23 The B&eacute;zier curve's control point locations. (CDXCurvePoints)
	kCDXProp_Bracket_Usage=2596					# 0x0A24 The syntactical chemical meaning of the bracket (SRU=2596 mer=2596 mon=2596 xlink=2596 etc). (INT8)
	kCDXProp_Polymer_RepeatPattern=2597			# 0x0A25 The head-to-tail connectivity of objects contained within the bracket. (INT8)
	kCDXProp_Polymer_FlipType=2598				# 0x0A26 The flip state of objects contained within the bracket. (INT8)
	kCDXProp_BracketedObjects=2599				# 0x0A27 The set of objects contained in a BracketedGroup. (CDXObjectIDArray)
	kCDXProp_Bracket_RepeatCount=2600			# 0x0A28 The number of times a multiple-group BracketedGroup is repeated. (INT16)
	kCDXProp_Bracket_ComponentOrder=2601		# 0x0A29 The component order associated with a BracketedGroup. (INT16)
	kCDXProp_Bracket_SRULabel=2602				# 0x0A2A The label associated with a BracketedGroup that represents an SRU. (CDXString)
	kCDXProp_Bracket_GraphicID=2603				# 0x0A2B The ID of a graphical object (bracket=2603 brace=2603 or parenthesis) associated with a Bracket Attachment. (CDXObjectID)
	kCDXProp_Bracket_BondID=2604				# 0x0A2C The ID of a bond that crosses a Bracket Attachment. (CDXObjectID)
	kCDXProp_Bracket_InnerAtomID=2605			# 0x0A2D The ID of the node located within the Bracketed Group and attached to a bond that crosses a Bracket Attachment. (CDXObjectID)
	kCDXProp_Curve_Points3D=2606				# 0x0A2E The B&eacute;zier curve's control point locations. (CDXCurvePoints3D)

	# Embedded pictures.
	kCDXProp_Picture_Edition = 0x0A60		# 0x0A60 The section information (SectionHandle) of the Macintosh Publish & Subscribe edition embedded in the CDX picture object. (Unformatted)
	kCDXProp_Picture_EditionAlias=2657			# 0x0A61 The alias information of the Macintosh Publish & Subscribe edition embedded in the CDX picture object. (Unformatted)
	kCDXProp_MacPICT=2658						# 0x0A62 A Macintosh PICT data object. (Unformatted)
	kCDXProp_WindowsMetafile=2659				# 0x0A63 A Microsoft Windows Metafile object. (Unformatted)
	kCDXProp_OLEObject=2660						# 0x0A64 An OLE object. (Unformatted)
	kCDXProp_EnhancedMetafile=2661				# 0x0A65 A Microsoft Windows Enhanced Metafile object. (Unformatted)

	# Spectrum properties
	kCDXProp_Spectrum_XSpacing = 0x0A80	# 0x0A80 The spacing in logical units (ppm, Hz, waveNumbers) between points along the X-axis of an evenly-spaced grid. (FLOAT64)
	kCDXProp_Spectrum_XLow=2689					# 0x0A81 The first data point for the X-axis of an evenly-spaced grid. (FLOAT64)
	kCDXProp_Spectrum_XType=2690				# 0x0A82 The type of units the X-axis represents. (INT16)
	kCDXProp_Spectrum_YType=2691				# 0x0A83 The type of units the Y-axis represents. (INT16)
	kCDXProp_Spectrum_XAxisLabel=2692			# 0x0A84 A label for the X-axis. (CDXString)
	kCDXProp_Spectrum_YAxisLabel=2693			# 0x0A85 A label for the Y-axis. (CDXString)
	kCDXProp_Spectrum_DataPoint=2694			# 0x0A86 The Y-axis values for the spectrum. It is an array of double values corresponding to X-axis values. (FLOAT64)
	kCDXProp_Spectrum_Class=2695				# 0x0A87 The type of spectrum represented. (INT16)
	kCDXProp_Spectrum_YLow=2696					# 0x0A88 Y value to be used to offset data when storing XML. (FLOAT64)
	kCDXProp_Spectrum_YScale=2697				# 0x0A89 Y scaling used to scale data when storing XML. (FLOAT64)

	# TLC properties
	kCDXProp_TLC_OriginFraction = 0x0AA0	# 0x0AA0 The distance of the origin line from the bottom of a TLC Plate, as a fraction of the total height of the plate. (FLOAT64)
	kCDXProp_TLC_SolventFrontFraction=2721		# 0x0AA1 The distance of the solvent front from the top of a TLC Plate=2721 as a fraction of the total height of the plate. (FLOAT64)
	kCDXProp_TLC_ShowOrigin=2722				# 0x0AA2 Show the origin line near the base of the TLC Plate if non-zero. (CDXBoolean)
	kCDXProp_TLC_ShowSolventFront=2723			# 0x0AA3 Show the solvent front line near the top of the TLC Plate if non-zero. (CDXBoolean)
	kCDXProp_TLC_ShowBorders=2724				# 0x0AA4 Show borders around the edges of the TLC Plate if non-zero. (CDXBoolean)
	kCDXProp_TLC_ShowSideTicks=2725				# 0x0AA5 Show tickmarks up the side of the TLC Plate if non-zero. (CDXBoolean)
	kCDXProp_TLC_Rf = 0x0AB0				# 0x0AB0 The Retention Factor of an individual spot. (FLOAT64)
	kCDXProp_TLC_Tail=2737						# 0x0AB1 The length of the "tail" of an individual spot. (CDXCoordinate)
	kCDXProp_TLC_ShowRf=2738					# 0x0AB2 Show the spot's Retention Fraction (Rf) value if non-zero. (CDXBoolean)

	# Alternate Group properties
	kCDXProp_NamedAlternativeGroup_TextFrame = 0x0B00	# 0x0B00 The bounding box of upper portion of the Named Alternative Group, containing the name of the group. (CDXRectangle)
	kCDXProp_NamedAlternativeGroup_GroupFrame=2817			# 0x0B01 The bounding box of the lower portion of the Named Alternative Group=2817 containing the definition of the group. (CDXRectangle)
	kCDXProp_NamedAlternativeGroup_Valence=2818				# 0x0B02 The number of attachment points in each alternative in a named alternative group. (INT16)

	# Geometry and Constraint properties
	kCDXProp_GeometricFeature = 0x0B80	# 0x0B80 The type of the geometrical feature (point, line, plane, etc.). (INT8)
	kCDXProp_RelationValue=2945					# 0x0B81 The numeric relationship (if any) among the basis objects used to define this object. (INT8)
	kCDXProp_BasisObjects=2946					# 0x0B82 An ordered list of objects used to define this object. (CDXObjectIDArray)
	kCDXProp_ConstraintType=2947				# 0x0B83 The constraint type (distance or angle). (INT8)
	kCDXProp_ConstraintMin=2948					# 0x0B84 The minimum value of the constraint (FLOAT64)
	kCDXProp_ConstraintMax=2949					# 0x0B85 The maximum value of the constraint (FLOAT64)
	kCDXProp_IgnoreUnconnectedAtoms=2950		# 0x0B86 Signifies whether unconnected atoms should be ignored within the exclusion sphere. (CDXBooleanImplied)
	kCDXProp_DihedralIsChiral=2951				# 0x0B87 Signifies whether a dihedral is signed or unsigned. (CDXBooleanImplied)
	kCDXProp_PointIsDirected=2952				# 0x0B88 For a point based on a normal=2952 signifies whether it is in a specific direction relative to the reference point. (CDXBooleanImplied)

	# Reaction properties
	kCDXProp_ReactionStep_Atom_Map = 0x0C00 # 0x0C00 Represents pairs of mapped atom IDs; each pair is a reactant atom mapped to to a product atom. (CDXObjectIDArray)
	kCDXProp_ReactionStep_Reactants=3073		# 0x0C01 An order list of reactants present in the Reaction Step. (CDXObjectIDArray)
	kCDXProp_ReactionStep_Products=3074			# 0x0C02 An order list of products present in the Reaction Step. (CDXObjectIDArray)
	kCDXProp_ReactionStep_Plusses=3075			# 0x0C03 An ordered list of pluses used to separate components of the Reaction Step. (CDXObjectIDArray)
	kCDXProp_ReactionStep_Arrows=3076			# 0x0C04 An ordered list of arrows used to separate components of the Reaction Step. (CDXObjectIDArray)
	kCDXProp_ReactionStep_ObjectsAboveArrow=3077# 0x0C05 An order list of objects above the arrow in the Reaction Step. (CDXObjectIDArray)
	kCDXProp_ReactionStep_ObjectsBelowArrow=3078# 0x0C06 An order list of objects below the arrow in the Reaction Step. (CDXObjectIDArray)
	kCDXProp_ReactionStep_Atom_Map_Manual=3079	# 0x0C07 Represents pairs of mapped atom IDs; each pair is a reactant atom mapped to to a product atom. (CDXObjectIDArray)
	kCDXProp_ReactionStep_Atom_Map_Auto=3080	# 0x0C08 Represents pairs of mapped atom IDs; each pair is a reactant atom mapped to to a product atom. (CDXObjectIDArray)

	# CDObjectTag properties
	kCDXProp_ObjectTag_Type = 0x0D00		# 0x0D00 The tag's data type. (INT16)
	kCDXProp_Unused6=3329						# 0x0D01 obsolete (obsolete)
	kCDXProp_Unused7=3330						# 0x0D02 obsolete (obsolete)
	kCDXProp_ObjectTag_Tracking=3331			# 0x0D03 The tag will participate in tracking if non-zero. (CDXBoolean)
	kCDXProp_ObjectTag_Persistent=3332			# 0x0D04 The tag will be resaved to a CDX file if non-zero. (CDXBoolean)
	kCDXProp_ObjectTag_Value=3333				# 0x0D05 The value is a INT32=3333 FLOAT64 or unformatted string depending on the value of ObjectTag_Type. (varies)
	kCDXProp_Positioning=3334					# 0x0D06 How the indicator should be positioned with respect to its containing object. (INT8)
	kCDXProp_PositioningAngle=3335				# 0x0D07 Angular positioning=3335 in radians * 65536. (INT32)
	kCDXProp_PositioningOffset=3336				# 0x0D08 Offset positioning. (CDXPoint2D)

	# CDSequence properties
	kCDXProp_Sequence_Identifier = 0x0E00 	# 0x0E00 A unique (but otherwise random) identifier for a given Sequence object. (CDXString)

	# CDCrossReference properties
	kCDXProp_CrossReference_Container = 0x0F00	# 0x0F00 An external object containing (as an embedded object) the document containing the Sequence object being referenced. (CDXString)
	kCDXProp_CrossReference_Document=3841		# 0x0F01 An external document containing the Sequence object being referenced. (CDXString)
	kCDXProp_CrossReference_Identifier=3842		# 0x0F02 A unique (but otherwise random) identifier for a given Cross-Reference object. (CDXString)
	kCDXProp_CrossReference_Sequence=3843		# 0x0F03 A value matching the SequenceIdentifier of the Sequence object to be referenced. (CDXString)

	# Miscellaneous properties.
	kCDXProp_Template_PaneHeight =4096	# 0x1000 The height of the viewing window of a template grid. (CDXCoordinate)
	kCDXProp_Template_NumRows=4097				# 0x1001 The number of rows of the CDX TemplateGrid object. (INT16)
	kCDXProp_Template_NumColumns=4098			# 0x1002 The number of columns of the CDX TemplateGrid object. (INT16)

	kCDXProp_Group_Integral =4352		# 0x1100 The group is considered to be integral (non-subdivisible) if non-zero. (CDXBoolean)

	kCDXProp_SplitterPositions =8176	# 0x1FF0 An array of vertical positions that subdivide a page into regions. (CDXObjectIDArray)
	kCDXProp_PageDefinition=8177				# 0x1FF1 An array of vertical positions that subdivide a page into regions. (CDXObjectIDArray)

	# User defined properties
	# First 1024 tags are reserved for temporary tags used only during the runtime.
	kCDXUser_TemporaryBegin = kCDXTag_UserDefined
	kCDXUser_TemporaryEnd = kCDXTag_UserDefined + 0x0400

	# Objects.
	kCDXObj_Document = kCDXTag_Object	# 0x8000
	kCDXObj_Page=32769						# 0x8001
	kCDXObj_Group=32770						# 0x8002
	kCDXObj_Fragment=32771					# 0x8003
	kCDXObj_Node=32772						# 0x8004
	kCDXObj_Bond=32773						# 0x8005
	kCDXObj_Text=32774						# 0x8006
	kCDXObj_Graphic=32775					# 0x8007
	kCDXObj_Curve=32776						# 0x8008
	kCDXObj_EmbeddedObject=32777				# 0x8009
	kCDXObj_NamedAlternativeGroup=32778		# 0x800a
	kCDXObj_TemplateGrid=32779				# 0x800b
	kCDXObj_RegistryNumber=32780				# 0x800c
	kCDXObj_ReactionScheme=32781				# 0x800d
	kCDXObj_ReactionStep=32782				# 0x800e
	kCDXObj_ObjectDefinition=32783			# 0x800f
	kCDXObj_Spectrum=32784					# 0x8010
	kCDXObj_ObjectTag=32785					# 0x8011
	kCDXObj_OleClientItem=32786				# 0x8012	# obsolete
	kCDXObj_Sequence=32787                   # 0x8013
	kCDXObj_CrossReference=32788             # 0x8014
	kCDXObj_Splitter=32789				    # 0x8015
	kCDXObj_Table=32790					    # 0x8016
	kCDXObj_BracketedGroup=32791				# 0x8017
	kCDXObj_BracketAttachment=32792			# 0x8018
	kCDXObj_CrossingBond=32793				# 0x8019
	kCDXObj_Border=32794						# 0x8020
	kCDXObj_Geometry=32795					# 0x8021
	kCDXObj_Constraint=32796					# 0x8022
	kCDXObj_TLCPlate=32797					# 0x8023
	kCDXObj_TLCLane=32798					# 0x8024
	kCDXObj_TLCSpot=32799					# 0x8025
	# Add new objects here
	kCDXObj_UnknownObject = 0x8FFF

	def find(val):
		for i in CDXDatumID:
			if i.value==val:
				return i
		else:
			return None



class  CDXNodeType(Enum):
	kCDXNodeType_Unspecified=0
	kCDXNodeType_Element=1
	kCDXNodeType_ElementList=2
	kCDXNodeType_ElementListNickname=3
	kCDXNodeType_Nickname=4
	kCDXNodeType_Fragment=5
	kCDXNodeType_Formula=6
	kCDXNodeType_GenericNickname=7
	kCDXNodeType_AnonymousAlternativeGroup=8
	kCDXNodeType_NamedAlternativeGroup=9
	kCDXNodeType_MultiAttachment=10
	kCDXNodeType_VariableAttachment=11
	kCDXNodeType_ExternalConnectionPoint=12
	kCDXNodeType_LinkNode=13


class  CDXLabelDisplay(Enum):
	kCDXLabelDisplay_Auto=0
	kCDXLabelDisplay_Left=1
	kCDXLabelDisplay_Center=2
	kCDXLabelDisplay_Right=3
	kCDXLabelDisplay_Above=4
	kCDXLabelDisplay_Below=5
	kCDXLabelDisplay_BestInitial=6


class  CDXRadical(Enum):
	kCDXRadical_None				=0
	kCDXRadical_Singlet				=1	# diradical singlet  (two dots)
	kCDXRadical_Doublet				=2	# monoradical		  (one dot)
	kCDXRadical_Triplet				= 3		# diradical triplet  (two dots)


class  CDXIsotope(Enum):
	kCDXIsotope_Natural				= 0


class  CDXRingBondCount(Enum):
	kCDXRingBondCount_Unspecified	= -1
	kCDXRingBondCount_NoRingBonds	=0
	kCDXRingBondCount_AsDrawn		=1
	kCDXRingBondCount_SimpleRing	=2
	kCDXRingBondCount_Fusion		=3
	kCDXRingBondCount_SpiroOrHigher	= 4


class  CDXUnsaturation(Enum):
	kCDXUnsaturation_Unspecified	=0
	kCDXUnsaturation_MustBeAbsent	=1
	kCDXUnsaturation_MustBePresent	=2
	kCDXUnsaturationLastEnum=3


class  CDXReactionStereo(Enum):
	kCDXReactionStereo_Unspecified	=0
	kCDXReactionStereo_Inversion	=1
	kCDXReactionStereo_Retention	= 2


class  CDXTranslation(Enum):
	kCDXTranslation_Equal	=0
	kCDXTranslation_Broad	=1
	kCDXTranslation_Narrow	=2
	kCDXTranslation_Any		= 3


class  CDXAbundance(Enum):
	kCDXAbundance_Unspecified	=0
	kCDXAbundance_Any			=1
	kCDXAbundance_Natural		=2
	kCDXAbundance_Enriched		=3
	kCDXAbundance_Deficient		=4
	kCDXAbundance_Nonnatural	= 5


class  CDXExternalConnectionType(Enum):
	kCDXExternalConnection_Unspecified	=0
	kCDXExternalConnection_Diamond		=1
	kCDXExternalConnection_Star			=2
	kCDXExternalConnection_PolymerBead	=3
	kCDXExternalConnection_Wavy			= 4


class  CDXAtomGeometry(Enum):
	kCDXAtomGeometry_Unknown				=0
	kCDXAtomGeometry_1Ligand				=1
	kCDXAtomGeometry_Linear					=2
	kCDXAtomGeometry_Bent					=3
	kCDXAtomGeometry_TrigonalPlanar			=4
	kCDXAtomGeometry_TrigonalPyramidal		=5
	kCDXAtomGeometry_SquarePlanar			=6
	kCDXAtomGeometry_Tetrahedral			=7
	kCDXAtomGeometry_TrigonalBipyramidal	=8
	kCDXAtomGeometry_SquarePyramidal		=9
	kCDXAtomGeometry_5Ligand				=10
	kCDXAtomGeometry_Octahedral				=11
	kCDXAtomGeometry_6Ligand				=12
	kCDXAtomGeometry_7Ligand				=13
	kCDXAtomGeometry_8Ligand				=14
	kCDXAtomGeometry_9Ligand				=15
	kCDXAtomGeometry_10Ligand				= 16


class  CDXBondOrder(Enum):
	kCDXBondOrder_Single		=1
	kCDXBondOrder_Double		=2
	kCDXBondOrder_Triple		=4
	kCDXBondOrder_Quadruple		=8
	kCDXBondOrder_Quintuple		=16
	kCDXBondOrder_Hextuple		=32
	kCDXBondOrder_Half		=64#0.5 dosent match
	kCDXBondOrder_OneHalf	=128
	kCDXBondOrder_TwoHalf		=256
	kCDXBondOrder_ThreeHalf		=512
	kCDXBondOrder_FourHalf		=1024
	kCDXBondOrder_FiveHalf		=2048
	kCDXBondOrder_Dative		=4096
	kCDXBondOrder_Ionic			=8192
	kCDXBondOrder_Hydrogen		=16384
	kCDXBondOrder_ThreeCenter	=32768
	kCDXBondOrder_SingleOrDouble = kCDXBondOrder_Single | kCDXBondOrder_Double
	kCDXBondOrder_SingleOrAromatic = kCDXBondOrder_Single | kCDXBondOrder_OneHalf
	kCDXBondOrder_DoubleOrAromatic = kCDXBondOrder_Double | kCDXBondOrder_OneHalf
	kCDXBondOrder_Any = -1



	def find(order):
		for item in CDXBondOrder:
			if item.value==order:
				return item

		return None


# Permit combination of CDXBondOrder values
# inline CDXBondOrder &operator |= (CDXBondOrder &lhs const CDXBondOrder &rhs)

# 	return lhs = CDXBondOrder(UINT32(lhs) | UINT32(rhs));
# }

class  CDXBondDisplay(Enum):
	kCDXBondDisplay_Solid				=0
	kCDXBondDisplay_Dash				=1
	kCDXBondDisplay_Hash				=2
	kCDXBondDisplay_WedgedHashBegin		=3
	kCDXBondDisplay_WedgedHashEnd		=4
	kCDXBondDisplay_Bold				=5
	kCDXBondDisplay_WedgeBegin			=6
	kCDXBondDisplay_WedgeEnd			=7
	kCDXBondDisplay_Wavy				=8
	kCDXBondDisplay_HollowWedgeBegin	=9
	kCDXBondDisplay_HollowWedgeEnd		=10
	kCDXBondDisplay_WavyWedgeBegin		=11
	kCDXBondDisplay_WavyWedgeEnd		=12
	kCDXBondDisplay_Dot					=13
	kCDXBondDisplay_DashDot				= 14

	def find(val):
		for item in CDXBondDisplay:
			if item.value==val:
				return item
		return CDXBondDisplay.UNKNOWN

class  CDXBondDoublePosition(Enum):
	kCDXBondDoublePosition_AutoCenter	=0
	kCDXBondDoublePosition_AutoRight	=1
	kCDXBondDoublePosition_AutoLeft		=2
	kCDXBondDoublePosition_UserCenter	=256
	kCDXBondDoublePosition_UserRight	=257
	kCDXBondDoublePosition_UserLeft		= 0x0102
	
		
class  CDXBondTopology(Enum):
	kCDXBondTopology_Unspecified	=0
	kCDXBondTopology_Ring			=1
	kCDXBondTopology_Chain			=2
	kCDXBondTopology_RingOrChain	= 3


class  CDXBondReactionParticipation(Enum):
	kCDXBondReactionParticipation_Unspecified		=0
	kCDXBondReactionParticipation_ReactionCenter	=1
	kCDXBondReactionParticipation_MakeOrBreak		=2
	kCDXBondReactionParticipation_ChangeType		=3
	kCDXBondReactionParticipation_MakeAndChange		=4
	kCDXBondReactionParticipation_NotReactionCenter	=5
	kCDXBondReactionParticipation_NoChange			=6
	kCDXBondReactionParticipation_Unmapped			= 7


class  CDXTextJustification(Enum):
	kCDXTextJustification_Right = -1
	kCDXTextJustification_Left=0
	kCDXTextJustification_Center=1
	kCDXTextJustification_Full=2
	kCDXTextJustification_Above=3
	kCDXTextJustification_Below=4
	kCDXTextJustification_Auto=5
	kCDXTextJustification_BestInitial=6


#define kCDXTagType_Unknown			"unknown"
#define kCDXTagType_Query			"query"
#define kCDXTagType_Rxn				"reaction"
#define kCDXTagType_Stereo			"stereo"
#define kCDXTagType_Number			"number"
#define kCDXTagType_Heading			"heading"
#define kCDXTagType_IDTerm			"idterm"
#define kCDXTagType_BracketUsage	"bracketusage"
#define kCDXTagType_PolymerRepeat	"polymerrepeat"
#define kCDXTagType_PolymerFlip		"polymerflip"
#define kCDXTagType_Deviation		"deviation"
#define kCDXTagType_Distance		"distance"
#define kCDXTagType_Angle			"angle"
#define kCDXTagType_Rf				"rf"

class  CDXPositioningType(Enum):
	kCDXPositioningType_Auto =0
	kCDXPositioningType_Angle=1
	kCDXPositioningType_Offset=2
	kCDXPositioningType_Absolute=3


class  CDXPageDefinition(Enum):
	kCDXPageDefinition_Undefined =0
	kCDXPageDefinition_Center=1
	kCDXPageDefinition_TL4=2
	kCDXPageDefinition_IDTerm=3
	kCDXPageDefinition_FlushLeft=4
	kCDXPageDefinition_FlushRight=5
	kCDXPageDefinition_Reaction1=6
	kCDXPageDefinition_Reaction2=7
	kCDXPageDefinition_MulticolumnTL4=8
	kCDXPageDefinition_MulticolumnNonTL4=9
	kCDXPageDefinition_UserDefined=10


#define kCDXLineHeight_Variable  0
#define kCDXLineHeight_Automatic 1

class  CDXGraphicType(Enum):
	kCDXGraphicType_Undefined =0
	kCDXGraphicType_Line=1
	kCDXGraphicType_Arc=2
	kCDXGraphicType_Rectangle=3
	kCDXGraphicType_Oval=4
	kCDXGraphicType_Orbital=5
	kCDXGraphicType_Bracket=6
	kCDXGraphicType_Symbol=7


class  CDXBracketType(Enum):

	kCDXBracketType_RoundPair=0
	kCDXBracketType_SquarePair=1
	kCDXBracketType_CurlyPair=2
	kCDXBracketType_Square=3
	kCDXBracketType_Curly=4
	kCDXBracketType_Round=5


class  CDXRectangleType(Enum):

	kCDXRectangleType_Plain =0
	kCDXRectangleType_RoundEdge =1
	kCDXRectangleType_Shadow =2
	kCDXRectangleType_Shaded =4
	kCDXRectangleType_Filled =8
	kCDXRectangleType_Dashed =16
	kCDXRectangleType_Bold = 0x0020


class  CDXOvalType(Enum):

	kCDXOvalType_Circle =1
	kCDXOvalType_Shaded =2
	kCDXOvalType_Filled =4
	kCDXOvalType_Dashed =8
	kCDXOvalType_Bold   =16
	kCDXOvalType_Shadowed   = 0x0020


class  CDXSymbolType(Enum):

	kCDXSymbolType_LonePair=0
	kCDXSymbolType_Electron=1
	kCDXSymbolType_RadicalCation=2
	kCDXSymbolType_RadicalAnion=3
	kCDXSymbolType_CirclePlus=4
	kCDXSymbolType_CircleMinus=5
	kCDXSymbolType_Dagger=6
	kCDXSymbolType_DoubleDagger=7
	kCDXSymbolType_Plus=8
	kCDXSymbolType_Minus=9
	kCDXSymbolType_Racemic=10
	kCDXSymbolType_Absolute=11
	kCDXSymbolType_Relative=12


class  CDXLineType(Enum):

	kCDXLineType_Solid  =0
	kCDXLineType_Dashed =1
	kCDXLineType_Bold	=2
	kCDXLineType_Wavy	= 0x0004


class  CDXArrowType(Enum):

	kCDXArrowType_NoHead			=0
	kCDXArrowType_HalfHead			=1
	kCDXArrowType_FullHead			=2
	kCDXArrowType_Resonance			=4
	kCDXArrowType_Equilibrium		=8
	kCDXArrowType_Hollow			=16
	kCDXArrowType_RetroSynthetic	= 32


class  CDXOrbitalType(Enum):

	kCDXOrbitalType_s=0					# s orbital
	kCDXOrbitalType_oval=1				# Oval-shaped sigma or pi orbital
	kCDXOrbitalType_lobe=2				# One lobe of a p orbital
	kCDXOrbitalType_p=3					# Complete p orbital
	kCDXOrbitalType_hybridPlus=4			# hydrid orbital
	kCDXOrbitalType_hybridMinus=5		# hydrid orbital (opposite shading)
	kCDXOrbitalType_dz2Plus=6			# dz2 orbital
	kCDXOrbitalType_dz2Minus=7			# dz2 orbital (opposite shading)
	kCDXOrbitalType_dxy=8				# dxy orbital

	kCDXOrbitalType_sShaded =256	# shaded s orbital
	kCDXOrbitalType_ovalShaded=257			# shaded Oval-shaped sigma or pi orbital
	kCDXOrbitalType_lobeShaded=258			# shaded single lobe of a p orbital
	kCDXOrbitalType_pShaded=259			# shaded Complete p orbital
	
	kCDXOrbitalType_sFilled =512	# filled s orbital
	kCDXOrbitalType_ovalFilled=513			# filled Oval-shaped sigma or pi orbital
	kCDXOrbitalType_lobeFilled=514			# filled single lobe of a p orbital
	kCDXOrbitalType_pFilled=515			# filled Complete p orbital
	kCDXOrbitalType_hybridPlusFilled=516	# filled hydrid orbital
	kCDXOrbitalType_hybridMinusFilled=517	# filled hydrid orbital (opposite shading)
	kCDXOrbitalType_dz2PlusFilled=518		# filled dz2 orbital
	kCDXOrbitalType_dz2MinusFilled=519		# filled dz2 orbital (opposite shading)
	kCDXOrbitalType_dxyFilled		=520	# filled dxy orbital



class  CDXBracketUsage(Enum):

	kCDXBracketUsage_Unspecified =0
	kCDXBracketUsage_Anypolymer =18
	kCDXBracketUsage_Component =13
	kCDXBracketUsage_Copolymer =6
	kCDXBracketUsage_CopolymerAlternating =7
	kCDXBracketUsage_CopolymerBlock =9
	kCDXBracketUsage_CopolymerRandom =8
	kCDXBracketUsage_Crosslink =10
	kCDXBracketUsage_Generic =17
	kCDXBracketUsage_Graft =11
	kCDXBracketUsage_Mer =5
	kCDXBracketUsage_MixtureOrdered =15
	kCDXBracketUsage_MixtureUnordered =14
	kCDXBracketUsage_Modification =12
	kCDXBracketUsage_Monomer =4
	kCDXBracketUsage_MultipleGroup =16
	kCDXBracketUsage_SRU =3
	kCDXBracketUsage_Unused1 =1
	kCDXBracketUsage_Unused2 = 2


class  CDXPolymerRepeatPattern(Enum):

	kCDXPolymerRepeatPattern_HeadToTail =0
	kCDXPolymerRepeatPattern_HeadToHead=1
	kCDXPolymerRepeatPattern_EitherUnknown=2


class  CDXPolymerFlipType(Enum):

	kCDXPolymerFlipType_Unspecified =0
	kCDXPolymerFlipType_NoFlip=1
	kCDXPolymerFlipType_Flip=2


class  CDXSpectrumYType(Enum):

	kCDXSpectrumYType_Unknown=0
	kCDXSpectrumYType_Absorbance=1
	kCDXSpectrumYType_Transmittance=2
	kCDXSpectrumYType_PercentTransmittance=3
	kCDXSpectrumYType_Other=4
	kCDXSpectrumYType_ArbitraryUnits=2


class  CDXSpectrumXType(Enum):

	kCDXSpectrumXType_Unknown=0
	kCDXSpectrumXType_Microns=1
	kCDXSpectrumXType_Hertz=2
	kCDXSpectrumXType_MassUnits=3
	kCDXSpectrumXType_PartsPerMillion=4
	kCDXSpectrumXType_Other=5


class  CDXSpectrumClass(Enum):

	kCDXSpectrumClass_Unknown=0
	kCDXSpectrumClass_Chromatogram=1
	kCDXSpectrumClass_Infrared=2
	kCDXSpectrumClass_UVVis=3
	kCDXSpectrumClass_XRayDiffraction=4
	kCDXSpectrumClass_MassSpectrum=5
	kCDXSpectrumClass_NMR=6
	kCDXSpectrumClass_Raman=7
	kCDXSpectrumClass_Fluorescence=8
	kCDXSpectrumClass_Atomic=9


class  CDXDrawingSpaceType(Enum):

	kCDXDrawingSpace_Pages=0
	kCDXDrawingSpace_Poster=1


class  CDXAtomCIPType(Enum):

	kCDXCIPAtom_Undetermined			=0
	kCDXCIPAtom_None=1
	kCDXCIPAtom_R=2
	kCDXCIPAtom_S=3
	kCDXCIPAtom_r=4
	kCDXCIPAtom_s=5
	kCDXCIPAtom_Unspecified	=6					# No hash/wedge but if there were one, it would have stereochemistry.


class  CDXBondCIPType(Enum):

	kCDXCIPBond_Undetermined			=0
	kCDXCIPBond_None=1
	kCDXCIPBond_E=2
	kCDXCIPBond_Z=3


class  CDXObjectTagType(Enum):

	kCDXObjectTagType_Undefined			=0
	kCDXObjectTagType_Double=1
	kCDXObjectTagType_Long=2
	kCDXObjectTagType_String=3


class  CDXSideType(Enum):

	kCDXSideType_Undefined				=0
	kCDXSideType_Top=1
	kCDXSideType_Left=2
	kCDXSideType_Bottom=3
	kCDXSideType_Right=4


class  CDXGeometricFeature(Enum):

	kCDXGeometricFeature_Undefined				=0
	kCDXGeometricFeature_PointFromPointPointDistance=1
	kCDXGeometricFeature_PointFromPointPointPercentage=2
	kCDXGeometricFeature_PointFromPointNormalDistance=3
	kCDXGeometricFeature_LineFromPoints=4
	kCDXGeometricFeature_PlaneFromPoints=5
	kCDXGeometricFeature_PlaneFromPointLine=6
	kCDXGeometricFeature_CentroidFromPoints=7
	kCDXGeometricFeature_NormalFromPointPlane=8


class  CDXConstraintType(Enum):

	kCDXConstraintType_Undefined			=0
	kCDXConstraintType_Distance=1
	kCDXConstraintType_Angle=2
	kCDXConstraintType_ExclusionSphere=3


class  CDXCharSet(Enum):

	# kCDXCharSetUnknown =0
	# kCDXCharSetEBCDICOEM =37
	# kCDXCharSetMSDOSUS =437
	# kCDXCharSetEBCDIC500V1 =500
	# kCDXCharSetArabicASMO708 =708
	# kCDXCharSetArabicASMO449P=709
	# kCDXCharSetArabicTransparent=710
	# kCDXCharSetArabicTransparentASMO =720
	# kCDXCharSetGreek437G =737
	# kCDXCharSetBalticOEM =775
	# kCDXCharSetMSDOSLatin1 =850
	# kCDXCharSetMSDOSLatin2 =852
	# kCDXCharSetIBMCyrillic =855
	# kCDXCharSetIBMTurkish =857
	# kCDXCharSetMSDOSPortuguese =860
	# kCDXCharSetMSDOSIcelandic=861
	# kCDXCharSetHebrewOEM=862
	# kCDXCharSetMSDOSCanadianFrench=863
	# kCDXCharSetArabicOEM=864
	# kCDXCharSetMSDOSNordic=865
	# kCDXCharSetMSDOSRussian=866
	# kCDXCharSetIBMModernGreek =869
	# kCDXCharSetThai =874
	# kCDXCharSetEBCDIC=875
	# kCDXCharSetJapanese =932
	# kCDXCharSetChineseSimplified =936 # PRC Singapore
	# kCDXCharSetKorean =949
	# kCDXCharSetChineseTraditional =950 # Taiwan, Hong Kong
	# kCDXCharSetUnicodeISO10646 =1200
	# kCDXCharSetWin31EasternEuropean =1250
	# kCDXCharSetWin31Cyrillic=1251
	# kCDXCharSetWin31Latin1=1252
	# kCDXCharSetWin31Greek=1253
	# kCDXCharSetWin31Turkish=1254
	# kCDXCharSetHebrew=1255
	# kCDXCharSetArabic=1256
	# kCDXCharSetBaltic=1257
	# kCDXCharSetVietnamese=1258
	# kCDXCharSetKoreanJohab =1361
	# kCDXCharSetMacRoman =10000
	# kCDXCharSetMacJapanese=10001
	# kCDXCharSetMacTradChinese=10002
	# kCDXCharSetMacKorean=10003
	# kCDXCharSetMacArabic=10004
	# kCDXCharSetMacHebrew=10005
	# kCDXCharSetMacGreek=10006
	# kCDXCharSetMacCyrillic=10007
	# kCDXCharSetMacReserved=10008
	# kCDXCharSetMacDevanagari=10009
	# kCDXCharSetMacGurmukhi=10010
	# kCDXCharSetMacGujarati=10011
	# kCDXCharSetMacOriya=10012
	# kCDXCharSetMacBengali=10013
	# kCDXCharSetMacTamil=10014
	# kCDXCharSetMacTelugu=10015
	# kCDXCharSetMacKannada=10016
	# kCDXCharSetMacMalayalam=10017
	# kCDXCharSetMacSinhalese=10018
	# kCDXCharSetMacBurmese=10019
	# kCDXCharSetMacKhmer=10020
	# kCDXCharSetMacThai=10021
	# kCDXCharSetMacLao=10022
	# kCDXCharSetMacGeorgian=10023
	# kCDXCharSetMacArmenian=10024
	# kCDXCharSetMacSimpChinese=10025
	# kCDXCharSetMacTibetan=10026
	# kCDXCharSetMacMongolian=10027
	# kCDXCharSetMacEthiopic=10028
	# kCDXCharSetMacCentralEuroRoman=10029
	# kCDXCharSetMacVietnamese=10030
	# kCDXCharSetMacExtArabic=10031
	# kCDXCharSetMacUninterpreted=10032
	# kCDXCharSetMacIcelandic =10079
	# kCDXCharSetMacTurkish = 10081
	kCDXCharSetUnknown = (0, 'Unknown')
	kCDXCharSetEBCDICOEM = (37, 'EBCDICOEM')
	kCDXCharSetMSDOSUS = (437, 'MSDOSUS')
	kCDXCharSetEBCDIC500V1 = (500, 'EBCDIC500V1')
	kCDXCharSetArabicASMO708 = (708, 'ASMO-708')
	kCDXCharSetArabicASMO449P = (709, 'ArabicASMO449P')
	kCDXCharSetArabicTransparent = (710, 'ArabicTransparent')
	kCDXCharSetArabicTransparentASMO = (720, 'DOS-720')
	kCDXCharSetGreek437G = (737, 'Greek437G')
	kCDXCharSetBalticOEM = (775, 'cp775')
	kCDXCharSetMSDOSLatin1 = (850, 'windows-850')
	kCDXCharSetMSDOSLatin2 = (852, 'ibm852')
	kCDXCharSetIBMCyrillic = (855, 'cp855')
	kCDXCharSetIBMTurkish = (857, 'cp857')
	kCDXCharSetMSDOSPortuguese = (860, 'cp860')
	kCDXCharSetMSDOSIcelandic = (861, 'cp861')
	kCDXCharSetHebrewOEM = (862, 'DOS-862')
	kCDXCharSetMSDOSCanadianFrench = (863, 'cp863')
	kCDXCharSetArabicOEM = (864, 'cp864')
	kCDXCharSetMSDOSNordic = (865, 'cp865')
	kCDXCharSetMSDOSRussian = (866, 'cp866')
	kCDXCharSetIBMModernGreek = (869, 'cp869')
	kCDXCharSetThai = (874, 'windows-874')
	kCDXCharSetEBCDIC = (875, 'EBCDIC')
	kCDXCharSetJapanese = (932, 'shift_jis')
	kCDXCharSetChineseSimplified = (936, 'gb2312')
	kCDXCharSetKorean = (949, 'ks_c_5601-1987')
	kCDXCharSetChineseTraditional = (950, 'big5')
	kCDXCharSetUnicodeISO10646 = (1200, 'iso-10646')
	kCDXCharSetWin31EasternEuropean = (1250, 'windows-1250')
	kCDXCharSetWin31Cyrillic = (1251, 'windows-1251')
	kCDXCharSetWin31Latin1 = (1252, 'iso-8859-1')
	kCDXCharSetWin31Greek = (1253, 'iso-8859-7')
	kCDXCharSetWin31Turkish = (1254, 'iso-8859-9')
	kCDXCharSetHebrew = (1255, 'windows-1255')
	kCDXCharSetArabic = (1256, 'windows-1256')
	kCDXCharSetBaltic = (1257, 'windows-1257')
	kCDXCharSetVietnamese = (1258, 'windows-1258')
	kCDXCharSetKoreanJohab = (1361, 'windows-1361')
	kCDXCharSetMacRoman = (10000, 'x-mac-roman')
	kCDXCharSetMacJapanese = (10001, 'x-mac-japanese')
	kCDXCharSetMacTradChinese = (10002, 'x-mac-tradchinese')
	kCDXCharSetMacKorean = (10003, 'x-mac-korean')
	kCDXCharSetMacArabic = (10004, 'x-mac-arabic')
	kCDXCharSetMacHebrew = (10005, 'x-mac-hebrew')
	kCDXCharSetMacGreek = (10006, 'x-mac-greek')
	kCDXCharSetMacCyrillic = (10007, 'x-mac-cyrillic')
	kCDXCharSetMacReserved = (10008, 'x-mac-reserved')
	kCDXCharSetMacDevanagari = (10009, 'x-mac-devanagari')
	kCDXCharSetMacGurmukhi = (10010, 'x-mac-gurmukhi')
	kCDXCharSetMacGujarati = (10011, 'x-mac-gujarati')
	kCDXCharSetMacOriya = (10012, 'x-mac-oriya')
	kCDXCharSetMacBengali = (10013, 'x-mac-nengali')
	kCDXCharSetMacTamil = (10014, 'x-mac-tamil')
	kCDXCharSetMacTelugu = (10015, 'x-mac-telugu')
	kCDXCharSetMacKannada = (10016, 'x-mac-kannada')
	kCDXCharSetMacMalayalam = (10017, 'x-mac-Malayalam')
	kCDXCharSetMacSinhalese = (10018, 'x-mac-sinhalese')
	kCDXCharSetMacBurmese = (10019, 'x-mac-burmese')
	kCDXCharSetMacKhmer = (10020, 'x-mac-khmer')
	kCDXCharSetMacThai = (10021, 'x-mac-thai')
	kCDXCharSetMacLao = (10022, 'x-mac-lao')
	kCDXCharSetMacGeorgian = (10023, 'x-mac-georgian')
	kCDXCharSetMacArmenian = (10024, 'x-mac-armenian')
	kCDXCharSetMacSimpChinese = (10025, 'x-mac-simpChinese')
	kCDXCharSetMacTibetan = (10026, 'x-mac-tibetan')
	kCDXCharSetMacMongolian = (10027, 'x-mac-mongolian')
	kCDXCharSetMacEthiopic = (10028, 'x-mac-ethiopic')
	kCDXCharSetMacCentralEuroRoman = (10029, 'x-mac-ce')
	kCDXCharSetMacVietnamese = (10030, 'x-mac-vietnamese')
	kCDXCharSetMacExtArabic = (10031, 'x-mac-extArabic')
	kCDXCharSetMacUninterpreted = (10032, 'x-mac-uninterpreted')
	kCDXCharSetMacIcelandic = (10079, 'x-mac-icelandic')
	kCDXCharSetMacTurkish = (10081, 'x-mac-turkish')
	def find(val):
		for i in CDXCharSet:
			if i.value[0]==val:
				return i.value[1]
		else:
			return CDXCharSet.kCDXCharSetUnknown.value[1]


#endif # _H_CDXConstants

CDX_Objects=[
	CDXDatumID.kCDXObj_Document,
	CDXDatumID.kCDXObj_Page,
	CDXDatumID.kCDXObj_Group,
	CDXDatumID.kCDXObj_Fragment,
	CDXDatumID.kCDXObj_Node,
	CDXDatumID.kCDXObj_Bond,
	CDXDatumID.kCDXObj_Text,
	CDXDatumID.kCDXObj_Graphic,
	CDXDatumID.kCDXObj_Curve,
	CDXDatumID.kCDXObj_EmbeddedObject,
	CDXDatumID.kCDXObj_NamedAlternativeGroup,
	CDXDatumID.kCDXObj_TemplateGrid,
	CDXDatumID.kCDXObj_RegistryNumber,
	CDXDatumID.kCDXObj_ReactionScheme,
	CDXDatumID.kCDXObj_ReactionStep,
	CDXDatumID.kCDXObj_ObjectDefinition,
	CDXDatumID.kCDXObj_Spectrum,
	CDXDatumID.kCDXObj_ObjectTag,
	CDXDatumID.kCDXObj_OleClientItem,
	CDXDatumID.kCDXObj_Sequence,
	CDXDatumID.kCDXObj_CrossReference,
	CDXDatumID.kCDXObj_Splitter,
	CDXDatumID.kCDXObj_Table,
	CDXDatumID.kCDXObj_BracketedGroup,
	CDXDatumID.kCDXObj_BracketAttachment,
	CDXDatumID.kCDXObj_CrossingBond,
	CDXDatumID.kCDXObj_Border,
	CDXDatumID.kCDXObj_Geometry,
	CDXDatumID.kCDXObj_Constraint,
	CDXDatumID.kCDXObj_TLCPlate,
	CDXDatumID.kCDXObj_TLCLane,
	CDXDatumID.kCDXObj_TLCSpot,
	CDXDatumID.kCDXObj_UnknownObject
]
CDX_TAG_TYPE={
	CDXDatumID.kCDXProp_EndObject:'EndObject',
	CDXDatumID.kCDXProp_CreationUserName:'CreationUserName',
	CDXDatumID.kCDXProp_CreationDate:'CreationDate',
	CDXDatumID.kCDXProp_CreationProgram:'CreationProgram',
	CDXDatumID.kCDXProp_ModificationUserName:'ModificationUserName',
	CDXDatumID.kCDXProp_ModificationDate:'ModificationDate',
	CDXDatumID.kCDXProp_ModificationProgram:'ModificationProgram',
	CDXDatumID.kCDXProp_Unused1:'Unused1',
	CDXDatumID.kCDXProp_Name:'Name',
	CDXDatumID.kCDXProp_Comment:'Comment',
	CDXDatumID.kCDXProp_ZOrder:'ZOrder',
	CDXDatumID.kCDXProp_RegistryNumber:'RegistryNumber',
	CDXDatumID.kCDXProp_RegistryAuthority:'RegistryAuthority',
	CDXDatumID.kCDXProp_Unused2:'Unused2',
	CDXDatumID.kCDXProp_RepresentsProperty:'RepresentsProperty',
	CDXDatumID.kCDXProp_IgnoreWarnings:'IgnoreWarnings',
	CDXDatumID.kCDXProp_ChemicalWarning:'ChemicalWarning',
	CDXDatumID.kCDXProp_Visible:'Visible',
	CDXDatumID.kCDXProp_FontTable:'FontTable',
	CDXDatumID.kCDXProp_2DPosition:'2DPosition',
	CDXDatumID.kCDXProp_3DPosition:'3DPosition',
	CDXDatumID.kCDXProp_2DExtent:'2DExtent',
	CDXDatumID.kCDXProp_3DExtent:'3DExtent',
	CDXDatumID.kCDXProp_BoundingBox:'BoundingBox',
	CDXDatumID.kCDXProp_RotationAngle:'RotationAngle',
	CDXDatumID.kCDXProp_BoundsInParent:'BoundsInParent',
	CDXDatumID.kCDXProp_3DHead:'3DHead',
	CDXDatumID.kCDXProp_3DTail:'3DTail',
	CDXDatumID.kCDXProp_TopLeft:'TopLeft',
	CDXDatumID.kCDXProp_TopRight:'TopRight',
	CDXDatumID.kCDXProp_BottomRight:'BottomRight',
	CDXDatumID.kCDXProp_BottomLeft:'BottomLeft',
	CDXDatumID.kCDXProp_ColorTable:'ColorTable',
	CDXDatumID.kCDXProp_ForegroundColor:'ForegroundColor',
	CDXDatumID.kCDXProp_BackgroundColor:'BackgroundColor',
	CDXDatumID.kCDXProp_Node_Type:'Node_Type',
	CDXDatumID.kCDXProp_Node_LabelDisplay:'Node_LabelDisplay',
	CDXDatumID.kCDXProp_Node_Element:'Node_Element',
	CDXDatumID.kCDXProp_Atom_ElementList:'Atom_ElementList',
	CDXDatumID.kCDXProp_Atom_Formula:'Atom_Formula',
	CDXDatumID.kCDXProp_Atom_Isotope:'Atom_Isotope',
	CDXDatumID.kCDXProp_Atom_Charge:'Atom_Charge',
	CDXDatumID.kCDXProp_Atom_Radical:'Atom_Radical',
	CDXDatumID.kCDXProp_Atom_RestrictFreeSites:'Atom_RestrictFreeSites',
	CDXDatumID.kCDXProp_Atom_RestrictImplicitHydrogens:'Atom_RestrictImplicitHydrogens',
	CDXDatumID.kCDXProp_Atom_RestrictRingBondCount:'Atom_RestrictRingBondCount',
	CDXDatumID.kCDXProp_Atom_RestrictUnsaturatedBonds:'Atom_RestrictUnsaturatedBonds',
	CDXDatumID.kCDXProp_Atom_RestrictRxnChange:'Atom_RestrictRxnChange',
	CDXDatumID.kCDXProp_Atom_RestrictRxnStereo:'Atom_RestrictRxnStereo',
	CDXDatumID.kCDXProp_Atom_AbnormalValence:'Atom_AbnormalValence',
	CDXDatumID.kCDXProp_Unused3:'Unused3',
	CDXDatumID.kCDXProp_Atom_NumHydrogens:'Atom_NumHydrogens',
	CDXDatumID.kCDXProp_Unused4:'Unused4',
	CDXDatumID.kCDXProp_Unused5:'Unused5',
	CDXDatumID.kCDXProp_Atom_HDot:'Atom_HDot',
	CDXDatumID.kCDXProp_Atom_HDash:'Atom_HDash',
	CDXDatumID.kCDXProp_Atom_Geometry:'Atom_Geometry',
	CDXDatumID.kCDXProp_Atom_BondOrdering:'Atom_BondOrdering',
	CDXDatumID.kCDXProp_Node_Attachments:'Node_Attachments',
	CDXDatumID.kCDXProp_Atom_GenericNickname:'Atom_GenericNickname',
	CDXDatumID.kCDXProp_Atom_AltGroupID:'Atom_AltGroupID',
	CDXDatumID.kCDXProp_Atom_RestrictSubstituentsUpTo:'Atom_RestrictSubstituentsUpTo',
	CDXDatumID.kCDXProp_Atom_RestrictSubstituentsExactly:'Atom_RestrictSubstituentsExactly',
	CDXDatumID.kCDXProp_Atom_CIPStereochemistry:'Atom_CIPStereochemistry',
	CDXDatumID.kCDXProp_Atom_Translation:'Atom_Translation',
	CDXDatumID.kCDXProp_Atom_AtomNumber:'Atom_AtomNumber',
	CDXDatumID.kCDXProp_Atom_ShowQuery:'Atom_ShowQuery',
	CDXDatumID.kCDXProp_Atom_ShowStereo:'Atom_ShowStereo',
	CDXDatumID.kCDXProp_Atom_ShowAtomNumber:'Atom_ShowAtomNumber',
	CDXDatumID.kCDXProp_Atom_LinkCountLow:'Atom_LinkCountLow',
	CDXDatumID.kCDXProp_Atom_LinkCountHigh:'Atom_LinkCountHigh',
	CDXDatumID.kCDXProp_Atom_IsotopicAbundance:'Atom_IsotopicAbundance',
	CDXDatumID.kCDXProp_Atom_ExternalConnectionType:'Atom_ExternalConnectionType',
	CDXDatumID.kCDXProp_Mole_Racemic:'Mole_Racemic',
	CDXDatumID.kCDXProp_Mole_Absolute:'Mole_Absolute',
	CDXDatumID.kCDXProp_Mole_Relative:'Mole_Relative',
	CDXDatumID.kCDXProp_Mole_Formula:'Mole_Formula',
	CDXDatumID.kCDXProp_Mole_Weight:'Mole_Weight',
	CDXDatumID.kCDXProp_Frag_ConnectionOrder:'Frag_ConnectionOrder',
	CDXDatumID.kCDXProp_Bond_Order:'Bond_Order',
	CDXDatumID.kCDXProp_Bond_Display:'Bond_Display',
	CDXDatumID.kCDXProp_Bond_Display2:'Bond_Display2',
	CDXDatumID.kCDXProp_Bond_DoublePosition:'Bond_DoublePosition',
	CDXDatumID.kCDXProp_Bond_Begin:'Bond_Begin',
	CDXDatumID.kCDXProp_Bond_End:'Bond_End',
	CDXDatumID.kCDXProp_Bond_RestrictTopology:'Bond_RestrictTopology',
	CDXDatumID.kCDXProp_Bond_RestrictRxnParticipation:'Bond_RestrictRxnParticipation',
	CDXDatumID.kCDXProp_Bond_BeginAttach:'Bond_BeginAttach',
	CDXDatumID.kCDXProp_Bond_EndAttach:'Bond_EndAttach',
	CDXDatumID.kCDXProp_Bond_CIPStereochemistry:'Bond_CIPStereochemistry',
	CDXDatumID.kCDXProp_Bond_BondOrdering:'Bond_BondOrdering',
	CDXDatumID.kCDXProp_Bond_ShowQuery:'Bond_ShowQuery',
	CDXDatumID.kCDXProp_Bond_ShowStereo:'Bond_ShowStereo',
	CDXDatumID.kCDXProp_Bond_CrossingBonds:'Bond_CrossingBonds',
	CDXDatumID.kCDXProp_Bond_ShowRxn:'Bond_ShowRxn',
	CDXDatumID.kCDXProp_Text:'Text',
	CDXDatumID.kCDXProp_Justification:'Justification',
	CDXDatumID.kCDXProp_LineHeight:'LineHeight',
	CDXDatumID.kCDXProp_WordWrapWidth:'WordWrapWidth',
	CDXDatumID.kCDXProp_LineStarts:'LineStarts',
	CDXDatumID.kCDXProp_LabelAlignment:'LabelAlignment',
	CDXDatumID.kCDXProp_LabelLineHeight:'LabelLineHeight',
	CDXDatumID.kCDXProp_CaptionLineHeight:'CaptionLineHeight',
	CDXDatumID.kCDXProp_InterpretChemically:'InterpretChemically',
	CDXDatumID.kCDXProp_MacPrintInfo:'MacPrintInfo',
	CDXDatumID.kCDXProp_WinPrintInfo:'WinPrintInfo',
	CDXDatumID.kCDXProp_PrintMargins:'PrintMargins',
	CDXDatumID.kCDXProp_ChainAngle:'ChainAngle',
	CDXDatumID.kCDXProp_BondSpacing:'BondSpacing',
	CDXDatumID.kCDXProp_BondLength:'BondLength',
	CDXDatumID.kCDXProp_BoldWidth:'BoldWidth',
	CDXDatumID.kCDXProp_LineWidth:'LineWidth',
	CDXDatumID.kCDXProp_MarginWidth:'MarginWidth',
	CDXDatumID.kCDXProp_HashSpacing:'HashSpacing',
	CDXDatumID.kCDXProp_LabelStyle:'LabelStyle',
	CDXDatumID.kCDXProp_CaptionStyle:'CaptionStyle',
	CDXDatumID.kCDXProp_CaptionJustification:'CaptionJustification',
	CDXDatumID.kCDXProp_FractionalWidths:'FractionalWidths',
	CDXDatumID.kCDXProp_Magnification:'Magnification',
	CDXDatumID.kCDXProp_WidthPages:'WidthPages',
	CDXDatumID.kCDXProp_HeightPages:'HeightPages',
	CDXDatumID.kCDXProp_DrawingSpaceType:'DrawingSpaceType',
	CDXDatumID.kCDXProp_Width:'Width',
	CDXDatumID.kCDXProp_Height:'Height',
	CDXDatumID.kCDXProp_PageOverlap:'PageOverlap',
	CDXDatumID.kCDXProp_Header:'Header',
	CDXDatumID.kCDXProp_HeaderPosition:'HeaderPosition',
	CDXDatumID.kCDXProp_Footer:'Footer',
	CDXDatumID.kCDXProp_FooterPosition:'FooterPosition',
	CDXDatumID.kCDXProp_PrintTrimMarks:'PrintTrimMarks',
	CDXDatumID.kCDXProp_LabelStyleFont:'LabelStyleFont',
	CDXDatumID.kCDXProp_CaptionStyleFont:'CaptionStyleFont',
	CDXDatumID.kCDXProp_LabelStyleSize:'LabelStyleSize',
	CDXDatumID.kCDXProp_CaptionStyleSize:'CaptionStyleSize',
	CDXDatumID.kCDXProp_LabelStyleFace:'LabelStyleFace',
	CDXDatumID.kCDXProp_CaptionStyleFace:'CaptionStyleFace',
	CDXDatumID.kCDXProp_LabelStyleColor:'LabelStyleColor',
	CDXDatumID.kCDXProp_CaptionStyleColor:'CaptionStyleColor',
	CDXDatumID.kCDXProp_BondSpacingAbs:'BondSpacingAbs',
	CDXDatumID.kCDXProp_LabelJustification:'LabelJustification',
	CDXDatumID.kCDXProp_FixInplaceExtent:'FixInplaceExtent',
	CDXDatumID.kCDXProp_Side:'Side',
	CDXDatumID.kCDXProp_FixInplaceGap:'FixInplaceGap',
	CDXDatumID.kCDXProp_Window_IsZoomed:'Window_IsZoomed',
	CDXDatumID.kCDXProp_Window_Position:'Window_Position',
	CDXDatumID.kCDXProp_Window_Size:'Window_Size',
	CDXDatumID.kCDXProp_Graphic_Type:'Graphic_Type',
	CDXDatumID.kCDXProp_Line_Type:'Line_Type',
	CDXDatumID.kCDXProp_Arrow_Type:'Arrow_Type',
	CDXDatumID.kCDXProp_Rectangle_Type:'Rectangle_Type',
	CDXDatumID.kCDXProp_Oval_Type:'Oval_Type',
	CDXDatumID.kCDXProp_Orbital_Type:'Orbital_Type',
	CDXDatumID.kCDXProp_Bracket_Type:'Bracket_Type',
	CDXDatumID.kCDXProp_Symbol_Type:'Symbol_Type',
	CDXDatumID.kCDXProp_Curve_Type:'Curve_Type',
	CDXDatumID.kCDXProp_Arrow_HeadSize:'Arrow_HeadSize',
	CDXDatumID.kCDXProp_Arc_AngularSize:'Arc_AngularSize',
	CDXDatumID.kCDXProp_Bracket_LipSize:'Bracket_LipSize',
	CDXDatumID.kCDXProp_Curve_Points:'Curve_Points',
	CDXDatumID.kCDXProp_Bracket_Usage:'Bracket_Usage',
	CDXDatumID.kCDXProp_Polymer_RepeatPattern:'Polymer_RepeatPattern',
	CDXDatumID.kCDXProp_Polymer_FlipType:'Polymer_FlipType',
	CDXDatumID.kCDXProp_BracketedObjects:'BracketedObjects',
	CDXDatumID.kCDXProp_Bracket_RepeatCount:'Bracket_RepeatCount',
	CDXDatumID.kCDXProp_Bracket_ComponentOrder:'Bracket_ComponentOrder',
	CDXDatumID.kCDXProp_Bracket_SRULabel:'Bracket_SRULabel',
	CDXDatumID.kCDXProp_Bracket_GraphicID:'Bracket_GraphicID',
	CDXDatumID.kCDXProp_Bracket_BondID:'Bracket_BondID',
	CDXDatumID.kCDXProp_Bracket_InnerAtomID:'Bracket_InnerAtomID',
	CDXDatumID.kCDXProp_Curve_Points3D:'Curve_Points3D',
	CDXDatumID.kCDXProp_Picture_Edition:'Picture_Edition',
	CDXDatumID.kCDXProp_Picture_EditionAlias:'Picture_EditionAlias',
	CDXDatumID.kCDXProp_MacPICT:'MacPICT',
	CDXDatumID.kCDXProp_WindowsMetafile:'WindowsMetafile',
	CDXDatumID.kCDXProp_OLEObject:'OLEObject',
	CDXDatumID.kCDXProp_EnhancedMetafile:'EnhancedMetafile',
	CDXDatumID.kCDXProp_Spectrum_XSpacing:'Spectrum_XSpacing',
	CDXDatumID.kCDXProp_Spectrum_XLow:'Spectrum_XLow',
	CDXDatumID.kCDXProp_Spectrum_XType:'Spectrum_XType',
	CDXDatumID.kCDXProp_Spectrum_YType:'Spectrum_YType',
	CDXDatumID.kCDXProp_Spectrum_XAxisLabel:'Spectrum_XAxisLabel',
	CDXDatumID.kCDXProp_Spectrum_YAxisLabel:'Spectrum_YAxisLabel',
	CDXDatumID.kCDXProp_Spectrum_DataPoint:'Spectrum_DataPoint',
	CDXDatumID.kCDXProp_Spectrum_Class:'Spectrum_Class',
	CDXDatumID.kCDXProp_Spectrum_YLow:'Spectrum_YLow',
	CDXDatumID.kCDXProp_Spectrum_YScale:'Spectrum_YScale',
	CDXDatumID.kCDXProp_TLC_OriginFraction:'TLC_OriginFraction',
	CDXDatumID.kCDXProp_TLC_SolventFrontFraction:'TLC_SolventFrontFraction',
	CDXDatumID.kCDXProp_TLC_ShowOrigin:'TLC_ShowOrigin',
	CDXDatumID.kCDXProp_TLC_ShowSolventFront:'TLC_ShowSolventFront',
	CDXDatumID.kCDXProp_TLC_ShowBorders:'TLC_ShowBorders',
	CDXDatumID.kCDXProp_TLC_ShowSideTicks:'TLC_ShowSideTicks',
	CDXDatumID.kCDXProp_TLC_Rf:'TLC_Rf',
	CDXDatumID.kCDXProp_TLC_Tail:'TLC_Tail',
	CDXDatumID.kCDXProp_TLC_ShowRf:'TLC_ShowRf',
	CDXDatumID.kCDXProp_NamedAlternativeGroup_TextFrame:'NamedAlternativeGroup_TextFrame',
	CDXDatumID.kCDXProp_NamedAlternativeGroup_GroupFrame:'NamedAlternativeGroup_GroupFrame',
	CDXDatumID.kCDXProp_NamedAlternativeGroup_Valence:'NamedAlternativeGroup_Valence',
	CDXDatumID.kCDXProp_GeometricFeature:'GeometricFeature',
	CDXDatumID.kCDXProp_RelationValue:'RelationValue',
	CDXDatumID.kCDXProp_BasisObjects:'BasisObjects',
	CDXDatumID.kCDXProp_ConstraintType:'ConstraintType',
	CDXDatumID.kCDXProp_ConstraintMin:'ConstraintMin',
	CDXDatumID.kCDXProp_ConstraintMax:'ConstraintMax',
	CDXDatumID.kCDXProp_IgnoreUnconnectedAtoms:'IgnoreUnconnectedAtoms',
	CDXDatumID.kCDXProp_DihedralIsChiral:'DihedralIsChiral',
	CDXDatumID.kCDXProp_PointIsDirected:'PointIsDirected',
	CDXDatumID.kCDXProp_ReactionStep_Atom_Map:'ReactionStep_Atom_Map',
	CDXDatumID.kCDXProp_ReactionStep_Reactants:'ReactionStep_Reactants',
	CDXDatumID.kCDXProp_ReactionStep_Products:'ReactionStep_Products',
	CDXDatumID.kCDXProp_ReactionStep_Plusses:'ReactionStep_Plusses',
	CDXDatumID.kCDXProp_ReactionStep_Arrows:'ReactionStep_Arrows',
	CDXDatumID.kCDXProp_ReactionStep_ObjectsAboveArrow:'ReactionStep_ObjectsAboveArrow',
	CDXDatumID.kCDXProp_ReactionStep_ObjectsBelowArrow:'ReactionStep_ObjectsBelowArrow',
	CDXDatumID.kCDXProp_ReactionStep_Atom_Map_Manual:'ReactionStep_Atom_Map_Manual',
	CDXDatumID.kCDXProp_ReactionStep_Atom_Map_Auto:'ReactionStep_Atom_Map_Auto',
	CDXDatumID.kCDXProp_ObjectTag_Type:'ObjectTag_Type',
	CDXDatumID.kCDXProp_Unused6:'Unused6',
	CDXDatumID.kCDXProp_Unused7:'Unused7',
	CDXDatumID.kCDXProp_ObjectTag_Tracking:'ObjectTag_Tracking',
	CDXDatumID.kCDXProp_ObjectTag_Persistent:'ObjectTag_Persistent',
	CDXDatumID.kCDXProp_ObjectTag_Value:'ObjectTag_Value',
	CDXDatumID.kCDXProp_Positioning:'Positioning',
	CDXDatumID.kCDXProp_PositioningAngle:'PositioningAngle',
	CDXDatumID.kCDXProp_PositioningOffset:'PositioningOffset',
	CDXDatumID.kCDXProp_Sequence_Identifier:'Sequence_Identifier',
	CDXDatumID.kCDXProp_CrossReference_Container:'CrossReference_Container',
	CDXDatumID.kCDXProp_CrossReference_Document:'CrossReference_Document',
	CDXDatumID.kCDXProp_CrossReference_Identifier:'CrossReference_Identifier',
	CDXDatumID.kCDXProp_CrossReference_Sequence:'CrossReference_Sequence',
	CDXDatumID.kCDXProp_Template_PaneHeight:'Template_PaneHeight',
	CDXDatumID.kCDXProp_Template_NumRows:'Template_NumRows',
	CDXDatumID.kCDXProp_Template_NumColumns:'Template_NumColumns',
	CDXDatumID.kCDXProp_Group_Integral:'Group_Integral',
	CDXDatumID.kCDXProp_SplitterPositions:'SplitterPositions',
	CDXDatumID.kCDXProp_PageDefinition:'PageDefinition',
	CDXDatumID.kCDXUser_TemporaryBegin:'TemporaryBegin',
	CDXDatumID.kCDXUser_TemporaryEnd:'TemporaryEnd',
	CDXDatumID.kCDXObj_Document:'Document',
	CDXDatumID.kCDXObj_Page:'Page',
	CDXDatumID.kCDXObj_Group:'Group',
	CDXDatumID.kCDXObj_Fragment:'Fragment',
	CDXDatumID.kCDXObj_Node:'Node',
	CDXDatumID.kCDXObj_Bond:'Bond',
	CDXDatumID.kCDXObj_Text:'Text',
	CDXDatumID.kCDXObj_Graphic:'Graphic',
	CDXDatumID.kCDXObj_Curve:'Curve',
	CDXDatumID.kCDXObj_EmbeddedObject:'EmbeddedObject',
	CDXDatumID.kCDXObj_NamedAlternativeGroup:'NamedAlternativeGroup',
	CDXDatumID.kCDXObj_TemplateGrid:'TemplateGrid',
	CDXDatumID.kCDXObj_RegistryNumber:'RegistryNumber',
	CDXDatumID.kCDXObj_ReactionScheme:'ReactionScheme',
	CDXDatumID.kCDXObj_ReactionStep:'ReactionStep',
	CDXDatumID.kCDXObj_ObjectDefinition:'ObjectDefinition',
	CDXDatumID.kCDXObj_Spectrum:'Spectrum',
	CDXDatumID.kCDXObj_ObjectTag:'ObjectTag',
	CDXDatumID.kCDXObj_OleClientItem:'OleClientItem',
	CDXDatumID.kCDXObj_Sequence:'Sequence',
	CDXDatumID.kCDXObj_CrossReference:'CrossReference',
	CDXDatumID.kCDXObj_Splitter:'Splitter',
	CDXDatumID.kCDXObj_Table:'Table',
	CDXDatumID.kCDXObj_BracketedGroup:'BracketedGroup',
	CDXDatumID.kCDXObj_BracketAttachment:'BracketAttachment',
	CDXDatumID.kCDXObj_CrossingBond:'CrossingBond',
	CDXDatumID.kCDXObj_Border:'Border',
	CDXDatumID.kCDXObj_Geometry:'Geometry',
	CDXDatumID.kCDXObj_Constraint:'Constraint',
	CDXDatumID.kCDXObj_TLCPlate:'TLCPlate',
	CDXDatumID.kCDXObj_TLCLane:'TLCLane',
	CDXDatumID.kCDXObj_TLCSpot:'TLCSpot',
	CDXDatumID.kCDXObj_UnknownObject:'UnknownObject'
}

BOND_TYPE={
	CDXBondOrder.kCDXBondOrder_Single: BondType.SINGLE,
	CDXBondOrder.kCDXBondOrder_Double: BondType.DOUBLE,
	CDXBondOrder.kCDXBondOrder_Triple: BondType.TRIPLE,
	CDXBondOrder.kCDXBondOrder_Quadruple: BondType.QUADRUPLE,
	CDXBondOrder.kCDXBondOrder_Quintuple: BondType.QUINTUPLE,
	CDXBondOrder.kCDXBondOrder_Hextuple: BondType.HEXTUPLE,
	# CDXBondOrder.kCDXBondOrder_Half: BondType.AROMATIC,#半键，F
	CDXBondOrder.kCDXBondOrder_OneHalf: BondType.ONEANDAHALF,
	CDXBondOrder.kCDXBondOrder_TwoHalf: BondType.TWOANDAHALF,
	CDXBondOrder.kCDXBondOrder_ThreeHalf: BondType.THREEANDAHALF,
	CDXBondOrder.kCDXBondOrder_FourHalf: BondType.FOURANDAHALF,
	CDXBondOrder.kCDXBondOrder_FiveHalf: BondType.FIVEANDAHALF,
	CDXBondOrder.kCDXBondOrder_Dative: BondType.DATIVE,
	CDXBondOrder.kCDXBondOrder_Ionic: BondType.IONIC,
	CDXBondOrder.kCDXBondOrder_Hydrogen: BondType.HYDROGEN,
	CDXBondOrder.kCDXBondOrder_ThreeCenter: BondType.THREECENTER,
	# CDXBondOrder.kCDXBondOrder_SingleOrDouble: BondType.SINGLEORDOUBLE,
	# CDXBondOrder.kCDXBondOrder_SingleOrAromatic: BondType.SINGLEORAROMATIC,
	# CDXBondOrder.kCDXBondOrder_DoubleOrAromatic: BondType.DOUBLEORAROMATIC,
	# CDXBondOrder.kCDXBondOrder_Any: BondType.ANY
}

# 5 = Single or Double, 6 = Single or Aromatic, 7 = Double or Aromatic, 8 = Any
BOND_DISPLAY={
	0:'Solid',
	1:'Dash',
	2:'Hash',
	3:'WedgedHashBegin',
	4:'WedgedHashEnd',
	5:'Bold',
	6:'WedgeBegin',
	7:'WedgeEnd',
	8:'Wavy',
	9:'HollowWedgeBegin',
	10:'HollowWedgeEnd',
	11:'WavyWedgeBegin',
	12:'WavyWedgeEnd',
	13:'Dot',
	14:'DashD',
}
if __name__=="__main__":
	dic=[]
	res=""
	for item in CDXBondOrder:
		name=str(item)
		index=name.index("_")
		res+=f"\t{name}:BondType.{name[index+1:].upper()},\n"
	print(res)
	for item in BOND_TYPE:
		print(BOND_TYPE[item])
	# help(CDXDatumID)
	# help(CDXDatumID.__members__['kCDXProp_EndObject'])
	# print(CDXDatumID.find(12))