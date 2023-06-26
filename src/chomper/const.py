import sys

if sys.version_info >= (3, 8):
    from typing import Literal
else:
    from typing_extensions import Literal

# Endian type
BIG_ENDIAN: Literal["big"] = "big"
LITTLE_ENDIAN: Literal["little"] = "little"

# Supported arch
ARCH_ARM = 0
ARCH_ARM64 = 1

MODE_ARM = 0
MODE_THUMB = 1

# The address of thread local storage (TLS)
TLS_ADDRESS = 0x10000
TLS_SIZE = 0x400

# The address of stack
STACK_ADDRESS = 0x50000
STACK_SIZE = 0x50000

# The address of module
MODULE_ADDRESS = 0x1000000

# The address of heap
HEAP_ADDRESS = 0x80000000

# Minimum size of memory pool
MINIMUM_POOL_SIZE = 8**4
