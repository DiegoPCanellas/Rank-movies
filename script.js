const axios = require('axios');

const url = 'https://www.imdb.com/chart/moviemeter/?ref_=nv_mv_mpm'

axios(url).then(response => {
    const html = response.data;
    const $ = cheerio.load(html);
    const movieName = $('.ranking-item-wrapper');
    const tableMovies = [];
}).catch(console.error);
