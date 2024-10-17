<?php 
    class Solution {
        function twoSum($numbers, $target) {
            $left = 0;
            $right = count($numbers) - 1;
            while($left <= $right){
                $mid = $numbers[$left] + $numbers[$right];
                if ($mid === $target){
                    return [$left+1,$right+1];
                }else if ($mid < $target){
                    $left++;
                }else{
                    $right--;
                }
            }
        }
    }
