import serial
import time
import binascii
import struct
import string


def hex2int(_hex):
    # Convertit les hexadécimaux en entier
    return list(_hex)[0]

def int2binList(_int):
    # Convertit les entiers en une liste de binaire, sur un octet
    sortie = []
    for i in range(8):
        if (_int >= pow(2,7-i)):
            sortie.append(1)
            _int = _int - pow(2,7-i)
        else:
            sortie.append(0)
    return sortie

def hex2binList(_hex):
    # Convertit un hexadécimal en liste de binaire, sur un ocet
    return int2binList(hex2int(_hex))

def binList2int(_bin_list):
    # Convertit une liste de binaire sur un octet en entier, entre 0 et 255
    somme = 0
    for i in range(len(_bin_list)):
        somme += _bin_list[i] * pow(2,7-i)
    return somme


def int2bytes(_value_int):
    # Convertit un entier entre 0 et 255 en un hexadécimal
    traduction_table=[b'\x00',b'\x01',b'\x02',b'\x03',b'\x04',b'\x05',b'\x06',b'\x07',b'\x08',b'\x09',b'\x0a',b'\x0b',b'\x0c',b'\x0d',b'\x0e',b'\x0f',b'\x10',b'\x11',b'\x12',b'\x13',b'\x14',b'\x15',b'\x16',b'\x17',b'\x18',b'\x19',b'\x1a',b'\x1b',b'\x1c',b'\x1d',b'\x1e',b'\x1f',b'\x20',b'\x21',b'\x22',b'\x23',b'\x24',b'\x25',b'\x26',b'\x27',b'\x28',b'\x29',b'\x2a',b'\x2b',b'\x2c',b'\x2d',b'\x2e',b'\x2f',b'\x30',b'\x31',b'\x32',b'\x33',b'\x34',b'\x35',b'\x36',b'\x37',b'\x38',b'\x39',b'\x3a',b'\x3b',b'\x3c',b'\x3d',b'\x3e',b'\x3f',b'\x40',b'\x41',b'\x42',b'\x43',b'\x44',b'\x45',b'\x46',b'\x47',b'\x48',b'\x49',b'\x4a',b'\x4b',b'\x4c',b'\x4d',b'\x4e',b'\x4f',b'\x50',b'\x51',b'\x52',b'\x53',b'\x54',b'\x55',b'\x56',b'\x57',b'\x58',b'\x59',b'\x5a',b'\x5b',b'\x5c',b'\x5d',b'\x5e',b'\x5f',b'\x60',b'\x61',b'\x62',b'\x63',b'\x64',b'\x65',b'\x66',b'\x67',b'\x68',b'\x69',b'\x6a',b'\x6b',b'\x6c',b'\x6d',b'\x6e',b'\x6f',b'\x70',b'\x71',b'\x72',b'\x73',b'\x74',b'\x75',b'\x76',b'\x77',b'\x78',b'\x79',b'\x7a',b'\x7b',b'\x7c',b'\x7d',b'\x7e',b'\x7f',b'\x80',b'\x81',b'\x82',b'\x83',b'\x84',b'\x85',b'\x86',b'\x87',b'\x88',b'\x89',b'\x8a',b'\x8b',b'\x8c',b'\x8d',b'\x8e',b'\x8f',b'\x90',b'\x91',b'\x92',b'\x93',b'\x94',b'\x95',b'\x96',b'\x97',b'\x98',b'\x99',b'\x9a',b'\x9b',b'\x9c',b'\x9d',b'\x9e',b'\x9f',b'\xa0',b'\xa1',b'\xa2',b'\xa3',b'\xa4',b'\xa5',b'\xa6',b'\xa7',b'\xa8',b'\xa9',b'\xaa',b'\xab',b'\xac',b'\xad',b'\xae',b'\xaf',b'\xb0',b'\xb1',b'\xb2',b'\xb3',b'\xb4',b'\xb5',b'\xb6',b'\xb7',b'\xb8',b'\xb9',b'\xba',b'\xbb',b'\xbc',b'\xbd',b'\xbe',b'\xbf',b'\xc0',b'\xc1',b'\xc2',b'\xc3',b'\xc4',b'\xc5',b'\xc6',b'\xc7',b'\xc8',b'\xc9',b'\xca',b'\xcb',b'\xcc',b'\xcd',b'\xce',b'\xcf',b'\xd0',b'\xd1',b'\xd2',b'\xd3',b'\xd4',b'\xd5',b'\xd6',b'\xd7',b'\xd8',b'\xd9',b'\xda',b'\xdb',b'\xdc',b'\xdd',b'\xde',b'\xdf',b'\xe0',b'\xe1',b'\xe2',b'\xe3',b'\xe4',b'\xe5',b'\xe6',b'\xe7',b'\xe8',b'\xe9',b'\xea',b'\xeb',b'\xec',b'\xed',b'\xee',b'\xef',b'\xf0',b'\xf1',b'\xf2',b'\xf3',b'\xf4',b'\xf5',b'\xf6',b'\xf7',b'\xf8',b'\xf9',b'\xfa',b'\xfb',b'\xfc',b'\xfd',b'\xfe',b'\xff']
    return traduction_table[_value_int]
    
    
