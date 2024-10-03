<?php
class Solution {
    function canJump($nums) {
        $n = count($nums);
        $goal = $n-1;
        for($i = $n - 2;$i >= 0;$i--){
            if($goal - $i <= $nums[$i]){
                $goal = $i;
            }
        }
        echo $goal;
        if ($goal === 0){
            return true;
        }
        return false;
    }
}
?>