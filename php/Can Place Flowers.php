<?php 
class Solution {

    function canPlaceFlowers($flowerbed, $n) {
        for($i = 0;$i<count($flowerbed);$i++){
            if(
                $flowerbed[$i]   === 0 &&
                $flowerbed[$i-1] !== 1 && 
                $flowerbed[$i+1] !== 1
            ) {
                $n--;
                $flowerbed[$i] = 1;
            }
        }
        return $n <= 0;
    }
}