import cocotb
from cocotb.triggers import Timer
from inverter_model import inverter_model

# This test is really bad. Just learning cocotb and python...
# Going to attempt to increase the sophistication in this example.

@cocotb.test()
async def inverter(dut):
    """Try accessing the design."""

    output_z = str(dut.output_z)
    
    ###############################
    # Test 1 - Change Inputs to 1 #
    ###############################
    
    dut.input_a <= 1

    await Timer(1, units='ns') # Wait for 1 ns for the output signal to channge.

    dut._log.info("output_z")
    dut._log.info(output_z)
    dut._log.info("dut.output_z:")
    dut._log.info(dut.output_z)
    dut._log.info("dut.input_a:")
    dut._log.info(dut.input_a)
    
    # Set error if the output was not inverted
    if (output_z == 1) :
        raise dut._log.error("Output equals input. Output should be 0.")
    else:
        dut._log.info("Test 1 Pass - Values are expected as 0.")


@cocotb.test()
async def inverter_using_model(dut):
    """ Test simple inverter """

    dut.input_a <= 1

    await Timer(2, units='ns')

    assert dut.output_z.value == inverter_model(1), "Inverter result is incorrect: {} != 0".format(dut.output_z.value)
