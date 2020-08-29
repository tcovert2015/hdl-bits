-------------------------------------------------------------------------------
-- Inverter Problem
--
-- Description:
-- Input signal that gets inverted and sent to an output signal.
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    input_a  : in  std_logic;
    output_z : out std_logic);

end entity top;

architecture rtl of top is
begin

  output_z <= not(input_a);

end architecture rtl;
