<?php 
    class Solution {
        function maxArea($height) {
            $left = 0;
            $n = count($height);
            $right = $n - 1;
            $ans = 0;
            while($left <= $right ){
                $maxarea = min($height[$left], $height[$right])*($right - $left);
                if ($maxarea > $ans){
                    $ans = $maxarea;
                }
                if($height[$left] >= $height[$right]){
                    $right--;
                }else{
                    $left++;
                }
            }
            return $ans;
    
        }
    }