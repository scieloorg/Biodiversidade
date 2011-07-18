<?php

class ArrayList{
	
	var $list = Array();

	
	/**
	 * Adiciona um elemento a lista existente
	 * @param String $id
	 */
	function addElement($id){
		$this->list[] = $id;
		$this->list = array_unique($this->list);
	}
	
	/**
	 * Remove um elemento da lista
	 * @param String $id
	 */
	function removeElement($id){
        $temparray = array();
        foreach ($this->list as $value) {
        	if(strcmp($id,$value) != 0){
            	$temparray[] = $value;
        	}
        }
        $this->list = $temparray;
	}
	
	/**
	 * Remove todos bookmarks
	 */
	function removeAll(){
		$this->list = array();
	}
}
?>