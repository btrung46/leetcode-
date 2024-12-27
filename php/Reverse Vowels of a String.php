<?php 
    class Solution {
        function reverseVowels($s) {
            if (strlen($s)<= 1) 
            {
                return $s;
            }
            $left = 0;
            $right = strlen($s) - 1;
            while($left <= $right){
                if (in_array($s[$left],["a", "e", "i", "o", "u","A","E","I","O","U"])){
                    while($left <= $right){
                        if(in_array($s[$right],["a", "e", "i", "o", "u","A","E","I","O","U"]) ){
                            $temp = $s[$left];
                            $s[$left] = $s[$right];
                            $s[$right] = $temp;
                            $right--;
                            break;
                        }
                        $right--;
                    }
                }
                $left++;
            }
            return $s;
        }
    }