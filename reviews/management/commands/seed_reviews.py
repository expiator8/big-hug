import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from reviews import models as review_models
from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates Reviews"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many reviews do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_posts = post_models.Post.objects.all()
        all_users = user_models.User.objects.all()
        seeder.add_entity(
            review_models.Review,
            number,
            {
                "user": lambda x: random.choice(all_users),
                "post": lambda x: random.choice(all_posts),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} reviews created!"))
