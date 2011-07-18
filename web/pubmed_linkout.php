<?php
// Turn off all error reporting
error_reporting(0);

$lang = 'pt';
if(isset($_REQUEST['lang'])){
	if(preg_match("/en|pt|es/",$_REQUEST['lang'])){
		$lang = $_REQUEST['lang'];
	}
}else if(isset($_COOKIE['clientLanguage'])){
	if(preg_match("/en|pt|es/",$_COOKIE['clientLanguage'])){
		$lang = $_COOKIE['clientLanguage'];
	}
}

$trans = parse_ini_file("languages/$lang/texts.ini");

if ($lang == 'pt'){
	$langOneLetter = "p";
}else if ($lang == 'es'){
	$langOneLetter = "e";
}else{
	$langOneLetter = "i";
}

$pmid = $_REQUEST['pmid'];

$linkout_url = "http://eutils.ncbi.nlm.nih.gov/entrez/eutils/elink.fcgi?dbfrom=pubmed&id=" . $pmid ."&cmd=llinks";

$linkout_xml = @simplexml_load_file($linkout_url);

header("Content-Type: text/html charset=UTF-8");
?>

<html>
    <head>
        <title>PubMed Services</title>
        <style>
            BODY TD{
                font-size:11px;
            }
        </style>
    </head>
<body>

<?php

if(isset($_GET['debug'])){
	print($query."\n");
	print_r($decs);
}else{

    if ($linkout_xml){
        $set = $linkout_xml->LinkSet->IdUrlList->IdUrlSet;
        echo "The following resources are supplied by external providers. These providers are responsible for maintaining the links.";
        echo '<table width="400" cellspacing=0>' . "\n";
        echo "  <tr>\n";
        echo "      <th>Type</th><th>Info</th><th>Provider</th><th>Full Text</th>";
        echo "  </tr>\n";

        foreach ($set->ObjUrl as $item) {
            echo "  <tr valign='top'>\n";
            echo "      <td>" . $item->SubjectType . "</td>";
            echo "<td>";
            foreach ($item->Attribute as $attr) {
                $attr = str_replace('/', '/ ', $attr);
                echo $attr . "<br/>";
            }
            echo "</td>";            
            echo "      <td>" . $item->Provider->Name . "</td>";
            echo '      <td><a href="'. $item->Url . '" target="blank"><img src="'. $item->IconUrl . '" border="0"/></a></td>';
            echo "  </tr>\n";
            

            //echo $item->Url;
        }
        echo "</table>\n";

    }
}

echo "</body>";
echo "</html>";


?>