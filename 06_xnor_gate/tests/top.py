import cocotb
from cocotb.triggers import Timer
from xnor_model import xnor_model
import random

@cocotb.test()
async def random_nor_gate(dut):
    """ Test simple XNOR gate with random bits """

    for i in range (10000):
        # Create random values to send to model and dut
        a_rand = random.randint(0,1)
        b_rand = random.randint(0,1)

        # Send random values to model
        model_output = xnor_model(a_rand, b_rand)

        # Send random values to dut
        dut.a <= a_rand
        dut.b <= b_rand

        # Wait for dut to do its thing
        await Timer(1, units='ns')

        # Compare results
        assert int(dut.z.value) == model_output, "XNOR gate result is incorrect: Model output is {a}, dut output is {b}.".format(a=model_output, b=dut.b.value)