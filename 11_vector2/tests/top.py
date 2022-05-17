import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
from model import model
import random

@cocotb.test()
async def random_wires(dut):
    """ Test simple wires logic with random bits """

    for i in range (10000):

        # Create random values to send to model and dut
        # Random int value with max 16 bits. unsigned.
        random_dec_value = random.randint(0,65536)
        
        # Convert random decimal to a string to represnt binary.
        a_binary = f'{random_dec_value:016b}'

        # Convert to cocotb structure BinaryValue, 16 bits long.
        a_bin_cocotb = BinaryValue(n_bits=16)
        a_bin_cocotb.binstr = a_binary

        # Set high and low values to compare with the DUT
        a_bin_cocotb_hi = str(a_bin_cocotb[0:7])
        a_bin_cocotb_lo = str(a_bin_cocotb[8:15])

        # Send random values to dut
        dut.vec <= int(random_dec_value)

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Get values from DUT
        dut_out_hi = BinaryValue(n_bits=16)
        dut_out_hi = dut.out_hi.value
        dut_out_lo = BinaryValue(n_bits=16)
        dut_out_lo = dut.out_lo.value

        print("---------------------------------")
        print("Test                             ", i)
        print("Input value                      ", a_binary)
        print("DUT Output      dut.out_hi.value ", dut.out_hi.value)
        print("DUT Output      dut.out_lo.value         ", dut.out_lo.value)
        print("---------------------------------\n")
        
        # Compare results
        if str(dut.out_hi.value) != a_bin_cocotb_hi:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.out_hi.value), a_bin_cocotb_hi))        
        if str(dut.out_lo.value) != a_bin_cocotb_lo:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.out_lo.value), a_bin_cocotb_lo))
