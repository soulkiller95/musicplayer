import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplayer.settings')
django.setup()

from musicapp.models import Song
from django.core.files.base import ContentFile

def seed_data():
    if Song.objects.count() < 7:
        print("Seeding database with dummy songs...")
        for i in range(1, 10):
            song, created = Song.objects.get_or_create(
                id=i,
                defaults={
                    'name': f'Dummy Song {i}',
                    'album': f'Dummy Album {i}',
                    'language': 'Hindi' if i % 2 == 0 else 'English',
                    'year': 2024,
                    'singer': 'Antigravity AI',
                }
            )
            if created:
                # Add dummy files if they don't exist
                # Note: In a real app we'd need actual files, but for the crash fix, 
                # just having the rows in DB is enough to prevent DoesNotExist.
                # We'll use a placeholder string for the path.
                song.song_img.save(f'dummy_img_{i}.jpg', ContentFile(b'dummy'), save=False)
                song.song_file.save(f'dummy_song_{i}.mp3', ContentFile(b'dummy'), save=False)
                song.save()
                print(f"Created song {i}")
    else:
        print("Database already has enough songs.")

if __name__ == '__main__':
    seed_data()
