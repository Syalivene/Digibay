function zoomImageDetail(img) {
  if (img.classList.contains('scale-150', 'z-20')) {
    img.classList.remove('scale-150', 'z-20');
    img.classList.add('scale-100');
  }
  else {
    img.classList.remove('scale-100');
    img.classList.add('scale-150', 'z-20');
  }
  document.addEventListener('click', function(event) {
    if (event.target !== img) {
      if (img.classList.contains('scale-150', 'z-20')) {
        img.classList.remove('scale-150', 'z-20');
        img.classList.add('scale-100');
      }
    }
  });
}


