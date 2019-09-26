<html>
<body style="margin:32px">
<head>
<?php include('menu.php');
    require_once 'mysqli_connect.php';
	echo "<br>";
 ?>
<link rel="stylesheet" type="text/css" href="style.css">
</head>
<body>
		 <form action="singleinsertionmain.php" name="readfile" method="post" enctype="multipart/form-data">

                    <center>
					<br>
					<b> Select Table <b>
					<?php

					$sql = "SHOW TABLES FROM $db_name";
					$result = mysqli_query($con,$sql);

					if (!$result) {
						echo "Could not list tables\n";
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
					<input type="submit" id="myfile" name="read" value="Insert">
			</center>
		  </form>
		 <div id="insert"></div>

	</body>
<!-- To display the error status and for the submmit button to get reloaded -->
<script>
function fetch_select(str) {
  var xhttp;
  if (str == "") {
    document.getElementById("insert").innerHTML = "";
    return;
  }
  xhttp = new XMLHttpRequest();
  xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("insert").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "singleinsertionmain.php? q2="+str, true);
  xhttp.send();
}
</script>
</html>
