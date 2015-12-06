<!doctype html>
   <head>
<title>Simple Login Form</title>
<meta charset="UTF-8" />
<link rel="stylesheet" typ="text/css" href="/css/reset.css">
<link rel="stylesheet" type="text/css" href="/css/structure.css">
</head>
<body>
<form class="box login" action="/login" method="post">

	<fieldset class="boxBody">

	  <label>Username</label>
	  <input name="nome" type="text" tabindex="1" placeholder="Digite seu nome de usuário" required>

	  <label>Password</label>
	  <input name="email" type="text" tabindex="1" placeholder="Digite sua email" required required>

	  <label>CPF</label>
	  <input name="cpf" type="text" tabindex="1" placeholder="Digite seu CPF" required required>

      <input type="submit" class="btnLogin" value="Login" tabindex="4">
      </br>
      <h1>{{ message }}</h1>

	</fieldset>

</form>
</body>
</html>