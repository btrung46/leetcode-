<?php
    class Solution {

        function maxProfit($prices) {
            $buy = 0;
            $sell = 1;
            $max = 0;
            while($sell < count($prices)-1){
                $ans = $prices[$sell] - $prices[$buy];
                if ($ans < 0){
                    $buy = $sell;
                }
                if ($ans >= 0 && $ans > $max){
                    $max = $ans;
                }
                $sell++;
            }
            return $max;
        }
}
?>