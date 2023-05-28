# This script using ai model transcribe audio to text
This code use openai-whisper library

+ Make sure you have the ```openai-whisper``` library installed. You can install it by running
```pip install openai-whisper``` in your command prompt or terminal.
+ lace an audio file named "name.mp3" in a folder named "data" in the same directory as your Python file.
Alternatively, you can change the file path in the speech_recognition function to the location of your audio file.
+ The program will display a list of available models along with their corresponding numbers. Choose the appropriate number for the selected model and enter it.
+ If you enter a number that is not listed, the program will raise a
```KeyError``` with a message stating that the model is unsupported. In that case, you should choose another model.
+ Once you have selected a valid model, the program will start the speech recognition process using the chosen model. Wait for the process to complete.
+ After the transcription is finished, a file named 
```transcription_model.txt``` will be created in the same directory as your Python file. The 
```model``` placeholder will be replaced with the name of the selected model. This file will contain the transcribed text from the audio file.

P.S The program assumes that you have the necessary permissions to read the audio file and write the transcription file in the specified locations.