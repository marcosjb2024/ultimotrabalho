document.addEventListener('DOMContentLoaded', () => {
    fetch('http://127.0.0.1:5000/doces')
        .then(response => response.json())
        .then(doces => {
            const lista = document.getElementById('doces-lista');
            doces.forEach(doce => {
                const item = document.createElement('li');
                item.textContent = `${doce.nome} - R$ ${doce.preco.toFixed(2)}`;
                lista.appendChild(item);
            });
        })
        .catch(error => console.error('Erro ao buscar doces:', error));
});