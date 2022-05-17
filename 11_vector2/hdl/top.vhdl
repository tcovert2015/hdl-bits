-------------------------------------------------------------------------------
-- Vectors in more detail. hdlbits.01xz.net/wiki/Vector1
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    -- Vector Input
    vec : in std_logic_vector(15 downto 0);

    -- Outputs
    out_hi : out std_logic_vector(7 downto 0);
    out_lo : out std_logic_vector(7 downto 0)
    );

end entity top;

architecture rtl of top is

begin

  out_hi <= vec(15 downto 8);
  out_lo <= vec(7 downto 0);

end architecture rtl;
