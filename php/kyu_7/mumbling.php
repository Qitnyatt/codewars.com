<?php

// https://www.codewars.com/kata/5667e8f4e3f572a8f2000039/train/php

function accum($s)
{
    $result = [];
    foreach (str_split($s) as $index => $item) {
        array_push($result, mb_strtoupper($item) . str_repeat(mb_strtolower($item), $index));
    }
    return join("-", $result);
}
