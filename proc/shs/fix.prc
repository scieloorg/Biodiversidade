'd4d999',

,if v1='FAPESP' then
    '<4>FAPESPBIOTA</4>'
    '<999>FAPESP BIOTA</999>'
,fi
,if v1='BHL' then
    ,if v85:'Brazil' then
        '<4>BHLB</4>'
        '<999>BHL Brasil</999>'
    ,else
        '<4>BHLG</4>'
        '<999>BHL Global</999>'
    fi,
,fi

,if a(v35) or a(v69) then
  (if v993:'ISSN' then
     '<35>',v993^i,'</35>',
   else
      if v993:'ISBN' then
        '<69>',v993^i,'</69>'
      fi
   fi)
fi,

if a(v900) then
  (
  if v910:'TitleID' then
    '<900>',v910,'</900>'
  fi
  ),

fi,

