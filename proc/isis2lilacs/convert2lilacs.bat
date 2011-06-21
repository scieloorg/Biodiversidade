set src=%1
set dest=%2
set src2=%3


set cisis=D:\c.917173\home\scielo\www\proc\cisis1030
%cisis%\id2i %1 create=temp\bhl_brasil
%cisis%\mx temp\bhl_brasil "proc=@add.prc" "proc='a999{BHL Brasil{a91{20101105{'" "proc='s'" create=%dest% now -all

if not "@" == "@%src2%" %cisis%\id2i %src2% create=temp\bhl_global
if not "@" == "@%src2%" %cisis%\mx temp\bhl_global "proc=@add.prc" "proc='a999{BHL Global{a91{20101117{'"  "proc='s'" append=%dest% now -all

%cisis%\i2id %dest% > %dest%.id

