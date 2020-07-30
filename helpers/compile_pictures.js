

const testFolder = 'assets/img/pildid_proc/';
const fs = require('fs');
const yaml = require('js-yaml');
let data = new Object();

data.filmslugs = new Object()

fs.readdirSync(testFolder).forEach(folder => {
    console.log(folder);

    filmSlug = {
        poster: '',
        pics: []
    }

    fs.readdirSync(testFolder + '/' + folder).forEach(file => {
        if (file.substring(0, 4) == 'F_1_') {
            filmSlug.poster = file
            //filmSlug.pics.push(file)
        }else{
            filmSlug.pics.push(file)
        }
        console.log(file.substring(0, 3));
        console.log(file);
    });
    filmSlug.pics.unshift(filmSlug.poster);

    data.filmslugs[folder] = filmSlug

    console.log(data)

});


let yamlStr = yaml.safeDump(data);
fs.writeFileSync('source/pictures.yaml', yamlStr, 'utf8');
