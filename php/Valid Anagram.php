<?php 
    class Solution {
        function isAnagram($s, $t) {
            if (count_chars($s, 1) == count_chars($t, 1)) return true; else return false;
        }
    }