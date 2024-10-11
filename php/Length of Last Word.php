<?php
    class Solution {
        function lengthOfLastWord($s) {
            $result = 0;
            $n = strlen($s);
            for($i = $n - 1; $i > -1; $i--){
                if($s[$i] != ' '){
                    $result++;
                    if ($s[$i - 1] == ' '){
                        return $result;
                    }
                }
            }
            return $result;
        }
    }