<?php

// start session

session_start();


if(isset($_POST["Submit"]))
{
#$export =  shell_exec ('export RDBASE=/opt/RDKit_2013_06_1');
#$export2 =  shell_exec ('LD_LIBRARY_PATH=$RDBASE/lib:$LD_LIBRARY_PATH');
#$export3 =  shell_exec ('PYTHONPATH=$RDBASE:$PYTHONPATH');
//username assigning

$_SESSION['JobName']=$_POST['JobName'];
$JobName=$_SESSION['JobName'];
#echo $JobName;
$_SESSION['Prob']=$_POST['Prob'];
$Probabilty=$_SESSION['Prob'];
echo $Probabilty;
$_SESSION['Mode']=$_POST['Mode'];
$Mode=$_SESSION['Mode'];
echo $Mode;
#$_SESSION['OutPut']=$_POST['OutPut'];
#$OutPut="./UserData/Results_" . $_SESSION['OutPut'].'out';



$_SESSION['Email']=$_POST['Email'];
$Email=$_SESSION['Email'];
echo $Email;

//filename specifications

$_SESSION["file"] = $_FILES["FileUpload1"]["name"];
$FileNameParts = explode(".", $_SESSION["file"]);
$_SESSION["IntermOutputINP"] = $FileNameParts[0]."ATOMS.txt";
$_SESSION["OutputINP"] = $FileNameParts[0].".inp";
}
#echo "This is FIle___________";
#echo $JobName;

#echo "This is Probability_______";
#echo $Mode;

#$tmp = exec("python testscriptphp.py .$item");
#echo "On Khaled.php\n";

if(isset($_POST["Submit"]))
{
//In the above POST, the name of the submit button has to be used (This name is given while creating the button in WebBuilder8)
  if ($_FILES["FileUpload1"]["error"] > 0)
    {
	//In the above $_FILES the first [] must have the name of the input i.e. FileUpload1 here (This name is given while creating the upload box in WebBuilder8)
      //echo "Return Code: " . $_FILES["FileUpload1"]["error"] . "<br />";
    }
  else
    {
    //echo "Upload: " . $_FILES["FileUpload1"]["name"] . "<br />";
    //echo "Type: " . $_FILES["FileUpload1"]["type"] . "<br />";
    //echo "Size: " . ($_FILES["FileUpload1"]["size"] / 1024) . " Kb<br />";
    //echo "Temp file: " . $_FILES["FileUpload1"]["tmp_name"] . "<br />";

    if (file_exists($_SESSION["file"]))
      {
      //echo $_FILES["FileUpload1"]["name"] . " already exists. ";
      }
    else
      {
       move_uploaded_file($_FILES["FileUpload1"]["tmp_name"], "./UserData/" . $_SESSION["file"]);
        // echo "Stored in: " . "./UserData/" . $_FILES["FileUpload1"]["name"];
       $f=$_SESSION["file"];
	}
    }

}
$input="./UserData/" . $f;

$myResults = array();
#$Script = "./preditar/preditar.py";
//$command = "sudo " . "$Script" . ' -n ' . "$JobName" . ' -i ' . "$input" . ' -m ' . "$Mode" . ' -p ' . "$Probabilty" . ' -e ' . "$Email" . " 1>&1";
#$command = "activate preditar; python " . "$Script" . ' -n ' . "$JobName" . ' -i ' . "$input" . ' -m ' . "$Mode" . ' -p ' . "$Probabilty" . ' -e ' . "$Email" . " 1>&1";
$output1 = "./UserData/temp.pdb";

$command1 = 'grep ATOM '   . "$input" .  ' > ' . "$output1" . " 1>&1";
echo $command1;
$myResults = shell_exec($command1);
$_SESSION['Results']=$myResults;
$_SESSION['Command']=$command;
#echo "This is Command <br>";
//echo $command;

#echo "<br \>";
#echo "Results has been sent to your Email ID:  ";
#echo $Email;
echo "<br \>";
#echo "Returned";
echo "<br>";
#//echo $mystring;
//echo $_SESSION['Results'];

echo "<br>";
/* Redirect browser */
#header("Location: ./results.php");
 
/* Make sure that code below does not get executed when we redirect. */
exit;
?>
