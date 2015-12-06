<!DOCTYPE html>
<html >
  <head>
    <meta charset="UTF-8">
    <title>Login</title>

        <link rel="stylesheet" href="css/style.css">
  </head>

  <body>

    <hgroup>
    </hgroup>
    <form action="/login" method="post">
    <img src="http://lorempixel.com/400/200/" width="320">
      <div class="group">
        <input type="text" name="nome"><span class="highlight"></span><span class="bar"></span>
        <label>Nome</label>
      </div>
      <div class="group">
        <input type="email" name="email"><span class="highlight"></span><span class="bar"></span>
        <label>Email</label>
      </div>
      <div class="group">
        <input type="text" name="cpf"><span class="highlight"></span><span class="bar"></span>
        <label>CPF</label>
      </div>
    <button type="submit" class="button buttonBlue">Conectar
    <div class="ripples buttonRipples"><span class="ripplesCircle"></span></div>

  </button>

</form>
  <footer>
  <h1> {{message}} </h1>
  </footer>

        <script src="js/index.js"></script>

    
    
    
  </body>
</html>
