<?php
session_start();
?><!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>PrediTar: Home</title>
<meta name="generator" content="WYSIWYG Web Builder 9 - http://www.wysiwygwebbuilder.com">
<style type="text/css">
div#container
{
   width: 960px;
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
   background-image: url(images/background.png);
   background-attachment: fixed;
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
#wb_CssMenu1
{
   border: 0px #02A681 solid;
   background-color: transparent;
}
#wb_CssMenu1 ul
{
   list-style-type: none;
   margin: 0;
   padding: 0;
   position: relative;
   display: inline-block;
}
#wb_CssMenu1 li
{
   float: left;
   margin: 0;
   padding: 0px 10px 0px 0px;
   width: 100px;
}
#wb_CssMenu1 a
{
   display: block;
   float: left;
   color: #FFFFFF;
   border: 0px #C0C0C0 none;
   background-color: #02A681;
   background-image: none;
   font-family: Arial;
   font-size: 16px;
   font-weight: normal;
   font-style: normal;
   text-decoration: none;
   width: 88px;
   height: 33px;
   padding: 0px 5px 0px 5px;
   vertical-align: middle;
   line-height: 33px;
   text-align: center;
}
#wb_CssMenu1 li:hover a, #wb_CssMenu1 a:hover
{
   color: #2E8B57;
   background-color: #A1FEE8;
   background-image: none;
   border: 1px #C0C0C0 none;
}
#wb_CssMenu1 li.firstmain
{
   padding-left: 0px;
}
#wb_CssMenu1 li.lastmain
{
   padding-right: 0px;
}
#wb_CssMenu1 br
{
   clear: both;
   font-size: 1px;
   height: 0;
   line-height: 0px;
}
</style>
<style type="text/css">
table.altrowstable {
	font-family: verdana,arial,sans-serif;
	font-size: 18px;
	color: #FFFFFF;
	border-width: 1px;
	border-color: #FFFFFF;
	border-collapse: collapse;
}
table.altrowstable th {
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #FFFFFF;
}
table.altrowstable td {
	border-width: 1px;
	padding: 8px;
	border-style: solid;
	border-color: #FFFFFF;
	font-size: 16px;
	color: #000;
}
.oddrowcolor{
	background-color:#D4E1DF;
}
.evenrowcolor{
	background-color:#B2C2D1;
}
</style>
</head>
<body>
<div id="container">
<div id="wb_Image1" style="position:absolute;left:0px;top:0px;width:960px;height:149px;z-index:0;">
<img src="images/header.png" id="Image1" alt="" style="width:960px;height:149px;"></div>
<div id="wb_CssMenu1" style="position:absolute;left:257px;top:156px;width:440px;height:35px;text-align:center;z-index:1;">
<ul>
<li class="firstmain"><a href="./index.php" target="_self">Home</a>
</li>
<li><a href="#" target="_self">Help</a>
</li>
<li><a href="#" target="_self">Download</a>
</li>
<li><a href="#" target="_self">Contact</a>
</li>
</ul>
<br>
</div>
<div id="Html1" style="position:absolute;left:0px;top:232px;width:960px;height:369px;z-index:2">
<?php
$results = $_SESSION['Results'];
echo $results;
?></div>
</div>
</body>
</html>