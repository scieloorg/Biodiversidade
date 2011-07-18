
<div class="results">
	<div class="resultSet">
	{foreach from=$result->response->docs item=doc}
			<table width="90%">
				<tr valign="top">
					<td colspan="2">
						<br/>
						<font size="4" color="#0068CF">
							<a href="{$url}resources/{$doc->id}">
								{occ element=$doc->ti separator=/}
							</a>
						</font>
					</td>
				</tr>
				<tr valign="top">
					<td width="15%">
						<b>
							{$texts.LABEL_AUTHOR}
						</b>
					</td>
					<td>
						{occ element=$doc->au separator=;}
					</td>
				</tr>
				<tr valign="top">
					<td>
						<b>
							{$texts.LABEL_SOURCE}
						</b>
					</td>
					<td>
						{occ element=$doc->fo separator=;}
					</td>
				</tr>
				{ if isset($doc->ab) }
				<tr valign="top">
					<td>
						<b>
							{$texts.LABEL_ABSTRACT}
						</b>
					</td>
					<td>
						{occ element=$doc->ab separator=<hr>}
					</td>
				</tr>
				{/if}
				<tr valign="top">
					<td>
						<b>
							{$texts.LABEL_SUBJECT}
						</b>
					</td>
					<td>
						{occ element=$doc->mh separator=;}
					</td>
				</tr>
			</table>
	{/foreach}
	</div>
</div>