def binList2hex(_bin_list):
    # Convertit une liste de binaire sur un octet en un entier
    _int = binList2int(_bin_list)
    return int2bytes(_int)

def bit_xor(a1,a2):
    # Opération booléenne OU EXCLUSIF
    # 0 ^ 0 = 0
    # 0 ^ 1 = 1
    # 1 ^ 0 = 1
    # 1 ^ 1 = 0
    if (a1!=a2):
        return 1
    else:
        return 0

def bit_and(a1,a2):
    # Opération booléenne ET
    # 0 ^ 0 = 0
    # 0 ^ 1 = 1
    # 1 ^ 0 = 1
    # 1 ^ 1 = 1
    if (a1==1 and a2==1):
        return 1
    else:
        return 0

def binList_xor(_binList):
    # Applique l'opérateur XOR sur deux listes de binaire, contenues dans _binList
    taille = len(_binList)
    sortie = []
    for i in range(8):
        result = bit_xor(_binList[0][i],_binList[1][i])
        for j in range(2,taille):
            result = bit_xor(result,_binList[j][i])
        sortie.append(result)
    return sortie

def binList_and(_binList):
    # Applique l'opérateur AND sur deux listes de binaire, contenues dans _binList
    taille = len(_binList)
    sortie = []
    for i in range(8):
        result = bit_and(_binList[0][i],_binList[1][i])
        for j in range(2,taille):
            result = bit_and(result,_binList[j][i])
        sortie.append(result)
    return sortie

def binList_not(_binList):
    # Applique l'opérateur NOT ~. Les 0 deviennent des 1 et inversement
    sortie = []
    for i in range(8):
        sortie.append(abs(_binList[i]-1))
    return sortie


def CheckSum1(_liste):
    # Calcule le CS1 à partir d'une liste qui contient en hexadécimal
    # PacketSize, ID, CMD, Data[0], Data[1], ... , Data[n]
    taille = len(_liste)
    _bin=[]
    for i in range(taille):
        _bin.append(hex2binList(_liste[i]))
    _liste_xor = binList_xor(_bin)
    _liste_and = binList_and([_liste_xor,hex2binList(b'\xfe')])
    return binList2hex(_liste_and)

def CheckSum2(_CS1):
    # Calcule le CS2 à partir du CS1
    _CS1_bin = hex2binList(_CS1)
    _CS1_bin = binList_not(_CS1_bin) 
    _CS1_bin = binList_and([_CS1_bin,hex2binList(b'\xfe')])
    return binList2hex(_CS1_bin)

def ser_write(_ser,_data):
    # Permet d'écrire une liste d'octets contenue dans _data sur le prot série _ser
    if _ser.isOpen():
        for i in _data:
            _ser.write(i)
    else:
        print("Port série non ouvert")

