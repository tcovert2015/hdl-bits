import cocotb
from cocotb.triggers import Timer
from model_7458 import model_7458
import random

# Python debugger
#from remote_pdb import RemotePdb; rpdb = RemotePdb("127.0.0.1", 4000)

@cocotb.test()
async def random_wires(dut):

    for i in range (10000):

        # Set debug breakpoint
        #rpdb.set_trace()
        
        # Create random values to send to model and dut
        p1a_rand = random.randint(0,1)
        p1b_rand = random.randint(0,1)
        p1c_rand = random.randint(0,1)
        p1d_rand = random.randint(0,1)
        p1e_rand = random.randint(0,1)
        p1f_rand = random.randint(0,1)

        p2a_rand = random.randint(0,1)
        p2b_rand = random.randint(0,1)
        p2c_rand = random.randint(0,1)
        p2d_rand = random.randint(0,1)

        # Send random values to model
        p1y, p2y = model_7458(p1a_rand, p1b_rand, p1c_rand, p1d_rand, p1e_rand, p1f_rand, p2a_rand, p2b_rand, p2c_rand, p2d_rand)

        # Send random values to dut
        dut.p1a <= p1a_rand
        dut.p1b <= p1b_rand
        dut.p1c <= p1c_rand
        dut.p1d <= p1d_rand
        dut.p1e <= p1e_rand
        dut.p1f <= p1f_rand

        dut.p2a <= p2a_rand
        dut.p2b <= p2b_rand
        dut.p2c <= p2c_rand
        dut.p2d <= p2d_rand

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Compare results
        if int(dut.p1y.value) != int(p1y):
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (int(dut.p1y.value), int(p1y)))        

        if int(dut.p2y.value) != int(p2y):
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (int(dut.p2y.value), int(p2y)))        
