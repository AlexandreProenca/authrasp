<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Login</title>

        <link rel="stylesheet" href="css/style.css">
  </head>

  <body>

    <form action="/login" method="post">
    <div align="center">
    <img src="images/wifi.png" width="150">
    </div>
      <div class="group">
        <input type="text" name="nome" placeholder="Nome"><span class="highlight"></span><span class="bar"></span>

      </div>
      <div class="group">
        <input type="email" name="email" placeholder="Email"><span class="highlight"></span><span class="bar"></span>

      </div>
      <div class="group">
        <input type="text" name="cpf" placeholder="CPF" ><span class="highlight"></span><span class="bar"></span>

      </div>
    <button type="submit" class="button buttonBlue">Conectar
    <div class="ripples buttonRipples"><span class="ripplesCircle"></span></div>

  </button>

</form>
  <footer>
  <h1> {{message}} </h1>
  </footer>

  </body>
</html>
