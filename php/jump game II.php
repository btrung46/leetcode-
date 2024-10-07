<?php
    class Solution {
    function jump($nums) {
        $far = $near = $jump = 0;
        while($far < count($nums)-1){
            $farthest = 0;
            for ($i = $near; $i <= $far; $i++){
                $farthest  = max($farthest, $i + $nums[$i]);
            }
            $near = $far + 1;
            $far = $farthest;
            $jump++;
        }
        return $jump;
    
    }
}