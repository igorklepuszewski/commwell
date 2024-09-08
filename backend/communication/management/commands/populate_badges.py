from django.core.management.base import BaseCommand

from communication.models import Badge, KudosCategory

class Command(BaseCommand):
    help = 'Populates the Badge table with predefined data including categories'


    def handle(self, *args, **options):
        categories_and_badges = [
            {"name": "Star Chart Apprentice", "required_kudos": 5, "category": "Stellar Navigator Award"},
            {"name": "Nebula Explorer", "required_kudos": 25, "category": "Stellar Navigator Award"},
            {"name": "Lunar Pathfinder", "required_kudos": 75, "category": "Stellar Navigator Award"},
            {"name": "Comet Tracker", "required_kudos": 150, "category": "Stellar Navigator Award"},
            {"name": "Solar System Mapper", "required_kudos": 250, "category": "Stellar Navigator Award"},
            {"name": "Celestial Cartographer", "required_kudos": 400, "category": "Stellar Navigator Award"},
            {"name": "Wormhole Voyager", "required_kudos": 600, "category": "Stellar Navigator Award"},
            {"name": "Asteroid Belt Navigator", "required_kudos": 850, "category": "Stellar Navigator Award"},
            {"name": "Black Hole Avoider", "required_kudos": 1150, "category": "Stellar Navigator Award"},
            {"name": "Galactic Pathfinder", "required_kudos": 1500, "category": "Stellar Navigator Award"},

            {"name": "Spark of Genius", "required_kudos": 5, "category": "Cosmic Innovator"},
            {"name": "Orbital Idea Generator", "required_kudos": 25, "category": "Cosmic Innovator"},
            {"name": "Astrobiology Pioneer", "required_kudos": 75, "category": "Cosmic Innovator"},
            {"name": "Quantum Thinker", "required_kudos": 150, "category": "Cosmic Innovator"},
            {"name": "Light-Speed Innovator", "required_kudos": 250, "category": "Cosmic Innovator"},
            {"name": "Space-Time Designer", "required_kudos": 400, "category": "Cosmic Innovator"},
            {"name": "Planetary Architect", "required_kudos": 600, "category": "Cosmic Innovator"},
            {"name": "Stellar Visionary", "required_kudos": 850, "category": "Cosmic Innovator"},
            {"name": "Cosmic Problem-Solver", "required_kudos": 1150, "category": "Cosmic Innovator"},
            {"name": "Universe Shaperd", "required_kudos": 1500, "category": "Cosmic Innovator"},

            {"name": "Crew Mate", "required_kudos": 5, "category": "Galactic Team Player Tribute"},
            {"name": "Mission Support Specialist", "required_kudos": 25, "category": "Galactic Team Player Tribute"},
            {"name": "Solar System Synchronized", "required_kudos": 75, "category": "Galactic Team Player Tribute"},
            {"name": "Satellite Communicator", "required_kudos": 150, "category": "Galactic Team Player Tribute"},
            {"name": "Asteroid Field Collaborator", "required_kudos": 250, "category": "Galactic Team Player Tribute"},
            {"name": "Lunar Base Builder", "required_kudos": 400, "category": "Galactic Team Player Tribute"},
            {"name": "Starship Co-Pilot", "required_kudos": 600, "category": "Galactic Team Player Tribute"},
            {"name": "Nebula Networker", "required_kudos": 850, "category": "Galactic Team Player Tribute"},
            {"name": "Galactic Team Builder", "required_kudos": 1150, "category": "Galactic Team Player Tribute"},
            {"name": "Universal Collaborator", "required_kudos": 1500, "category": "Galactic Team Player Tribute"},

            {"name": "Cosmic Survivor", "required_kudos": 5, "category": "Mission Resilience Rocket"},
            {"name": "Nebula Storm Navigator", "required_kudos": 25, "category": "Mission Resilience Rocket"},
            {"name": "Asteroid Dodger", "required_kudos": 75, "category": "Mission Resilience Rocket"},
            {"name": "Meteor Shield Bearer", "required_kudos": 150, "category": "Mission Resilience Rocket"},
            {"name": "Black Hole Escapee", "required_kudos": 250, "category": "Mission Resilience Rocket"},
            {"name": "Supernova Resistor", "required_kudos": 400, "category": "Mission Resilience Rocket"},
            {"name": "Comet Chaser", "required_kudos": 600, "category": "Mission Resilience Rocket"},
            {"name": "Stellar Storm Survivor", "required_kudos": 850, "category": "Mission Resilience Rocket"},
            {"name": "Deep Space Adventurer", "required_kudos": 1150, "category": "Mission Resilience Rocket"},
            {"name": "Cosmic Resilience Champion", "required_kudos": 1500, "category": "Mission Resilience Rocket"},

            {"name": "Solar Smile", "required_kudos": 5, "category": "Orbit Optimist Praise"},
            {"name": "Lunar Lifter", "required_kudos": 25, "category": "Orbit Optimist Praise"},
            {"name": "Shooting Star of Positivity", "required_kudos": 75, "category": "Orbit Optimist Praise"},
            {"name": "Cosmic Cheerleader", "required_kudos": 150, "category": "Orbit Optimist Praise"},
            {"name": "Planetary Uplifter", "required_kudos": 250, "category": "Orbit Optimist Praise"},
            {"name": "Starlight Bringer", "required_kudos": 400, "category": "Orbit Optimist Praise"},
            {"name": "Nebula of Hope", "required_kudos": 600, "category": "Orbit Optimist Praise"},
            {"name": "Meteor of Motivation", "required_kudos": 850, "category": "Orbit Optimist Praise"},
            {"name": "Galaxy Glimmer", "required_kudos": 1150, "category": "Orbit Optimist Praise"},
            {"name": "Cosmic Optimism Overlord", "required_kudos": 1500, "category": "Orbit Optimist Praise"},

            {"name": "Gratitude Cadet", "required_kudos": 5, "category": "Captain of Appreciation"},
            {"name": "Thankfulness Pioneer", "required_kudos": 25, "category": "Captain of Appreciation"},
            {"name": "Solar Salute", "required_kudos": 75, "category": "Captain of Appreciation"},
            {"name": "Galactic Recognizer", "required_kudos": 150, "category": "Captain of Appreciation"},
            {"name": "Comet of Gratitude", "required_kudos": 250, "category": "Captain of Appreciation"},
            {"name": "Appreciation Astronaut", "required_kudos": 400, "category": "Captain of Appreciation"},
            {"name": "Stellar Thanker", "required_kudos": 600, "category": "Captain of Appreciation"},
            {"name": "Orbit of Recognition", "required_kudos": 850, "category": "Captain of Appreciation"},
            {"name": "Cosmic Compliment Commander", "required_kudos": 1150, "category": "Captain of Appreciation"},
            {"name": "Universal Gratitude General", "required_kudos": 1500, "category": "Captain of Appreciation"},
        ]

        for entry in categories_and_badges:
            category,_ = KudosCategory.objects.update_or_create(name=entry["category"])
            Badge.objects.update_or_create(
                name=entry['name'],
                defaults={
                    'required_kudos': entry['required_kudos'],
                    'category': category
                }
            )

        self.stdout.write(self.style.SUCCESS('Successfully populated Badge table with categories.'))
