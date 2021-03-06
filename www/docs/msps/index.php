<?php

include_once "../../includes/easyparliament/init.php";
include_once INCLUDESPATH."easyparliament/people.php";

$this_page = 'msps';

$args = array();

if (get_http_var('all')) {
	$DATA->set_page_metadata($this_page, 'title', 'All MSPs, including former ones');
	$args['all'] = true;
}

if (get_http_var('o') == 'f') {
	$args['order'] = 'first_name';
} elseif (get_http_var('o') == 'l') {
	$args['order'] = 'last_name';
} elseif (get_http_var('o') == 'c') {
	$args['order'] = 'constituency';
} elseif (get_http_var('o') == 'p') {
	$args['order'] = 'party';
}

if (get_http_var('f') != 'csv') {
	$PAGE->page_start();
	$PAGE->stripe_start();
	$format = 'html';
} else {
	$format = 'csv';
}

$PEOPLE = new PEOPLE;
$PEOPLE->display('msps', $args, $format);

if (get_http_var('f') != 'csv') {
	$PAGE->stripe_end(array(
		array('type'=>'include', 'content'=>'people'),
		array('type'=>'include', 'content'=>'msp_search')
	));
	$PAGE->page_end();
}

?>
