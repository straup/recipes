Little Printer
--

Note the part where we remove all the `;`; characters. I know, right...

	curl -X POST --data "html=`markdown RECIPE.md | tr -d '\n' | tr -d ';' `" http://remote.bergcloud.com/playground/direct_print/[CODE](http://remote.bergcloud.com/developers/direct_print_codes)
