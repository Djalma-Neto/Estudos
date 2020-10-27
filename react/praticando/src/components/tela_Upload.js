// esse arquivo pode ser JSX ou JS

function Up(props) {
    return (
        <div class="card">
            <div class="card-body">
                <p>Fazer Upload de musicas</p>
                <form>
                    <label for="nome">NOME: </label>
                    <input type="text" name="nome" />
                </form>
                <div class="modal-footer">
                    {props.children}
                </div>
            </div>
      </div>
    )
}
export default Up