

const testFolder = '../assets/img/pildid_proc/';
const fs = require('fs');
const yaml = require('js-yaml');
let data = new Object();

data.filmslugs = []

fs.readdirSync(testFolder).forEach(folder => {
    console.log(folder);

    filmSlug = {
        slug: folder,
        poster: '',
        pics: []
    }

    fs.readdirSync(testFolder + '/' + folder).forEach(file => {
        if (file.substring(0, 4) == 'F_1_') {
            filmSlug.poster = file
        }else{
            filmSlug.pics.push(file)
        }
            console.log(file.substring(0, 3));
            console.log(file);

    });

    data.filmslugs.push(filmSlug)

    console.log(data)

});


let yamlStr = yaml.safeDump(data);
fs.writeFileSync('../source/pictures.yaml', yamlStr, 'utf8');
