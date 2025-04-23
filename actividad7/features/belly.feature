# language: es

Característica: Característica del estómago

  Escenario: comer muchos pepinos y gruñir
    Dado que he comido 42 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: comer pocos pepinos y no gruñir
    Dado que he comido 10 pepinos
    Cuando espero 2 horas
    Entonces mi estómago no debería gruñir

  Escenario: comer muchos pepinos y esperar menos de una hora
    Dado que he comido 50 pepinos
    Cuando espero media hora
    Entonces mi estómago no debería gruñir

  Escenario: comer pepinos y esperar en minutos
    Dado que he comido 30 pepinos
    Cuando espero 90 minutos
    Entonces mi estómago debería gruñir

  Escenario: comer pepinos y esperar en diferentes formatos
    Dado que he comido 25 pepinos
    Cuando espero "dos horas y treinta minutos"
    Entonces mi estómago debería gruñir

  Escenario: Comer pepinos y esperar un tiempo aleatorio
    Dado que he comido 25 pepinos
    Cuando espero un tiempo aleatorio entre 1 y 3 horas
    Entonces mi estómago debería gruñir

  Escenario: Manejar tiempos complejos
    Dado que he comido 50 pepinos
    Cuando espero "1 hora, 30 minutos y 45 segundos"
    Entonces mi estómago debería gruñir

  Escenario: Comer suficientes pepinos y esperar el tiempo adecuado
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Comer pocos pepinos y no esperar suficiente tiempo
    Dado que he comido 5 pepinos
    Cuando espero 1 hora
    Entonces mi estómago no debería gruñir

  Escenario: Saber cuántos pepinos he comido
    Dado que he comido 15 pepinos
    Entonces debería haber comido 15 pepinos

  Escenario: Comer muchos pepinos y esperar el tiempo suficiente
    Dado que he comido 15 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Predecir si mi estómago gruñirá tras comer y esperar
    Dado que he comido 12 pepinos
    Cuando espero 1.5 horas
    Entonces mi estómago debería gruñir

  Escenario: Ver cuántos pepinos puedo comer antes de que el estómago gruña
    Dado que he comido 8 pepinos
    Cuando pregunto cuántos pepinos más puedo comer
    Entonces debería decirme que puedo comer 2 pepinos más

  Escenario: Verificar que el estómago gruñe tras comer suficientes pepinos y esperar
    Dado que he comido 20 pepinos
    Cuando espero 2 horas
    Entonces mi estómago debería gruñir

  Escenario: Manejar tiempos complejos
    Dado que he comido 20 pepinos
    Cuando espero "1 hora, 10 minutos y 10 segundos"
    Entonces mi estómago no debería gruñir

  @english
  Escenario: Esperar usando horas en inglés
      Dado que he comido 50 pepinos
      Cuando espero "two hours and thirty minutes"
      Entonces mi estómago debería gruñir

  @english
  Escenario: Esperar solo 30 minutos en inglés
    Dado que he comido 25 pepinos
    Cuando espero "thirty minutes"
    Entonces mi estómago no debería gruñir


