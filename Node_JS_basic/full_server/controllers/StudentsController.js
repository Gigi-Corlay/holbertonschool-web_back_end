import { readDatabase } from '../utils.js';

class StudentsController {
    static getAllStudents(req, res) {
        const dbPath = process.argv[2];

        readDatabase(dbPath)
            .then((fields) => {
                res.status(200);
                res.write('This is the list of our students\n');

                const sortedFields = Object.keys(fields).sort(
                    (a, b) => a.toLowerCase().localeCompare(b.toLowerCase())
                );

                for (const field of sortedFields) {
                    const list = fields[field];
                    res.write(
                        `Number of students in ${field}: ${list.length}. List: ${list.join(', ')}\n`
                    );
                }

                res.end();
            })
            .catch(() => {
                res.status(500).send('Cannot load the database');
            });
    }

    static getAllStudentsByMajor(req, res) {
        const dbPath = process.argv[2];
        const { major } = req.params;

        if (major !== 'CS' && major !== 'SWE') {
        res.status(500).send('Major parameter must be CS or SWE');
        return;
        }

        readDatabase(dbPath)
        .then((fields) => {
            const list = fields[major] || [];
            res.status(200).send(`List: ${list.join(', ')}`);
        })
        .catch(() => {
            res.status(500).send('Cannot load the database');
        });
    }
}

export default StudentsController;
