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
        # Random int value with max 3 bits. unsigned.
        random_dec_value_a = random.randint(0,7)
        random_dec_value_b = random.randint(0,7)
        
        # Convert random decimal to a string to represnt binary.
        a_binary = f'{random_dec_value_a:03b}'
        b_binary = f'{random_dec_value_b:03b}'

        # Convert to cocotb structure BinaryValue, 3 bits long.
        a_bin_cocotb = BinaryValue(n_bits=3)
        a_bin_cocotb.binstr = a_binary
        b_bin_cocotb = BinaryValue(n_bits=3)
        b_bin_cocotb.binstr = b_binary

        # Send random values to dut
        dut.a <= int(random_dec_value_a)
        dut.b <= int(random_dec_value_b)

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Get values from DUT
        dut_out_or_bitwise = BinaryValue(n_bits=3)
        dut_out_or_bitwise = dut.out_or_bitwise.value

        # Skipped converting || from verilog. It just tests if both values are 0.
        #dut_out_or_logical = BinaryValue(n_bits=1)
        #dut_out_or_logical = dut.out_or_logical.value

        dut_out_not = BinaryValue(n_bits=6)
        dut_out_not = dut.out_not.value

        # Python Model
        python_bitwise = a_bin_cocotb | b_bin_cocotb
        python_not = ~b_bin_cocotb + ~a_bin_cocotb
        
        print("-----------------------------------------")
        print("Test                                     ", i)
        print("Input value a                            ", a_binary)
        print("Input value b                            ", b_binary)
        print("DUT Output      dut.out_or_bitwise.value ", dut.out_or_bitwise.value)
        print("DUT Output      dut.out_not.value        ", dut.out_not.value)
        print("-----------------------------------------\n")

        # Compare results
        if int(dut.out_or_bitwise.value) != python_bitwise:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.out_or_bitwise.value), python_bitwise))
        if str(dut.out_not.value) != python_not:
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                str(dut.out_not.value), python_not))
