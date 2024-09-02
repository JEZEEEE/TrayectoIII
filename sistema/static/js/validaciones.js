/*function confirmar() {
    return confirm('¿Estás seguro de que deseas eliminar este usuario?');
}**/

function confirmDelete(cod_usu) {
    var confirmModal = new bootstrap.Modal(document.getElementById('confirmModal'));
    var confirmDeleteBtn = document.getElementById('confirmDeleteBtn');
    
    confirmDeleteBtn.href = '/eliminar_usuario/' + cod_usu;
    
    confirmModal.show();
}

