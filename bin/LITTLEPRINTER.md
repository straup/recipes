Little Printer
--

This *appears* to be truncating itself at 800 pixels. No idea, really...

	curl -X POST --data "html=`markdown RECIPE.md | tr -d '\n'`" http://remote.bergcloud.com/playground/direct_print/CODE
