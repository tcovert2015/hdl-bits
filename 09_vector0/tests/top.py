import cocotb
from cocotb.triggers import Timer
from model_vector0 import model_vector0
import random

# Python debugger
#from remote_pdb import RemotePdb; rpdb = RemotePdb("127.0.0.1", 4000)

@cocotb.test()
async def random_wires(dut):

    for i in range (10000):

        # Set debug breakpoint
        #rpdb.set_trace()
        
        # Create random values to send to model and dut
        vec_rand = random.randint(0,8)

        # Send random values to model
        vec = model_vector0(vec_rand)

        # Send random values to dut
        dut.vec <= vec_rand

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Compare results
        if int(dut.p1y.value) != int(p1y):
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (int(dut.p1y.value), int(p1y)))        

        if int(dut.p2y.value) != int(p2y):
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (int(dut.p2y.value), int(p2y)))        
