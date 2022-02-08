'use strict'

function basketUpdate() {
    const basket_quantity = document.querySelector('.basket_quantity');
    const quantity = document.querySelector('.quantity');
    const total_cost = document.querySelector('.total_cost');
    if (basket_quantity.dataset.quantity !== '0') {
        quantity.innerHTML = basket_quantity.dataset.quantity;
        total_cost.innerHTML = ` Всего:&nbsp;${basket_quantity.dataset.total_cost}&nbsp;&#8381`;

    } else {
        quantity.classList.toggle('visually-hidden');
        total_cost.classList.toggle('visually-hidden');
    }

}

const basket_ajax = document.querySelector('.basket_ajax')
basket_ajax.addEventListener('input', event => {
    if (event.target.classList.contains('basket_quantity')) {
        axios.get('/basket/edit', {
            params: {
                quantity: event.target.value,
                pkey: event.target.dataset.pk,
            }
        }).then(response => {
            basket_ajax.innerHTML = response.data;
            basketUpdate();

        })
    }
})

basket_ajax.addEventListener('click', event => {
    if (event.target.classList.contains('basket-remove-product')) {
        event.preventDefault();
        axios.get('/basket/remove', {
            params: {
                pkey: event.target.dataset.pk,
            }
        }).then(response => {
            basket_ajax.innerHTML = response.data;
            basketUpdate();

        })
    }
})

