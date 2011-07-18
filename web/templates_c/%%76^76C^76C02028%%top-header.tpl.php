<?php /* Smarty version 2.6.19, created on 2010-11-10 07:43:43
         compiled from top-header.tpl */ ?>
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" 	
	"http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">

<html lang="<?php echo $this->_tpl_vars['lang']; ?>
" xmlns="http://www.w3.org/1999/xhtml" xml:lang="<?php echo $this->_tpl_vars['lang']; ?>
">
	<head>
		<title>
			<?php if ($this->_tpl_vars['detail'] == '1'): ?>
				<?php echo $this->_tpl_vars['result']->response->docs[0]->ti[0]; ?>
 [BVS]
			<?php else: ?>
				<?php echo $this->_tpl_vars['texts']['TITLE']; ?>

			<?php endif; ?>
		</title>
		
		<!-- meta-tags -->
		<meta http-equiv="Expires" content="-1" />
		<meta http-equiv="pragma" content="no-cache" />
		<meta http-equiv="Content-Type" content="text/html; charset=UTF-8" />
		<meta http-equiv="Content-Language" content="<?php echo $this->_tpl_vars['lang']; ?>
" />
		<meta name="robots" content="all" />
		
		<meta http-equiv="keywords" content="<?php echo $this->_tpl_vars['texts']['KEYWORDS']; ?>
" />
		<meta http-equiv="description" content="<?php echo $this->_tpl_vars['texts']['DESCRIPTION']; ?>
" />

		<script language="JavaScript" type="text/javascript" src="./js/functions.js"></script>
		<script language="JavaScript" type="text/javascript" src="./js/jquery.js"></script>
		<script language="JavaScript" type="text/javascript" src="./js/jquery.hoverIntent.js"></script>
		<script language="JavaScript" type="text/javascript" src="./js/jquery.cluetip.js"></script>
		<script language="JavaScript" type="text/javascript" src="./js/decs_window.js"></script>
        <script language="JavaScript" type="text/javascript" src="./js/pubmed_linkout.js"></script>
		<script language="JavaScript" type="text/javascript" src="./js/thickbox.js"></script>
		<script language="JavaScript" type="text/javascript" src="./local/functions.js"></script>
        <script language="JavaScript" type="text/javascript" src="./local/add_collection.js"></script>


		<!-- Page icon -->
		<link rel="shortcut icon" href="./image/favicon.ico">
		
		<!-- Stylesheet -->		
		<?php if ($this->_tpl_vars['printMode'] == 'true'): ?>
			<link rel="stylesheet" rev="stylesheet" href="./css/print.css" type="text/css"/>
		<?php else: ?>
			<link rel="stylesheet" rev="stylesheet" href="./css/print.css" type="text/css" media="print"/>	
			<link rel="stylesheet" rev="stylesheet" href="./css/screen.css" type="text/css" media="screen"/>
			<link rel="stylesheet" rev="stylesheet" href="./css/thickbox.css" type="text/css" media="screen"/>
			<link rel="stylesheet" rev="stylesheet" href="./css/jquery.cluetip.css" type="text/css" media="screen"/>
		<?php endif; ?>
				
		<!-- RSS -->
		<link rel="alternate" type="application/rss+xml" title="RSS" href="index.php?output=rss&site=<?php echo $this->_tpl_vars['site']; ?>
&col=<?php echo $this->_tpl_vars['col']; ?>
&lang=<?php echo $this->_tpl_vars['lang']; ?>
<?php echo $this->_tpl_vars['getParams']; ?>
"/>
		
	</head>

	<?php if ($this->_tpl_vars['printMode'] == 'true'): ?>
		<body onload="showPrintDialog()">
	<?php else: ?>
		<body>
	<?php endif; ?>
	