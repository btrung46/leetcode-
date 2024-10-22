<?php
    class Solution {
        function isIsomorphic($s, $t) {
            $mapS = [];
            $mapT = []; 
            for ($i = 0; $i < strlen($s); $i++) {
                $charS = $s[$i];
                $charT = $t[$i];
                if (isset($mapS[$charS]) && $mapS[$charS] != $charT) {
                    return false;
                }
                if (isset($mapT[$charT]) && $mapT[$charT] != $charS) {
                    return false;
                }
    
                $mapS[$charS] = $charT;
                $mapT[$charT] = $charS;
            }
    
            return true;
        }
    }