def WriteLedColor(_ser,_ID,_color):
    # Permet de changer la couleur de la LED du moteur _ID à la couleur choisie en paramètre, en passant par le port série _ser
    _PacketSize = b'\x0a'
    _CMD = RAM_WRITE
    _Data = [RAM_LED_CONTROL,ONE,_color]
    _cs1 = CheckSum1([_PacketSize,_ID,_CMD,_Data[0],_Data[1],_Data[2]])
    _cs2 = CheckSum2(_cs1)
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1],_Data[2]])

def ReadLedColor(_ser,_ID):
    # Permet de lire la couleur de la LED du moteur _ID, en passant par le port série _ser
    _PacketSize = b'\x09'
    _CMD = RAM_READ
    _Data = [RAM_LED_CONTROL,ONE]
    _cs1 = CheckSum1([_PacketSize,_ID,_CMD,_Data[0],_Data[1]])
    _cs2 = CheckSum2(_cs1)
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1]])
    _readed_color = ReadBytes(_ser,1)[0]
    return _readed_color

def ReadBytes(_ser,_length):
    #permet de lire _length données intéressantes sur le port série _ser. On ignore les autres. On renvoit les octets lus sous forme d'une liste
    sortie = []
    _x = _ser.read(9)
    for i in range(_length):
        sortie.append(_ser.read())
    _x = _ser.read(2)
    return sortie
    
def ReadAbsolutePosition(_ser,_ID):
    # Permet de lire la position angulaire actuelle du moteur _ID sur le port série _ser
    _PacketSize = b'\x09'
    _CMD = RAM_READ
    _Data = [RAM_ABSOLUTE_POSITION,TWO]
    _cs1 = CheckSum1([_PacketSize,_ID,_CMD,_Data[0],_Data[1]])
    _cs2 = CheckSum2(_cs1)
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1]])
    _readed_pos = ReadBytes(_ser,2)
    return hex2angle(_readed_pos)

def hex2angle(_pos):
    # Convertit un hexadécimal en entier, puis le convertit en angle à l'aide de la résolution des servos
    sortie = 255 * hex2int(_pos[1])+hex2int(_pos[0])
    return sortie*0.325

def ReadStatus(_ser,_ID):
    # Lit le status d'error et le les détails du moteur _ID sur le port série _ser, et les retourne sous forme d'une liste de deux éléments
    _sortie = []
    _PacketSize = NINE
    _CMD = RAM_READ
    _Data = [RAM_STATUS_ERROR,ONE]
    _cs1 = CheckSum1([_PacketSize,_ID,_CMD,_Data[0],_Data[1]])
    _cs2 = CheckSum2(_cs1)
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1]])
    _sortie.append(ReadBytes(_ser,1)[0])
    
    _PacketSize = NINE
    _CMD = RAM_READ
    _Data = [RAM_STATUS_DETAIL,ONE]
    _cs1 = CheckSum1([_PacketSize,_ID,_CMD,_Data[0],_Data[1]])
    _cs2 = CheckSum2(_cs1)
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1]])
    _sortie.append(ReadBytes(_ser,1)[0])
    return _sortie

def SetTorqueOn(_ser,_ID):
    _PacketSize = TEN
    _CMD = RAM_WRITE
    _Data = [RAM_TORQUE_POLICY,ONE,TORQUE_ON]
    _cs1 = CheckSum1([_PacketSize,_ID,_CMD,_Data[0],_Data[1],_Data[2]])
    _cs2 = CheckSum2(_cs1)
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1],_Data[2]])

def MovePosMotor(_ser,_ID,_angle):
    _PacketSize = TWELVE
    _CMD = FIVE
    _cs1 = b'\x32'
    _cs2 = b'\xcc'
    _Data = [b'\x00',b'\x02',b'\x04',b'\xfd',b'\x3c']
    ser_write(_ser,[HEADER,HEADER,_PacketSize,_ID,_CMD,_cs1,_cs2,_Data[0],_Data[1],_Data[2],_Data[3],_Data[4]])

