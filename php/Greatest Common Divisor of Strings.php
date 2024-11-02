<?php 
class Solution {
    function gcd($a,$b){
        return ($b == 0) ? $a : $this->gcd($b,$a%$b);
    }
    function gcdOfStrings($str1, $str2) {
        if ($str1.$str2 !== $str2.$str1){
            return "";
        }
        return substr($str1,0,$this->gcd(strlen($str1),strlen($str2)));
    }
}