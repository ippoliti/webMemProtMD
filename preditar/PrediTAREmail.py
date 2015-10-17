import smtplib, os
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email.Utils import COMMASPACE, formatdate
from email import Encoders

def send_mail(send_from, send_to, subject, text, files=[], server="localhost"):
    assert isinstance(send_to, list)
    assert isinstance(files, list)

    msg = MIMEMultipart()
    msg['From'] = send_from
    msg['To'] = COMMASPACE.join(send_to)
    msg['Date'] = formatdate(localtime=True)
    msg['Subject'] = subject

    msg.attach( MIMEText(text, 'html') )

    for f in files:
        part = MIMEBase('application', "octet-stream")
        part.set_payload( open(f,"rb").read() )
        Encoders.encode_base64(part)
        part.add_header('Content-Disposition', 'attachment; filename="%s"' % os.path.basename(f))
        msg.attach(part)

    smtp = smtplib.SMTP(server)
    smtp.sendmail(send_from, send_to, msg.as_string())
    smtp.close()




def CallHeader():
    Header = '''\
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Untitled Page</title>
<meta name="generator" content="WYSIWYG Web Builder 9 - http://www.wysiwygwebbuilder.com">
<style type="text/css ">
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
body
{
   margin: 0;
   padding: 0;
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
h1
{
   font-family: Arial;
   font-size: 19px;
   font-weight: bold;
   font-style: normal;
   text-decoration: none;
   color: #483D8B;
   background-color: transparent;
   margin: 0px 0px 0px 0px;
   padding: 0px 0px 0px 0px;
   display: inline;
}
</style>
<style type="text/css">
#Table1
{
}
#Table1 td
{
   padding: 1px 1px 1px 1px;
}
#Table1 td div
{
   white-space: nowrap;
}
</style>
</head>
<body>
'''
    return (Header)
    
def CallFooter():
    Footer = '''\
</table>
</body>
</html>
'''
    return (Footer)


def Print3DHeader():
    Header3D = '''\
    
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0" class="altrowstable" id="alternatecolor">
<tr>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Ligand Name</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> PDB ID for Predicted Target(s)</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:128px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Co-Crystalized Ligand</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Probability</span></div>
</th>
'''
    return (Header3D + "\n")
    
def Print2DHeader():
    Header2D = '''\
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0" class="altrowstable" id="alternatecolor">
<tr>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Ligand Name</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> UniProt ID for Predicted Target(s)</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Probability</span></div>
</th>
'''
    return (Header2D + "\n")

def PrintComboHeader():
    HeaderCombo = '''\
<table width="98%" border="0" align="center" cellpadding="0" cellspacing="0" class="altrowstable" id="alternatecolor">
<tr>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Ligand Name</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> PDB ID for Predicted Target(s)</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:128px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Co-Crystalized Ligand</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:center;vertical-align:top;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Probability</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> UniProt ID for Predicted Target(s)</span></div>
</th>
<th style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"> Probability</span></div>
</th>
'''
    return (HeaderCombo + "\n")

def TableDataGeneratorFor3D (LigName, PDBID, HetAtomID, Probabilty):
    
    x1 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ LigName+'</span></div>\n'
    x3 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"><a href="http://ligand-expo.rcsb.org/pyapps/ldHandler.py?formid=cc-index-search&target='+HetAtomID+'&operation=ccid "target="_blank">'+HetAtomID+'</a></span></div>\n'
    x2 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"><a href="http://www.rcsb.org/pdb/explore.do?structureId='+PDBID+ '"target="_blank">'+PDBID+'</a></span></div>\n'
    x4 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ Probabilty+'</span></div>\n'
    return ("<tr>\n"+x1+"</td>\n"+x2+"</td>\n"+x3+"</td>\n"+x4+"</td>\n</tr>\n\n")


def TableDataGeneratorFor2D (LigName, PDBID, Probabilty):
    x1 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ LigName+'</span></div>\n'
    x2 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"><a href="http://www.uniprot.org/uniprot/'+PDBID+ '"target="_blank">'+PDBID+'</a></span></div>\n'
    x3 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ Probabilty+'</span></div>\n'
    return ("<tr>\n"+x1+"</td>\n"+x2+"</td>\n"+x3+"</td>\n</tr>\n\n")
    
def TableDataGeneratorForCombo (LigName, PDBID, HetAtomID, Probabilty3, uni, Prob2 ):
    x1 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ LigName+'</span></div>\n'
    x3 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"><a href="http://ligand-expo.rcsb.org/pyapps/ldHandler.py?formid=cc-index-search&target='+HetAtomID+'&operation=ccid "target="_blank">'+HetAtomID+'</a></span></div>\n'
    x2 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"><a href="http://www.rcsb.org/pdb/explore.do?structureId='+PDBID+ '"target="_blank">'+PDBID+'</a></span></div>\n'
    x4 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ Probabilty3+'</span></div>\n'
    x5 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:318px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;"><a href="http://www.uniprot.org/uniprot/'+uni+ '"target="_blank">'+uni+'</a></span></div>\n'
    x6 = '<td style="background-color:transparent;border:1px #C0C0C0 solid;text-align:left;vertical-align:top;width:168px;height:24px;"><div><span style="color:#000000;font-family:Arial;font-size:13px;">'+ Prob2+'</span></div>\n'
    return ("<tr>\n"+x1+"</td>\n"+x2+"</td>\n"+x3+"</td>\n"+x4+"</td>\n"+x5+"</td>\n"+x6+"</td>\n</tr>\n\n")  
    


