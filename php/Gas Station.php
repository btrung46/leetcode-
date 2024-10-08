<?php 
class Solution {
function canCompleteCircuit($gas, $cost) {
    if (array_sum($gas) < array_sum($cost)){
        return -1;
    }
    $current_gas = 0;
    $start_index = 0;
    for ($i = 0;$i<count($gas);$i++){
        $current_gas += $gas[$i] - $cost[$i];
        if ($current_gas < 0){
            $current_gas = 0;
            $start_index = $i+1;
        }
    }
    return $start_index;
}
}