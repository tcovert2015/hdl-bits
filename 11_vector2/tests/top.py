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
        # Random int value with max 32 bits. unsigned.
        random_dec_value = random.randint(0,4294967295)
        
        # Convert random decimal to a string to represnt binary.
        a_binary = f'{random_dec_value:032b}'

        # Convert to cocotb structure BinaryValue, 32 bits long.
        a_bin_cocotb = BinaryValue(n_bits=32)
        a_bin_cocotb.binstr = a_binary

        # Set high and low values to compare with the DUT
        # Byte order seems to be reverse from VHDL
        a_bin_cocotb_byte_0 = str(a_bin_cocotb[0:7]) # Left most value (MSB)
        a_bin_cocotb_byte_1 = str(a_bin_cocotb[8:15])
        a_bin_cocotb_byte_2 = str(a_bin_cocotb[16:23])
        a_bin_cocotb_byte_3 = str(a_bin_cocotb[24:31]) # Right most value (LSB)

        # Send random values to dut
        dut.vec <= int(random_dec_value)

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Get values from DUT
        dut_outvec = BinaryValue(n_bits=32)
        dut_outvec = dut.outvec.value


        print("---------------------------------")
        print("Test                             ", i)
        print("Input value                      ", a_binary)
        print("DUT Output      dut.outvec.value ", dut.outvec.value)
        print("---------------------------------\n")
        
        # Compare results
        if str(dut.outvec.value[24:31]) != a_bin_cocotb_byte_0:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.outvec.value[24:31]), a_bin_cocotb_byte_0))        
        if str(dut.outvec.value[16:23]) != a_bin_cocotb_byte_1:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.outvec.value[16:23]), a_bin_cocotb_byte_1))        
        if str(dut.outvec.value[8:15]) != a_bin_cocotb_byte_2:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.outvec.value[8:15]), a_bin_cocotb_byte_2))        
        if str(dut.outvec.value[0:7]) != a_bin_cocotb_byte_3:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.outvec.value[0:7]), a_bin_cocotb_byte_3))        
