import os

from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth import get_user_model


class Command(BaseCommand):
    help = "Create or update the GalaxyCo owner account."

    def handle(self, *args, **options):
        username = os.getenv("OWNER_USERNAME")
        email = os.getenv("OWNER_EMAIL")
        password = os.getenv("OWNER_PASSWORD")

        if not username or not email or not password:
            raise CommandError(
                "OWNER_USERNAME, OWNER_EMAIL, and OWNER_PASSWORD "
                "must be set in Render Environment Variables."
            )

        User = get_user_model()

        user, created = User.objects.get_or_create(
            username=username
        )

        user.email = email
        user.is_staff = True
        user.is_superuser = True

        if created or not user.has_usable_password():
            user.set_password(password)

        user.save()

        self.stdout.write(
            self.style.SUCCESS(
                f"Owner account ready: {username}"
            )
        )