<?php 
    class Solution {
        function wordPattern($pattern, $s) {
            $s = explode(" ",$s);
            $temp = [];
           
            if (count($s) !== strlen($pattern)){
                return false;
            }
            for ($i = 0;$i < strlen($pattern);$i++){
                if(isset($temp[$pattern[$i]]) && $temp[$pattern[$i]] !== $s[$i]){
                    return false;
                }
                if (in_array($s[$i], $temp) && !isset($temp[$pattern[$i]])){
                    return false;
                }
                $temp[$pattern[$i]] = $s[$i];
            }
            return true;
        }
    }