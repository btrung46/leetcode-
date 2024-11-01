<?php 
class Solution {
    function mergeAlternately($word1, $word2) {
        $letters1 = str_split($word1);
        $letters2 = str_split($word2);
        $count1 = count($letters1);
        $count2 = count($letters2);
        $ind1 = 0;
        $ind2 = 0;
        $indRes = 0;

        $res = [];
        while ($ind1 < $count1 && $ind2 < $count2) {
            $res[$indRes++] = $letters1[$ind1++];
            $res[$indRes++] = $letters2[$ind2++];
        }

        if ($ind1 < $count1) {
            for ($i = $ind1 ; $i<$count1 ; $i++) {
                $res[$indRes++] = $letters1[$i];
            }
        }

        if ($ind2 < $count2) {
            for ($i = $ind2 ; $i<$count2 ; $i++) {
                $res[$indRes++] = $letters2[$i];
            }
        }

        return implode('', $res);
    }
}