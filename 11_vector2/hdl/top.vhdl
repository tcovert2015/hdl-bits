-------------------------------------------------------------------------------
-- Vectors in more detail. hdlbits.01xz.net/wiki/Vector2
--
-- Reverse the byte order
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    -- Vector Input
    vec : in std_logic_vector(31 downto 0);

    -- Outputs
    outvec : out std_logic_vector(31 downto 0)
    );

end entity top;

architecture rtl of top is

begin

  outvec(31 downto 24) <= vec(07 downto 00);
  outvec(23 downto 16) <= vec(15 downto 08);
  outvec(15 downto 08) <= vec(23 downto 16);
  outvec(07 downto 00) <= vec(31 downto 24);

end architecture rtl;
