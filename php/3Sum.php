<?php
class Solution {
    function threeSum(&$nums) {
        $n = count($nums);
        sort($nums);
        $ans = [];
        for ($i = 0;$i < $n;$i++){
            $j = $i + 1;
            $k = $n - 1;
            if ($i > 0){
                if( $nums[$i] === $nums[$i-1]){
                    continue;
                }
            }
            while($j<$k){
                $total = $nums[$i] + $nums[$j] + $nums[$k];
                if ($total < 0){
                    $j++;
                }else if ($total > 0){
                    $k--;
                }else{
                    $ans[] = [$nums[$i], $nums[$j], $nums[$k]];
                    $j++;
                    while($j<$k && $nums[$j] === $nums[$j-1]){
                        $j++;
                    }
                }
            }
        }
        return $ans;
    }
}