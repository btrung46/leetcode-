<?php
class Solution {
function productExceptSelf($nums) {
    $result = [];
    $left = 1;
    $n = count($nums);
    for ($i = 0; $i < $n; $i++){
        array_push($result,$left);
        $left = $left*$nums[$i];
    }
    $right = 1;
    for ($i = $n-1; $i >= 0;$i--){
        $result[$i] *= $right;
        $right *= $nums[$i];
    }
    return $result;
}
}