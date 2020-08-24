import cocotb
from cocotb.triggers import Timer

@cocotb.test()
async def simple_wires(dut):
    """Try accessing the design."""

    input = str(dut.input)
    output = str(dut.output)
    
    dut._log.info("Running test!")
    
    # Change input to a 1.
    dut.input <= 1
    await Timer(1, units='ns') # Wait for 1 ns for the output signal to channge.

    # Read the output signal
    dut._log.info("The output should be 1")

    # Set error if the output does not equal the input
    if output != 0:
        raise dut._log.error("output does not equal input")
    else:
        dut._log.info("Else branch")
        
    # Print out the output value
    dut._log.info(dut.output)

    # Verify output is a 0 after input becomes 0    
    dut.input <= 0
    await Timer(1, units='ns')
    if output != input:
        raise dut._log.error("dut.output != dut.input")

    dut._log.info("The output should be 0")
    dut._log.info(dut.output)
