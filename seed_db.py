import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'musicplayer.settings')
django.setup()

from musicapp.models import Song
from django.core.files.base import ContentFile

def seed_data():
    print("Seeding database with high-quality placeholder data...")
    for i in range(1, 10):
        # Rotate through the 3 placeholder images
        img_num = ((i - 1) % 3) + 1
        img_filename = f'placeholder{img_num}.png'
        
        song, created = Song.objects.get_or_create(
            id=i,
            defaults={
                'name': f'Premium Track {i}',
                'album': f'Vibrant Vibes Vol {((i-1)//3)+1}',
                'language': 'Hindi' if i % 2 == 0 else 'English',
                'year': 2024,
                'singer': 'Antigravity AI',
            }
        )
        
        # Update images even if already exists to ensure quality
        img_path = os.path.join('media', img_filename)
        if os.path.exists(img_path):
            with open(img_path, 'rb') as f:
                song.song_img.save(f'track_img_{i}.png', ContentFile(f.read()), save=False)
        
        # Placeholder for song file
        song.song_file.save(f'track_file_{i}.mp3', ContentFile(b'dummy_audio_content'), save=False)
        song.save()
        print(f"Updated song {i} with cover {img_filename}")

if __name__ == '__main__':
    seed_data()
