function get_testcases() {
    var worklaod = document.getElementById("workload-select");

    var workloadValue = worklaod.value;
    let params = new URLSearchParams();
    params.set('workload', workloadValue);
    window.location.search = params.toString();
    //console.log(workloadValue);
}
function get_cloud() {
    var workload = document.getElementById("workload-select");
    var testcase = document.getElementById('testcase-select');
    var workloadValue = workload.value;
    var testcaseValue = testcase.value;
    let params = new URLSearchParams();
    params.set('workload', workloadValue);
    params.set('testcase', testcaseValue);
    window.location.search = params.toString();
    //console.log(workloadValue);
}

function get_microarchitecture() {
    var workload = document.getElementById("workload-select");
    var testcase = document.getElementById('testcase-select');
    var cloud = document.getElementById('cloud-select');
    var workloadValue = workload.value;
    var testcaseValue = testcase.value;
    var cloudValue = cloud.value;
    let params = new URLSearchParams();
    params.set('workload', workloadValue);
    params.set('testcase', testcaseValue);
    params.set('cloud',cloudValue);
    window.location.search = params.toString();
    // console.log(cloudValue);
}


Highcharts.chart('highchart-body', {

    title: {
        text: 'U.S Solar Employment Growth',
        align: 'left'
    },


    yAxis: {
        title: {
            text: 'Number of Employees'
        }
    },

    xAxis: {
        accessibility: {
            rangeDescription: 'Range: 2010 to 2020'
        }
    },

    legend: {
        layout: 'vertical',
        align: 'right',
        verticalAlign: 'middle'
    },

    plotOptions: {
        series: {
            label: {
                connectorAllowed: false
            },
            pointStart: 2010
        }
    },

    series: [{
        name: 'Installation & Developers',
        data: [43934, 48656, 65165, 81827, 112143, 142383,
            171533, 165174, 155157, 161454, 154610]
    }, {
        name: 'Manufacturing',
        data: [24916, 37941, 29742, 29851, 32490, 30282,
            38121, 36885, 33726, 34243, 31050]
    }, {
        name: 'Sales & Distribution',
        data: [11744, 30000, 16005, 19771, 20185, 24377,
            32147, 30912, 29243, 29213, 25663]
    }, {
        name: 'Operations & Maintenance',
        data: [null, null, null, null, null, null, null,
            null, 11164, 11218, 10077]
    }, {
        name: 'Other',
        data: [21908, 5548, 8105, 11248, 8989, 11816, 18274,
            17300, 13053, 11906, 10073]
    }],

    responsive: {
        rules: [{
            condition: {
                maxWidth: 500
            },
            chartOptions: {
                legend: {
                    layout: 'horizontal',
                    align: 'center',
                    verticalAlign: 'bottom'
                }
            }
        }]
    }

});

var columnDefs = [
    { headerName: "Workload", field: "workload"},
    { headerName: "Testcase", field: "testcase" },
    { headerName: "Cloud", field: "cloud" },
  ];

  // specify the data
  var rowData = [
      { workload: "nginx", testcase: "Testngix1", cloud: "AWS" },
      { workload: "Casendra", testcase: "Testcasndra234", cloud: "AliCloud" },
      { workload: "Bertlarge", testcase: "TestBertlarge987", cloud: "heroku" },
  ];

  // let the grid know which columns and what data to use
  var gridOptions = {
    columnDefs: columnDefs,
    defaultColDef : {sortable : true, filter : true},
    rowData: rowData,
    rowSelection : 'multiple'
  };

  // setup the grid after the page has finished loading
  document.addEventListener("DOMContentLoaded", function () {
    var gridDiv = document.querySelector("#myagGrid");
    new agGrid.Grid(gridDiv, gridOptions);
  });