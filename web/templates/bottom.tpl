				<div class="footer">
					<div class="powered">
						powered by <strong>iAHx-{$smarty.const.VERSION}</strong> {$texts.BVS_TITLE}
					</div>
					<div class="links">
						<a href="{$config->bvs_url}">{$texts.BACK_HOME}</a>
						|
						<a href="{$config->about_bvs_url}">{$texts.ABOUT_BVS}</a>
					</div>
				</div>
				{literal}
				<script language="JavaScript" type="text/javascript">
					if(!cookiesEnabled()){
						document.getElementById('yourSelection').style.display = 'none';
						document.getElementById('searchHistory').style.display = 'none';
						document.getElementById('mailSend').style.display = 'none';
						hideClass('div','yourSelectionCheck');
						alertBookmarkUnavailable();
					}
				</script>
				{/literal}
			</div>

		</div> <!-- div content -->

		<!-- google analytics -->
		<script type="text/javascript">
			var gaJsHost = (("https:" == document.location.protocol) ? "https://ssl." : "http://www.");
			document.write(unescape("%3Cscript src='" + gaJsHost + "google-analytics.com/ga.js' type='text/javascript'%3E%3C/script%3E"));
		</script>
		<script type="text/javascript">
			var pageTracker = _gat._getTracker("UA-624952-7");
			pageTracker._trackPageview();
		</script>
	</body>
</html>
