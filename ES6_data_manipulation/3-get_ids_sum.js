export default function getStudentIdsSum(student) {
    return student.reduce((accumulator, student) => {
        return accumulator + student.id;
    }, 0);
}