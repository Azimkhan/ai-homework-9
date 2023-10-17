import json

from app import classify_image


def handler(event, context):
    body = {}
    if event.get('body'):
        body = json.loads(event['body'])

    image_url = body.get(
        'imageUrl',
        'https://upload.wikimedia.org/wikipedia/commons/thumb/d/df/Smaug_par_David_Demaret.jpg/1280px'
        '-Smaug_par_David_Demaret.jpg')

    res = classify_image(image_url)
    res['imageUrl'] = image_url
    return {'statusCode': 200, 'body': json.dumps(res)}
