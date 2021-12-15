import cocotb
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
from model import model
import random

# Python debugger
# from remote_pdb import RemotePdb; rpdb = RemotePdb("127.0.0.1", 4000)

@cocotb.test()
async def random_wires(dut):
    """ Test simple wires logic with random bits """

    for i in range (10000):

        # Set debug breakpoint
        # rpdb.set_trace()
        
        # Create random values to send to model and dut
        # Random int value with max 16 bits. unsigned.
        random_dec_value = random.randint(0,65536)
        #print(random_dec_value)
#        random_binary_vector = rand_key(16)
#        print(random_binary_vector)
        
        # Send random values to model
        # out_hi, out_lo = model(random_binary_vector)
        # print(out_hi, type(out_hi))
        
        # Convert random decimal to bin
        a_binary = f'{random_dec_value:016b}'
        a_bin_cocotb = BinaryValue(n_bits=16)
        a_bin_cocotb.binstr = a_binary
        #print(a_bin_cocotb, type(a_bin_cocotb))
        #print("a_binary", a_binary, type(a_binary))
        a_bin_cocotb_hi = str(a_bin_cocotb[0:7])
        a_bin_cocotb_lo = str(a_bin_cocotb[8:15])
        #print(a_bin_cocotb_hi)
        #print(a_bin_cocotb_lo)
        
#        print("out_hi", out_hi, type(out_hi))
#        out_hi = int(out_hi, base=2)
#        out_lo = int(out_lo, base=2)

        # Send random values to dut
        dut.vec <= int(random_dec_value)

        # Wait for dut to do its thing
        await Timer(1, units='ns')
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
