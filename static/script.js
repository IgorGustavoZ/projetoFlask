document.querySelector("input#arq").addEventListener("change", ()=>{
    const arquivo = document.querySelector("input#arq").files[0];
    if (!arquivo) return;

    const formData = new FormData();
    formData.append('arq', arquivo);

    fetch('/save', {
        method: 'POST',
        body: formData
    })
})
