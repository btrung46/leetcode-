<?php

class Solution {
function isPalindrome($s) {
    $s = preg_replace("/[^a-z0-9]/","",strtolower($s));
    $end = strlen($s) -1;
    echo $s;
    for ($start = 0;$start <= $end; $start++,$end--){
        if ($s[$start] != $s[$end]){
            return false;
        }
    }
    return true;
}
}