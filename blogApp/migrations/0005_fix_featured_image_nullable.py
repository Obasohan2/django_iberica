from django.db import migrations
import cloudinary.models


class Migration(migrations.Migration):

    dependencies = [
        ('blogApp', '0004_alter_category_slug_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='featured_image',
            field=cloudinary.models.CloudinaryField(
                'image',
                blank=True,
                null=True
            ),
        ),
    ]
