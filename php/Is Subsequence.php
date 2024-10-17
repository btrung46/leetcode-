<?php
    class Solution {
        function isSubsequence($s, $t) {
            $n = strlen($t);
            $j = 0;
            for ($i = 0;$i < $n;$i++){
                if ($s[$j] === $t[$i]){
                    $j++;
                }
            }
            if ($j === strlen($s)){
                return true;
            }
            return false;
        }
    }