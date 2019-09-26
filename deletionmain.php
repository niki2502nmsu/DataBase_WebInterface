<html>
<body style="margin:32px">
<head>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<?php

include("mysqli_connect.php");

echo "<b>Database Name:</b> ". $db_name. "<br>";

//Creating Connection
if(isset($_GET['q3']))
{
	$tablename = $_GET['q3'];
	//echo $tablename;
	$q1= "SELECT * FROM $tablename";
	$q = "DELETE FROM $tablename";
	ini_set('max_execution_time', 10000);
	$results1 = mysqli_query($con, $q1);
	$row_cnt = mysqli_num_rows($results1);

	$startedtime = microtime(true);
	$results = mysqli_query($con, $q);
	if(!$results)
	{
	$res = mysqli_error($con);
	echo "<font color='red'>Error: </font>".$res;
	exit;
	}
	$endtime = microtime(true);
	$difference = $endtime-$startedtime;
	$queryTime = number_format($difference, 10);

	echo "<b>Results: </b>All rows of <b>$tablename</b> are deleted<br>";
	echo "<b>No of rows affected:<b> $row_cnt";
	echo "<br><b>Duration to exectue: </b>$queryTime seconds";

}
?>

</body>
<script>
function delete1() {
var x=document.getElementById("trdelete1").value;


  if (window.XMLHttpRequest) {
    // code for IE7+, Firefox, Chrome, Opera, Safari
    xmlhttp=new XMLHttpRequest();
  } else { // code for IE6, IE5
    xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
  }
  xmlhttp.onreadystatechange=function() {
    if (this.readyState==4 && this.status==200) {
      document.getElementById("txtHint").innerHTML=this.responseText;
    }
  }
  xmlhttp.open("POST","insertionmain.php?q5="+x,true);
  xmlhttp.send();
}
</script>
</html>
