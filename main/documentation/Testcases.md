# Test Cases für Crypto Alarme

Wir haben verschiedene Szenarien getestet, um sicherzustellen, dass unser Crypto Alarm Bot reibungslos funktioniert und den Benutzern eine nahtlose Erfahrung bietet. Jeder Testfall umfasst eine spezifische Funktion des Bots und die erwarteten Ergebnisse, die wir anstreben. Hier sind die Testfälle im Detail:

1. **Funktionalität des !crypto help Befehls:** Wir haben die Funktionalität des !crypto help Befehls überprüft, um sicherzustellen, dass der Bot korrekt Informationen über verfügbare Befehle liefert.

2. **Auswahl einer Kryptowährung zum Verfolgen:** Wir haben getestet, ob der Bot in der Lage ist, die Auswahl einer Kryptowährung zu bestätigen und mit dem Verfolgen der ausgewählten Kryptowährung zu beginnen.

3. **Festlegung des Update-Intervalls:** Wir haben überprüft, ob der Bot in der Lage ist, das Update-Intervall gemäß den Benutzereingaben festzulegen, um regelmäßige Updates bereitzustellen.

4. **Behandlung ungültiger Befehle:** Wir haben getestet, wie der Bot mit ungültigen Befehlen umgeht und sicherstellt, dass er angemessen darauf reagiert und Benutzern bei Bedarf Hilfe anbietet.

5. **Auswahl einer nicht vorhandenen Kryptowährung:** Wir haben überprüft, wie der Bot auf den Versuch reagiert, eine Kryptowährung auszuwählen, die nicht existiert, und ob er Benutzern alternative Optionen vorschlägt.

6. **Behandlung eines ungültigen Update-Intervalls:** Wir haben getestet, wie der Bot auf ungültige Eingaben beim Festlegen des Update-Intervalls reagiert und Benutzern Anweisungen zur korrekten Formatierung bereitstellt.

7. **Auswahl einer Kryptowährung ohne Angabe:** Wir haben getestet, ob der Bot angemessen darauf reagiert, wenn der Benutzer versucht, eine Kryptowährung auszuwählen, ohne eine zu spezifizieren.

8. **Festlegung eines Update-Intervalls ohne Angabe:** Wir haben überprüft, wie der Bot reagiert, wenn der Benutzer versucht, das Update-Intervall festzulegen, ohne eine Zeitangabe zu machen.

9. **Aktualisierung der Hilfeinformationen nach Hinzufügen neuer Befehle:** Wir haben sicherstellt, dass der Bot nach dem Hinzufügen neuer Befehle die Hilfeinformationen aktualisiert und den Benutzern alle verfügbaren Optionen klar darstellt.

10. **Gewährleistung der Aktualisierung gemäß festgelegtem Intervall:** Abschließend haben wir überprüft, ob der Bot die Kryptowährungsdaten korrekt und pünktlich gemäß dem festgelegten Intervall aktualisiert.

Diese Testfälle stellen sicher, dass unser Crypto Alarm Bot zuverlässig und benutzerfreundlich ist, und bieten den Benutzern eine effektive Möglichkeit, Kryptowährungen zu verfolgen und auf dem Laufenden zu bleiben.
<br>
<br>

| Case    | What was tested                                                          | What do I expect                                                                                              | What happened                                                                                                      |
|---------|--------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------------|
| Case01  | The functionality of the !crypto help command.                          | When I input !crypto help, I expect to receive a message displaying information about available commands.      | The bot responded with a message detailing all available commands and their functionalities.                       |
| Case02  | The functionality of selecting a cryptocurrency to track.               | When I input !crypto select [currency], I expect the bot to acknowledge the selection and start tracking the specified cryptocurrency. | The bot acknowledged the selection of the specified cryptocurrency and started tracking it for updates.             |
| Case03  | The functionality of setting the update interval.                       | When I input !crypto interval [time], I expect the bot to set the update interval accordingly (e.g., 15 minutes, 1 hour). | The bot confirmed the update interval was set to the specified time and adjusted its update frequency accordingly. |
| Case04  | Handling of invalid commands.                                           | When I input a command that is not recognized (e.g., !crypto somethingrandom), I expect the bot to respond with a message indicating that the command is not valid. | The bot responded with nothing stating that the command is not recognized and provided help information on available commands. |
| Case05  | Handling of selecting a cryptocurrency that doesn't exist.              | When I input !crypto select [non-existing currency], I expect the bot to respond with a message indicating that the specified cryptocurrency does not exist. | The bot responded with a message stating that the specified cryptocurrency does not exist and provided suggestions or alternatives. |
| Case06  | Handling of setting an invalid update interval.                         | When I input !crypto interval [invalid time format], I expect the bot to respond with a message indicating that the time format is invalid and provide instructions on the correct format. | The bot responded with a message stating that the provided time format is invalid and provided instructions on the correct format. |
| Case07  | Handling of selecting a cryptocurrency without specifying one.          | When I input !crypto select without specifying a cryptocurrency, I expect the bot to respond with a message indicating that a cryptocurrency must be specified. | The bot responded with a message stating that a cryptocurrency must be specified when using the select command.       |
| Case08  | Handling of setting an update interval without specifying one.          | When I input !crypto interval without specifying a time, I expect the bot to respond with a message indicating that a time interval must be specified. | The bot responded with a message stating that a time interval must be specified when using the interval command. |
| Case09  | Ensuring !crypto help command reflects newly added commands.            | When I input !crypto help after new commands are added, I expect the bot to display help information including the newly added commands. | The bot responded with a message displaying help information, including details about the newly added commands.  |
| Case10  | Ensuring the bot updates at the specified interval.                     | After setting a long interval, I expect the bot to update the cryptocurrency data at the specified interval accurately. | The bot updated the cryptocurrency data at the specified interval of 1 day accurately, without any delays or discrepancies. |
