
test_hello()
{
  curl localhost:5000/api/global/hello
}

test_download_playlist()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/downloadPlaylist -d "{\"playlist_url\": \"$1\"}" --output "${DOWNLOADS_TEST_DIR}/playlist.zip"
}

test_download_audio()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/downloadAudio -d "{\"audio_url\": \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"}" --output "${DOWNLOADS_TEST_DIR}/audio.mp3"
}

test_upload_audio()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/uploadAudio -d "{\"audio_url\": \"https://www.youtube.com/watch?v=e9dZQelULDk\"}"
}

test_upload_playlist()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/uploadPlaylist -d "{\"playlist_url\": \"$1\"}"
}

set -e
TEST_DIR=$(dirname "$(realpath "$0")")
DOWNLOADS_TEST_DIR="${TEST_DIR}/downloads"
mkdir -p "${TEST_DIR}/downloads"

test_hello
#test_download_playlist https://www.youtube.com/playlist?list=PLsS6gopj1BA1WYUc04ieKU2Z7cH893sQ7
#test_download_playlist https://youtu.be/3tw2P65wv5E?si=nmZ7QaRCZb5yg-MY
#test_download_audio
test_upload_audio
#test_upload_playlist https://www.youtube.com/playlist?list=PLsS6gopj1BA1WYUc04ieKU2Z7cH893sQ7
test_upload_playlist https://www.youtube.com/playlist?list=PLsS6gopj1BA0hCo27eqw1eB6lLK6Fu-9Z