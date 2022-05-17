# No need for a model for this design
def model(a: int):

    # Convert a to bin with 16 bit width. Pad with zeros.
    a = int(a)
    a_binary = f'{a:016b}'
    out_hi = a_binary[0:8]
    out_lo = a_binary[8:16]

    return out_hi, out_lo
