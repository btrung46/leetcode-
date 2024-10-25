<?php
    class Solution {
        function groupAnagrams($strs) {
            $temp =[];
            foreach($strs as $s){
               $sortword = str_split($s);
               sort($sortword);
               $sortword = implode('',$sortword);
               $temp[$sortword][] = $s;
            }
            return array_values($temp);
        }
    }