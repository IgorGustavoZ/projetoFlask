let val = 0

let i = 1

let preview_img = (arq)=>{
    const img_preview = document.querySelector("div#image-preview")
    const img = document.createElement("img")
    
    arq = arq.split('')

    for (ind in arq){
        if (arq[ind] != ".") arq[ind] = ""            
        else break 
    }
    
    arq = arq.join("")

    console.log(i.toString() + arq )
    // {{ url_for('static', filename='upload/exemplo-logo.png') }}
    img.src = `{{ url_for('static', filename='img/${i.toString() + arq}') }}`

    img_preview.append(img)

    i++
}

document.querySelector("input#arq").addEventListener("change", ()=>{
    const total = document.querySelector("div#totalPag")

    const ul = document.querySelector("ul")
    const li = document.createElement("li")
    li.innerHTML = "Foto para impressão 3:4"

    val += 5

    const arquivo = document.querySelector("input#arq").files[0]
    if (!arquivo) return

    const formData = new FormData()
    formData.append('arq', arquivo)

    console.log(arquivo)

    ul.appendChild(li)

    total.innerHTML = `Total : R$ ${val}` 

    fetch('/save', {
        method: 'POST',
        body: formData
    })

    preview_img(arquivo.name)
})


