<?php

// start session
session_start();

$Email=$_SESSION['Email'];
echo "Execited the mail process"
?>

<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Untitled Page</title>
<meta name="generator" content="WYSIWYG Web Builder 9 - http://www.wysiwygwebbuilder.com">
<style type="text/css">
div#container
{
   width: 970px;
   position: relative;
   margin-top: 0px;
   margin-left: auto;
   margin-right: auto;
   text-align: left;
}
body
{
   text-align: center;
   margin: 0;
   background-color: #FFFFFF;
   color: #000000;
}
</style>
<style type="text/css">
a
{
   color: #0000FF;
   text-decoration: underline;
}
a:visited
{
   color: #800080;
}
a:active
{
   color: #FF0000;
}
a:hover
{
   color: #0000FF;
   text-decoration: underline;
}
</style>
<style type="text/css">
#Image1
{
   border: 0px #000000 solid;
}
#wb_Text1 
{
   background-color: transparent;
   border: 0px #000000 solid;
   padding: 0;
   text-align: left;
}
#wb_Text1 div
{
   text-align: left;
}
<!--C:\\wamp\\www\\Naeem\\-->
</style>
</head>
<body>
<div id="container">
<div id="wb_Image1" style="position:absolute;left:361px;top:248px;width:302px;height:302px;z-index:0;">
<a href=<?php echo './UserData/Results_'. $_SESSION['OutPut'].'out'; ?> target="_blank"><img src="images/icon-download.gif" id="Image1" alt="" style="width:302px;height:302px;"></a></div>
<div id="wb_Text1" style="position:absolute;left:405px;top:599px;width:241px;height:16px;z-index:1;text-align:left;">
<span style="color:#000000;font-family:Arial;font-size:13px;">Click Image to download results.</span></div>
</div>
</body>
</html>
