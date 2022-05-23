from base64 import b16encode
 
def rgb_color(rgb):
    return(b'#' + b16encode(bytes(rgb)))
 
print(rgb_color((0,0,0)))