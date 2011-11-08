,'d4d999d2d777d35d69',
,if size(v65)<>8 then 'd65' fi
,if v1='FAPESP' then
   ,'<2>biota-',(if v990^x='id' then v990^* fi),'</2>',
    '<4>fapespbiota</4>'
    '<999>FAPESP BIOTA</999>'

,fi
,if v1='BHL' then

    ,'<2>bhl-',v901^*,'</2>',
    ,if v85:'Brazil' then
        '<4>bhlb</4>'
        '<999>BHL Brasil</999>'
    ,else
        '<4>bhlg</4>'
        '<999>BHL Global</999>'
    fi,


,if size(v65)<>8 then
    proc('d702a702~',replace(replace(s(v31,';',(if v990^x:'/Year' then if size(v990^*)>0 then v990^* fi fi),';',v64),'-','0'),'?','0'),'~'),
    proc('d700a700~',replace(replace(replace(replace(replace(replace(replace(replace(replace(v702,'1','0'),'2','0'),'3','0'),'4','0'),'5','0'),'6','0'),'7','0'),'8','0'),'9','0'),'~'),
    ,if instr(v700,'0000')>0 then
        ,proc('d701a701~',mid(v702,instr(v700,'0000'),4),'~'),
        ,|<65>|v701|0000</65>|,'<990>^xpublicationdate v990^x,v64</990>'
    ,fi
,fi
/* ,if a(v35) or a(v69) then */
  ,(if v993^d='ISSN' then
     '<35>',v993^i,'</35>',
   else
      if v993^d='ISBN' then
        '<69>',v993^i,'</69>'
      fi
   fi),
/* fi, */
/*
,(|<35>|v35|</35>|),
,(|<69>|v69|</69>|),
*/
if a(v900) then
  (
  if v910^x='TitleID' then
    '<900>',v910,'</900>'
  fi
  ),

,fi,
,fi,
proc('d700d701d702'),
