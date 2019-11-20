// JS - Select Solution or Prevention Page
var btn_p = document.getElementById('prevention');
var btn_s = document.getElementById('solutions');
// Change Bkground
var menu1 = document.getElementById('menu-viewMenu');
var menu2 = document.getElementById('menu-viewMenu2');
var content = document.getElementById('about');
var prevContent = document.getElementById('prevContent');
var solContent = document.getElementById('solContent');
var close = document.getElementById('close');

// Call Methods
btn_p.addEventListener("click", prevention);
btn_s.addEventListener("click", solutions);

function load(){
  content.remove();
  document.body.scrollTop = 0; // Safari
  document.documentElement.scrollTop = 0; // Chrome, Firefox, IE
}
function prevention(){
  load()
  menu2.style.width = "100%";
  menu1.style.width = "0px";
  close.style.visibility= "visible";
  prevContent.style.display= "block";
};
function solutions(){
  load()
  menu1.style.width = "100%";
  menu2.style.width = "0px";
  close.style.visibility= "visible";
  solContent.style.display= "block";
};

// jQuery - Close Page
$('#close').click(function(){

  $('#content > div').css("visibility", "hidden");
  $('.menu div').css("width", "50%");
  $('#about').show();
  $(this).css("visibility", "hidden");
});

// Select Company to vie Info/ Donate
$('.boxes ul li a').click(function(){
  $("#companylink").show();
  var index = $(".boxes ul li a").index(this);
  title= $('.info .company .cont h2');
  info=$('.info .company .cont p');
  link=$("#companylink");
 switch(index){
  case 0:
    title.text('4 Ocean');
    info.text('"We’re here to clean the ocean and coastlines while working to stop the inflow of plastic by changing consumption habits."');
    link.attr("href","https://4ocean.com");
    break;
  case 1:
    title.text('The Ocean Cleanup');
    info.text('"The Ocean Cleanup develops advanced technologies to rid the world’s oceans of plastic. A full-scale deployment of our systems is estimated to clean up 50% of the Great Pacific Garbage Patch every five years."');
    link.attr("href","https://theoceancleanup.com");
    break;
  case 2:
    title.text('Plastic Oceans');
    info.text('"Plastic Oceans International is a nonprofit organization raising awareness about plastic pollution to inspire behavioral change."');
    link.attr("href","https://plasticoceans.org");
    break;
  case 3:
    title.text('Marine Mega Fauna Foundation');
    info.text('"Our vision is to live in a world where marine life and humans thrive together. Watch our Strategic Manifesto video to see what steps we are taking to achieve this. With your help, we can save #OurOceanOurFuture"');
    link.attr("href","https://marinemegafaunafoundation.org");
    break;
  case 4:
    title.text('Marine Conservation Society');
    info.text('"The Marine Conservation Society is the UK’s leading marine charity. We work to ensure our seas are healthy, pollution free and protected."');
    link.attr("href","https://www.mcsuk.org");
    break;
  default:
    title.text('How Can You Help?');
    info.text('Companies contributing to plastic pollution, click on the logos to find out more');
  }
});
