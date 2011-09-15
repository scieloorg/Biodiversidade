,'d8',

"proc='d1d4a1{BHL{a4{BHL_', if v85:'Brazil' then 'BRASIL', else 'GLOBAL' fi,'{a999{BHL , if v85:'Brazil' then 'BRASIL', else 'GLOBAL' fi,{a91{',s(date)*0.8,'{'"
,'<1>BHL</1>'
,'<4>BHL_',if v85:'Brazil' then 'BRASIL', else 'GLOBAL' fi,'</4>',
,'<999>BHL ',if v85:'Brazil' then 'Brasil', else 'Global' fi,'</999>',
/* ,'<2>',v900^*,mid(s('000000',v901^*),size(s('000000',v901^*))-5,6),'</2>' */
,'<2>',v900^*,s(f(100000000+val(v901^*),1,0))*1,'</2>'
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
,if a(v940) then 
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

,else
   ,'<40>'
   ,select s(v940)
       case 'English':'en'
       case 'French':'fr'
       case 'German':'de'
       case 'Portuguese':'pt'
       case 'Portugese':'pt'
       case 'Spanish':'es'
       case 'Latin':'la'
       case 'Danish':'da'
       case 'Dutch':'nl'
       case 'Multiple':'ml'
   ,endsel,
   ,'</40>',
,fi
