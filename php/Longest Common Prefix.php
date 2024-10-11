<?php
class Solution {

/**
 * @param String[] $strs
 * @return String
 */
function longestCommonPrefix($strs) {
    sort($strs);
    $m = count($strs);
    $start = $strs[0];
    $end = $strs[$m - 1];
    $ans = "";
    $n = min(strlen($start), strlen($end));
    for ($i = 0;$i < $n;$i++){
        if ($start[$i] != $end[$i]){
            return $ans;
        }
        $ans .= $start[$i];
        echo $ans;
    }
    return $ans;
}
}