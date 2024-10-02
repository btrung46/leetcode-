<?php
    class Solution {
        function rotate(&$nums, $k) {
            $n = $k % count($nums);
            $this->reverse($nums, 0, count($nums) - 1);
            $this->reverse($nums, 0, $n - 1);
            $this->reverse($nums, $n, count($nums) - 1);
        }
        function reverse(&$nums,$left,$right){
            while($left < $right){
                $temp = $nums[$left];
                $nums[$left] = $nums[$right];
                $nums[$right] = $temp;
                $left++;
                $right--;
            }
        }
    }
?>