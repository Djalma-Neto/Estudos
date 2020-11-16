// esse arquivo pode ser JSX ou JS

function click() {
    console.log('click')
}

function Botao() {
    return (
    <button onClick={click}>Button</button>
    )
}
export default Botao