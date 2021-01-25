import cocotb
from cocotb.triggers import Timer
from model import model
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
        random_binary_vector = rand_key(4)

        # Send random values to model
        outv, o0, o1, o2 = model(random_binary_vector)

        # Send random values to dut
        dut.vec <= int(random_binary_vector)

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Compare results
        if int(dut.outv.value) != int(outv):
            raise cocotb.result.TestFailure("DUT recorded %d value but model recorded %d" % (
                int(dut.outv.value), int(outv)))        


# Function to create a binary string
def rand_key(p):
    key1 = ""

    for i in range(p):

        temp = str(random.randint(0,1))
        key1 += temp

    return(key1)
