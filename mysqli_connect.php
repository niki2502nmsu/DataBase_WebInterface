<?php
  $host = "localhost";
  $username = "root";
  $password = "";
  $db_name = "databaseproject";
  $con = new mysqli($host, $username, $password, $db_name);
  if(mysqli_connect_errno()) {
  echo "Connection could not be established";
  exit;


}
?>
