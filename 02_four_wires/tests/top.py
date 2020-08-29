import cocotb
from cocotb.triggers import Timer

# This test is really bad. Just learning cocotb and python...

@cocotb.test()
async def four_wires(dut):
    """Try accessing the design."""

    input_a = str(dut.input_a)
    input_b = str(dut.input_b)
    input_c = str(dut.input_c)
    output_w = str(dut.output_w)
    output_x = str(dut.output_x)
    output_y = str(dut.output_y)
    output_z = str(dut.output_z)
    
    ###############################
    # Test 1 - Change Inputs to 1 #
    ###############################
    
    # Change inputs to a 1
    dut.input_a <= 1
    dut.input_b <= 1
    dut.input_c <= 1
    await Timer(1, units='ns') # Wait for 1 ns for the output signal to channge.

    # Set error if the output does not equal the input
    if (output_w != input_a) or (output_x != input_b) or (output_y != input_b) or (output_z != input_c) :
        raise dut._log.error("Output does not equal input. All outputs should be 1.")
    else:
        dut._log.info("Test 1 Pass - All values are expected as 1.")

    ###############################
    # Test 2 - Change Inputs to 0 #
    ###############################
    
    # Change inputs to a 0
    dut.input_a <= 0
    dut.input_b <= 0
    dut.input_c <= 0
    await Timer(1, units='ns') # Wait for 1 ns for the output signal to channge.

    # Set error if the output does not equal the input
    if (output_w != input_a) or (output_x != input_b) or (output_y != input_b) or (output_z != input_c) :
        raise dut._log.error("Output does not equal input. All outputs should be 0.")
    else:
        dut._log.info("Test 2 Pass - All values are expected as 0.")
        
