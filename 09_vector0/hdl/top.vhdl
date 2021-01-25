library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    vec   : in  std_logic_vector(2 downto 0);
    outv  : out std_logic_vector(2 downto 0);
    out_0 : out std_logic_vector(0 downto 0);
    out_1 : out std_logic_vector(0 downto 0);
    out_2 : out std_logic_vector(0 downto 0)
    );

end entity top;

architecture rtl of top is

begin

  outv <= vec;
  out_0 <= vec(0 downto 0);
  out_1 <= vec(1 downto 1);
  out_2 <= vec(2 downto 2);
  
end architecture rtl;
