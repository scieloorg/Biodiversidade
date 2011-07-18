<?php
/*
*     Smarty plugin
* -------------------------------------------------------------
* File:     	function.ou.php
* Type:     	function
* Name:     	ou
* Description: This TAG renders an Organizational Unit.
*
* -------------------------------------------------------------
* @license GNU Public License (GPL)
*
* -------------------------------------------------------------
* Parameter:
* - element     	= the element containing the OU data.
* - class
* -------------------------------------------------------------
* Example usage:
*
* <div>{ou element=$doc->inst_data_struc class=unit}</div>
*/

function smarty_function_ou($params, &$smarty)
{
  $output = "";
  $element = $params['element'];
  $text_transform = $params['text_transform'];

  if (!isset($element) || $element == '' || count($element) == 0 )
  {
    return;
  }

  $element = json_decode($params['element']);

  if ( isset($params['label']) )
  {
    $labels = $params['label'];
  }

  if ( isset($params['class']) )
  {
    $output .= "<div class=\"". $params['class'] ."\">\n";
  }



  if ( isset($params['span']) )
  {
    $output .= "<span>";
  }

  if (is_array($element))
  {
    $output .= '<h4>' . $labels['LABEL_OU'] . '</h4>';

    foreach($element as $i => $ou)
    {

      $preOut  = '<div class="inst_ou">';
      $preOut .=   '<div class="inst_ou_name"><a href="#">';
      $preOut .= $ou->name;
      if($ou->description){
         $preOut .= ' - ' . $ou->description;
      }
      $preOut .=   '</a></div>';
      $preOut .=   '<div class="inst_ou_data">';
        $preOut .=   '<div class="inst_phone">'. $labels['LABEL_PHONE'] . ': ' . $ou->phone_number . '</div>';
        $preOut .=   '<div class="inst_fax">'. $labels['LABEL_FAX'] . ': ' . $ou->fax_number . '</div>';
        $preOut .=   '<div class="inst_email">'. $labels['LABEL_EMAIL'] . ': ' . $ou->email_address . '</div>';
        $preOut .=   '<div class="inst_site">'. $labels['LABEL_WEBSITE'] . ': ' . $ou->web_site . '</div>';
        foreach($ou->contacts as $j => $contact)
        {
          $preOut .= '<div class="inst_contact">';
          $preOut .=   '<div class="inst_name">' . $contact->name . '</div>';
          $preOut .=   '<div class="inst_function">'. $labels['LABEL_FUNCTION'] . ': ' . $contact->function . '</div>';
          $preOut .=   '<div class="inst_phone">'. $labels['LABEL_PHONE'] . ': ' . $contact->phone_number . '</div>';
          $preOut .=   '<div class="inst_mobile">'. $labels['LABEL_MOBILE'] . ': ' . $contact->cel_number . '</div>';
          $preOut .=   '<div class="inst_email">'. $labels['LABEL_EMAIL'] . ': ' . $contact->email_address . '</div>';
          $preOut .= '</div>';
        }
      $preOut .= '</div>';
      $preOut .= '</div>';
      $output .= $preOut;
    }
  }

  if ( isset($params['span']) )
  {
    $output .= "</span>";
  }

  if ( isset($params['class']) )
  {
    $output .= "</div>\n";
  }

  // $output .= '</fieldset>';

  return $output;
}

?>

