,'d8',
,'<1>BR1.1</1>'
,'<2>',v900^*,mid(s('000000',v901^*),size(s('000000',v901^*))-5,6),'</2>'
,'<4>BIODIVERSIDADE</4>'
,(if v992:'Personal' then
     if v5='S' then
        ,'<10>',v992^n,'</10>',
     else
        if v5='M' then
           ,'<16>',v992^n,'</16>',
        else
          ,'<23>',v992^n,'</23>',
        fi
     fi
  else
     if v5='S' then
        ,'<11>',v992^n,'</11>',
     else
        if v5='M' then
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
,'<92>FML</92>'
,'<110>s</110>'
,if a(v940) then 
,if instr(s(v18,' ',v12),' the ')>0 then
   ,'<40>En</40>' 
,else
,if instr(s(v18,' ',v12),' y ')>0 or instr(s(v18,' ',v12),' las ')>0  or instr(s(v18,' ',v12),' los ')>0 then
   ,'<40>Es</40>' 
,else
,if instr(s(v18,' ',v12),' und ')>0 or instr(s(v18,' ',v12),' die ')>0  or  instr(s(v18,' ',v12),' der ')>0 then
   ,'<40>De</40>' 
,else
,if instr(s(v18,' ',v12),' e ')>0 or instr(s(v18,' ',v12),' as ')>0  or  instr(s(v18,' ',v12),' os ')>0 then
   ,'<40>Pt</40>' 
,else
,if instr(s(v18,' ',v12),' i ')>0 or instr(s(v18,' ',v12),' gli ')>0   then
   ,'<40>It</40>' 
,else
,if instr(s(v18,' ',v12),' les ')>0 or instr(s(v18,' ',v12),' le ')>0 then
   ,'<40>Fr</40>' 
,fi
,fi

,fi

,fi

,fi

,fi

,else
   ,'<40>'
   ,select s(v940)
       case 'English':'En'
       case 'French':'Fr'
       case 'German':'De'
       case 'Portugese':'Pt'
       case 'Spanish':'Es'
       case 'Latin':'La'
       case 'Danish':'Da'
       case 'Dutch':'Nl'
       case 'Multiple':'Ml'
   ,endsel,
   ,'</40>',
,fi
