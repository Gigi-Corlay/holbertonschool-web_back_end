const express = require('express');
const countStudents = require('./3-read_file_async');

const app = express();
const database = process.argv[2];

app.get('/', (req, res) => {
  res.type('text/plain');
  res.send('Hello Holberton School!');
});

app.get('/students', async (req, res) => {
  res.type('text/plain');
  res.write('This is the list of our students\n');

  if (!database) {
    res.end('Cannot load the database');
    return;
  }

  try {
    const data = await countStudents(database);
    res.end(data);
  } catch (err) {
    res.end('Cannot load the database');
  }
});

app.listen(1245);

module.exports = app;
