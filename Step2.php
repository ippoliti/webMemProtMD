<?php
echo "This is test";
include "Step0.php";
?>
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Untitled Page</title>
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
#Image2
{
   border: 0px #000000 solid;
}
#Image1
{
   border: 0px #000000 solid;
}
</style>
</head>
<body>
<div id="container">
<div id="wb_Image2" style="position:absolute;left:146px;top:43px;width:630px;height:630px;z-index:0;">
<img src="images/processing%20%281%29.gif" id="Image2" alt="" style="width:630px;height:630px;"></div>
<div id="wb_Image1" style="position:absolute;left:146px;top:526px;width:630px;height:131px;z-index:1;">
<img src="images/img0001.png" id="Image1" alt="" style="width:630px;height:131px;"></div>
</div>
</body>
</html>

<?php
/* Redirect browser */
header("Location: ./results.php");
 
/* Make sure that code below does not get executed when we redirect. */
exit;
?>
