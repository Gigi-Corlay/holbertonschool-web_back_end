import getFullResponseFromAPI from './1-promise';

getFullResponseFromAPI(true)
  .then((res) => console.log(res))
  .catch((err) => console.log(err));

getFullResponseFromAPI(false)
  .then((res) => console.log(res))
  .catch((err) => console.log(err));
  