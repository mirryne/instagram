var keyword = document.createElement('input');
keyword.setAttribute('type', 'text');
keyword.setAttribute('id', 'keyword');
keyword.setAttribute('placeholder', 'keyword');
document.body.appendChild(keyword);
var button = document.createElement('button');
button.innerHTML = 'search';
button.setAttribute('onclick', 'search()');
document.body.appendChild(button);
var result = document.createElement('div');
result.setAttribute('id', 'result');
document.body.appendChild(result);
function search() {
  var keyword = document.getElementById('keyword').value;
  var url = 'https://www.google.com/search?q=' + keyword;
  var xhr = new XMLHttpRequest();
  xhr.open('GET', url, true);
  xhr.onreadystatechange = function() {
    if (xhr.readyState == 4) {
      var html = xhr.responseText;
      var parser = new DOMParser();
      var doc = parser.parseFromString(html, 'text/html');
      var result = document.getElementById('result');
      result.innerHTML = '';
      var items = doc.querySelectorAll('div.g');
      for (var i = 0; i < items.length; i++) {
        var item = items[i];
        var title = item.querySelector('h3.r').innerText;
        var link = item.querySelector('a').href;
        var desc = item.querySelector('span.st').innerText;
        var div = document.createElement('div');
        div.innerHTML = '<a href="' + link + '">' + title + '</a><br>' + desc;
        result.appendChild(div);
      }
    }
  };
  xhr.send();
}