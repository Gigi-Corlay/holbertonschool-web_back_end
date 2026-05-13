const http = require('http');
const countStudents = require('./3-read_file_async');

const app = http.createServer((req, res) => {
  res.setHeader('Content-Type', 'text/plain');

  if (req.url === '/') {
    res.end('Hello Holberton School!');
  }

  else if (req.url === '/students') {
    const db = process.argv[2];

    countStudents(db)
      .then((result) => {
        res.end(`This is the list of our students\n${result}`);
      })
      .catch(() => {
        res.end('This is the list of our students\nCannot load the database');
      });
  }
});

app.listen(1245);

module.exports = app;
