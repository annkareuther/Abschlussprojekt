# Abschlussprojekt

In diesem Projekt wurde ein Versuch gestartet einen Ev3-Roboter zu programmieren, welcher einen anderen Roboter mit Hilfe des Ultraschallsensors sucht, ihn verfolgt, und anschliessend aus einem schwarz eigekreisten Spielfeld schiebt. Das ist sozusagen der Angriff des Roboters.
Damit der Roboter nicht verliert braucht es noch ein Nebenprogramm, welches ihm verbietet nicht die schwarze Linie zu übertreten. Dafür wurde ein Farbsensor verwendet. Wenn der Farbwert unter 500 geht soll der Roboter sich nach hinten bewegen und anschliessend sich nach rechts drehen und dann wieder den Gegnerischen Roboter finden. 

Dabei wurde versucht ein Threading hinzubekommen, dass zwei Befehle gleichzeitig ablaufen jedoch hat das nicht geklappt, weshalb es nun mit zwei "if" verbunden wurde. Zuerst soll der Roboter schauen ob er auf der schwarzen Linie ist, wenn ja soll er das Manöver starten, falls nein geht es zum nächsten "if" welches den Abstand zum nächsten Objekt misst und wenn dieser Wert unter 255 ist dann soll er in diese Richtung fahren. Ansonsten fährt er immer geradeaus.
