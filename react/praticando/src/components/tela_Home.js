
function render(props){
    return (
        <div class="card">
            <div>
                <p class="">TESTE DE TELA HOME</p>
            </div>
            <div class="modal-footer">
                {props.children}
            </div>
        </div>
    )
}

export default render