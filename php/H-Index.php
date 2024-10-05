<?php
class Solution {
    function hIndex($citations) {
        rsort($citations);
        $i = 0;
        foreach ($citations as $citation) {
            if ($i < $citations[$i]) $i++;
        }
        return $i;
    }
}