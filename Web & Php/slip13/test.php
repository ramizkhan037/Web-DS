<?php
$str1 = $_GET['str1'];
$str2 = $_GET['str2'];
$ch = $_GET['ch'];

echo "First String is = $str1.<br><br>";
echo "second String is = ".$str2."<br><br>";
echo "String for Replace is = ".$str3."<br><br>";

I               f(strlen($str1)>strlen($str2))
{
                                switch($ch)
                                {
                                case 1 : $pos = strpos($str1,$str2);
                                                if($pos != 0)
                                                echo "string '$str2' Not present at the start of '$str1'.<br>";
                                                else echo "string '$str2' present at the start of '$str1'.<br>";
                                                break;
                                
}
else
{
                                switch($ch)
                                {
                                case 1 : $pos = strpos($str2,$str1);
                                                if($pos != 0)
                                                echo "string '$str1' Not present at the start of '$str2'.<br>";
                                                else  echo "string '$str1' present at the start of '$str2'.<br>";
                                                break;
                                
}

if (strcasecmp($str1,$str2)==0){
    echo '$str1 is equal to $str2 in a case-insensitive string comparison';
}

?>