Modify the lambda function from [Hands-on](lesson13.md) task from lesson 13 to process png and jpg images uploaded to `name-surname-upload` bucket. The function should add text overlay saying `Modified by Lambda`. Bonus points for using a custom font and setting the text color to white with black outline.

<details><summary>Solution</summary>

```python
import boto3

from io import BytesIO
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
from urllib.parse import unquote_plus


def lambda_handler(event, context):
    s3 = boto3.client('s3')
    store_bucket = 'armen-manukyan-store'
    upload_bucket = event['Records'][0]['s3']['bucket']['name']
    key = unquote_plus(event['Records'][0]['s3']['object']['key'])

    extension = key.split('.')[-1].lower()
    format_map = {
        'jpeg': 'jpeg',
        'jpg': 'jpeg',
        'png': 'png',
    }
    if extension not in format_map.keys():
        return 'not an image'
    file_name = key.split('/')[-1]

    s3_obj = s3.get_object(Bucket=upload_bucket, Key=key)
    img = Image.open(s3_obj['Body'])
    drawer = ImageDraw.Draw(img)

    text = "Modified by Lambda"
    font_size = int(img.height / 20)
    font_stroke = int(font_size / 10) + 1
    font = ImageFont.truetype(
        font='fonts/Anton-Regular.ttf',  # https://fonts.google.com/specimen/Anton
        size=font_size,
    )
    text_w, text_h = drawer.textsize(text, font)
    text_pos = (
        (img.width - text_w) / 2,
        img.height - text_h - (img.height / 100),
    )
    drawer.text(
        xy=text_pos,
        text=text,
        font=font,
        stroke_width=font_stroke,
        stroke_fill=(0, 0, 0),
    )

    file_content = BytesIO()
    img.save(file_content, format=format_map[extension])
    s3.put_object(
        Bucket=store_bucket,
        Key=f'processed/{file_name}',
        Body=file_content.getvalue(),
    )

    s3.delete_object(Bucket=upload_bucket, Key=key)

```

</details>
