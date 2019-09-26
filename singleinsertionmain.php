<html>
<body style="margin:32px">
<head>
<link rel="stylesheet" type="text/css" href="styles.css">
</head>
<?php
  //  include('menu.php');
    include("mysqli_connect.php");
    require_once 'mysqli_connect.php';

if(isset($_GET['q2']))
  {
	 $tablename=$_GET['q2'];
	 echo "<b>Table Name ".$tablename;
	 $query = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'databaseproject' AND TABLE_NAME = '$tablename'";
	 $columnnames = mysqli_query($con,$query)
	 or die("<br>$q<br>".mysqli_error($columnnames));
	 if($columnnames == false) die("Some problem occured <br>$q<br>");
	 echo "<form action='singleinsertionmain.php' name='readtable' method='post' enctype='multipart/form-data'>";
	 echo "<table class= 'style' id='rams'>";
	 $index = 0;
	 echo "<input type='hidden' id='custId' name='tablename' value='$tablename'>";
	while($arr = mysqli_fetch_array($columnnames))
		{
			$table = $tablename;
			foreach($arr as $x => $x_value)
			{
              if( intval($x)!== 0 || $x == '0') continue;
				echo "<tr class='style3'>";
				echo "<th class= 'style1'>$x_value</th>";
				echo "<td class= 'style1'><input type='text' name='$x_value'></td>";
                echo "</tr>";
                echo "<br>";
			}

		}
		echo "</table>";
        echo "<input type='submit' id='myfile' name='reading' value='Insert'>";
		echo "</form>";
  }


/*/*insert file operations*/

if(isset($_POST['read'])){//check if button have been click or not

		$start = microtime(true); //start time
		$tablenames = $_POST['tableselect']; //table selection
        $terminated=",";
		$file_type=$_FILES['file1']['type'];//get file type of selected file to read
		$allow_type=array('text/plain');//allow only file that have extesion with .txt
		$fieldall="";
		if(in_array($file_type,$allow_type)){//check if selected file type is match to the allow file type we have defined
		  $file=fopen("/Applications/Xampp/htdocs/dbproject/single/".$_FILES['file1']['name'],"r") or die ("Unable to open file!");//open file to read

             echo "<table class='style'  cellspacing='5' cellpadding='8' overflow:scroll; >";

		  while(!feof($file)){//check if not yet end of files while reading data
		  $line = fgets($file);//get data from selected file

		  $values=str_replace($terminated,",",$line);//we use str_replace to replace the character we want to terminated to seperate the table columns
		   //creating table names
		  $query1 = "SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_SCHEMA = 'databaseproject' AND TABLE_NAME = '$tablenames'";

	 $columnnames = mysqli_query($con,$query1)
	 or die("<br>$q<br>".mysqli_error($columnnames));

	 if($columnnames == false) die("Problem occured :<br>$q<br>");
	 $clnames="";
	 $i=0;
	 while($arr = mysqli_fetch_array($columnnames))
		{
            foreach($arr as $x => $x_value)
			{
				if( intval($x)!== 0 || $x == '0') continue;

				if($i==0)
				{
				$clnames.= "$x_value";
				$i++;
				}
				else
				{
				$clnames.= ",$x_value";
				}

			}
		}

		  $sql="insert into $tablenames($clnames) values($values)";//query string //i have added extra ($clnames) after some errors
          ini_set('max_execution_time', 10000); //maximum execution time
		  $inserts= mysqli_query($con,$sql); //execute query insert data to database

		  if (!$inserts)
		  {
			$s = mysqli_error($con);
            echo "<tr class='style3'>";
		    echo "<td class='style1' ><img src='failimage.png' width='20' height='25' /></td><td class='style1' > $sql<br> <font color='red'> Error $s </font> </td> ";
		    echo "</tr>";
		  }
         if($inserts)
		  {
            echo "<tr class='style3'>";
		    echo "<td class='style1' ><img src='success.png' width='20' height='30' /></td><td class='style1' > $sql</td> ";
		    echo "</tr>";
          }
		}

		echo "</table>";

		$end = microtime(true);
			$diff = $end-$start;
			$querytime = number_format($diff,10);
			echo "<br><b>Time taken for execution </b>$querytime seconds";
            fclose($file);//close the file after read
		}else{
			echo "Please select only text file(.txt file is recomended)!";
		}
	}

?>
<br />
</body>
</html>
