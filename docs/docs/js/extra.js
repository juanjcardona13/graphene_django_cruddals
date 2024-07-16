

function removeAsterisk() {
  const asterisk = document.querySelectorAll('.ge');
  asterisk.forEach(function (el) {
    el.innerHTML = el.innerHTML.replace(/\*/g, '');
  });
}

removeAsterisk();