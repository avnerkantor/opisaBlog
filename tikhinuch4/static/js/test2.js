jQuery(document).ready(function() {

            var options = {
                chart: {
                    renderTo: 'container',
                type: 'line'
                },
                colors: ["grey"],
            title: {
                text: 'הישגים במתמטיקה',
                x: -20 //center
            },
            subtitle: {
                text: 'מקור: מבחני פיז"ה',
                x: -20
            },
            xAxis: {
                tickPositions: [2006, 2009, 2012],
                // crosshair: true,
                title: {
                    text: 'שנת מבחן'
                }
            },
                            yAxis: [
                //     {
                //     gridLineWidth: 0,
                //     min: 0,
                //     max: 800,
                //     tickInterval: 100,
                //     lineWidth: 1,
                //     labels: {
                //         format: '{value}',
                //         style: {
                //             color: Highcharts.getOptions().colors[2]
                //         }
                //     },
                //
                //     crosshair: true,
                //     title: {
                //         text: 'ממוצע נקודות',
                //         style: {
                //             color: Highcharts.getOptions().colors[0]
                //         }
                //     },
                //     plotLines: [{
                //         value: 0,
                //         width: 1,
                //         color: '#808080'
                //     }]
                // },
                { // Secondary yAxis
                    gridLineWidth: 1,
                    // min: 200,
                    // max: 800,
                    lineWidth: 1,
                    gridLineDashStyle: 'Dash',
                    opposite: true,
                    tickPositions: [200, 358, 420, 482, 545, 607, 669, 800],
                    // min: 0,
                    // max: 800,
                    title: {
                        text: 'רמות בקיאות',
                        style: {
                            color: Highcharts.getOptions().colors[0]
                        }
                    },
                    plotLines: [{
                        value: 0,
                        width: 1,
                        color: '#808080'
                    }],
                    labels: {
                        format: '{value}',
                        style: {
                            color: Highcharts.getOptions().colors[0]
                        }
                    }
                }],
            tooltip: {
                shared: false
            },
                series: []
            };
            // JQuery function to process the csv data
            $.get('..tikhinuch4/static/data/pisa5.csv', function(data) {
                // Split the lines
                var lines = data.split('\n');
                $.each(lines, function(lineNo, line) {
                    var items = line.split(',');

                    // header line contains names of categories
                    if (lineNo == 0) {
                        $.each(items, function(itemNo, item) {
                            //skip first item of first line
                            if (itemNo > 0) options.xAxis.categories.push(item);
                        });
                    }

                    // the rest of the lines contain data with their name in the first position
                    else {
                        var series = {
                            data: []
                        };
                        $.each(items, function(itemNo, item) {
                            if (itemNo == 0) {
                                series.name = item;
                            } else {
                                series.data.push(parseFloat(item));
                            }
                        });

                        options.series.push(series);

                    }

                });
                //putting all together and create the chart
                var chart = new Highcharts.Chart(options);
            });

        });