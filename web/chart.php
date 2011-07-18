<?php
include_once( 'classes/open-flash-chart.php' );

$data = $_REQUEST['d'];
$labels = $_REQUEST['l'];
$title = $_REQUEST['title'];
$type  = $_REQUEST['type'];
$sort  = $_REQUEST['sort'];

$resubmit = $PHP_SELF . "?" .  $_SERVER['QUERY_STRING'];

$g = new graph();
$g->title( $title, '{font-size: 18px; color: #A0A0A0;}' );
$g->set_inner_background( '#E3F0FD', '#CBD7E6', 90 );
$g->bg_colour = '#FFFFFF';

if ($sort == true){
	array_multisort($labels,$data);
}  

if ($type == 'line'){

	$g->set_data($data);
	$g->line_hollow( 2, 4, '#5E83BF', 'Documentos', 10 );

	$g->set_x_labels($labels);
	$g->set_x_label_style( 10, '0x000000', 0, 2 );

	$g->set_y_max( max($data) );
	$g->y_label_steps(4);

}else if ($type == 'pie'){

	$g->pie(60,'#505050','{font-size: 11px; color: #404040}');
	
	$g->pie_values( $data, $labels );
	$g->pie_slice_colours( array('#d01f3c','#356aa0','#C79810','#FFCC99','#009933','#FF99FF','#33FFFF','#CCCC99','#330033','#00CCFF','#CCCCCC','#FFCC00','#FF0033','#660000','#FFCCCC','#33FF33','#FF6633' ) );

}else{

	$bar = new bar( 95, '#5E83BF', '#424581' );
	//$bar->key( 'documentos', 10 );
	
	$bar->data = $data;
	
	// set the X axis labels
	$g->set_x_labels( $labels );
	
	//$g->set_data( $data );
	//$g->bar_sketch( 50, 6, '#99FF00', '#7030A0', '% Complete', 10 );
	// add the bar object to the graph
	//
	$g->data_sets[] = $bar;
	
	$g->set_x_max(count($labels));
	$g->set_x_min(count($labels));
	
	$g->set_x_label_style( 11, '#A0A0A0', 2 );
	$g->set_y_label_style( 11, '#A0A0A0' );
	$g->x_axis_colour( '#A0A0A0', '#FFFFFF' );
	
	//$g->set_x_legend( 'Week 1', 12, '#A0A0A0' );
	$g->y_axis_colour( '#A0A0A0', '#FFFFFF' );
	
	
	$g->set_y_min( min($data) );
	$g->set_y_max( max($data) );
	$g->y_label_steps( 2 );
}
?>

<html>
	<head>
		<title><?=$title?></title>
		<link rel="stylesheet" rev="stylesheet" href="css/chart.css" type="text/css" media="screen"/>	
	</head>
	<body>
	<ul> 
		<li class="chart_bar">
			<a href="<?=$resubmit. "&type=bar"?>"><span>Barra</span></a>
		</li>
		<li class="chart_line">
			<a href="<?=$resubmit. "&type=line"?>"><span>Linha</span></a>
		</li>
		<li class="chart_pie">
			<a href="<?=$resubmit. "&type=pie"?>"><span>Pizza</span></a>
		</li>
	</ul>


<?
$g->set_width( 630 );
$g->set_height( 430 );

$g->set_output_type('js');
echo $g->render();
?>

</body>
</html>