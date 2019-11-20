$(document).ready(function(){

    //change text
    function likeButtonText(btn, count, text){
    btn.text(count + " " + text)
    }
    // Add/ Remove likes
    $(".like-button").click(function(e){
    e.preventDefault()
    var likeBtn = $(".like-button")
    var likeUrl = likeBtn.attr("data-href")
    var likeTotal = parseInt(likeBtn.attr("data-likes"))
    var img = $("#liked")
    $.ajax({
      url: likeUrl,
      method: "GET",
      data: {},
      success: function(data){
        switch(data.liked){
         case true:
            likeButtonText(likeBtn, data.total, "Unlike")
            img.attr("src", "{% static 'img/button.png'%} ")
            break;
         case false:
            likeButtonText(likeBtn, data.total, "Like")
            img.attr("src", "{% static 'img/liked.png'%} ")
            break;
        }
      }
    });
  });
});
