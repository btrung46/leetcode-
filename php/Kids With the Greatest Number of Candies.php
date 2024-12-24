<?php

class Solution {

    function kidsWithCandies($candies, $extraCandies) {
        $result = [];
        $maxcandy = max($candies);
        foreach($candies as $candy){
            if ($candy + $extraCandies >= $maxcandy){
                array_push($result,true);
            }else{
                array_push($result,false);
            }
        }
        return $result;
    }
}