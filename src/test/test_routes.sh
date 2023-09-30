
test_hello()
{
  curl localhost:5000/api/global/hello
}

test_secure_hello()
{
  curl localhost:5000/api/global/secure_hello -u "ytm@ytm.com:changeit"
}

test_download_playlist()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/downloadPlaylist -d "{\"playlist_url\": \"$1\"}" --output "${DOWNLOADS_TEST_DIR}/playlist.zip" -u "ytm@ytm.com:changeit"
}

test_download_audio()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/downloadAudio -d "{\"audio_url\": \"https://www.youtube.com/watch?v=dQw4w9WgXcQ\"}" --output "${DOWNLOADS_TEST_DIR}/audio.mp3" -u "ytm@ytm.com:changeit"
}

test_upload_audio()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/uploadAudio -d "{\"audio_url\": \"https://www.youtube.com/watch?v=e9dZQelULDk\"}" -u "ytm@ytm.com:changeit"
}

test_upload_playlist()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/global/uploadPlaylist -d "{\"playlist_url\": \"$1\"}" -u "ytm@ytm.com:changeit"
}

test_login()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/user/login -d "{\"email\": \"$1\", \"password\": \"$2\"}"
}

test_signup()
{
  curl -X POST -H "Content-Type: application/json" localhost:5000/api/user/signup -d "{\"email\": \"$1\", \"password\": \"$2\"}"
}

set -e
TEST_DIR=$(dirname "$(realpath "$0")")
DOWNLOADS_TEST_DIR="${TEST_DIR}/downloads"
mkdir -p "${TEST_DIR}/downloads"

test_secure_hello
#test_hello
#test_download_playlist https://www.youtube.com/playlist?list=PLsS6gopj1BA1WYUc04ieKU2Z7cH893sQ7
test_download_playlist "https://youtu.be/3tw2P65wv5E?si=nmZ7QaRCZb5yg-MY"
test_download_audio
#test_upload_audio
#test_upload_playlist https://www.youtube.com/playlist?list=PLsS6gopj1BA1WYUc04ieKU2Z7cH893sQ7
#test_upload_playlist https://www.youtube.com/watch?v=3tw2P65wv5E&list=PLvEI0iOxif017-fv4P0ApFmzRI-vWBPvb
#test_login "ytmt@ytm.com" "changeit"
#test_signup "ytmt@ytm.com" "changeit"
