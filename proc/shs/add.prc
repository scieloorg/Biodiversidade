,'d8d4d999',


,'<1>BHL</1>'

    ,if v85:'Brazil' then
        '<4>bhlb</4>'
        '<999>BHL Brasil</999>'
    ,else
        '<4>bhlg</4>'
        '<999>BHL Global</999>'
    fi,
,'<2>',v901^*,'</2>'
,(if v992:'Personal' then
     if v5[1]='S' then
        ,'<10>',v992^n,'</10>',
     else
        if v5[1]='M' then
           ,'<16>',v992^n,'</16>',
        else
          ,'<23>',v992^n,'</23>',
        fi
     fi
  else
     if v5[1]='S' then
        ,'<11>',v992^n,'</11>',
     else
        if v5[1]='M' then
           ,'<17>',v992^n,'</17>',
        else
          ,'<24>',v992^n,'</24>',
        fi
     fi

  fi
 ,),
,(if p(v8) then '<8>','^u',v8,'^qpdf^yPDF^gTexto completo'
,'</8>' fi)
,'<9>a</9>'
,'<92>AUTO</92>'
,'<110>s</110>'

,if a(v40) or v40='' then
    
        ,if instr(s(v18,' ',v12),' the ')>0 then
           ,'<40>en</40>'
        ,else
            ,if instr(s(v18,' ',v12),' y ')>0 or  instr(s(v18,' ',v12),' los ')>0 then
               ,'<40>es</40>'
            ,else
                ,if instr(s(v18,' ',v12),' und ')>0 or instr(s(v18,' ',v12),' die ')>0  or  instr(s(v18,' ',v12),' der ')>0 then
                   ,'<40>de</40>'
                ,else
                    ,if instr(s(v18,' ',v12),' e ')>0 or instr(s(v18,' ',v12),' as ')>0  or  instr(s(v18,' ',v12),' os ')>0 then
                       ,'<40>pt</40>'
                    ,else
                        ,if instr(s(v18,' ',v12),' i ')>0 or instr(s(v18,' ',v12),' gli ')>0   then
                           ,'<40>it</40>'
                        ,else
                            ,if instr(s(v18,' ',v12),' les ')>0 or instr(s(v18,' ',v12),' aux ')>0 or instr(s(v18,' ',v12),' le ')>0 then
                               ,'<40>fr</40>'
                            ,fi
                        ,fi
                    ,fi

                ,fi

            ,fi

        ,fi

   
,fi