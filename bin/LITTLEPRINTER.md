Little Printer
==

Note the part where we remove all the `;` characters. I know, right. Who knows, really. There are a bunch of mystery characters that cause either curl or Little Printer itself to send back an `HTTP 200 OK` message and then send nothing to the printer...

	curl -X POST --data "html=`markdown RECIPE.md | tr -d '\n' | tr -d ';' `" http://remote.bergcloud.com/playground/direct_print/CODE

See also
--

* [BERG Cloud Developers: Direct Print Codes](http://remote.bergcloud.com/developers/direct_print_codes)
