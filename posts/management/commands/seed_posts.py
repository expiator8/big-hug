import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from posts import models as post_models
from users import models as user_models


class Command(BaseCommand):

    help = "This command creates Post"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=2,
            type=int,
            help="How many posts do you want to create",
        )

    def handle(self, *args, **options):
        number = options.get("number", 1)
        seeder = Seed.seeder()
        all_users = user_models.User.objects.all()
        post_types = post_models.PostType.objects.all()
        seeder.add_entity(
            post_models.Post,
            number,
            {
                "writer": lambda x: random.choice(all_users),
                "post_type": lambda x: random.choice(post_types),
            },
        )
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} posts created!"))
