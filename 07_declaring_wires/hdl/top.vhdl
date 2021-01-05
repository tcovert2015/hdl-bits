-------------------------------------------------------------------------------
-- Declaring Wires Problem
--
-- Description:
-- Simple program to declare wires
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    a   : in  std_logic;
    b   : in  std_logic;
    c   : in  std_logic;
    d   : in  std_logic;
    z   : out std_logic;
    z_n : out std_logic
    );

end entity top;

architecture rtl of top is

  signal a_and_b : std_logic;
  signal c_and_d : std_logic;

begin

  a_and_b <= a and b;
  c_and_d <= c and d;

  z   <= a_and_b or c_and_d;
  z_n <= not(a_and_b or c_and_d);

end architecture rtl;
