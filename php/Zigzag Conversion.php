<?php
    class Solution {
        function convert($s, $numRows) {
            if ($numRows === 1 || $numRows >= strlen($s)){
                return $s;
            }
            $index = 0;
            $d = 1;
            $rows = array_fill(0,$numRows, "");
    
            for($i = 0; $i < strlen($s);$i++){
                $rows[$index] .= $s[$i];
                if ($index === 0){
                    $d = 1;
                }
                if($index === $numRows - 1){
                    $d = -1;
                }
                $index += $d;
            }
    
            return implode("",$rows);
        }
    
    }