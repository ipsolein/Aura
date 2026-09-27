document.querySelectorAll('[data-model]').forEach(btn=>{
  btn.addEventListener('click',()=>alert(`${btn.dataset.model} — model page coming soon.`));
});

