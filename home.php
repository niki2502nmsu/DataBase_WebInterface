<html>
<body style="margin:32px">
<head>
<?php include('menu.php');

	  require_once 'mysqli_connect.php';
		echo "<br>";
 ?>
 <link rel="stylesheet" type="text/css" href="styles.css">

</head>

<center>
<h2> SQL INTERFACE </h2>

<form id='sqledi' action="query.php" method="POST">
<h3> Write your query below: <br></h3>
<textarea name="sqlquery" rows="10" cols="50">
</textarea><br>
<input type="submit" value="Submit" name="submit">
</form>

<!-- Overlay effect when opening sidebar on small screens -->


</center>
</body>
</html>
