"use strict";
const category = document.querySelector('.ajax-category');
if (category) {
    category.addEventListener('click', evt => {
        if (evt.target.classList.contains('category-delete')) {
            evt.preventDefault();
            axios.get(`/admin/categoreis/delete/${evt.target.dataset['pk']}`)
                .then(response => {
                    category.innerHTML = response.data;
                })
                .catch(e => {
                    console.log(e)
                });

        }
    });
}
;

const users = document.querySelector('.ajax-users');
if (users) {
    users.addEventListener('click', evt => {
        if (evt.target.classList.contains('users-delete')) {
            evt.preventDefault();
            axios.get(`/admin/user_delete/${evt.target.dataset['pk']}`)
                .then(response => {
                    users.innerHTML = response.data;
                })
                .catch(e => {
                    console.log(e);
                });
        }
    });
}
;