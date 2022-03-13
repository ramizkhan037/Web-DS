<?php

$hname = $_GET['hname'];

$db = pg_connect("host=localhost dbname=Slips user=hp password= ");
if($db)
{
$query = "select * from event where eno in(select eno from event_com where cno in(select cno from com where
name='$hname'))";
$resultSet = pg_query($db,$query);
echo "<h1>Event from Committee $hname are ...</h1>";
echo "<table style=height:400;width:400; border=3>";
echo "<tr><th>Eno</th>";
echo "<th>Title</th>";
echo "<th>Date</th>";
while(($row = pg_fetch_array($resultSet)) != null)
{
echo "<tr><td>".$row['eno']."</td>";
echo "<td>".$row['title']."</td>";
echo "<td>".$row['date']."</td>";
}
echo "</table>";
}

?>