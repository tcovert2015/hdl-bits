


library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (
    c : in  std_logic;
    d : in  std_logic;
    q : out std_logic := '0');
end entity top;

architecture rtl of top is
begin
  -- It is also possible to add an delay of less than one clock period here.
  q <= d when rising_edge(c);
end architecture rtl;
