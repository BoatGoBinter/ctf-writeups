import os
import sys
import struct
from collections import defaultdict


def extract_pieces(stream_bytes):
    pieces = defaultdict(list)
    i = 0
    n = len(stream_bytes)

    while i + 9 <= n:
        length = int.from_bytes(stream_bytes[i:i+4], "big", signed=False)

        if length == 0:
            i += 4
            continue

        if length < 0 or length > 2 * 1024 * 1024:
            i += 1
            continue


        if i + 4 + length > n:

            break

        msg_id = stream_bytes[i+4]


        if msg_id == 7 and length >= 9:
            piece_index = int.from_bytes(stream_bytes[i+5:i+9], "big")
            begin_offset = int.from_bytes(stream_bytes[i+9:i+13], "big")
            block_data = stream_bytes[i+13:i+4+length]
            #check
            if len(block_data) == (length - 9) and len(block_data) > 0:
                pieces[piece_index].append((begin_offset, block_data))

            i += 4 + length
            continue

        i += 1

    return pieces

def main():

    stream_path = sys.argv[1]
    outdir = sys.argv[2]

    with open(stream_path, "rb") as f:
        data = f.read()

    pieces = extract_pieces(data)

    #output folder
    os.makedirs(outdir, exist_ok=True)

    # stitch everything together in order into one file
    concat_path = os.path.join(outdir, "go.bin")
    with open(concat_path, "wb") as out_f:
        for piece_index in sorted(pieces.keys()):
            for begin_offset, block_data in sorted(pieces[piece_index], key=lambda x: x[0]):
                out_f.write(block_data)


if __name__ == "__main__":
    main()
