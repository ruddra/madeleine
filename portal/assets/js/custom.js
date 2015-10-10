$(document).ready(function()
{
    $("button").click(function(){
    var query = $('.madeleine_search').val();

     $.ajax(
         {
             type: "POST",
             url: '/twitter',
             data: {'query': query},
             success: function(result)
             {
             var r = jQuery.parseJSON( result );

             var resLang = r.language;
             var langDataPoints = [];
             for (var key in resLang) {
                var value = resLang[key];
                var colDict = { label: key, y: value};
                langDataPoints.push(
                colDict
             );
             }

             var resLoc = r.location;
             var locDataPoints = [];
             for (var key in resLoc) {
                var value = resLoc[key];
                var colDict = { legendText: key, indexLabel: key , y: value};
                locDataPoints.push(
                colDict
             );
             }




var options_lang = {
		title: {
			text: "Language"
		},
                animationEnabled: true,
		data: [
		{
			type: "column",
			dataPoints: langDataPoints
		}
		]
	};

var options_loc = {
		title: {
			text: "Location"
		},
                animationEnabled: true,
		data: [
		{
			type: "column",
			dataPoints: locDataPoints
		}
		]
	};


console.log(locDataPoints);
	$("#chartContainerLang").CanvasJSChart(options_lang);
//	$("#chartContainerLoc").CanvasJSChart(options_loc);


// -------

var chart = new CanvasJS.Chart("chartContainerLoc",
	{
		title:{
			text: "Location"
		},
                animationEnabled: true,
		legend:{
			verticalAlign: "bottom",
			horizontalAlign: "center"
		},
		data: [
		{
			indexLabelFontSize: 20,
			indexLabelFontFamily: "Monospace",
			indexLabelFontColor: "darkgrey",
			indexLabelLineColor: "darkgrey",
			indexLabelPlacement: "outside",
			type: "doughnut",
			showInLegend: true,
			toolTipContent: "{y} - <strong>#percent%</strong>",
			dataPoints: locDataPoints
		}
		]
	});
	chart.render();


// -------

    $('.madeleine_result').show();

             }
         });
});
});
