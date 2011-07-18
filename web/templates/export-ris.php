{foreach from=$result->response->docs item=doc}
{if $doc->db|@contains:"MEDLINE"}
	{assign var=refDB value=MEDLINE}
	{assign var=refID value=$doc->id|substring_after:"-"}
{else}
	{if $doc->db[0] eq 'GHL'}
		{assign var=refDB value=$doc->db[1]}
	{else}
		{assign var=refDB value=$doc->db[0]}
	{/if}
	{assign var=refID value=$doc->id}
{/if}

{if $doc->type eq 'article'}
TY  - JOUR
{/if}
{if $doc->type eq 'non-conventional'}
TY  - GEN
{/if}
{if $doc->type eq 'book'}
TY  - BOOK
{/if}
{foreach item=au from=$doc->au}
A1  - {$au}
{/foreach}
{foreach item=ti from=$doc->ti}
T1  - {$ti}
{/foreach}
DB  - {$refDB}
DP  - http://www.globalhealthlibrary.net
ID  - {$refID}
LA  - {$doc->la[0]}
{if $doc->type eq 'article' AND $doc->ta > 0}
JO  - {$doc->ta[0]}
{/if}
{if $doc->pg > 0}
{if $doc->pg[0]|contains:"-"}
SP  - {$doc->pg[0]|substring_before:"-"}
EP  - {$doc->pg[0]|substring_after:"-"}
{else}
SP  - {$doc->pg[0]}
EP  - {$doc->pg[0]}
{/if}
{/if}
{if $doc->da > 0}
PY  - {$doc->da[0]|substr:0:4}
{/if}
{foreach item=mh from=$doc->mh}
KW  - {$mh}
{/foreach}
{foreach item=ab from=$doc->ab}
N2  - {$ab}
{/foreach}
{foreach item=ur from=$doc->ur}
UR  - {$ur}
{/foreach}
ER  -

{/foreach}