# Generated by Django 2.1 on 2018-11-13 12:15

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import imagekit.models.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=20, verbose_name='카테고리명')),
                ('category_image', models.ImageField(blank=True, upload_to='', verbose_name='카테고리 사진')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price_star', models.IntegerField(verbose_name='가격 만족도')),
                ('taste_star', models.IntegerField(verbose_name='맛 만족도')),
                ('clean_star', models.IntegerField(verbose_name='청결성 만족도')),
                ('dish_eaten', models.CharField(blank=True, max_length=30, null=True, verbose_name='먹은 음식')),
                ('content', models.CharField(blank=True, max_length=160, null=True, verbose_name='150자평')),
                ('food_image', imagekit.models.fields.ProcessedImageField(blank=True, null=True, upload_to='blog/%Y/%m/%d')),
                ('try_again', models.TextField(blank=True, choices=[('꼭 다시 먹는다', '꼭 다시 먹는다'), ('잘 모르겠다', '잘 모르겠다'), ('절대 안 먹는다', '절대 안 먹는다')], null=True, verbose_name='다시 먹을 지 여부')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='작성자')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(max_length=20, verbose_name='음식 종류(밥, 국, 주류...)')),
                ('name', models.CharField(max_length=20, verbose_name='음식명')),
                ('price', models.IntegerField(verbose_name='음식 가격')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Restaurant',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=12, verbose_name='음식점 이름')),
                ('phone_number', models.CharField(blank=True, max_length=17, verbose_name='음식점 전화번호')),
                ('open_to_close', models.TextField(blank=True, verbose_name='오픈 & 마감')),
                ('is_package_possible', models.TextField(blank=True, choices=[('O', 'O'), ('X', 'X'), ('-', '-')], verbose_name='포장 가능 여부')),
                ('is_delivery_possible', models.TextField(blank=True, choices=[('O', 'O'), ('X', 'X'), ('-', '-')], verbose_name='배달 가능 여부')),
                ('is_card_possible', models.TextField(blank=True, choices=[('O', 'O'), ('X', 'X'), ('-', '-')], verbose_name='카드 가능 여부')),
                ('detail', models.TextField(blank=True, verbose_name='음식점 설명')),
                ('latitude', models.CharField(max_length=20)),
                ('longitude', models.CharField(max_length=20)),
                ('register', models.DateTimeField(auto_now_add=True, verbose_name='음식점 등록일')),
                ('category', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.Category', verbose_name='카테고리')),
                ('menu', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='base_app.Menu', verbose_name='음식점 메뉴')),
            ],
            options={
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='restaurant',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='base_app.Restaurant', verbose_name='해당 가게'),
        ),
    ]
