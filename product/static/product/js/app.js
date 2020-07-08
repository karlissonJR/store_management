window.onload = function() {
    replaceAllComma()
}

function replaceAllComma() {
    priceValue = document.querySelector('#id_price').value
    newValue = priceValue.split(',').join('.')
    document.querySelector('#id_price').value = newValue
}