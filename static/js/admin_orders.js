"use strict";

const ordersAjax = document.querySelector('#orders-ajax');
setCommonCost();

if (ordersAjax) {
    ordersAjax.addEventListener('change', (evt) => {
        if (evt.target.tagName === 'SELECT') {
            axios.get('/admin/item_price', {
                params: {
                    pkey: evt.target.value,
                }
            }).then(response => {
                const price = evt.target.parentElement.parentElement.querySelector('.item_price');
                price.textContent = response.data;
                const cost = evt.target.parentElement.parentElement.querySelector('.item_cost');
                const inputQ = evt.target.parentElement.parentElement.querySelector('input[type="number"]');
                console.log(inputQ.value)
                if (parseInt(inputQ.value)) {
                    cost.textContent = ((+inputQ.value) * (+price.textContent)).toString();
                    setCommonCost();

                }

            }).catch(e => console.log(e))


        }

        if (evt.target.classList.contains('form-item')) {
            evt.preventDefault();
            if (evt.target.type === 'number') {
                const cost = evt.target.parentElement.parentElement.querySelector('.item_cost');
                const price = evt.target.parentElement.parentElement.querySelector('.item_price');
                if (parseInt(price.textContent)) {
                    cost.textContent = ((+evt.target.value) * (+price.textContent)).toString();
                    setCommonCost();

                }
            }
        }
    });
}


function setCommonCost() {
    const commonCost = document.querySelector('#common-cost');
    const itemsCost = document.querySelectorAll('.item_cost');
    let priceSum = 0;
    for (const commonCostElement of itemsCost) {
        if (parseInt(commonCostElement.textContent)) {
            priceSum += +commonCostElement.textContent;
        }
    }
    commonCost.textContent = priceSum.toString();

}