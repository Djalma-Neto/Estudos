// A sintaxe: R"=====(...)===== serve para possibilitar usar '' e "" sem erros
// PROGMEM é uma referencia a memoria flesh (essa String sera armazenada na memoria flesh e não na RAM)

const char MAIN_page[] PROGMEM = R"=====(
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="">
	<title>VUEJS</title>
	<meta charset="utf-8">
</head>
<body>
	<form action="teste" method="get">
		<label for="nome">Nome: </label>
		<input type="text" name="nome" placeholder="nome">

		<label for="idade">Idade: </label>
		<input type="number" name="idade" placeholder="idade">

		<label for="sexo">Sexo: </label>
		<select name="sexo">
		  <option value="Masculino">Masculino</option>
		  <option value="Feminino">Feminino</option>
		</select>

		<button type="submit">ENVIAR</button>
	</form>
</body>
</html>)=====";

const char teste[] PROGMEM = R"=====(
<!DOCTYPE html>
<html>
<head>
	<link rel="stylesheet" type="text/css" href="">
	<title>VUEJS</title>
	<meta charset="utf-8">
</head>
<body>
	<div id="app" v-if="status">{{nome}} tem {{idade}} anos e é do sexo {{sexo}}</div>

	<form action="/">
		<button type="submit">VOLTAR</button>
	</form>

	<script src="https://unpkg.com/vue"></script>
	<script >
		var app = new Vue({
			el:"#app",

			data:{
				nome:"Marcos",
				idade:"20",
				sexo:"Masculino",
				status: true,
			}

		});

	</script>
</body>
</html>)=====";