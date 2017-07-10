$(function() {

  SimpleJekyllSearch({
    searchInput: document.getElementById("search-input"),
    resultsContainer: document.getElementById("results-container"),
    json: "/search.json",
    searchResultTemplate: ("<div><a href='{url}'><h3>{title}</h3></a></div>"),
    noResultsText: ("<div><h3>Não encontramos nada <i class='fa fa-meh-o'></i></h3></div>") 
  })

});
