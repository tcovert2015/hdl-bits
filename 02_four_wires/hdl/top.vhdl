library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    input_a  : in  std_logic;
    input_b  : in  std_logic;
    input_c  : in  std_logic;
    output_w : out std_logic;
    output_x : out std_logic;
    output_y : out std_logic;
    output_z : out std_logic);

end entity top;

architecture rtl of top is
begin

  output_w <= input_a;
  output_x <= input_b;
  output_y <= input_b;
  output_z <= input_c;

end architecture rtl;