class DataMotor:
    # Classe en développement
    def __init__(self,_ser,_ID):
        self._ser = _ser
        self._ID = _ID
        self.led_color = b'\xff'
    
    def getColor(self):
        return self.led_color
    
    def update(self):
        led_color = ReadLedColor(self._ser,self._ID)
        absolute_position = ReadAbsolutePosition(self._ser,self._ID)
        [status_error,status_detail] = ReadStatus(self._ser,self._ID)
        

# L'ensemble des registres utilisés pour le moment

EEP_WRITE = b'\x01'
EEP_READ = b'\x02'
RAM_WRITE = b'\x03'
RAM_READ = b'\x04'
I_JOG = b'\x05'
S_JOG = b'\x06'
STAT = b'\x07'
ROLLBACK = b'\x08'
REBOOT = b'\x09'
ALL = b'\xfe'

#EEP regsiters
EEP_BAUD_RATE = b'\x04'
EEP_ID = b'\x05'
EEP_ALARM_LED_POLICY = b'\x08'
EEP_TORQUE_POLICY = b'\x09'
EEP_ACCELERATION_RATIO = b'\x0e'

EEP_POSITION_KP = b'\x1e'
EEP_POSITION_KD = b'\x20'
EEP_POSITION_KI = b'\x22'

EEP_LED_BLINK_PERIOD = b'\x2c'


# RAM registers
RAM_ID = b'\x00'
RAM_ALARM_LED_POLICY = b'\x02'
RAM_TORQUE_POLICY = b'\x03'
RAM_ACCELERATION_RATIO = b'\x08'
RAM_POSITION_KP = b'\x18'
RAM_POSITION_KD = b'\x1A'
RAM_POSITION_KI = b'\x1C'
RAM_LED_BLINK_PERIOD = b'\x26'
RAM_TORQUE_CONTROL = b'\x34'
RAM_LED_CONTROL = b'\x35'
RAM_CURRENT_CONTROL_MODE = b'\x38'
RAM_ABSOLUTE_POSITION = b'\x3c'
RAM_STATUS_ERROR = b'\x30'
RAM_STATUS_DETAIL = b'\x31'

# COLORS FOR LED
GREEN = b'\x01'
BLUE = b'\x02'
CYAN = b'\x03'
RED = b'\x04'
LIGHT_GREEN = b'\x05'
PINK = b'\x06'
WHITE = b'\x07'

HEADER = b'\xff'

ZERO = b'\x00'
ONE = b'\x01'
TWO = b'\x02'
THREE = b'\x03'
FOUR = b'\x04'
FIVE = b'\x05'
SIX = b'\x06'
SEVEN = b'\x07'
EIGHT = b'\x08'
NINE = b'\x09'
TEN = b'\x0a'
ELEVEN = b'\x0b'
TWELVE = b'\x0c'
THIRTEEN = b'\x0d'
FOURTEEN = b'\x0e'
FIFTEEN = b'\x0f'

TORQUE_ON = b'\x60'
# Pour les tests, on choisit les paramètres de la trame, on les assemble et on calcule les CheckSums
PacketSize = b'\x0a'
pID = b'\xfe'
CMD = RAM_WRITE
Data = [RAM_LED_CONTROL,ONE,GREEN]

list_cs = [PacketSize,pID,CMD]
for i in Data:
    list_cs.append(i)

cs1 = CheckSum1(list_cs)
cs2 = CheckSum2(cs1)



with serial.Serial(port="/dev/ttyUSB0", baudrate=115200, timeout=1, writeTimeout=1) as port_serie:
    #DataMotor = DataMotor(port_serie,b'\xfd')
    SetTorqueOn(port_serie,ALL)
    while(1):
        MovePosMotor(port_serie,ALL,0)
        time.sleep(1)