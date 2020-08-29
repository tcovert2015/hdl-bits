import cocotb
from cocotb.triggers import Timer
from and_model import and_model
import random

##########
# Test 1 #
##########
@cocotb.test()
async def random_and_gate(dut):
    """ Test simple AND gate with random bits """

    for i in range (10000):
        a_rand = random.randint(0,1)
        b_rand = random.randint(0,1)

        dut.a <= a_rand
        dut.b <= b_rand

        await Timer(1, units='ns')

        dut._log.info(dut.a.value)
        dut._log.info(a_rand)
        dut._log.info(dut.b.value)
        dut._log.info(b_rand)
        dut._log.info(dut.z.value)

        assert int(dut.z.value) == and_model(a_rand, b_rand), "AND gate result is incorrect: {a} AND {b} = {z}".format(a=dut.a.value, b=dut.b.value, z=dut.z.value)
