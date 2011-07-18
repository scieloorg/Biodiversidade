<?php /* Smarty version 2.6.19, created on 2010-11-10 07:43:43
         compiled from bottom.tpl */ ?>
				<div class="footer">
					<div class="powered">
						powered by <strong>iAHx-<?php echo @VERSION; ?>
</strong> <?php echo $this->_tpl_vars['texts']['BVS_TITLE']; ?>

					</div>
					<div class="links">
						<a href="<?php echo $this->_tpl_vars['config']->bvs_url; ?>
"><?php echo $this->_tpl_vars['texts']['BACK_HOME']; ?>
</a>
						|
						<a href="<?php echo $this->_tpl_vars['config']->about_bvs_url; ?>
"><?php echo $this->_tpl_vars['texts']['ABOUT_BVS']; ?>
</a>
					</div>
				</div>
				<?php echo '
				<script language="JavaScript" type="text/javascript">
					if(!cookiesEnabled()){
						document.getElementById(\'yourSelection\').style.display = \'none\';
						document.getElementById(\'searchHistory\').style.display = \'none\';
						document.getElementById(\'mailSend\').style.display = \'none\';
						hideClass(\'div\',\'yourSelectionCheck\');
						alertBookmarkUnavailable();
					}
				</script>
				'; ?>

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