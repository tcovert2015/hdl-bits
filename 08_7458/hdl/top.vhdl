-------------------------------------------------------------------------------
-- Modeling the 7458 chip
--
-- Description:
-- Simple program to model the 7458 chip. It has 4 AND gates and two OR gates
-------------------------------------------------------------------------------

library ieee;
use ieee.std_logic_1164.all;

entity top is
  port (

    -- P1 Inputs
    p1a   : in  std_logic;
    p1b   : in  std_logic;
    p1c   : in  std_logic;
    p1d   : in  std_logic;
    p1e   : in  std_logic;
    p1f   : in  std_logic;

    -- P2 Inputs
    p2a   : in  std_logic;
    p2b   : in  std_logic;
    p2c   : in  std_logic;
    p2d   : in  std_logic;

    -- Outputs
    p1y : out std_logic;
    p2y : out std_logic
    );

end entity top;

architecture rtl of top is

begin

  p1y <= ((p1a and p1b and p1c) or (p1f and p1e and p1d));
  p2y <= ((p2a and p2b) or (p2c and p2d));
  
end architecture rtl;
