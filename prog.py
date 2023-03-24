from flask import Flask, url_for

app = Flask(__name__)


@app.route('/')
@app.route('/carousel ')
def carousel ():
    return """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Фото животных</title>
    <link crossorigin="anonymous" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css"
          integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" rel="stylesheet">
</head>
<body>
<h3 align="center">Зверушки</h3>
<div id="carouselExampleSlidesOnly" class="carousel slide" data-bs-ride="carousel">
  <div class="carousel-inner">
    <div class="carousel-item active">
      <img src="/static/img/mimi_mishka.jpg" class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="carousel-item">
      <img src="/static/img/enot.jpg" class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась">
    </div>
    <div class="carousel-item">
      <img src="/static/img/zaika.jpg" class="d-block w-100" alt="здесь должна была быть картинка, но не нашлась">
    </div>
  </div>
</div>"""

if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')