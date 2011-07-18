<?php
session_start();
require("classes/Bookmark.php");

$action = $_REQUEST['action'];

$id = 0;
if(!strpos($_REQUEST['id'],'|')){
	$id = $_REQUEST['id'];
}else{
	$id = explode('|',$_REQUEST['id']);
	array_pop($id);
}

//die(var_dump($id));

if( !isset($_SESSION["bookmark"])){
	$bm = new ArrayList();
	$_SESSION["bookmark"] = serialize($bm);
}

$bookmark = unserialize($_SESSION["bookmark"]);
//$bookmark = new Bookmark();

switch($action){
	case 'a': if(is_array($id)){
			      foreach($id as $i){
			      	$bookmark->addElement($i);
			      }
			  }else{
		      	$bookmark->addElement($id);
			  }
			  break;
	case 'r': if(is_array($id)){
			      foreach($id as $i){
			      	$bookmark->removeElement($i);
			      }
			  }else{
		      	$bookmark->removeElement($id);
			  }
			  break;
	case 'c': $bookmark->removeAll();
			  break;
	case 'l': $javascriptArray = $bookmark->list[0];
			  $len = sizeOf($bookmark->list);
			  for($i = 1; $i < $len; $i=$i+1){
				$javascriptArray .= ";".$bookmark->list[$i]; 
			  }
			  print $javascriptArray;
			  break;
	case 's': print(sizeOf($bookmark->list));
			  break;
}
//$bookmark2 = $bookmark;
$_SESSION["bookmark"] = serialize($bookmark);

//print_r($javascriptArray);

?>
