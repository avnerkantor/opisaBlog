$(function () {
    // $.get('https://www.dropbox.com/s/5y15scipobozkcw/pisa5.csv?dl=0', function (csv) {
        // var lines = csv.split('\n');
        // console.log(csv);
    $.get('{% static "data/pisa5.csv" %}', function (csv) {
        // var chart = new Highcharts.Chart({
            $('#container').highcharts({
            chart: {
                renderTo: 'container',
                type: 'line',
                plotBackgroundImage: '{% media "ExampleBG.jpg" %}'
            },
            data: {
                csv:  csv
                // succesful: alert(csv)
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
            series: [{
                name: ["הולנד"],
                color: 'Yellow',
                marker: {
                    fillColor: 'Green'
                }
            }],
            plotOptions: {
                // series:{
                //     marker:{
                //         radius: 12
                //     }
                // },
                series: {
                    marker:{
                        radius: 2,
                        symbol: 'circle'
                    },
                    events: {
                        mouseOver: function () {
                            this.update({
                                color: '#acc74e',
                                lineWidth: 4
                            });
                        },
                        mouseOut: function () {
                            this.update({
                                color: '#9d9d9d',
                                lineWidth: 2
                            });
                        }
                    }
                }
            },
            legend: {
                enabled: false,
                layout: 'vertical',
                align: 'right',
                verticalAlign: 'middle',
                borderWidth: 0
            }
        });
    });
});