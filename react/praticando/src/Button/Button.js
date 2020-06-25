import React from 'react';
import '.././App.css';

function Botao(obj) {
    var { nome, onClick} = obj
    return (
        <div>
            <button onClick = {onClick}>{ nome }</button>
        </div>
    )
}

export default Botao;