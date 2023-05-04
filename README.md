# Abschlussprojekt Ev3 Lego Roboter

Für dieses Projekt braucht es:
1. Ev3 Lego Roboter Core set
2. Ultraschallsensor 
3. Farb- oder Lichtsensor

In diesem Abschlussprojekt ging es darum einen Lego Roboter zu programmieren, welcher einen anderen Roboter aus einem Kreis schieben soll, aber selber dabei nicht aus dem Kreis gedrängt oder rausfahren soll.

Der Lego-Roboter soll mit dem Ultraschallsensort erkennen, wo und wie weit der Gegenspielende Roboter sich aufhält. Wenn der gengnerische Roboter entdeckt wurde soll der eigene Roboter diesem schnell hinterherfahren und versuchen aus dem Kreis zu drängen. Das ist sozusagen der Angriff des Roboters.

Damit der Roboter aber nicht verliert braucht es noch ein Nebenprogramm, welches ihm verbietet nicht die schwarze Linie zu übertreten. Dafür wurde ein Farbsensor verwendet. Wenn der Farbwert unter 500 geht soll der Roboter sich nach hinten bewegen und anschliessend sich nach rechts drehen, weiterfahren und dann wieder den Gegnerischen Roboter finden. Um das Angriffsmanöver zu starten.

Dabei wurde versucht ein Threading hinzubekommen, dass zwei Befehle gleichzeitig ablaufen jedoch hat das nicht geklappt, weshalb es nun mit zwei "if" verbunden wurde. Zuerst soll der Roboter schauen ob er auf der schwarzen Linie ist, wenn ja soll er das Manöver starten, falls nein geht es zum nächsten "if" welches den Abstand zum nächsten Objekt misst und wenn dieser Wert unter 255 ist dann soll er in diese Richtung fahren. Ansonsten fährt er immer geradeaus. Dieses Programm wiederholt sich bis eines der "If" ausgeführt wird. 

Nachdem läuft es wieder in die Repeatschleife und geht ständig durch das Programm
