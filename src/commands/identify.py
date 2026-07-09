from utils.parse_args import parse_args
from utils.print_result import print_result


def b6432_detector(value: str) -> tuple[bool, bool]:
    b64tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    b32tokens = "ABCDEFGHIJKLMNOPQRSTUVWXYZ234567"
    if value[-1] == "=":
        return (True, True) # return b64 true and b32 true
        
    
    b64tokens_count = 0
    b32tokens_count = 0
    for c in value:
        if c in b64tokens:
            b64tokens_count += 1
        if c in b32tokens:
            b32tokens_count += 1

    b64, b32 = False, False
    if b64tokens_count >= (len(value) // 2):
        b64 = True
        
    elif b32tokens_count >= (len(value) // 2):
        b32 = True
    
    return (b64, b32)
    

def hash_detector(value: str) -> tuple[bool, bool]:
    # hashtokens = "1234567890abcdef"
    md5 = False
    sha256 = False
    if len(value) == 32:
        md5 = True
    elif len(value) == 64:
        sha256 = True
    

    for c in value:
        c_decimal = ord(c)

        if (c_decimal >= 48 and c_decimal <= 57) or (c_decimal >= 97 and c_decimal <= 102):
            continue

        # if c in hashtokens:
        #     continue
        
        md5, sha256 = False, False
        break
    return (md5, sha256)
        
    
    

def hex_detector(value: str) -> bool:
    hex = False
    for c in value:
        c_decimal = ord(c)
        if (c_decimal >= 48 and c_decimal <= 57) or (c_decimal >= 97 and c_decimal <= 102):
            hex = True
            continue
        hex = False
        break
    return hex


def identify_command(value: str = "", method: str = ""):
    print("Identify Command")
    is_b64, is_b32 = b6432_detector(value)
    is_md5, is_sha256 = hash_detector(value)
    is_hex = hex_detector(value)
    if is_md5:
        is_b64, is_b32 = False, False
    if is_b32:
        print_result('Base32 detected')
    if is_b64:
        print_result('Base64 detected')
    if is_md5:
        print_result('md5 detected')
    if is_sha256:
        print_result('sha256 detected')
    if is_hex:
        print_result('Hex detected')