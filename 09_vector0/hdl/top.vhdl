-------------------------------------------------------------------------------
-- Simple Vector in VHDL from hdlbits.
--
-- Description:
-- VHDL to route vectors in a design.
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    -- Vector Input
    vec : in std_logic_vector(2 downto 0);

    -- Outputs
    outv : out std_logic_vector(2 downto 0);
    o0   : out std_logic;
    o1   : out std_logic;
    o2   : out std_logic
    );

end entity top;

architecture rtl of top is

begin

  outv <= vec;
  o0   <= vec(0);
  o1   <= vec(1);
  o2   <= vec(2);

end architecture rtl;
