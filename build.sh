
# ls -lRm assets/img/img_films/* > uusfail.txt
node ./helpers/compile_film_pictures.js
node ./helpers/compile_article_pictures.js

cp -R assets build/assets
node ./node_modules/entu-ssg/src/serve.js ./entu-ssg.yaml full
