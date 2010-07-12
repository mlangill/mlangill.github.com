<?php 

require_once "morganlangille.php";

$special_head = '
       <script src="http://static.simile.mit.edu/exhibit/api-2.0/exhibit-api.js" type="text/javascript"></script>
       <link rel="exhibit/data"
          href="http://edhar.genomecenter.ucdavis.edu/~mlangill/morganlangille.com/morganlangille.bib" 
          type="application/x-bibtex" />
       
       <style>
           body {
               font-family: sans-serif;
           }
           div.publication { margin-bottom: 0em; padding: 1em; border: 0px solid #ccc; }
           div.author { }
           div.title { font-weight: bold; font-size: 90%;}
	   div.journal {font-style: italic;}
       </style>
';

stdhead("Morgan Langille - Publications",4, $special_head);
?>


       <table width="100%">
           <tr valign="top">
               <td>
                       <div ex:role="collection" ex:itemTypes="Publication"></div>
                       <div ex:role="exhibit-lens" ex:itemTypes="Publication" class="publication" style="display: none">
                           <span ex:control="copy-button" style="float: right"></span>
                           <div class="title"><span ex:content=".label"></span></div>
                           <div class="journal"><span ex:content=".journal"></span>, <span ex:content=".volume"></span>: <span ex:content=".pages"></span></div>
			   <div class="author"><span ex:content=".author"></span></div>
			  
                           <!-- <p ex:content=".abstract"></p> -->
                       </div>

                       <div ex:role="exhibit-lens" ex:itemTypes="Author" class="author" style="display: none">
                           <span ex:control="copy-button" style="float: right"></span>
                           <div class="title"><span ex:content=".label"></span></div>
                           
                           <ol class="publications" ex:content="!author">
                               <li ex:content="value"></li>
                           </ol>
                       </div>
                       <div ex:role="exhibit-view"
                           ex:viewClass="Exhibit.TileView"
                           ex:orders=".pub-type, .year"
			   ex:directions="ascending, descending"
                           ex:possibleOrders=".pub-type, .author, .year, .label">
		       </div>
               </td>
               <td width="25%">
                   <div ex:role="facet" ex:expression=".pub-type" ex:height="6em"></div>
                   <div ex:role="facet" ex:expression=".author" ex:sortMode="count" ex:height="15em"></div>
                   <div ex:role="facet" ex:expression=".year" ex:sortDirection="reverse"></div>
               </td>
           </tr>
       </table>




<?php
stdfoot(0);
?>