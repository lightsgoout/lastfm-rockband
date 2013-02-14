from django.core.management.base import BaseCommand, CommandError
from crawler.base import RockbandCrawler


class Command(BaseCommand):
    args = ''
    help = 'Fills local database with rockband song`s info'

    def handle(self, *args, **options):
        crawler = RockbandCrawler()
        crawler.update_db()
