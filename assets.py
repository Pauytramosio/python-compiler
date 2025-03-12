#%% get the C standard lib (very useful)
import ctypes

# load the c stdlib (libc.so.6 on linux)
libc = ctypes.CDLL("libc.so.6")

isalpha = libc.isalpha
isalpha.argtypes = [ctypes.c_int]
isalpha.restype = ctypes.c_int

isdigit = libc.isdigit
isdigit.argtypes = [ctypes.c_int]
isdigit.restype = ctypes.c_int

isalnum = libc.isalnum
isalnum.argtypes = [ctypes.c_int]
isalnum.restype = ctypes.c_int

isspace = libc.isspace
isspace.argtypes = [ctypes.c_int]
isspace.restype = ctypes.c_int

# %% end