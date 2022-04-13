$("#reportButton").click(function(){
    $("#reportView").show();
});

document.getElementById("generateButton").addEventListener("click", displayData);
function displayData() {
  $("#reportView").hide();
  $("#downloadLink").hide();
  $("#viewReportButton").hide();
  $("#wait-message").show();

  var wrapper = document.getElementById('showStats')
  wrapper.innerHTML = "";
  var url='http://127.0.0.1:8000/api/'
  fetch(url)
  .then((results) => results.json())
  .then(function(data){
      if(Object.keys(data).length){
        $("#wait-message").hide();
        $("#downloadLink").show();
        $("#viewReportButton").show();
      }
      // View report button section
      var randCount=data["randCount"];
      const randCountObj = JSON.parse(randCount);
      var item = `
          <p>Alphabetical String: ${randCountObj.alphabetic}</p>
          <p>Real Numbers: ${randCountObj.realnumber}</p>
          <p>Ingetegers: ${randCountObj.integernumber}</p>
          <p>Alphanumerics: ${randCountObj.alphanumeric}</p>
					`
      wrapper.innerHTML += item

      // Download text file link section
      var text = data["randData"];
      var data = new Blob([text], {type: 'text/plain'});
      var url = window.URL.createObjectURL(data);
      document.getElementById('download_link').href = url;
  })
}
