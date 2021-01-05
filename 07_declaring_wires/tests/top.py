import cocotb
from cocotb.triggers import Timer
from declaring_wires_model import declaring_wires_model
import random

# Python debugger
#from remote_pdb import RemotePdb; rpdb = RemotePdb("127.0.0.1", 4000)

@cocotb.test()
async def random_wires(dut):
    """ Test simple wires logic with random bits """

    for i in range (10000):

        # Set debug breakpoint
        #rpdb.set_trace()
        
        # Create random values to send to model and dut
        a_rand = random.randint(0,1)
        b_rand = random.randint(0,1)
        c_rand = random.randint(0,1)
        d_rand = random.randint(0,1)

        # Send random values to model
        z, z_n = declaring_wires_model(a_rand, b_rand, c_rand, d_rand)

        # Send random values to dut
        dut.a <= a_rand
        dut.b <= b_rand
        dut.c <= c_rand
        dut.d <= d_rand

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Compare results
        if int(dut.z.value) != int(z):
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.z.value), int(z)))        

