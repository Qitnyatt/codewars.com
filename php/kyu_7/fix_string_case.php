<?php

// https://www.codewars.com/kata/5b180e9fedaa564a7000009a/train/php'

function solve($s)
{
    $lowerCase = mb_strtolower($s);
    $upperCase = mb_strtoupper($s);

    $countLower = similar_text($s, $lowerCase);
    $countUppercase = similar_text($s, $upperCase);

    if ($countLower >= $countUppercase) {
        return $lowerCase;
    }
    return $upperCase;
}
