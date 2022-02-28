
function openBar(){
  document.getElementById('sideBar').style.width = '100%'
  document.body.style.overflow = "hidden"
  document.getElementById('sidebar-background').style.visibility = 'visible'
  document.getElementById('sidebar-background').style.opacity = '0.7'
  
}

function closeBar(){
  document.getElementById('sideBar').style.width = '0'
  document.body.style.overflow = "auto"
  
  document.getElementById('sidebar-background').style.opacity = '0'
  setTimeout(function(){
    document.getElementById('sidebar-background').style.visibility = 'hidden'
  }, 1000)
}

