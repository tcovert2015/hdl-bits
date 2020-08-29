-------------------------------------------------------------------------------
-- AND Gate Problem
--
-- Description:
-- Simple AND gate
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    a : in  std_logic;
    b : in  std_logic;
    z : out std_logic);

end entity top;

architecture rtl of top is
begin

  z <= a and b;

end architecture rtl;
