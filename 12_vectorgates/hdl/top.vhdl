-------------------------------------------------------------------------------
-- Vectors in more detail. hdlbits.01xz.net/wiki/Vectorgates
--
-- Basic combination logic
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    -- Vector Input
    a : in std_logic_vector(2 downto 0);
    b : in std_logic_vector(2 downto 0);

    -- Outputs
    out_or_bitwise : out std_logic_vector(2 downto 0);
    out_or_logical : out std_logic;
    out_not        : out std_logic_vector(5 downto 0)
    );

end entity top;

architecture rtl of top is

begin

  -- Bitwise OR
  out_or_bitwise      <= a or b;
  -- Logical OR
  -- out_or_logical      <= a or b;
  -- NOT
  out_not <= (not b) & (not a);

end architecture rtl;
