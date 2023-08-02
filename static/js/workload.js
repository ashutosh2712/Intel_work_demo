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
    var gridDiv = document.querySelector("#myGrid");
    new agGrid.Grid(gridDiv, gridOptions);
  });