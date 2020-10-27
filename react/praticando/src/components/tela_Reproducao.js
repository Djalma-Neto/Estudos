// esse arquivo pode ser JSX ou JS

function Listar(props) {
    return (
        <div class="card">
            <h2 class="card-title">Musicas</h2>
            <p class="card-text">Reprodutor de MP3</p>
            <div class="modal-footer">
                {props.children}
            </div>
      </div>
    )
}
export default Listar