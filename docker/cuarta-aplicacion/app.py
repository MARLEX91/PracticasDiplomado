import boto3
from flask import Flask, request, jsonify, send_file
import json
import os

app = Flask(__name__)

@app.route('/voice', methods=['POST'])
def voice():
  try:
    data = request.json
    text = data.get('text')
    voice = 'Mia'
    output_format = 'mp3'
    
    if not text:
      return jsonify({'error':'No se recibió el texto'}), 400

    polly = boto3.client('polly',  region_name='us-east-1')

    response = polly.synth_speech(
      Text=text,
      OutputFormat=output_format,
      VoiceId=voice
    )
    audiofile = 'output.mp3'
    with open(audiofile, 'wb') as file:
      file.write(response['AudioStream'].read())

    return send_file(audiofile, mimetype='audio/mpeg')

  except Exception as e:
    return jsonify({'error': str(e)}), 500
  