window.onload = function () {
    $('.formset_row').formset({
        addText: '<i class="fa fa-plus-square-o" aria-hidden="true"></i> добавить',
        addCssClass: 'admin-button',
        deleteText: '<i class="fa fa-trash-o" aria-hidden="true"></i>',
        deleteCssClass: 'admin-button',
        // prefix: 'orderitems',
        // removed: deleteOrderItem,
    });
}