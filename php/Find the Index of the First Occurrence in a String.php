<?php

    class Solution {
        function strStr($haystack, $needle) {
            $n = strlen($haystack);
            $m = strlen($needle);
            if ($n < $m){
                return -1;
            }
            $startidx = -1;
            for ($i = 0;$i<$n;$i++){
                $dem = 0;
                $x = 0;
                $y = $i;
                while($x < $m ){
                    if ($haystack[$y] === $needle[$x]){
                        $dem++;
                    }
                    $x++;
                    $y++;
                }
                if ($dem === $m){
                    $startidx = $i;
                    break;
                }
            }
            
            return $startidx;
        }
    }