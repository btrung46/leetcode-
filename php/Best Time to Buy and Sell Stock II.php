<?php
    class Solution {
        function maxProfit($prices) {
            $sell = 1;
            $buy = 0;
            $profit = 0;
            while($sell < count($prices)){
                $ans = $prices[$sell] - $prices[$buy];
                if ($ans > 0){
                    $profit += $ans;
                }
                $buy = $sell;
                $sell++;
            }
            return $profit;
        }
    }
?>