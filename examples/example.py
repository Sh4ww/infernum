import os

from infernum import Infernum

BASE_PATH = os.path.abspath(os.path.dirname(__file__))


def main():
    # Initialize emulator
    emulator = Infernum()

    # Load modules
    emulator.load_module(f"{BASE_PATH}/lib64/libz.so")

    # Construct arguments
    data = b"infernum"

    a1 = 0
    a2 = emulator.create_buffer(len(data))
    a3 = len(data)

    emulator.write_bytes(a2, data)

    # Call function
    result = emulator.call_symbol("crc32", a1, a2, a3)

    emulator.logger.info(hex(result))


if __name__ == "__main__":
    main()
