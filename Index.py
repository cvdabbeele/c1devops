
def handler(event, context):
    print("EVENT: %s" % (event,))
    content = ""

    if event.get("queryStringParameters") and 'file' in event["queryStringParameters"]:
        filename = event["queryStringParameters"]['file']
        try:
            with open(filename, 'r') as f:
                content = f.read()
                content = content.replace('\0', '\n')
        except BaseException:
            return _403()

    BODY = """<!DOCTYPE html>
    <html>
    <head>
      <title>Hello World</title>
    </head>
    <body>
      <h3>Hello World </h3>

      <form method="POST" action="" enctype="multipart/form-data">
        <input type="text" name="hello"/>
        <input type="file" name="content" />
        <input type="submit" />
      </form>

      <pre>%s</pre>
    </body>
    """ % content

    return {
        'statusCode': 200,
        'headers': {
            'Content-Type': 'text/html; charset=utf8'
        },
        'isBase64Encoded': False,
        'body': BODY,
    }


def _403():
    return {
        'statusCode': 403,
        'headers': {
        },
        'isBase64Encoded': False,
        'body': 'Blocked',
    }
