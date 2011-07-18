<?php

$page_top =
'<a href="'. $config->bvs_url .'">' .
'    <h1>'. $texts['TITLE'] .'</h1>'  .
'</a>' .
$texts['SEND_BY'] . ' ' . $senderName . '  [' . $senderMail .']' .
'<hr/>';

if (isset($comments) && $comments  != ''){
    $page_top .= $texts['MAIL_COMMENT'] . "<br/>" . $comments . '<hr/>';
}
?>
