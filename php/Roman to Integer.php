<?php
    class Solution {

    /**
     * @param String $s
     * @return Integer
     */
    function romanToInt($s) {
        $m = array(
            "I" => 1,
            "V" => 5,
            "X" => 10,
            "L" => 50,
            "C" => 100,
            "D" => 500,
            "M" => 1000
        );
        $ans = 0;
        for($i = 0;$i < strlen($s);$i++){
            if ($i < strlen($s)-1 && $m[$s[$i]] < $m[$s[$i+1]]){
                $ans -= $m[$s[$i]];
            }
            else{
                
                $ans += $m[$s[$i]];
            }
        }
        return $ans;
    }
    }