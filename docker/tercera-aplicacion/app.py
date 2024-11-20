from flask import Flask
import boto3

app = Flask(__name__)
dynamodb = boto3.resouce('dynamodb', region_name='us-east-1')
tabla = dynamodb.Table('tabla-alexanderagudelo')


@app.route('/insert', methods=['POST'])
def index():
  data = request.json
  item = {**data}

  tabla.put_item(Item=item)

  return 'Se guardó exitosamente la información'


if __name__ == '__main__':
  app.run(debug=True, host='0.0.0.0', port=5000)
