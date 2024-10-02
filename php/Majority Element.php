<?php
    class Solution {
        function majorityElement($nums) {
            $test = array_count_values($nums);
            return array_search(max($test), $test); 
        }
    }
?>