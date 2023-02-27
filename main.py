import streamlit as st
import whisper

st.title('Whisper Transcription App')

audio_file = st.file_uploader('Upload Audio', type=['wav', 'mp3', 'm4a'])

# @st.cache
# def load_whisper_media():
#     model = whisper.load_model('base')
#     return model

# if st.sidebar.button('Load Whisper Model'):
#     model = load_whisper_media()
#     st.sidebar.success('Whisper Model Loaded')

model = whisper.load_model('base')
st.text('Whisper Model Loaded')

# def get_audio_file_details(file):
#     file_details = {'FileName': file.name, 'FileType': file.type, 'FileSize': file.size}
#     return file_details

if st.sidebar.button('Transcribe Audio'):
    if audio_file is not None:
        st.sidebar.success('Transcribing Audio')
        transcription = model.transcribe(audio_file.name)
        st.sidebar.success('Transcription Complete')
        st.markdown(transcription['text'])
    else:
        st.sidebar.error('Please upload an ausio file')

st.sidebar.header('Play Original Audio File')
st.sidebar.audio(audio_file)