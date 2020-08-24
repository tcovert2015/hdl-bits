library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (
    input  : in  std_logic;
    output : out std_logic);
end entity top;

architecture rtl of top is
begin

  output <= input;

end architecture rtl;
