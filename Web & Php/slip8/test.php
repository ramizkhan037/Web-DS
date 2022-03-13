<?php
/* Function to get Factorial of a Number */
function getFactorial($num)
{
    $fact = 1;
    for($i = 1; $i <= $num ;$i++)
    $fact = $fact * $i;
    return $fact;
}
?>