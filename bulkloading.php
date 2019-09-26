<html>
<body style="margin:32px">

<head>

<?php include('menu.php');

	include("mysqli_connect.php");
	$conn = mysqli_connect($host, $username, $password, "databaseproject")
	or die("MySQL database '".$db_name."' not accessible.<br>\n");

		echo "<br>";
	//echo "<b>Database selected:</b> ". $db_name. "<br>";

 ?>
 <link rel="stylesheet" type="text/css" href="styles.css">

 </head>
 <body>

<!--
  <!-- create a form interface to be read and insert data into database -->
		 <form action="bulkloadingmain.php" name="readfile" method="post" enctype="multipart/form-data">

					<center>
					<br>
					<b>Table <b>

					<!-- PHP dynamic table select-->
					<?php

					$sql = "SHOW TABLES FROM $db_name";
					$result = mysqli_query($conn,$sql);

					if (!$result) {
						echo "DB Error, could not list tables\n";
						echo 'MySQL Error: ' . mysql_error();
						exit;
					}
						echo "<select name='tableselect'>";
					while ($row = mysqli_fetch_row($result)) {

						echo "<option value=$row[0]>$row[0]</option>";
					}
						echo "</select>";
						mysqli_free_result($result);


					?>


					<label for="txt-file"><b>(Only txt files)</b></label>
					<br>
					<br>
					<input type="file" name="file1">
					<br>
					<input type="submit" id="myfile" name="reads" value="Insert">
					</center><!--button to submit the form to read data from the file
			<!--	<input type="button" id="myfile" name="read" onclick="show()">Submit</button><!--button to submit the form to read data from the file-->

		  </form>

 </body>
 </html>
