../../bases/cisis1660/mx ../db/LILACS "pft=v2,'|',mfn/" now |sort > temp.id.lst
../../bases/cisis1660/mx seq=temp.id.lst create=temp.id now -all
../../bases/cisis1660/mx temp.id lw=999 "pft=if v1=ref(mfn+1,v1) then v2,'|',v1/ fi" now > temp.repetidos.txt
vi temp.repetidos.txt

