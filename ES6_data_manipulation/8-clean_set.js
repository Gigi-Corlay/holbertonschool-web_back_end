export default function cleanSet(set, startString) {
    if (startString === '') {
        return '';
    }
    const tables = [];
    for (const value of set) {
        if (typeof value === "string" && value.startsWith(startString)) {
            tables.push(value.slice(startString.length));
        }
    }
    return tables.join('-');
}
