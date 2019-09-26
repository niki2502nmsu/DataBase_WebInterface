<html>
<body style="margin:32px">
<head>
<?php include('menu.php');

	  require_once 'mysqli_connect.php';
		echo "<br>";
 ?>
<link rel="stylesheet" type="text/css" href="styles.css">
<center>
<p>Delete all records from the table selected </p>
<br>

		  <select name="table_select" id="table_select">
		  <option value=""></option>
		  <?php

					$sql = "SHOW TABLES FROM $db_name";
					$result = mysqli_query($con,$sql);

					if (!$result) {
						echo " Error : Tables are not listed\n";
						echo 'Error: ' . mysql_error();
						exit;
					}

					while ($row = mysqli_fetch_row($result)) {

						echo "<option value=$row[0]>".$row[0]."</option>";
					}
		  ?>

			</select>
			<br>
			<br>
			<p><button onclick="fetch_select()"/>Delete</button></p>
		    <div id="delete"></div>
			</center>
	</body>
   <script>
   function fetch_select() {
    var str=document.getElementById("table_select").value;
    var xhttp;
    if (str == "") {
         document.getElementById("delete").innerHTML = "";
    return;
    }
   xhttp = new XMLHttpRequest();
   xhttp.onreadystatechange = function() {
    if (this.readyState == 4 && this.status == 200) {
      document.getElementById("delete").innerHTML = this.responseText;
    }
  };
  xhttp.open("GET", "deletionmain.php?q3="+str, true);
  xhttp.send();
}
</script>
</html>
