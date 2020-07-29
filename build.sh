
# ls -lRm assets/img/pildid_proc/* > uusfail.txt
node ./helpers/compile_pictures.js
node ./node_modules/entu-ssg/src/serve.js ./entu-ssg.yaml full
