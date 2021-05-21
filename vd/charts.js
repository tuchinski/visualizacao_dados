Highcharts.chart('container', {
    chart: {
        type: 'area'
    },
    accessibility: {
        description: ''
    },
    title: {
        text: 'Crimes de Ódio em Nova York'
    },
    xAxis: {
    		title: {
            text: 'Meses que ocorreram os crimes'
        },
        allowDecimals: false,
        labels: {
            formatter: function () {
                return this.value; // clean, unformatted number for year
            }
        },
        accessibility: {
            rangeDescription: 'Range: 01 to 12.'
        }
    },
    yAxis: {
        title: {
            text: 'Quantidade Total de Crimes'
        },
        labels: {
            formatter: function () {
                return this.value;
            }
        }
    },
    
    
    tooltip: {
        pointFormat: 'Crime:{series.name} <br/> Quantidade: {point.y:,.0f}<br/> Mês: {point.x}'
    },
    plotOptions: {
        area: {
            pointStart: 01,
            marker: {
                enabled: false,
                symbol: 'circle',
                radius: 3,
                states: {
                    hover: {
                        enabled: true
                    }
                }
            }
        }
    },
    series: [
        {
            name: "Age",
            data: [
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0,
                0,
                0
            ]
        },
        {
            name: "Disability",
            data: [
                0,
                0,
                0,
                0,
                0,
                0,
                1,
                0,
                0,
                0,
                0,
                0
            ]
        },
        {
            name: "Ethnicity/National Origin/Ancestry",
            data: [
                1,
                3,
                7,
                1,
                1,
                3,
                1,
                2,
                2,
                3,
                3,
                3
            ]
        },
        {
            name: "Gender",
            data: [
                5,
                2,
                1,
                1,
                4,
                5,
                2,
                3,
                0,
                1,
                4,
                7
            ]
        },
        {
            name: "Race/Color",
            data: [
                15,
                22,
                73,
                9,
                5,
                12,
                16,
                22,
                8,
                10,
                5,
                10
            ]
        },
        {
            name: "Religion/Religious Practice",
            data: [
                57,
                49,
                56,
                21,
                35,
                28,
                24,
                32,
                27,
                46,
                33,
                43
            ]
        },
        {
            name: "Sexual Orientation",
            data: [
                7,
                10,
                7,
                8,
                7,
                7,
                14,
                6,
                15,
                11,
                8,
                7
            ]
        }
    ]
    
});