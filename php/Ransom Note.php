<?php 
class Solution {
    function canConstruct($ransomNote, $magazine) {
        $magazineCount = count_chars($magazine, 1);
        $ransomNoteCount = count_chars($ransomNote, 1);
        
        foreach ($ransomNoteCount as $char => $count) {
            if (!isset($magazineCount[$char]) || $magazineCount[$char] < $count) {
                return false;
            }
        }

        return true;
    }
}