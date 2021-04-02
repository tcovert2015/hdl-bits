CWD=$(shell pwd)

TOPLEVEL_LANG = vhdl

# Simulator
SIM = ghdl

# Import Model by adding the directory to PYTHONPATH
export PYTHONPATH := $(CWD)/../model:$(PYTHONPATH)

VHDL_SOURCES =$(CWD)/../hdl/top.vhdl

# Top level name in the VHDL design
TOPLEVEL = top

# Module is the name of the Python test file
MODULE := $(TOPLEVEL)

# CUSTOM_SIM_DEPS=$(CWD)/Makefile
SIM_ARGS = --vcd=sim_build/waveform.vcd

include $(shell cocotb-config --makefiles)/Makefile.sim
