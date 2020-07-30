

const testFolder = 'assets/img/pildid_proc/';
const fs = require('fs');
const yaml = require('js-yaml');
let data = new Object();

data.articles = new Object()

fs.readdirSync(testFolder).forEach(folder => {
    console.log(folder);

    article = {
        poster: '',
        pics: []
    }

    fs.readdirSync(testFolder + '/' + folder).forEach(file => {
        if (file.substring(0, 4) == 'A_1_') {
            article.poster = file

        }else{
            article.pics.push(file)
        }
        console.log(file.substring(0, 3));
        console.log(file);
    });
    article.pics.unshift(article.poster);

    data.articles[folder] = article

    console.log(data)

});


let yamlStr = yaml.safeDump(data);
fs.writeFileSync('source/article_pictures.yaml', yamlStr, 'utf8');
