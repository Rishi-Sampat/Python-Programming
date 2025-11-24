from pydub import AudioSegment

audio=AudioSegment.from_file(r"E:\College\Python Programming\Lab_20\file_example_WAV_1MG.wav")
audio_fade_in=audio.fade_in(3000)
audio_fade_in.export(r'E:\College\Python Programming\Lab_20\file_example_WAV_1MG.wav',format='wav')
