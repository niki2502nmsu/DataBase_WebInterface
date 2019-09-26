<html>
<body style="margin:32px">
<head>
  <link rel="stylesheet" type="text/css" href="styles.css">
</head>
<?php

include("mysqli_connect.php");
echo "<b>Database Name:</b> ". $db_name. "<br>";

if(isset($_POST['reads'])){//check if button have been click or not
		$start = microtime(true); //start time
		$tablenames = $_POST['tableselect']; //table selection

		$terminated=",";
		$file_type=$_FILES['file1']['type'];//get file type of selected file to read
		$allow_type=array('text/plain');//allow only file that have extesion with .txt
		$fieldall="";
			$filename = "/Applications/Xampp/htdocs/dbproject/bulk/".$_FILES['file1']['name'];
		$sql2 = "LOAD DATA LOCAL INFILE '$filename' INTO TABLE `$tablenames` FIELDS TERMINATED BY ',' ENCLOSED BY '' LINES TERMINATED BY '\\r\\n'";

		$loaddata = mysqli_query($con,$sql2);

		if (!$loaddata) {
		die('Could not load data from file into table: ' .mysqli_error($con));

		}

		$end = microtime(true);
			$diff = $end-$start;
			$querytime = number_format($diff,10);
			echo "<br><b>Duration to execute: </b>$querytime seconds";



	}
