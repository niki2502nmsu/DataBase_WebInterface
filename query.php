<html>
     <body style="margin:32px">
      <head>
         <link rel="stylesheet" type="text/css" href="styles.css">
      </head>
<?php
   include("mysqli_connect.php");
   echo "<b>Database :</b> ". $db_name. "<br>";
    if(isset($_REQUEST['submit']))
    {
          $ins=$_POST['sqlquery'];
          $start_time = microtime(true);
          $ref = $con->query($ins);
          $returnvalues = true;
           if(!$ref){
             die("<p>Error in executing query : ".$ins."<br>".$con->error." </p>");
           }
           if(preg_match("/^[t\r\n]*(CREATE|INSERT|DELETE|UPDATE|DROP)/i",trim($ins))){
            $returnvalues = false;
          }
          if($returnvalues){
             $rows =0;
             $cols =0;
          echo "<table class='w3-table-all'>";
          while ($result = mysqli_fetch_assoc($ref)){
             echo "<tr>";
             foreach ($result as $key1 => $value) {
               if($rows==0){echo "<th> $key1 </th>";
               }
            }
            echo "</tr>";
            $rows++;
            echo "<tr>";
            foreach ($result as $key1 => $value) {
                if($value==0 | intval($value)){echo "<th> $value </th>";
           }
        }
        echo "</tr>";
    }
    echo "</table>";
  }
  else
  {
      echo "<p>Query".$ins. "processed successfully. </p>";
  }
  echo 'Time taken for execution ' . (microtime(true) - $start_time) . ' seconds<br>';
}
?>
</body>
</html>
